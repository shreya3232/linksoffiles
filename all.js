const xlsx = require("xlsx");
const axios = require("axios");
const cheerio = require("cheerio");
const fs = require("fs");

// Load the Excel file
const workbook = xlsx.readFile("Product_List_File.xlsx");
const worksheet = workbook.Sheets[workbook.SheetNames[0]];
const rows = xlsx.utils.sheet_to_json(worksheet);

// Initialize array to store extracted data
const data = [];

// Loop through each row in the Excel file
for (let row of rows) {
  const amazonLink = row["Amazon"];
  const flipkartLink = row["FK"];
  const govolifeLink = row["Govo"];

  // Extract data from Amazon link
  if (amazonLink && amazonLink.includes("amazon.in")) {
    // Function to fetch and scrape data from Amazon
const scrapeAmazonData = async (link) => {
  try {
    const response = await axios.get(link);
    const $ = cheerio.load(response.data.html);

    const title = $('#productTitle').text().trim();
    const price = $('#priceblock_ourprice').text().trim();
    const availability = $('#availability').text().trim();
    const rating = $('#averageCustomerReviews').find('.a-icon-star').text().trim();
    const reviewCount = $('#acrCustomerReviewText').text().trim();

    scrapedData.push({
      Website: 'Amazon',
      Title: title,
      Price: price,
      Availability: availability,
      Rating: rating,
      'Review Count': reviewCount,
    });
  } catch (error) {
    console.error('Error fetching data from Amazon:', error.message);
  }
};

  }

  // Extract data from Flipkart link
  if (flipkartLink && flipkartLink.includes("flipkart.com")) {
    axios.get(flipkartLink).then((response) => {
      const html = response.data;
      const $ = cheerio.load(html);

      const title = $("._35KyD6").text().trim();
      const price = $("._16Jk6d").text().trim();
      const rating = $("._2d4LTz").text().trim();
      const reviewCount = $("._1i0wk8").text().trim();
      const timestamp = new Date().toISOString();

      data.push({
        Website: "Flipkart",
        Title: title,
        Price: price,
        Availability: "Available",
        Rating: rating,
        "Review Count": reviewCount,
        Timestamp: timestamp,
        Link: flipkartLink,
      });
    }).catch((err) => {
      console.error(`Error fetching data from Flipkart link: ${flipkartLink}`, err);
    });
  }

  // Extract data from Govolife link
  if (govolifeLink && govolifeLink.includes("govo.life")) {
    axios.get(govolifeLink).then((response) => {
      const html = response.data;
      const $ = cheerio.load(html);

      const title = $("h1.product_title").text().trim();
      const price = $("span.price").text().trim();
      const availability = $(".stock.in-stock").text().trim();
      const rating = $("div.star-rating").text().trim();
      const reviewCount = $("span.count").text().trim();
      const timestamp = new Date().toISOString();

      data.push({
        Website: "Govolife",
        Title: title,
        Price: price,
        Availability: availability,
        Rating: rating,
        "Review Count": reviewCount,
        Timestamp: timestamp,
        Link: govol});
    }).catch((err) => {
        console.error(`Error fetching data from Govolife link: ${govolifeLink}`, err);
    });
}
}
// Wait for all requests to complete before writing to file
Promise.all(data).then(() => {
    // Write data to output file
    const header = ["Website", "Title", "Price", "Availability", "Rating", "Review Count", "Timestamp", "Link"];
    const csv = [header.join(",")];
    
    for (let item of data) {
    const row = Object.values(item).join(",");
    csv.push(row);
    }
    
    fs.writeFileSync("output.csv", csv.join("\n"));
    }).catch((err) => {
    console.error("Error:", err);
});
