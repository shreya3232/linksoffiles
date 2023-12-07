import requests
from bs4 import BeautifulSoup

# URL of the product page you want to scrape
url = "https://www.flipkart.com/product/p/itme?pid=ACCGBWGVY5KQ6DER"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Extracting the price
price = soup.find("div", {"class": "_30jeq3 _16Jk6d"})
if price:
    price = price.text.strip()
else:
    price = "Price not available"

# Extracting the title
title = soup.find("span", {"class": "B_NuCI"})
if title:
    title = title.text.strip()
else:
    title = "Title not available"

# Extracting the reviews
reviews = soup.find("div", {"class": "_3LWZlK"})
if reviews:
    reviews = reviews.text.strip()
else:
    reviews = "No reviews available"

# Print the extracted information
print("Title:", title)
print("Price:", price)
print("Reviews:", reviews)
