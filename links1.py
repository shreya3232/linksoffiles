# 
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import datetime
import time
# List of URLs of the Amazon product pages you want to scrape
# urls = [
    
#     "https://www.flipkart.com/product/p/itme?pid=ACCGBWGVZYZYFHXD",
#     "https://www.flipkart.com/product/p/itme?pid=ACCGBWGV4ENPNSXH",
#     "https://www.flipkart.com/product/p/itme?pid=ACCGGWZPZHHZQFAM",
#     "https://www.flipkart.com/product/p/itme?pid=ACCGGWZPSCA9WYFU",	
#     "https://www.flipkart.com/product/p/itme?pid=ACCGGWZPQE7YFRGC",	
#     "https://www.flipkart.com/product/p/itme?pid=ACCGGWZP9QZNUDAG",	
#     "https://www.flipkart.com/product/p/itme?pid=ACCGBWGVUJRBZWDN",	
#     "https://www.flipkart.com/product/p/itme?pid=ACCGBWGVRFGFGZZP",	
#     "https://www.flipkart.com/product/p/itme?pid=ACCGBWGV7QNYZWG2",	
#     "https://www.flipkart.com/product/p/itme?pid=ACCGBWGVTFNBCGSG",	
#     "https://www.flipkart.com/product/p/itme?pid=ACCGC92S8ZP3PRVH",	
#     "https://www.flipkart.com/product/p/itme?pid=ACCGBWGVTVXMGZTR",	
#     "https://www.flipkart.com/product/p/itme?pid=ACCGBUTWYFGEZKBW",	
#     "https://www.flipkart.com/product/p/itme?pid=ACCGBUTW6GB2J4EF",	
#     "https://www.flipkart.com/product/p/itme?pid=ACCGBUTWRXG5DUNF",	
#     "https://www.flipkart.com/product/p/itme?pid=ACCGBWGSFSUGFGCU",	
#     "https://www.flipkart.com/product/p/itme?pid=ACCGBWGS6ERNM7GG",	
#     "https://www.flipkart.com/product/p/itme?pid=ACCGBWGSQSRUJEAH",	
#     "https://www.flipkart.com/product/p/itme?pid=ACCGBWGSHVEBZZW7",	
#     "https://www.flipkart.com/product/p/itme?pid=ACCGBWGSNZDFDGKM",	
#     "https://www.flipkart.com/product/p/itme?pid=ACCGHFZDG5GKHNWV",	
#     "https://www.flipkart.com/product/p/itme?pid=ACCGBWGSX5FUAY2J",	
#     "https://www.flipkart.com/product/p/itme?pid=ACCGC92SBJJ98WPQ",	
#     "https://www.flipkart.com/product/p/itme?pid=ACCGBWGSTZENH4HF",	
#     "https://www.flipkart.com/product/p/itme?pid=ACCGGWZPFUSFYBGU",	
#     "https://www.flipkart.com/product/p/itme?pid=ACCGHFZQSSZZ5ZHS",	
#     "https://www.flipkart.com/product/p/itme?pid=ACCGHFZQKCBYGAGG",	
#     "https://www.flipkart.com/product/p/itme?pid=ACCGHFZP7TF85AYH",	
#     "https://www.flipkart.com/product/p/itme?pid=ACCGHFZPATZCEHHN",	
#     "https://www.flipkart.com/product/p/itme?pid=ACCGHFZPSP7ZEYDP",	
#     "https://www.flipkart.com/product/p/itme?pid=ACCGHFZPTUUDKMG3"


    
# ]
# print(urls)
df = pd.read_excel('Product_List_File.xlsx')
data=[]
# print(df)
def scrape_and_save_to_csv():
    # Get current date and time
    now = datetime.datetime.now()

    # Create a CSV file if it doesn't exist, otherwise append to existing file
    filename = "product_details_Flipkart.csv"
    with open(filename, "a", newline="", encoding="utf-8") as csvfile:
        data = csv.to_csv(csvfile)
        
        # Check if file is empty, if so, write header row
        if csvfile.tell() == 0:
            data.append(["Product Name", "Product Price", "Product Rating", "Product Reviews", "Stock Availability", "Date", "Time"])
        
        # Loop through the Amazon URLs
        for url in df['FK']:
        # Send a GET request to the URL
            response = requests.get(url)
            # print(response)
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, "html.parser")

            # Get the product name      css-1gc4x7i
            product_name_element = soup.find("span", attrs={"class": "B_NuCI"})
            product_name = product_name_element.text.strip() if product_name_element else "N/A"

            # Get the product price
            product_price_element = soup.find("div", attrs={"class": "_30jeq3 _16Jk6d"})
            product_price = product_price_element.text.strip() if product_price_element else "N/A"

            # Get the product rating
            product_rating_element = soup.find("div", attrs={"class": "_3LWZlK"})
            product_rating = product_rating_element.text.strip() if product_rating_element else "N/A"

            # Get the product reviews
            product_reviews = []
            for review in soup.find_all("div", attrs={"class": "row _2afbiS"}):
                review_text = review.text.strip()
                product_reviews.append(review_text)

            # Get the stock availability
            stock_availability_element = soup.find("div", attrs={"class": "_2JC05C"})
            stock_availability = stock_availability_element.text.strip() if stock_availability_element else "N/A"

            now = datetime.datetime.now()
            date = now.strftime("%Y-%m-%d")
            time = now.strftime("%H:%M:%S")

            # Write the product details to the CSV file with current timestamp
            data.append([product_name, product_price,product_rating,product_reviews,stock_availability,  now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S")])

    print("Product details saved to {} file.".format(filename))

# Loop to continuously scrape and save to CSV every 10 seconds
while True:
    scrape_and_save_to_csv()
    time.sleep(800)
