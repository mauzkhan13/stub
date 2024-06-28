from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (NoSuchElementException, StaleElementReferenceException, TimeoutException)
import pandas as pd
import json
from time import sleep
import os
from selenium.webdriver.support.ui import WebDriverWait, Select
from bs4 import BeautifulSoup
import re
from selenium.webdriver.common.keys import Keys
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2.service_account import Credentials


options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-logging')
options.add_argument('--log-level=3')
options.add_argument('--headless')
options.add_argument('--window-size=1920,1080')
options.binary_location = '/usr/bin/google-chrome' 
driver = webdriver.Chrome(options=options)
url = 'https://www.google.com/maps/search/'
driver.get(url)
driver.maximize_window()
print('Browser is running')

api_file  = {
  "type": "service_account",
  "project_id": "hardy-palace-377114",
  "private_key_id": "051e5ef61c34c36c60c5d790e0b2f53d992ec9a2",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDWqjQytZWczMVz\nbHMg2BfNEskKmOn6jzyxxkBDWtRdyY0Je/LCiJDnNDAQ0+v6+Ve4vE4MxCR7OCHz\nbNX4EJe6WOigjR5T+pWdvdk6TKf1lAnmy4ZG+8KiBKJxnscEcdQSNj/cWf0tpbgM\nL2VKYn2c/xYBC+Rof37C2giJIwYOogUVYbVwYCUrc5NZLnOix1B7YrPAdNxMjiW2\nzCWk07ziihm+fwekZTZpFEY3zG65zz4PEUmqHQ7/JUT/Sa7FO5qb+kkKy39EPl9e\ngEPyBxuGt87tu7Ny8/vJqAGoFDDRuedZkSG3JhX+H/I9b0zXf51QbHiZex3UUJf8\nuixLak97AgMBAAECggEAQXeJEcoFRdvBgBEcD3E32QgYng3ClfKnLQRsRt5lk/DK\n/ZB6mc9yecCVxBwNhO4UTbfICearxZR57jZMDypoS6Gf2I8RJ8Vtab0jib8lHiU2\n29dILU/MrQLC0+n7giSA68j1susS5p/6wGSX/JaK/p1hBZKt5xyy+RPrtH8k8sLx\n0lKevmJ1HsesekK7G4VX/sN9woWj9kk8Uu+664vJXh5X9ospqLXjJHv7lJKiFOl4\n5bK5mB1J1RWpdJqNDasy+jTyQmVKZWeWJlx3NP9oTIxLgRU5/0ymOx9RoMZQ0G6P\nX5r36i/yOlZHJ237vHwD9yj0yqtTlM8slGRj6vZoWQKBgQDr/ym+4pjmsK+F+v9Q\n40zmcRzOZQRxRf26NkKjn63FqSrJ9WGeoz68WegnVafM63ziKhWj63+WMxVYEwCJ\n/BlC0ZwPcvhU1DhT67t8qfSyLJSZALImMrUk74wUshWllPJwXTfCoRVrY2kyQLkL\ncM0AEkt/jx6grI0YdttbItjLZwKBgQDo3Cpl8qDjtDN0qvrsneOTpys1oHVEJz+a\nuWSBqG6+ZRCxcA6Wndchj9FLxPnOMU9nFjXRsSezMsQOCrskZguzzOElTOBV3Jma\nMqEmtd6sxpP5dz4acXWm8GAvNFICGhbkRu13qdLfra0wS1cqEjrgUVERlgWRgYpU\nYJKq5T5izQKBgFdPIWyjfJnsSCOzRn3weeTPeC7LpKcbk9Eufdz3GF0GRvRMuf7s\nuisIwCC9ScVAYgVyOGtalutEnuLktNBX2iikT65PhJwtn2E81zI51nOMlrU8Uqxb\nGjU+An8tm2CVCFSVyClTWw9Nyf9zfoJDCzS5kADzPAuJivHAF0tSSw6FAoGADIyx\nDEWDPkJb85GzbEUmGrMLtRwstbuXxfLv47z8Gu6/c5CieKOREJH7qaW4ANDPgrLD\nu8Vcal/2CPuzEkcdolcMW0JFZNs6vAC2hquOkKkzGGLAyhQLTy/tPx4GvW5ChZL9\nAVH5t2xYxR2KWQ4adjRrthLrwefFWL7LqMIqFpECgYEAlaJ/DqnUIyW7TH+gC1wJ\nyTM+FPYQA6GHGzYFWpfYfWEW59DyXBVhhv/5OocqoT9ntm0Cl3KAP481HmugN2GN\nAA1KoRobvwbcqP3Le8DGDslqsqtAoD0sts1wA3FCgJG8JPDbWdIrcXtzdxubIv+u\nWzBJVidT24oA0PtlqtSwQrM=\n-----END PRIVATE KEY-----\n",
  "client_email": "google-sheet-api@hardy-palace-377114.iam.gserviceaccount.com",
  "client_id": "101013958315517785766",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/google-sheet-api%40hardy-palace-377114.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}




