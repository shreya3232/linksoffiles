# from bs4 import BeautifulSoup
# import requests
# import mysql.connector
# cnx = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='Shreyas@444',
#     database='daily_data'
# )
# cursor = cnx.cursor()

# def create_table(table_name):
#     # Create the table with dynamic table name
#     query = f"""
#     CREATE TABLE IF NOT EXISTS {table_name} (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         title VARCHAR(255),
#         price VARCHAR(50)
#     )
#     """
#     cursor.execute(query)

# def scrape_and_insert(url):
#     # Extract table name from the URL
#     table_name = url.split('/')[-1].split('?')[0]

#     # Make a request to the URL
#     response = requests.get(url)

#     # Parse the HTML content
#     soup = BeautifulSoup(response.content, 'html.parser')

#     # Extract the title and price from the HTML
#     title_element = soup.find('span', {'class': 'B_NuCI'})
#     title = title_element.get_text(strip=True) if title_element else 'N/A'

#     price_element = soup.find('div', {'class':"_30jeq3 _16Jk6d"})
#     price = price_element.get_text(strip=True).replace('₹', '') if price_element else 'N/A'

#     # Create the table if it doesn't exist
#     create_table(table_name)

#     # Insert the scraped data into the table
#     query = f"INSERT INTO {table_name} (title, price) VALUES (%s, %s)"
#     values = (title, price)
#     cursor.execute(query, values)
#     cnx.commit()


# url = 'https://www.flipkart.com/govo-gocrush-900-wireless-auxiliary-coaxial-speaker-ipx7-abs-fabric-16-w-bluetooth-speaker/p/itm7195500c7c5a3?pid=ACCGBUTWRXG5DUNF'

# # Scrape and insert data
# scrape_and_insert(url)

# cursor.close()
# cnx.close()
from bs4 import BeautifulSoup
import requests
import mysql.connector

cnx = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Shreyas@444',
    database='daily_data'
)
cursor = cnx.cursor()
# import re

# ...

# def generate_table_name(url):
#     # Extract alphanumeric characters from the URL to create a table name
#     alphanumeric = re.sub('[^0-9a-zA-Z]+', '_', url)
#     return alphanumeric[:50] 

