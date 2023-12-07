const axios = require('axios');
const cheerio = require('cheerio');
const xlsx = require('xlsx');
const fs = require('fs');
const { Parser } = require('json2csv');

// Load Excel file
const workbook = xlsx.readFile('Product_List_File.xlsx');
const worksheet = workbook.Sheets[workbook.SheetNames[0]];
const data = xlsx.utils.sheet_to_json(worksheet);

// Array to store scraped data
const scrapedData = [];

// Function to fetch and scrape data from Amazon
const scrapeAmazonData = async (link) => {
  try {
    const response = await axios.get(link);
    const $ = cheerio.load(response.data.data);

    const title = $('#productTitle').text().trim();
    const price = $('#tp_price_block_total_price_ww .a-offscreen').text().trim();
    const ratings = $('#acrCustomerReviewText').text().trim();
    const reviews = $('#acrPopover').text().trim();
    const stockAvailability = $('#availability').text().trim();
    const bestSellerRankingRegex = /#(\d+) in Electronics/i;
    const bestSellerRankingMatch = html.match(bestSellerRankingRegex);
    const bestSellerRanking = bestSellerRankingMatch ? bestSellerRankingMatch[1].trim(): 'null';
    const bestSellerRankingRegex1 = /#(\d+) in <a href=/i;
    const bestSellerRankingMatch1 = html.match(bestSellerRankingRegex1);
    const bestSellerRanking1 = bestSellerRankingMatch1 ? bestSellerRankingMatch1[1].trim(): 'null';
    const dateTimeNow = new Date().toLocaleString();
    data.push({
        Website: "Amazon",
        Title: title,
        Price: price,
        stockAvailability: stockAvailability,
        ratings:ratings,
        reviews:reviews,
        bestSellerRanking:bestSellerRanking,
        bestSellerRanking1:bestSellerRanking1,
        dateTimeNow:dateTimeNow
       
      });
  } catch (error) {
    console.error('Error fetching data from Amazon:', error.message);
  }
};

// Function to fetch and scrape data from Flipkart
const scrapeFlipkartData = async (link) => {
  try {
    const response = await axios.get(link);
    const $ = cheerio.load(response.data);

    const title = $('.B_NuCI').text().trim();
    const price = $('._30jeq3._16Jk6d').text().trim();
    const availability = $('._9-sL7L').text().trim();
    const rating = $('._3LWZlK').text().trim();
    const reviewCount = $('.row _2afbiS').text().trim();
    const dateTimeNow = new Date().toLocaleString();
    scrapedData.push({
      Website: 'Flipkart',
      Title: title,
      Price: price,
      Availability: availability,
      Rating: rating,
      'Review Count': reviewCount,
      dateTimeNow:dateTimeNow
    });
  } catch (error) {
    console.error('Error fetching data from Flipkart:', error.message);
  }
};

// Function to fetch and scrape data from Govolife
const scrapeGovolifeData = async (link) => {
  try {
    const response = await axios.get(link);
    const $ = cheerio.load(response.data);

    const title = $('h3.font-semibold mb-1').text().trim();
    const price = $('h3.font-semibold product-selling-price text-primary me-2 me-lg-12').first().text().trim();
    const dateTimeNow = new Date().toLocaleString();

    scrapedData.push({
      Website: 'Govolife',
      Title: title,
      Price: price,
      dateTimeNow:dateTimeNow
    });
  } catch (error) {
    console.error('Error fetching data from Govolife:', error.message);
  }
};

// Loop through the data and fetch/scrape information
const scrapeData = async () => {
  for (let item of data) {
      if (item['Amazon']) {
        await scrapeAmazonData(item['Amazon']);
      }
    }
        // Scrape Flipkart links
  for (let item of data) {
    if (item['FK']) {
      await scrapeFlipkartData(item['FK']);
    }
  }

  // Scrape Govolife links
  for (let item of data) {
    if (item['Govo']) {
      await scrapeGovolifeData(item['Govo']);
    }
  }

  // Convert scraped data to CSV format
  const fields = ['Website', 'Title', 'Price', 'Availability', 'Rating', 'Review Count','bestSellerRanking','bestSellerRanking1',];
  const json2csvParser = new Parser({ fields });
  const csvData = json2csvParser.parse(scrapedData);

  // Save the CSV file
  fs.writeFileSync('scraped_data.csv', csvData);

  console.log('Data scraped and saved as CSV file.');
};

scrapeData();
