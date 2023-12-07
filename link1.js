const XLSX = require('xlsx');
const axios = require('axios');
const cheerio = require('cheerio');
const fs = require('fs');

// Read the Excel file
const workbook = XLSX.readFile('D:/linksoffiles/Product_List_File.xlsx');
const worksheet = workbook.Sheets[workbook.SheetNames[0]];
const links = XLSX.utils.sheet_to_json(worksheet);

// Define the CSV file header
const csvHeader = "Amazon\n";

// Define a function to scrape Amazon data from a given link
async function scrapeAmazonData(link) {
  try {
    const response = await axios.get(link);
    const html = response.data;
    const $ = cheerio.load(html);
    const title = $('#productTitle').text().trim() || '';
    const price = $('#tp_price_block_total_price_ww .a-offscreen').text().trim() || '';
    const ratings = $('#acrCustomerReviewText').attr('title').trim() || '';
    const reviews = $('#acrPopover').text().trim() || '';
    const stockAvailability = $('#availability').text().trim() || '';
    return [title, price, ratings, reviews,stockAvailability];
  } catch (error) {
    console.error(error);
    return `Error: ${error.message}\n`;
  }
}

// Define a function to scrape data for all links and save to CSV file
async function scrapeAllLinks(links) {
  let csvData = csvHeader;
  for (const link of links) {
    if (link.Amazon) {
      const amazonData = await scrapeAmazonData(link.Amazon);
      csvData += amazonData;
    }
  }
  fs.writeFile('D:/linksoffiles/Amazon_Data.csv', csvData, (err) => {
    if (err) throw err;
    console.log('CSV file saved successfully.');
  });
}

// Call the scrapeAllLinks function
scrapeAllLinks(links);