def create_table(table_name):
    # Create the table with dynamic table name
    query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255),
        price VARCHAR(50)
    )
    """
    cursor.execute(query)

def scrape_and_insert_flipkart(url):
    # Extract table name from the URL
    table_name = url.split('/')[-1].split('?')[0]
    # table_name = generate_table_name(url)
    # Make a request to the URL
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the title and price from the HTML
    title_element = soup.find('span', {'class': 'B_NuCI'})
    title = title_element.get_text(strip=True) if title_element else 'N/A'

    price_element = soup.find('div', {'class': "_30jeq3 _16Jk6d"})
    price = price_element.get_text(strip=True).replace('₹', '') if price_element else 'N/A'

    # Create the table if it doesn't exist
    create_table(table_name)

    # Insert the scraped data into the table
    query = f"INSERT INTO {table_name} (title, price) VALUES (%s, %s)"
    values = (title, price)
    cursor.execute(query, values)
    cnx.commit()

def scrape_and_insert_govo(url):
    # Extract table name from the URL
    table_name = url.split('/')[-1]

    # Make a request to the URL
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the title and price from the HTML
    title_element = soup.find('span', {'class': 'govolife-title'})
    title = title_element.get_text(strip=True) if title_element else 'N/A'

    price_element = soup.find('div', {'class': 'govolife-price'})
    price = price_element.get_text(strip=True) if price_element else 'N/A'

    # Create the table if it doesn't exist
    create_table(table_name)

    # Insert the scraped data into the table
    query = f"INSERT INTO {table_name} (title, price) VALUES (%s, %s)"
    values = (title, price)
    cursor.execute(query, values)
    cnx.commit()

def scrape_and_insert_amazon(url):
    # Extract table name from the URL
    table_name = url.split('/')[-1]

    # Make a request to the URL
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the title and price from the HTML
    title_element = soup.find('span', {'id': 'productTitle'})
    title = title_element.get_text(strip=True) if title_element else 'N/A'

    price_element = soup.find('div', {'id': 'a-price-whole'})
    price = price_element.get_text(strip=True) if price_element else 'N/A'

    # Create the table if it doesn't exist
    create_table(table_name)

    # Insert the scraped data into the table
    query = f"INSERT INTO {table_name} (title, price) VALUES (%s, %s)"
    values = (title, price)
    cursor.execute(query, values)
    cnx.commit()
# List of URLs from Flipkart and govo.life
flipkart_urls = [
    'https://www.flipkart.com/product/p/itme?pid=ACCGBWGVY5KQ6DER',
    'https://www.flipkart.com/product/p/itme?pid=ACCGBWGVHTX3MAHN',
    'https://www.flipkart.com/product/p/itme?pid=ACCGHFZDYBQRGZ36',
    'https://www.flipkart.com/product/p/itme?pid=ACCGGWZZGUSGZ2K5',
    'https://www.flipkart.com/product/p/itme?pid=ACCGGWZZZHHJZGC2',
    'https://www.flipkart.com/product/p/itme?pid=ACCGBWGV3JZ3N6EB',
    'https://www.flipkart.com/product/p/itme?pid=ACCGBWGVZYZYFHXD',
    'https://www.flipkart.com/product/p/itme?pid=ACCGBWGV4ENPNSXH',
    'https://www.flipkart.com/product/p/itme?pid=ACCGGWZPZHHZQFAM',
    'https://www.flipkart.com/product/p/itme?pid=ACCGGWZPSCA9WYFU',
    'https://www.flipkart.com/product/p/itme?pid=ACCGGWZPQE7YFRGC',
    'https://www.flipkart.com/product/p/itme?pid=ACCGGWZP9QZNUDAG',
    'https://www.flipkart.com/product/p/itme?pid=ACCGBWGVUJRBZWDN',
    'https://www.flipkart.com/product/p/itme?pid=ACCGBWGVRFGFGZZP',
    'https://www.flipkart.com/product/p/itme?pid=ACCGBWGV7QNYZWG2',
    'https://www.flipkart.com/product/p/itme?pid=ACCGBWGVTFNBCGSG',
    'https://www.flipkart.com/product/p/itme?pid=ACCGC92S8ZP3PRVH',
    'https://www.flipkart.com/product/p/itme?pid=ACCGBWGVTVXMGZTR',
    'https://www.flipkart.com/product/p/itme?pid=ACCGBUTWYFGEZKBW',
    'https://www.flipkart.com/product/p/itme?pid=ACCGBUTW6GB2J4EF',
    'https://www.flipkart.com/product/p/itme?pid=ACCGBUTWRXG5DUNF',
    'https://www.flipkart.com/product/p/itme?pid=ACCGBWGSFSUGFGCU',
    'https://www.flipkart.com/product/p/itme?pid=ACCGBWGS6ERNM7GG',
    'https://www.flipkart.com/product/p/itme?pid=ACCGBWGSQSRUJEAH',
    'https://www.flipkart.com/product/p/itme?pid=ACCGBWGSHVEBZZW7',
    'https://www.flipkart.com/product/p/itme?pid=ACCGBWGSNZDFDGKM',
    'https://www.flipkart.com/product/p/itme?pid=ACCGHFZDG5GKHNWV',
    'https://www.flipkart.com/product/p/itme?pid=ACCGBWGSX5FUAY2J',
    'https://www.flipkart.com/product/p/itme?pid=ACCGC92SBJJ98WPQ',
    'https://www.flipkart.com/product/p/itme?pid=ACCGBWGSTZENH4HF',
    'https://www.flipkart.com/product/p/itme?pid=ACCGGWZPFUSFYBGU',
    'https://www.flipkart.com/product/p/itme?pid=ACCGHFZQSSZZ5ZHS',
    'https://www.flipkart.com/product/p/itme?pid=ACCGHFZQKCBYGAGG',
    'https://www.flipkart.com/product/p/itme?pid=ACCGHFZP7TF85AYH',
    'https://www.flipkart.com/product/p/itme?pid=ACCGHFZPATZCEHHN',
    'https://www.flipkart.com/product/p/itme?pid=ACCGHFZPSP7ZEYDP',
    'https://www.flipkart.com/product/p/itme?pid=ACCGHFZPTUUDKMG3',
]
govo_urls = [
    'https://govo.life/products/gobass-400-earphones',
    'https://govo.life/products/gobass-410-earphones',
    'https://govo.life/products/gobass-411-earphones',
    'https://govo.life/products/gobass-411-earphones',
    'https://govo.life/products/gobass-411-earphones',
    'https://govo.life/products/gobass-610-earphones',
    'https://govo.life/products/gobass-900-earphones',
    'https://govo.life/products/gobass-910-earphones',
    'https://govo.life/products/gobold-400-bluetooth-headphones',
    'https://govo.life/products/gobold-410-bluetooth-headphones',
    'https://govo.life/products/gobold-600-bluetooth-headphones',
    'https://govo.life/products/gobold-610-bluetooth-headphones',
    'https://govo.life/products/gobuds-400-earbuds',
    'https://govo.life/products/gobuds-410-earbuds',
    'https://govo.life/products/gobuds-600-earbuds',
    'https://govo.life/products/gobuds-621-earbuds',
    'https://govo.life/products/gobuds-900-earbuds',
    'https://govo.life/products/gobuds-901-earbuds',
    'https://govo.life/products/gobuds-902-earbuds',
    'https://govo.life/products/gobuds-920-earbuds',
    'https://govo.life/products/gocrush-410-bluetooth-speaker',
    'https://govo.life/products/gocrush-421-bluetooth-speaker',
    'https://govo.life/products/gocrush-900-bluetooth-speaker',
    'https://govo.life/products/gokixx-400-bluetooth-earphones-neckband',
    'https://govo.life/products/gokixx-410-bluetooth-earphones-neckband',
    'https://govo.life/products/gokixx-421-bluetooth-earphones-neckband',
    'https://govo.life/products/gokixx-610-bluetooth-earphones-neckband',
    'https://govo.life/products/gokixx-620-bluetooth-earphones-neckband',
    'https://govo.life/products/gokixx-621-bluetooth-earphones-neckband',
    'https://govo.life/products/gokixx-630-bluetooth-earphones-neckband',
    'https://govo.life/products/gokixx-651-bluetooth-earphones-neckband',
    'https://govo.life/products/gokixx-652-bluetooth-earphones-neckband',
    'https://govo.life/products/gokixx-900-bluetooth-earphones-neckband',
    'https://govo.life/products/gokixx-952-bluetooth-earphones-neckband',
    'https://govo.life/products/gosurround-410-soundbars',
    'https://govo.life/products/gosurround-430-soundbars',
    'https://govo.life/products/gosurround-610-soundbars',
    'https://govo.life/products/gosurround-620-soundbars',
    'https://govo.life/products/gosurround-900-soundbars',
    'https://govo.life/products/gosurround-920-soundbars',
    'https://govo.life/products/gobuds-661-earbuds',
    'https://govo.life/products/gokixx-621-bluetooth-earphones-neckband',
    'https://govo.life/products/gosurround-950',
    'https://govo.life/products/gobuds-945-1'
]
amazon_urls=[
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

# Scrape and insert data from Flipkart URLs
for url in flipkart_urls:
    scrape_and_insert_flipkart(url)

# Scrape and insert data from govo.life URLs
for url in govo_urls:
    scrape_and_insert_govo(url)
for url in amazon_urls:
    scrape_and_insert_amazon(url)

cursor.close()
cnx.close()