main_link = []
unique_links = []

creds = Credentials.from_service_account_info(api_file,
                                              scopes=["https://spreadsheets.google.com/feeds",
                                                      "https://www.googleapis.com/auth/drive"])
client = gspread.authorize(creds)
spreadsheet_id = '1We0hu5dHLuyUQAtvi946wi4I9oYKd56XwtFArqO3694'
spreadsheet = client.open_by_key(spreadsheet_id)

worksheet = spreadsheet.get_worksheet(0)
records = worksheet.get_all_records()
df = pd.DataFrame(records)

link_column_name = 'county'

for index, row in df.iterrows():
    city = row[link_column_name]
    search = f'Driving school in {city}, France'
    print(f'{index+1}, {city}')

    box = driver.find_element(By.XPATH, '//input[@id="searchboxinput"]')
    try:
        closing_sign = driver.find_element(By.XPATH, '(//*[contains(text(),"")])[1]').click()
    except Exception as e:
        pass
    sleep(0.5)
    box.send_keys(search)
    sleep(0.5)
    box.send_keys(Keys.ENTER)
    sleep(1)

    start_time = time.time()
    while True:   
        try:
            try:
                reached_page = driver.find_element(By.XPATH, '//*[contains(text(),"reached the end of the list.")]')
                if reached_page:
                    break
            except NoSuchElementException:
                pass
            try:
                name_page = driver.find_element(By.XPATH, '//h1[@class="DUwDvf lfPIob"]')
                if name_page:
                    break
            except NoSuchElementException:
                pass

            scroll_pages = driver.find_elements(By.XPATH, '//div[@class="qjESne veYFef"]')
            for scroll_page in scroll_pages:
                if time.time() - start_time > 40:
                    raise TimeoutException

                try:
                    sleep(0.5)
                    driver.execute_script("arguments[0].scrollIntoView(true);", scroll_page)
                    driver.execute_script("arguments[0].click();", scroll_page)
                except Exception as e:
                    raise NoSuchElementException
            else:
                continue
            break
        except (NoSuchElementException, TimeoutException):
            break
    sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    divs = soup.find_all('a', {'href': lambda x: x and x.startswith('https://www.google.com/maps/place/')})
    for link in divs:
        url = link.get('href')
        main_link.append(url)
 
 
print(f"Total links collected: {len(main_link)}")



names = []
address = []
website = []
cat = []
website_link = []
main_url = []

all_links = list(set(main_link))
print(len(all_links))

for index, link in enumerate (all_links):
    url = f'{link}'
    
    driver.get(url)
    print(f'Link Number: {index}')
    
    sleep(1)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    try:
        name = soup.find('h1').text
        names.append(name)
    except AttributeError:
        names.append("N/A")

    try:
        contacts = soup.find('div', attrs={'aria-label': lambda x: x and x.startswith("Information for")}).find_all('div')[2].text.replace('', '').replace('', '').strip()
        address.append(contacts)
    except AttributeError:
        address.append("N/A")

    try:
        sites = soup.find('a', {'data-tooltip': 'Open website'}).text.replace('', '').strip()
        website.append(sites)
    except AttributeError:
        website.append("N/A")

    try:
        a_tag = soup.find('a', {'data-tooltip': 'Open website'})

        if a_tag:
            href = a_tag.get('href')
            website_link.append(href)
        else:
            website_link.append("N/A")
    except AttributeError:
        website_link.append("N/A")

    try:
        ca = soup.find(lambda tag: tag.name == 'div' and tag.get('class') == ['fontBodyMedium'] and tag.find('span') and tag.find('span').find('button')).text
        cat.append(ca)
    except AttributeError:
        cat.append("N/A")
        
    main_url.append(link)

print('Successfully  extracted data..............')

df = pd.DataFrame(zip(names, address, website,website_link, cat, main_url ), columns= ['Company Name','address','Domain URL','website_link', 'Category', 'Link'])

creds = Credentials.from_service_account_info(api_file,
                                              scopes=["https://spreadsheets.google.com/feeds",
                                                      "https://www.googleapis.com/auth/drive"])
client = gspread.authorize(creds)

spreadsheet_id = '1Opx6iDLCn0tRxMcHRAA1HIXFqKxZgJxy4h22c-eUmlc'
spreadsheet = client.open_by_key(spreadsheet_id)

worksheet = spreadsheet.get_worksheet(0)
worksheet.append_rows(df.values.tolist(), value_input_option='USER_ENTERED')
