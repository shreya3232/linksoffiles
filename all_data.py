from bs4 import BeautifulSoup
import requests
import mysql.connector
import schedule
import time
from datetime import datetime
cnx = mysql.connector.connect(
    host= 'sql202.infinityfree.com',
    user='if0_34585113',
    password= 'KtAAjvaesslkI3h',
    database= 'if0_34585113_webscrape',
)
cursor = cnx.cursor()

def create_table():
    # Create the table with dynamic table name
    query = """
    CREATE TABLE IF NOT EXISTS if0_34585113_webscrape.product_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        website VARCHAR(255),
        title VARCHAR(255),
        price VARCHAR(50),
        datetime DATETIME
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
    current_datetime = datetime.now()

    # Convert current_datetime to a formatted string
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    # Insert the scraped data into the table
    query = "INSERT INTO product_data (website, title, price, datetime) VALUES (%s, %s, %s, %s)"
    values = ('Flipkart', title, price,formatted_datetime)
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

    current_datetime = datetime.now()

    # Convert current_datetime to a formatted string
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    # Insert the scraped data into the table
    query = "INSERT INTO product_data (website, title, price, datetime) VALUES (%s, %s, %s, %s)"
    values = ('Govo', title, price,formatted_datetime)
    cursor.execute(query, values)
    cnx.commit()

def scrape_and_insert_nyka(url):
    # Make a request to the URL
    # table_name = url.split('/')[-1].split('?')[0]
    response = requests.get(url)
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the title and price from the HTML
    title_element = soup.find('h1', {'class': 'css-1gc4x7i'})
    title = title_element.get_text(strip=True) if title_element else 'N/A'

    price_element = soup.find('span', {'class': 'css-1jczs19'})
    price = price_element.get_text(strip=True) if price_element else 'N/A'

    current_datetime = datetime.now()

    # Convert current_datetime to a formatted string
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    # Insert the scraped data into the table
    query = "INSERT INTO product_data (website, title, price, datetime) VALUES (%s, %s, %s, %s)"
    values = ('Nykaa', title, price,formatted_datetime)
    cursor.execute(query, values)
    cnx.commit()

def scrape_and_insert_reliance(url):
    # Make a request to the URL
    # table_name = url.split('/')[-1].split('?')[0]
    response = requests.get(url)
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the title and price from the HTML
    title_element = soup.find('h1', {'class': 'pdp__title'})
    title = title_element.get_text(strip=True) if title_element else 'N/A'

    price_element = soup.find('li', {'class': 'pdp__priceSection__priceListText'})
    price = price_element.get_text(strip=True) if price_element else 'N/A'

    current_datetime = datetime.now()

    # Convert current_datetime to a formatted string
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    # Insert the scraped data into the table
    query = "INSERT INTO product_data (website, title, price, datetime) VALUES (%s, %s, %s, %s)"
    values = ('Reliance', title, price,formatted_datetime)
    cursor.execute(query, values)
    cnx.commit()

def scrape_and_insert_jio(url):
    # Make a request to the URL
    # table_name = url.split('/')[-1].split('?')[0]
    response = requests.get(url)
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the title and price from the HTML
    title_element = soup.find('div', {'class': 'jm-body-m-bold'})
    title = title_element.get_text(strip=True) if title_element else 'N/A'

    price_element = soup.find('div', {'id': 'price_section'})
    price = price_element.get_text(strip=True) if price_element else 'N/A'

    current_datetime = datetime.now()

    # Convert current_datetime to a formatted string
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    # Insert the scraped data into the table
    query = "INSERT INTO product_data (website, title, price, datetime) VALUES (%s, %s, %s, %s)"
    values = ('Jiomart', title, price,formatted_datetime)
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
nyka_urls=[
    'https://www.nykaa.com/govo-gobass-400-in-ear-wired-earphones-3d-bass-hd-mic-passive-noise-cancellation-platinum-black/p/4957173?productId=4957173&pps=6',
    'https://www.nykaa.com/govo-gobass-410-in-ear-wired-earphones-3d-bass-hd-mic-passive-noise-cancellation-platinum-black/p/4957174?productId=4957174&pps=12',
    'https://www.nykaa.com/govo-gobass-410-in-ear-wired-earphones-3d-bass-hd-mic-passive-noise-cancellation-platinum-black/p/4957174?productId=4957174&pps=12',
    'https://www.nykaa.com/govo-gobass-900-in-ear-wired-earphones-3d-sound-super-bass-and-hd-mic-black/p/4957176?productId=4957176&pps=18',
    'https://www.nykaa.com/govo-gobass-910-in-ear-wired-earphones-3d-sound-magnetic-earbuds-and-hd-mic-black/p/4957177?productId=4957177&pps=2',
    'https://www.nykaa.com/govo-gobuds-400-tws-earbuds-3d-stereo-sound-20-hrs-battery-life-ipx5-touch-control-platinum-black/p/4957163?productId=4957163&pps=4',
    'https://www.nykaa.com/govo-gobuds-600-tws-earbuds-3d-stereo-sound-33-hrs-battery-ipx5-super-touch-control-black/p/4957164?productId=4957164&pps=7',
    'https://www.nykaa.com/govo-gobuds-920-tws-earbuds-30-hours-battery-life-ipx5-bt-v5-1-super-touch-control-platinum-black/p/4957165?productId=4957165&pps=5',
    'https://www.nykaa.com/govo-gokixx-400-in-ear-wireless-neckband-with-magnetic-earbuds-8-hrs-playtime-ipx5-platinum-black/p/4957166?productId=4957166&pps=17',
    'https://www.nykaa.com/govo-gokixx-410-in-ear-neckband-with-magnetic-earbuds-3d-stereo-8-hrs-playtime-platinum-black/p/4957167?productId=4957167&pps=16',
    'https://www.nykaa.com/govo-gokixx-421-in-ear-neckband-with-magnetic-earbuds-10-hrs-playtime-ipx5-platinum-black/p/4957168?productId=4957168&pps=9',
    'https://www.nykaa.com/govo-gokixx-610-in-ear-neckband-with-metallic-and-magnetic-earbuds-12h-playtime-ipx5-black/p/4957169?productId=4957169&pps=14',
    'https://www.nykaa.com/govo-gokixx-620-wireless-neckband-magnetic-buds-3d-surround-20-h-playtime-ipx5-platinum-black/p/4957170?productId=4957170&pps=8',
    'https://www.nykaa.com/govo-gokixx-630-in-ear-neckband-with-magnetic-earbuds-10-hrs-playtime-ipx5-platinum-black/p/4957171?productId=4957171&pps=13',
    'https://www.nykaa.com/govo-gokixx-900-in-ear-neckband-with-magnetic-earbuds-3d-surround-12h-playtime-ipx5-black/p/4957172?productId=4957172&pps=10',
    'https://www.nykaa.com/govo-gocrush-410-portable-bt-speaker-4w-sound-15-hrs-playtime-ipx7-abs-fabric-platinum-black/p/4957178?productId=4957178&pps=11',
    'https://www.nykaa.com/govo-gocrush-421-portable-bt-speaker-5w-sound-15-hrs-playtime-ipx7-abd-fabric-platinum-black/p/4957179?productId=4957179&pps=15',
    'https://www.nykaa.com/govo-gocrush-900-wireless-btspeaker-24w-explosive-sound-15h-playtime-ipx7-abs-fabric-black/p/4957180?productId=4957180&pps=1'   
]
reliance_urls=[
    'https://www.reliancedigital.in/govo-gobass-410-wired-earphone-with-super-bass-black/p/493072621',
    'https://www.reliancedigital.in/govo-gobass-610-wired-earphone-with-super-bass-black/p/493072622',
    'https://www.reliancedigital.in/govo-gobass-910-wired-earphone-with-super-bass-black/p/493072624',
    'https://www.reliancedigital.in/govo-gobuds-600-true-wireless-bluetooth-earbuds-with-up-to-33-hour-battery-life-platinum-black/p/493072611',
    'https://www.reliancedigital.in/govo-gobuds-920-true-wireless-bluetooth-earbuds-with-upto-30-hour-battery-life-platinum-black/p/493072613',
    'https://www.reliancedigital.in/govo-gokixx-410-wireless-bluetooth-neckband-earphone-with-ipx5-water-resistant-platinum-black/p/493072614',
    'https://www.reliancedigital.in/govo-gokixx-610-wireless-bluetooth-neckband-earphone-with-ipx5-water-resistant-platinum-black/p/493072616',
    'https://www.reliancedigital.in/govo-gokixx-620-wireless-bluetooth-neckband-earphone-with-ipx5-water-resistant-platinum-black/p/493072617',
    'https://www.reliancedigital.in/govo-gokixx-900-wireless-bluetooth-neckband-earphone-with-ipx5-water-resistant-gun-metal-grey/p/493072619',
    'https://www.reliancedigital.in/govo-gocrush-410-bluetooth-multimedia-speaker-with-3d-sound-ipx7-water-resistant-platinum-black/p/493072625',
    'https://www.reliancedigital.in/govo-gocrush-421-bluetooth-multimedia-speaker-with-3d-sound-ipx7-water-resistant-platinum-black/p/493072626',
    'https://www.reliancedigital.in/govo-go-buds-900-true-wireless-earbuds-with-up-to-20-hours-playback-black/p/493072612'

]
jio_urls=[
    'https://www.jiomart.com/p/electronics/govo-gobass-410-wired-earphone-with-super-bass-black/593273012',
    'https://www.jiomart.com/p/electronics/govo-gobass-610-wired-earphone-with-super-bass-black/593276465',
    'https://www.jiomart.com/p/electronics/govo-gobass-910-wired-earphone-with-super-bass-black/593270074',
    'https://www.jiomart.com/p/electronics/govo-gobuds-600-true-wireless-bluetooth-earbuds-with-up-to-33-hour-battery-life-platinum-black/593272315',
    'https://www.jiomart.com/p/electronics/govo-gobuds-920-true-wireless-bluetooth-earbuds-with-upto-30-hour-battery-life-platinum-black/593200402',
    'https://www.jiomart.com/p/electronics/govo-gokixx-410-wireless-bluetooth-earphone-with-ipx5-water-resistant-platinum-black/593276676',
    'https://www.jiomart.com/p/electronics/govo-gokixx-610-wireless-bluetooth-earphone-with-ipx5-water-resistant-platinum-black/593267299',
    'https://www.jiomart.com/p/electronics/govo-gokixx-620-wireless-bluetooth-earphone-with-ipx5-water-resistant-platinum-black/593273832',
    'https://www.jiomart.com/p/electronics/govo-gokixx-900-wireless-bluetooth-earphone-with-ipx5-water-resistant-gun-metal-grey/593262946',
    'https://www.jiomart.com/p/electronics/govo-gocrush-410-bluetooth-multimedia-speaker-with-3d-sound-ipx7-water-resistant-platinum-black/593272471',
    'https://www.jiomart.com/p/electronics/govo-gocrush-421-bluetooth-multimedia-speaker-with-3d-sound-ipx7-water-resistant-platinum-black/593278027',
    'https://www.jiomart.com/p/electronics/govo-go-buds-900-true-wireless-earbuds-with-up-to-20-hours-playback-black/594706097',

]
def run_scraping_job():
    create_table()
    
    # Scrape and insert data for each URL
    for url in flipkart_urls:
        scrape_and_insert_flipkart(url)

    # Scrape and insert data for Govobrand URLs
    for url in govo_urls:
        scrape_and_insert_govo(url)
    for url in reliance_urls:
        scrape_and_insert_reliance(url)
    for url in nyka_urls:
        scrape_and_insert_nyka(url)
    for url in jio_urls:
        scrape_and_insert_jio(url)
    cursor.close()
    cnx.close()

# Schedule the job to run daily at 10:30
schedule.every().day.at("03:34").do(run_scraping_job)

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
