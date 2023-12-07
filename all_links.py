import pandas as pd
import requests
from bs4 import BeautifulSoup
import datetime

# Load Excel file and read links from three columns
df = pd.read_excel('all_website_urls.xlsx')
amazon_links = df['Amazon'].tolist()
flipkart_links = df['Flipkart'].tolist()
govolife_links = df['Govo'].tolist()
Nyka_links = df['Nykaa'].tolist()
govolife_links = df['NYKA_Fashion'].tolist()
govolife_links = df['Jiomart'].tolist()
govolife_links = df['Reliance'].tolist()


# Scrape data from Amazon links
flipkart_data = []
for flipkart_link in flipkart_links:
    if isinstance(flipkart_link, str) and "flipkart.com" in flipkart_link:
        page = requests.get(flipkart_link)
        soup = BeautifulSoup(page.content, 'html.parser')
        product_name_element = soup.find("span", attrs={"class": "B_NuCI"})
        product_name = product_name_element.text.strip() if product_name_element else "N/A"
        # Get the product pric
        # print(product_name)
        product_price_element = soup.find("div", attrs={"class": "_30jeq3 _16Jk6d"})
        product_price = product_price_element.text.strip() if product_price_element else "N/A"
        product_rating_element = soup.find("div", attrs={"class": "_3LWZlK"})
        product_rating = product_rating_element.text.strip() if product_rating_element else "N/A"
        # Get the product reviews
        product_reviews = []
        for review in soup.find_all("div", attrs={"class": "row _2afbiS"}):
            review_text = review.text.strip()
            product_reviews.append(review_text)
        date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        flipkart_data.append([product_name, product_price,product_rating,product_reviews, date_time])
    elif isinstance(flipkart_link, float):
        continue
amazon_data = []
for amazon_link in amazon_links:
    if isinstance(amazon_link, str) and "amazon.in" in amazon_link:
        page = requests.get(amazon_link)
        soup = BeautifulSoup(page.content, 'html.parser')
        product_name_element = soup.find("span", attrs={"class": "a-size-medium product-title-word-break product-title-resize"})
        title = product_name_element.text.strip() if product_name_element else "N/A"

        # Get the product price
        product_price_element = soup.find("span", attrs={"id": "tp_price_block_total_price_ww"})
        price = product_price_element.text.strip() if product_price_element else "N/A"
        product_rating_element = soup.find("span", attrs={"id": "acrCustomerReviewText"})
        product_rating = product_rating_element.text.strip() if product_rating_element else "N/A"
        # Get the product reviews
        product_reviews = []
        for review in soup.find_all("span", attrs={"id": "acrPopover"}):
                review_text = review.text.strip()
                product_reviews.append(review_text)
        # append the extracted data to the list
        date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        amazon_data.append([title, price,product_rating,product_reviews, date_time])
    elif isinstance(amazon_link, float):
        continue
govolife_data = []
for govolife_link in govolife_links:
    try:
        if isinstance(govolife_link, str) and "govo.life" in govolife_link:
            page = requests.get(govolife_link)
            soup = BeautifulSoup(page.content, 'html.parser')
            product_name_element = soup.find("h3", attrs={"class": "font-semibold"})
            product_name = product_name_element.text.strip() if product_name_element else "N/A"
        # Get the product price
            product_price_element = soup.find("h3", attrs={"class": "font-semibold product-selling-price text-primary me-2 me-lg-12"})
            product_price = product_price_element.text.strip() if product_price_element else "N/A"
            
            date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            govolife_data.append([product_name, product_price, date_time])
    except Exception as e:
        print(f"Error fetching data from Govolife link: {govolife_link} {e}")
# Scrape data from Flipkart links


# Scrape data from Govolife links


# Combine the data from all three websites into a single list
all_data = amazon_data + flipkart_data+ govolife_data

# Save the data as a CSV file
df_data = pd.DataFrame(all_data, columns=['Title', 'Price','product_rating', 'product_reviews', 'Date/Time'])
df_data.to_csv('all_data.csv', index=False)
