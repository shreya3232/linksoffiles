import pandas as pd
import requests
from bs4 import BeautifulSoup
import datetime
import schedule
import time

# Function to scrape data from the provided Flipkart link
def scrape_data():
    # Your existing scraping logic goes here...

    # Load the Excel file using pandas
    df = pd.read_excel("flipkartsurround.xlsx")

    # Create empty lists to store the extracted data
    data = []

    for index, row in df.iterrows():
        flipkart_link = row["Flipkart"]
        
        # Extract the data for each link
        
        if isinstance(flipkart_link, str) and "flipkart.com" in flipkart_link:
            response = requests.get(flipkart_link)
            soup = BeautifulSoup(response.content, "html.parser")
            producname_element = soup.find("span", attrs={"class": "B_NuCI"})
            product_name = producname_element.text.strip() if producname_element else "N/A"
            # Get the product price
            product_price_element = soup.find("div", attrs={"class": "_30jeq3 _16Jk6d"})
            product_price = product_price_element.text.strip() if product_price_element else "N/A"
            # # Get the product rating
            # product_rating_element = soup.find("div", attrs={"class": "_3LWZlK"})
            # product_rating = product_rating_element.text.strip() if product_rating_element else "N/A"
            # # Get the product reviews
            # product_reviews = []
            # for review in soup.find_all("div", attrs={"class": "row _2afbiS"}):
            #         review_text = review.text.strip()
            #         product_reviews.append(review_text)
            # # append the extracted data to the list
            now = datetime.datetime.now()
            date = now.strftime("%Y-%m-%d")
            time = now.strftime("%H:%M:%S")
            data.append({'Website': 'Flipkart','Title': product_name,'Price': product_price,'Date':date,'Time':time})
        elif isinstance(flipkart_link, float):
            continue
        # Your existing scraping logic for each product link...

    result_df = pd.DataFrame(data)
    # result_df.to_csv("result1.csv", index=False)
    # Read the existing data from the CSV file
    existing_data = pd.read_csv("flipkart1.csv")

    # Concatenate the existing data and new data
    final_df = pd.concat([existing_data, result_df], ignore_index=True)

    # Save the concatenated DataFrame to the same CSV file
#     final_df.to_csv("result1.csv", index=False)
# schedule.every().day.at("17:40").do(scrape_data)
# # schedule.every().day.at("10:40").do(scrape_data)
# while True:
#     schedule.run_pending()
#     time.sleep(1)

    # Save the concatenated DataFrame to the CSV file
    final_df.to_csv("flipkart1.csv", index=False)
    print("Scraping completed at", datetime.datetime.now())

# Schedule scraping at 11:40 AM and 4:00 PM
schedule.every().day.at("11:20").do(scrape_data)
schedule.every().day.at("16:25").do(scrape_data)

while True:
    schedule.run_pending()
    time.sleep(1)
