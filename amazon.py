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
    'https://amazon.in/dp/B0C695T38L'
]

# Function to fetch HTML content from a URL
def fetch_html(url):
    response = requests.get(url)
    return response.text

# Function to parse the HTML content and extract data
def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    title_element = soup.select_one('#productTitle')
    title = title_element.get_text(strip=True) if title_element else 'N/A'

    # Extract the price element
    price_element = soup.select_one('.a-price-whole')
    price = price_element.get_text(strip=True) if price_element else 'N/A'
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
