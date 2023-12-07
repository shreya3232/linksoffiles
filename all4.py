from bs4 import BeautifulSoup
import requests
import mysql.connector
import schedule
import time
cnx = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Shreyas@444',
    database='daily_data'
)
cursor = cnx.cursor()

def create_table():
    # Create the table with dynamic table name
    query = """
    CREATE TABLE IF NOT EXISTS daily_data.product_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        website VARCHAR(255),
        title VARCHAR(255),
        price VARCHAR(50)
    )
    """
    cursor.execute(query)

def scrape_and_insert_flipkart(url):
    # Extract table name from the URL
    # table_name = url.split('/')[-1].split('?')[0]

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
    # create_table(table_name)

    # Insert the scraped data into the table
    query = "INSERT INTO product_data (website, title, price) VALUES (%s, %s, %s)"
    values = ('Flipkart', title, price)
    cursor.execute(query, values)
    cnx.commit()

def scrape_and_insert_govo(url):
    # Make a request to the URL
    # table_name = url.split('/')[-1].split('?')[0]
    response = requests.get(url)
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the title and price from the HTML
    title_element = soup.find('h3', {'class': 'font-semibold mb-1'})
    title = title_element.get_text(strip=True) if title_element else 'N/A'

    price_element = soup.find('h3', {'class': 'font-semibold product-selling-price text-primary me-2 me-lg-12'})
    price = price_element.get_text(strip=True) if price_element else 'N/A'

    # Insert the scraped data into the table
    query = "INSERT INTO product_data (website, title, price) VALUES (%s, %s, %s)"
    values = ('Govobrand', title, price)
    cursor.execute(query, values)
    cnx.commit()
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
    'https://www.flipkart.com/product/p/itme?pid=ACCGHFZPTUUDKMG3'
]
govo_urls = [
    'https://govo.life/products/gobass-400-earphones',
    'https://govo.life/products/gobass-410-earphones',
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
    'https://govo.life/products/gosurround-410-soundbar',
    'https://govo.life/products/gosurround-430-soundbar',
    'https://govo.life/products/gosurround-610-soundbar',
    'https://govo.life/products/gosurround-620-soundbar',
    'https://govo.life/products/gosurround-900-soundbar',
    'https://govo.life/products/gosurround-920-soundbar',
    'https://govo.life/products/gokixx-621-bluetooth-earphones-neckband',
    'https://govo.life/products/gosurround-950',
    'https://govo.life/products/gobuds-945-1'
]
def run_scraping_job():
    create_table()
    
    # Scrape and insert data for each URL
    for url in flipkart_urls:
        scrape_and_insert_flipkart(url)

    # Scrape and insert data for Govobrand URLs
    for url in govo_urls:
        scrape_and_insert_govo(url)

    cursor.close()
    cnx.close()

# Schedule the job to run daily at 10:30
schedule.every().day.at("10:30").do(run_scraping_job)

# Infinite loop to keep the program running
while True:
    schedule.run_pending()
    time.sleep(1)
# create_table()
# # Scrape and insert data for each URL
# for url in flipkart_urls:
#     scrape_and_insert_flipkart(url)

# # Scrape and insert data for Govobrand URLs
# for url in govo_urls:
#     scrape_and_insert_govo(url)

# cursor.close()
# cnx.close()
