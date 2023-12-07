import datetime
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import time

# read in the Excel file with the product links


# loop through each link and scrape the data
while True:
        df = pd.read_excel('Product_List_File.xlsx')
# print(df["Amazon"])
# create an empty list to store the extracted data
        data = []
        for link in df['Govo']:
                if pd.isna(link):
                        continue

                response = requests.get(link)
                #     print(response)
                soup = BeautifulSoup(response.content, 'html.parser')

                # extract the price_30jeq3 _16Jk6d
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

                data.append({'Title': product_name,'Price': product_price, 'Date':date,'Time':time})

        # convert the list of dictionaries to a DataFrame and save to a CSV file
        df_data = pd.DataFrame(data)
        # append the DataFrame to the CSV file
        with open('Govo.csv', mode='a', newline='', encoding='utf-8') as file:
                df_data.to_csv(file, header=file.tell()==0, index=False, encoding='utf-8')


        print('Data extraction complete.')
    
    # wait for 2 hours before running the script again
        time.sleep(86400)  # 2 hours in seconds