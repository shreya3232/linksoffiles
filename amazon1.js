const puppeteer = require('puppeteer');
const fs = require('fs');
const json2csv = require('json2csv').Parser;

const amazonUrls = [
    'https://amazon.in/dp/B09YV4PXDZ',
    'https://amazon.in/dp/B09YV463PY',
    'https://amazon.in/dp/B09YV3VFWD',
    'https://amazon.in/dp/B09YV2XRY7',
    'https://amazon.in/dp/B0BVW5D48T',
    'https://amazon.in/dp/B0BVW2DLB3',
    'https://amazon.in/dp/B0BCG5FH9M'
];

async function scrapeAmazon(url) {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto(url);

    const productInfo = await page.evaluate(() => {
        const title = document.querySelector('#productTitle').innerText.trim();
        const price = document.querySelector('#priceblock_ourprice').innerText.trim();
        return { title, price };
    });

    await browser.close();

    return productInfo;
}

async function runScraping() {
    const scrapedData = [];

    for (const url of amazonUrls) {
        const productInfo = await scrapeAmazon(url);
        scrapedData.push({ url, ...productInfo });
    }

    // Convert JSON to CSV
    const json2csvParser = new json2csv();
    const csv = json2csvParser.parse(scrapedData);

    // Save the CSV to a file
    const filename = `amazon_scraped_data_${new Date().toISOString()}.csv`;
    fs.writeFileSync(filename, csv);
    console.log('Data saved to', filename);
}

// Schedule the scraping at 11 AM and 4 PM
const now = new Date();
const hours = now.getHours();

if (hours === 11 || hours === 16) {
    runScraping();
}
