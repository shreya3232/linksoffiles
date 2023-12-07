const cheerio = require('cheerio');
const fs = require('fs');
const axios = require('axios');
const { url } = require('inspector');
const { log } = require('console');
const cron = require('node-cron');

// Array of URLs to scrape
const urls = [
    'https://amazon.in/dp/B09YV5LC7F',
    'https://amazon.in/dp/B09P33L9ZR',
    'https://amazon.in/dp/B09P32F8M5',
    'https://amazon.in/dp/B0B2DZZ4ZZ',
    'https://amazon.in/dp/B09P37YKMS',
    'https://amazon.in/dp/B09P31MBGH',
    'https://amazon.in/dp/B09P348V1P',
    'https://amazon.in/dp/B09P35224S',
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
    'https://www.amazon.in/dp/B0C6Y3GYGC',
    'https://www.amazon.in/dp/B0C6Y28BHN',
    'https://www.amazon.in/dp/B0CC9RR41T',
    'https://www.amazon.in/dp/B0CF9NVXW5',
    'https://www.amazon.in/dp/B0CCNNHMD3',
    'https://www.amazon.in/dp/B0CCNMVQBK',
    'https://www.amazon.in/dp/B0C697JRQX',
    'https://amazon.in/dp/B0CKYTNQB2',
    
]
const lengt=urls.length
console.log(lengt)
// Function to fetch HTML content from a URL
async function fetchHtml(url) {
  try {
    const response = await axios.get(url);
    
    return response.data;
  } catch (error) {
    console.error(`Error fetching HTML from ${url}: ${error}`);
  }
  // fs.writeFileSync('example.txt', response);
}

// Function to parse the HTML content and extract data
function parseHtml(html) {
  const $ = cheerio.load(html);
  // console.log($);
  // Extract data from the web page using CSS selectors
  const title = $('#productTitle').text().trim();
  const price = $('#tp_price_block_total_price_ww .a-offscreen').text().trim();
 
  const dateTimeNow = new Date().toLocaleString();
  // console.log(bestSellerRankingMatch1)
  // Return the extracted data as an array
  return [website='Amazon',title, price,dateTimeNow];
  
}

async function scrape() {
  // Check if the CSV file exists, and create it with header row if it doesn't
  if (!fs.existsSync('AMAZON_Data.csv')) {
    const csvHeader = 'website,Title,Price,Date Time Now\n';
    fs.writeFileSync('AMAZON_Data.csv', csvHeader);
  }

  for (const url of urls) {
    const html = await fetchHtml(url);
    const data = parseHtml(html);

    // Append the extracted data to the CSV file
    const csvRow = `"${data.join('","')}"\n`;
    fs.appendFileSync('AMAZON_Data.csv', csvRow);

    console.log(`Data from ${url} has been scraped and appended to scraped_data.csv`);
  }
}

// Schedule the web scraping process to run every two hours
// cron.schedule('0 */2 * * *', () => {
//   console.log('Starting web scraping process...');
scrape();
// });

console.log('Web scraping process scheduled to run every two hours...');