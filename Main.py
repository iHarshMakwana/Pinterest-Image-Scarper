from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import csv

scrollnum = 1
sleepTimer = 1
print("Pinterest Image Scraper")
search_queries = input("Enter Tags separated by commas: ").split(',')

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

for var in search_queries:
    url = f'https://in.pinterest.com/search/pins/?q={var}'
    driver.get(url)

    for _ in range(scrollnum):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print(f'Scrolling down for query: {var}')
        time.sleep(sleepTimer)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    csv_filename = f'{var}_images.csv'
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Image Source'])

        for link in soup.find_all('img'):
            img_src = link.get('src')
            if img_src and img_src.startswith("https://"):
                csv_writer.writerow([img_src])
                print(img_src)

    print(f"Image URLs saved to '{csv_filename}'")

driver.quit()
