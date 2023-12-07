import pandas as pd
import requests
from bs4 import BeautifulSoup
import datetime
from requests_html import HTMLSession

# from macpath import join

# Load the Excel file using pandas
df = pd.read_excel("all_website_urls.xlsx")
# df = pd.read_excel(join("./data", 'all_website_urls.xlsx') , sheet_name="Sheet1")
# Create empty lists to store the extracted data
data = []

# Loop through each row in the Excel file

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
for index, row in df.iterrows():
    govolife_link = row["Govo"]

    if isinstance(govolife_link, str) and "govo.life" in govolife_link:
        response = requests.get(govolife_link)
        soup = BeautifulSoup(response.content, "html.parser")
        product_name_element = soup.find("h3", attrs={"class": "font-semibold"})
        product_name = product_name_element.text.strip() if product_name_element else "N/A"
        # Get the product price
        product_price_element = soup.find("h3", attrs={"class": "font-semibold product-selling-price text-primary me-2 me-lg-12"})
        product_price = product_price_element.text.strip() if product_price_element else "N/A"
        # Get the product rating
        
        # append the extracted data to the list
        now = datetime.datetime.now()
        date = now.strftime("%Y-%m-%d")
        time = now.strftime("%H:%M:%S")
        data.append({'Website': 'Govolife','Title': product_name,'Price': product_price, 'Date':date,'Time':time})
    elif isinstance(govolife_link, float):
        continue
for index, row in df.iterrows():
    nyka_links = row["Nykaa"]

    if isinstance(nyka_links, str) and "nykaa.com" in nyka_links:
        response = requests.get(nyka_links)
        soup = BeautifulSoup(response.content, "html.parser")
        product_name_element = soup.find("h1", attrs={"class": "css-1gc4x7i"})
        product_name = product_name_element.text.strip() if product_name_element else "N/A"
        # Get the product price
        product_price_element = soup.find("span", attrs={"class": "css-1jczs19"})
        product_price = product_price_element.text.strip() if product_price_element else "N/A"
        # Get the product rating
        
        # append the extracted data to the list
        now = datetime.datetime.now()
        date = now.strftime("%Y-%m-%d")
        time = now.strftime("%H:%M:%S")
        data.append({'Website': 'Nyka.com','Title': product_name,'Price': product_price, 'Date':date,'Time':time})
    elif isinstance(nyka_links, float):
        continue

for index, row in df.iterrows():
    nyka_fashion_links = row["NYKA_Fashion"]

    if isinstance(nyka_fashion_links, str) and "nykaafashion.com" in nyka_fashion_links:
        response = requests.get(nyka_fashion_links)
        soup = BeautifulSoup(response.content, "html.parser")
        product_name_element = soup.find("span", attrs={"class": "css-cmh3n9"})
        product_name = product_name_element.text.strip() if product_name_element else "N/A"
        # Get the product price
        product_price_element = soup.find("span", attrs={"class": "css-1byl9fj"})
        product_price = product_price_element.text.strip() if product_price_element else "N/A"
        # Get the product rating
        
        # append the extracted data to the list
        now = datetime.datetime.now()
        date = now.strftime("%Y-%m-%d")
        time = now.strftime("%H:%M:%S")
        data.append({'Website': 'Nyka Fashion','Title': product_name,'Price': product_price, 'Date':date,'Time':time})
    elif isinstance(nyka_fashion_links, float):
        continue
for index, row in df.iterrows():
    jiomart_links = row["Jiomart"]

    if isinstance(jiomart_links, str) and "jiomart.com" in jiomart_links:
        response = requests.get(jiomart_links)
        soup = BeautifulSoup(response.content, "html.parser")
        product_name_element = soup.find("div", attrs={"class": "jm-body-m-bold"})
        product_name = product_name_element.text.strip() if product_name_element else "N/A"
        # Get the product price
        product_price_element = soup.find("dd", attrs={"class": "css-1kcvyns"})
        product_price = product_price_element.text.strip() if product_price_element else "N/A"
        # Get the product rating
        
        # append the extracted data to the list
        now = datetime.datetime.now()
        date = now.strftime("%Y-%m-%d")
        time = now.strftime("%H:%M:%S")
        data.append({'Website': 'Jiomart','Title': product_name,'Price': product_price, 'Date':date,'Time':time})
    elif isinstance(jiomart_links, float):
        continue

for index, row in df.iterrows():
    reliance_links = row["Reliance"]

    if isinstance(reliance_links, str) and "reliancedigital.in" in reliance_links:
        response = requests.get(reliance_links)
        soup = BeautifulSoup(response.content, "html.parser")
        product_name_element = soup.find("h1", attrs={"class": "pdp__title"})
        product_name = product_name_element.text.strip() if product_name_element else "N/A"
        # Get the product price
        product_price_element = soup.find("li", attrs={"class": "pdp__priceSection__priceListText"})
        product_price = product_price_element.text.strip() if product_price_element else "N/A"
        # Get the product rating
        
        # append the extracted data to the list
        now = datetime.datetime.now()
        date = now.strftime("%Y-%m-%d")
        time = now.strftime("%H:%M:%S")
        data.append({'Website': 'RelianceDigital','Title': product_name,'Price': product_price, 'Date':date,'Time':time})
    elif isinstance(reliance_links, float):
        continue
result_df = pd.DataFrame(data)
# result_df.to_csv("result.csv", index=False)
# Read the existing data from the CSV file
existing_data = pd.read_csv("result.csv")

# Concatenate the existing data and new data
final_df = pd.concat([existing_data, result_df], ignore_index=True)

# Save the concatenated DataFrame to the same CSV file
final_df.to_csv("result.csv", index=False)