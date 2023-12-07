// const puppeteer = require('puppeteer');
// const fs = require('fs');

// async function scrapeAmazonBestSellers() {
//   const browser = await puppeteer.launch();
//   const page = await browser.newPage();

//   const categoryUrl = 'https://www.amazon.in/gp/bestsellers/electronics/1389372031/ref=pd_zg_hrsr_electronics';

//   await page.goto(categoryUrl);
//   await page.waitForSelector('#gridItemRoot');

//   const data = await page.evaluate(() => {
//     const items = Array.from(document.querySelectorAll('#gridItemRoot'));
//     return items.map(item => {
//       const rank = item.querySelector('.zg-bdg-text').innerText.trim();
//       const title = item.querySelector('._cDEzb_p13n-sc-css-line-clamp-3_g3dy1').innerText.trim();
//       const price = (item.querySelector('._cDEzb_p13n-sc-price_3mJ9Z') || {}).innerText.trim();
//       return { rank, title, price };
//     });
//   });

//   await browser.close();

//   return data;
// }

// async function saveToCsv(data, filePath) {
//   const csvContent = data.map(item => Object.values(item).join(',')).join('\n');
//   fs.writeFileSync(filePath, `Rank,Title,Price\n${csvContent}`);
// }

// async function main() {
//   try {
//     const data = await scrapeAmazonBestSellers();

//     // Specify the desired file path and name
//     const filePath = 'amazon_bestsellers.csv';

//     await saveToCsv(data, filePath);
//     console.log(`Data saved to ${filePath}`);
//   } catch (error) {
//     console.error('Error:', error);
//   }
// }

// main();
const axios = require('axios');
const fs = require('fs');
const cheerio = require('cheerio');

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
      return { rank, title, price };
    }).get();

    return data;
  } catch (error) {
    throw new Error('Error scraping Amazon: ' + error.message);
  }
}

async function saveToCsv(data, filePath) {
  const csvContent = data.map(item => Object.values(item).join(',')).join('\n');
  fs.writeFileSync(filePath, `Rank,Title,Price\n${csvContent}`);
}

async function main() {
  try {
    const data = await scrapeAmazonBestSellers();

    // Specify the desired file path and name
    const filePath = 'amazon_soundbars_bestsellers.csv';

    await saveToCsv(data, filePath);
    console.log(`Data saved to ${filePath}`);
  } catch (error) {
    console.error(error.message);
  }
}

main();
