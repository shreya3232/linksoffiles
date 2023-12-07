const XLSX = require('xlsx');
const axios = require('axios');
const cheerio = require('cheerio');
const csv = require('fast-csv');
const fs = require('fs');


async function scrapeProductData() {
    try{
  // read in the Excel file with the product links
    const workbook = XLSX.readFile('Product_List_File.xlsx');
    const sheet_name_list = workbook.SheetNames;
    const xlData = XLSX.utils.sheet_to_json(workbook.Sheets[sheet_name_list[0]]);

    // create an empty array to store the extracted data
    const data = [];

    // loop through each link and scrape the data
    for (let i = 0; i < xlData.length; i++) {
        const link = xlData[i].Amazon;

        // skip rows with empty links
        if (!link) {
        continue;
        }
        // function()
        // make a request to the product page
        const response = await axios.get(link);
        const $ = cheerio.load(response.data);
        // const files= cheerio.load(html)
        // extract the price, title, ratings, and review count
        const title = $('#productTitle').text().trim();
        const price = $('#tp_price_block_total_price_ww .a-offscreen').text().trim();
        const ratings = $('#acrCustomerReviewText').text().trim();
        const reviews = $('#acrPopover').text().trim();
        const stockAvailability = $('#availability').text().trim();
        // const bestSellerRankingRegex = /#(\d+) in Electronics/i;
        // const bestSellerRankingMatch = html.match(bestSellerRankingRegex);
        // const bestSellerRanking = bestSellerRankingMatch ? bestSellerRankingMatch[1].trim(): 'null';
        const bestSellerRankingRegex = /Best\s*Sellers\s*Ranking\s*([#\d,]+)/i;
        const bestSellerRankingMatch = $('div#detailBullets_feature_div > ul > li').text().match(bestSellerRankingRegex);
        const bestSellerRanking = bestSellerRankingMatch ? bestSellerRankingMatch[1] : null;
        // const bestSellerRankingRegex1 = /#(\d+) in <a href=/i;
        // const bestSellerRankingMatch1 = html.match(bestSellerRankingRegex1);
        // const bestSellerRanking1 = bestSellerRankingMatch1 ? bestSellerRankingMatch1[1].trim(): 'null';
        const dateTimeNow = new Date().toLocaleString();

        // add the extracted data to the array
        data.push({ 'Price': price, 'Title': title, 'Ratings': ratings, 'Review Count': reviews, 'stock':stockAvailability,'bestseller rank':bestSellerRanking,  'DateTime':dateTimeNow });
    }

    const csvStream = csv.format({ headers: true });

    // pipe the data into the CSV stream
    data.forEach((row) => csvStream.write(row));
    csvStream.end();

    // write the CSV data to a file
    const writeStream = fs.createWriteStream('product_data.csv');
    csvStream.pipe(writeStream);

    writeStream.on('finish', () => {
        console.log('Data extraction complete.');
    });
    } catch (error) {
        console.error('An error occurred:', error);
    }
}
scrapeProductData();
