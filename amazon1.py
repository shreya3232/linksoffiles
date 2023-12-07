# import requests
# from bs4 import BeautifulSoup

# url = "https://www.amazon.in/dp/B0BCG41JJW"

# # Send a GET request to the URL
# response = requests.get(url)

# # Create a BeautifulSoup object from the response text
# soup = BeautifulSoup(response.text, "html.parser")

# # Extract the product title
# title_element = soup.find("span", attrs={"id": "productTitle"})
# title = title_element.get_text(strip=True) if title_element else "Title not found"

# # Extract the product price
# price_element = soup.find("span", attrs={"class": "a-price-whole"})
# price = price_element.get_text(strip=True) if price_element else "Price not found"

# # Print the title and price
# print("Title:", title)
# print("Price:", price)
import requests
from bs4 import BeautifulSoup
import mysql.connector
from datetime import datetime

# MySQL database connection configuration
connection = mysql.connector.connect(
    host= 'sql6.freesqldatabase.com',
    user='sql6630682',
    password= 'Fm3YGjWqg1',
    database= 'sql6630682',
)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Create table query
create_table_query = '''
CREATE TABLE IF NOT EXISTS scraped_data (
  id INT AUTO_INCREMENT PRIMARY KEY,
  website VARCHAR(255),
  title VARCHAR(255),
  price VARCHAR(255),
  datetime DATETIME
)
'''

# Execute table creation query
cursor.execute(create_table_query)
connection.commit()

# Array of URLs to scrape
urls = [
    # URLs here...
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
]

# CSS Selector for title element
title_css_selector = 'span#productTitle'

# CSS Selector for price element
price_css_selector = 'span.a-price-whole'

# Function to fetch HTML content from a URL
def fetch_html(url):
    response = requests.get(url)
    return response.text

# Function to parse the HTML content and extract data
def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    # Extract the title element
    title_element = soup.find("span", attrs={"id": "productTitle"})
    title = title_element.get_text(strip=True) if title_element else 'Title not found'

    # Extract the price element
    price_element = soup.find("span", attrs={"class": "a-price-whole"})
    price = price_element.get_text(strip=True) if price_element else 'Price not found'

    datetime_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Return the extracted data as a tuple
    return ('Amazon', title, price, datetime_now)

# Function to insert data into the MySQL database
def insert_data(data):
    query = '''
    INSERT INTO scraped_data (website, title, price, datetime)
    VALUES (%s, %s, %s, %s)
    '''
    cursor.execute(query, data)
    connection.commit()

# Iterate over the URLs, scrape data, and insert it into the database
for url in urls:
    html = fetch_html(url)
    data = parse_html(html)
    insert_data(data)
    print(f'Data from {url} has been scraped and inserted into the database')

# Close the cursor and connection
cursor.close()
connection.close()
