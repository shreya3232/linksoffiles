const axios = require('axios');
const cheerio = require('cheerio');
const fs = require('fs');
const moment = require('moment');

async function scrapeAmazonBestSellers() {
  try {
    const categoryUrl = 'https://www.amazon.in/gp/bestsellers/electronics/1389372031/ref=pd_zg_hrsr_electronics';
    const response = await axios.get(categoryUrl);

    if (response.status !== 200) {
      throw new Error('Failed to retrieve webpage');
    }

    const $ = cheerio.load(response.data);
    const items = $('#gridItemRoot');

    const data = items.map((index, element) => {
      const rank = $(element).find('.zg-bdg-text').text().trim();
      const title = $(element).find('._cDEzb_p13n-sc-css-line-clamp-3_g3dy1').text().trim();
      const price = $(element).find('._cDEzb_p13n-sc-price_3mJ9Z').text().trim();
      const asin = $(element).attr('data-asin');
      const dateTime = moment().format('YYYY-MM-DD HH:mm:ss');
      return { rank, title, price, asin, dateTime };
    }).get();

    return data;
  } catch (error) {
    throw new Error('Error scraping Amazon: ' + error.message);
  }
}

async function saveToCsv(data, filePath) {
  const csvContent = data.map(item => Object.values(item).join(',')).join('\n');

  // Append to the CSV file
  fs.appendFileSync(filePath, `${csvContent}\n`);
}

async function runScraping() {
  while (true) {
    try {
      const data = await scrapeAmazonBestSellers();

      // Specify the desired file path and name
      const filePath = 'amazon_soundbars_bestsellers2.csv';

      await saveToCsv(data, filePath);
      console.log(`Data saved to ${filePath}`);

      // Wait for 2 hours before running again
      await new Promise(resolve => setTimeout(resolve, 1 * 60 * 60 * 1000));
    } catch (error) {
      console.error(error.message);
      // Wait for 2 hours before retrying on error
      await new Promise(resolve => setTimeout(resolve, 1 * 60* 60 * 1000));
    }
  }
}

runScraping();
