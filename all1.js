const axios = require('axios');
const cheerio = require('cheerio');
const xlsx = require('xlsx');
const fs = require('fs');

// Load Excel file
const workbook = xlsx.readFile('Product_List_File.xlsx');
const worksheet = workbook.Sheets[workbook.SheetNames[0]];
const data = xlsx.utils.sheet_to_json(worksheet);

// Array to store fetched data
const fetchedData = [];

// Function to fetch and store data from Amazon
const fetchAmazonData = async (link) => {
  try {
    const response = await axios.get(link);
    const $ = cheerio.load(response.data);

    const title = $('#productTitle').text().trim();
    const price = $('#priceblock_ourprice').text().trim();
    const availability = $('#availability').text().trim();
    const rating = $('#averageCustomerReviews').find('.a-icon-star').text().trim();
    const reviewCount = $('#acrCustomerReviewText').text().trim();

    const amazonData = {
      Title: title,
      Price: price,
      Availability: availability,
      Rating: rating,
      'Review Count': reviewCount,
    };

    fetchedData.push(amazonData);
  } catch (error) {
    console.error('Error fetching data from Amazon:', error.message);
  }
};

// Function to fetch and store data from Flipkart
const fetchFlipkartData = async (link) => {
  try {
    const response = await axios.get(link);
    const $ = cheerio.load(response.data);

    const title = $('._35KyD6').text().trim();
    const price = $('._1vC4OE._3qQ9m1').text().trim();
    const availability = $('._9-sL7L').text().trim();
    const rating = $('._1i0wk8').text().trim();
    const reviewCount = $('._38sUEc').text().trim();

    const flipkartData = {
      Title: title,
      Price: price,
      Availability: availability,
      Rating: rating,
      'Review Count': reviewCount,
    };

    fetchedData.push(flipkartData);
  } catch (error) {
    console.error('Error fetching data from Flipkart:', error.message);
  }
};

// Function to fetch and store data from Govolife
const fetchGovolifeData = async (link) => {
  try {
    const response = await axios.get(link);
    const $ = cheerio.load(response.data);

    const title = $('h1.product__title').text().trim();
    const price = $('span.money').first().text().trim();
    const availability = $('button.btn--sold-out').length === 0 ? 'In Stock' : 'Out of Stock';
    const rating = $('.spr-badge').attr('data-rating');
    const reviewCount = $('.spr-badge-caption').text().trim();

    const govolifeData = {
      Title: title,
      Price: price,
      Availability: availability,
      Rating: rating,
      'Review Count': reviewCount,
    };

    fetchedData.push(govolifeData);
  } catch (error) {
    console.error('Error fetching data from Govolife:', error.message);
  }
};

// Array to store all fetch promises
const fetchPromises = [];

// Loop through the data and fetch information
for (let item of data) {
  if (item['Amazon']) {
    fetchPromises.push(fetchAmazonData(item['Amazon']));
  }

  if (item['FK']) {
    fetchPromises.push(fetchFlipkartData(item['FK']));
    }


  if (item['Govo']) {
    fetchPromises.push(fetchGovolifeData(item['Govo']));
    }
}
        
        // Wait for all fetch operations to complete
Promise.all(fetchPromises)
.then(() => {
        // Convert fetched data to CSV format
const csvContent = 'Title,Price,Availability,Rating,Review Count\n';
for (let data of fetchedData) {
    const row = Object.values(data).map(value => "${value}").join(',');
    csvContent += row + '\n';
    }
    fs.writeFileSync('fetched_data.csv', csvContent);

    console.log('CSV file saved successfully!');
    })
.catch(error => {
    console.error('Error fetching and saving data:', error.message);
    });
