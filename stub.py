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
import re
from selenium.webdriver.common.keys import Keys
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2.service_account import Credentials
import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth
import undetected_chromedriver as UC

options = Options()
# options.add_argument('--disable-blink-features=AutomationControlled')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-gpu')
# options.add_argument('--start-maximized')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--disable-logging')
# options.add_argument('--enable-automation')
# options.add_argument('--log-level=3')
# options.add_argument('--v=99')
# options.add_argument('--headless')
# driver = uc.Chrome(
#     options=options,
# )
# driver.get('https://www.google.com/')
driver = uc.Chrome(options=options)
driver.get('https://www.google.com/')

driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
while driver.execute_script("return document.readyState") != "complete":
    pass
driver.maximize_window()

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


emails_address_list = []
facebook_urls_list = []
instagram_urls_list = []
phone_numbers_list = []
x_urls_list = []
linkedin_urls_list = []
website_list = []

def extract_contacts(page_source):
    fb_url_pattern = re.compile(r'https?://(?:www\.)?facebook\.com/[a-zA-Z0-9._%+-/]+')
    email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    inst_url_pattern = re.compile(r'https?://(?:www\.)?instagram\.com/[a-zA-Z0-9._%+-/]+')
    x_url_pattern = re.compile(r'https?://(?:www\.)?twitter\.com/[a-zA-Z0-9._%+-/]+')
    l_url_pattern = re.compile(r'https?://(?:www\.)?linkedin\.com/[a-zA-Z0-9._%+-/]+')

    phone_pattern_1 = re.compile(r'(?i)(?:tel|phone|Telephone|Mobile|Phone|Phone Number|Tel:)[:\s]*\+?\(?\d{1,4}\)?[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}')
    phone_pattern_2 = re.compile(r'\+\d{1,4}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}')

    phone_numbers = phone_pattern_1.findall(page_source)
    # If no phone numbers were found with the first pattern, use the second pattern
    if not phone_numbers:
        phone_numbers = phone_pattern_2.findall(page_source)

    facebook_urls = fb_url_pattern.findall(page_source)
    emails = email_pattern.findall(page_source)
    instagram_urls = inst_url_pattern.findall(page_source)
    # phone_numbers = phone_pattern.findall(page_source)
    x_urls = x_url_pattern.findall(page_source)
    linkedin_urls = l_url_pattern.findall(page_source)

    return emails, facebook_urls, instagram_urls, phone_numbers, x_urls, linkedin_urls


creds = Credentials.from_service_account_info(api_file,
                                              scopes=["https://spreadsheets.google.com/feeds",
                                                      "https://www.googleapis.com/auth/drive"])
client = gspread.authorize(creds)
spreadsheet_id = '1fc65YhFEPShdJFs9M87aP7_ttDh7yGNlyVRr21jl0lk'
spreadsheet = client.open_by_key(spreadsheet_id)

worksheet = spreadsheet.get_worksheet(0)
records = worksheet.get_all_records()
df = pd.DataFrame(records)

