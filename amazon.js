const cheerio = require('cheerio');
const fs = require('fs');
const axios = require('axios');
const mysql = require('mysql2');

// MySQL database connection configuration
const connection = mysql.createConnection({
    host: 'sql202.infinityfree.com',
    user: 'if0_34585113',
    password: 'KtAAjvaesslkI3h',
    database: 'if0_34585113_webscrape',
});

// Table creation query
const createTableQuery = `
CREATE TABLE IF NOT EXISTS scraped_data (
  id INT AUTO_INCREMENT PRIMARY KEY,
  website VARCHAR(255),
  title VARCHAR(255),
  price VARCHAR(255),
  datetime DATETIME
);
`;

// Execute table creation query
connection.query(createTableQuery, (error, results) => {
  if (error) {
    console.error(`Error creating table: ${error}`);
  } else {
    console.log('Table created successfully');
  }
});
// 

const urls = [
    'https://amazon.in/dp/B09YV5LC7F',
    'https://amazon.in/dp/B09P33L9ZR',
    'https://amazon.in/dp/B09P32F8M5',
    'https://amazon.in/dp/B0B2DZZ4ZZ',
    'https://amazon.in/dp/B09P37YKMS',
    'https://amazon.in/dp/B09P31MBGH',
    'https://amazon.in/dp/B09P348V1P',
    'https://amazon.in/dp/B09P35224S',
    'https://amazon.in/dp/B09YV3YQVB',
    'https://amazon.in/dp/B09YV4PXDZ',
    'https://amazon.in/dp/B09YV463PY',
    'https://amazon.in/dp/B09YV3VFWD',
    'https://amazon.in/dp/B09YV2XRY7',
    'https://amazon.in/dp/B0BVW5D48T',
    'https://amazon.in/dp/B0BVW2DLB3',
    'https://amazon.in/dp/B0BCG5FH9M',
    'https://amazon.in/dp/B0BQVQVZHJ',
    'https://amazon.in/dp/B0BQVY767B',
    'https://amazon.in/dp/B0BQVCWXC1',
    'https://amazon.in/dp/B0BCG2XW1S',
    'https://amazon.in/dp/B0BCG29CNY',
    'https://amazon.in/dp/B0BCG41JJW',
    'https://amazon.in/dp/B0B2DZZZ43',
    'https://amazon.in/dp/B0B2DZ97JD',
    'https://amazon.in/dp/B0C2Z5SQN9',
    'https://amazon.in/dp/B0C695T38L',
    'https://amazon.in/dp/B09P35Y9Q8',
    'https://amazon.in/dp/B09P3GQ9TQ',
    'https://amazon.in/dp/B0BCG3HN8C',
    'https://amazon.in/dp/B09V196GQR',
    'https://amazon.in/dp/B09PRQ8MNW',
    'https://amazon.in/dp/B09PRQ8S8G',
    'https://amazon.in/dp/B09PRQGKH8',
    'https://amazon.in/dp/B09P34XY7M',
    'https://amazon.in/dp/B09P2Z8KWN',
    'https://amazon.in/dp/B09P385YZC',
    'https://amazon.in/dp/B09P2Z8P87',
    'https://amazon.in/dp/B09P33VQVG',
    'https://amazon.in/dp/B0BCG6L6FS',
    'https://amazon.in/dp/B09P3FZD31',
    'https://amazon.in/dp/B09P36YZN7',
    'https://amazon.in/dp/B0BCFZDXD8',
    'https://amazon.in/dp/B09P32HN32',
    'https://amazon.in/dp/B0BN8MW6VH',
    
];


// Function to fetch HTML content from a URL
async function fetchHtml(url) {
    try {
      const response = await axios.get(url);
      return response.data;
    } catch (error) {
      console.error(`Error fetching HTML from ${url}: ${error}`);
    }
  }
  
  // Function to parse the HTML content and extract data
  function parseHtml(html) {
    const $ = cheerio.load(html);
    const title = $('#productTitle').text().trim();
    const price = $('#tp_price_block_total_price_ww .a-offscreen').text().trim();
    const dateTimeNow = new Date().toLocaleString();
  
    // Return the extracted data as an object
    return {
      website: 'Amazon',
      title,
      price,
      dateTimeNow,
    };
  }
  
  async function scrape() {
    for (const url of urls) {
      const html = await fetchHtml(url);
      const data = parseHtml(html);
  
      // Insert the extracted data into the MySQL database
      connection.query(
        'INSERT INTO scraped_data (website, title, price, datetime) VALUES (?, ?, ?, ?)',
        [data.website, data.title, data.price, data.dateTimeNow],
        (error, results) => {
          if (error) {
            console.error(`Error inserting data into MySQL: ${error}`);
          } else {
            console.log(`Data from ${url} has been scraped and inserted into MySQL`);
          }
        }
      );
    }
    connection.end();
  }
  
//   scrape();
  
  // Close the MySQL connection when the scraping is done
  