link_column_name = 'place_website'
for index, row in df.iterrows():
    # if index >= 2:  # Process only the first two URLs
    #     break
    url = row[link_column_name]
    print(f"Processing Website URL {index} : {url}")
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    except Exception as e:
        print(f"Failed to load {url}")
        emails_address_list.append(['Failed to load'] * 3)
        facebook_urls_list.append('N/A')
        instagram_urls_list.append('N/A')
        phone_numbers_list.append(['N/A'] * 3)
        x_urls_list.append('N/A')
        linkedin_urls_list.append('N/A')
        website_list.append(url)
        continue

    emails, fb_urls, inst_urls, phones, x_urls, linkedin_urls = extract_contacts(driver.page_source)
    if emails:
        emails_padded = emails[:3] + ['N/A'] * (3 - len(emails[:3]))
    else:
        emails_padded = ['N/A'] * 3
    emails_address_list.append(emails_padded)
    facebook_urls_list.append(fb_urls[0] if fb_urls else 'N/A')
    instagram_urls_list.append(inst_urls[0] if inst_urls else 'N/A')
    
    if phones:
        if len(phones) >= 3:
            phones_padded = phones[-3:]
        else:
            phones_padded = ['N/A'] * (3 - len(phones)) + phones
    else:
        phones_padded = ['N/A'] * 3
    phone_numbers_list.append(phones_padded)
    x_urls_list.append(x_urls[0] if x_urls else 'N/A')
    linkedin_urls_list.append(linkedin_urls[0] if linkedin_urls else 'N/A')
    website_list.append(driver.current_url)

    contact_xpath1 = '//a[@class and contains(@href, "contact") and contains(translate(., "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "contact")]'
    contact_xpath2 = '//a[starts-with(@href, "/contact")]'
    contact_xpath3 = '//a[contains(@href, "contact")]'
    contact_xpath4 = '//a[contains(@href, "Contact")]'

    contact_found = False
    for xpath in [contact_xpath1, contact_xpath2, contact_xpath3,contact_xpath4]:
        try:
            contact_link = WebDriverWait(driver, 0.5).until(EC.presence_of_element_located((By.XPATH, xpath)))
            href = contact_link.get_attribute('href')
            if href:
                driver.get(href)
                WebDriverWait(driver, 0.5).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            else:
                contact_link.click()
                WebDriverWait(driver, 0.5).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            contact_found = True
            break
        except Exception as e:
            pass

    if contact_found:
        emails, fb_urls, inst_urls, phones, x_urls, linkedin_urls = extract_contacts(driver.page_source)
        if emails:
            emails_padded = emails[:3] + ['N/A'] * (3 - len(emails[:3]))
        else:
            emails_padded = ['N/A'] * 3
        emails_address_list[-1] = emails_padded
        facebook_urls_list[-1] = fb_urls[0] if fb_urls else 'N/A'
        instagram_urls_list[-1] = inst_urls[0] if inst_urls else 'N/A'
        if phones:
            if len(phones) >= 3:
                phones_padded = phones[-3:]
            else:
                phones_padded = ['N/A'] * (3 - len(phones)) + phones
        else:
            phones_padded = ['N/A'] * 3
        phone_numbers_list[-1] = phones_padded
        x_urls_list[-1] = x_urls[0] if x_urls else 'N/A'
        linkedin_urls_list[-1] = linkedin_urls[0] if linkedin_urls else 'N/A'
        website_list[-1] = driver.current_url
    else:
        emails_address_list[-1] = ['N/A'] * 3
        facebook_urls_list[-1] = 'N/A'
        instagram_urls_list[-1] = 'N/A'
        phone_numbers_list[-1] = ['N/A'] * 3
        x_urls_list[-1] = 'N/A'
        linkedin_urls_list[-1] = 'N/A'
        website_list[-1] = driver.current_url
        print("No contact page found or navigated")




max_emails = max(len(emails) for emails in emails_address_list)
max_phones = max(len(phones) for phones in phone_numbers_list)

email_columns = [f'emails_address {i+1}' for i in range(max_emails)]
phone_columns = [f'phone_numbers {i+1}' for i in range(max_phones)]

# Prepare the data for the DataFrame
data = []
for emails, fb_url, inst_url, phones, x_url, linkedin_url, website in zip(
    emails_address_list, facebook_urls_list, instagram_urls_list, phone_numbers_list, x_urls_list, linkedin_urls_list, website_list):
    row = emails + [''] * (max_emails - len(emails))
    row += phones + [''] * (max_phones - len(phones))
    row += [fb_url, inst_url, x_url, linkedin_url, website]
    data.append(row)


columns = email_columns + phone_columns + ['Facebook URL', 'Instagram URL', 'X URL', 'LinkedIn URL', 'Website URL']

df = pd.DataFrame(data, columns=columns)

creds = Credentials.from_service_account_info(api_file,
                                              scopes=["https://spreadsheets.google.com/feeds",
                                                      "https://www.googleapis.com/auth/drive"])
client = gspread.authorize(creds)

spreadsheet_id = '1lZzIeB8-GWNy66b9ShFbdPavSHVY9yG8R_tO7aVPGdI'
spreadsheet = client.open_by_key(spreadsheet_id)

worksheet = spreadsheet.get_worksheet(0)
worksheet.append_rows(df.values.tolist(), value_input_option='USER_ENTERED')


Print('Data Exported to the Google Sheet Successfully')
