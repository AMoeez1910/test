from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import random
from product import Product

class Scraper:
    def __init__(self, base_url='https://www.amazon.com/s'):
        self.base_url = base_url
        chrome_options = Options()
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("start-maximized")
        chrome_options.add_argument("disable-infobars")
        chrome_options.add_argument("--disable-extensions")
        self.service = Service()
        self.driver = webdriver.Chrome(service=self.service, options=chrome_options)

    def fetch_page(self, query, page):
        url = f"{self.base_url}?k={query}&page={page}"
        self.driver.get(url)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-main-slot"))
        )
        return self.driver.page_source

    def parse_product(self, product):
        title = product.find('span', class_='a-size-medium')
        title = title.text.strip() if title else None

        total_reviews = product.find('span', class_='a-size-base')
        total_reviews = total_reviews.text.strip() if total_reviews else None

        price = product.find('span', class_='a-offscreen')
        price = price.text.strip() if price else None

        image_url = product.find('img', class_='s-image')
        image_url = image_url['src'] if image_url else None

        return Product(
            title=title,
            total_reviews=total_reviews,
            price=price,
            image_url=image_url,
            creation_timestamp=time.time(),
            update_timestamp=time.time()
        )

    def scrape(self, query, pages=5):
        products = []
        for page in range(1, pages + 1):
            try:
                html = self.fetch_page(query, page)
                soup = BeautifulSoup(html, 'html.parser')
                product_elements = soup.find_all('div', class_='s-main-slot')[0].find_all('div', {'data-component-type': 's-search-result'})
                for product_element in product_elements:
                    product = self.parse_product(product_element)
                    products.append(product.to_dict())
                time.sleep(random.uniform(1, 5))
            except Exception as e:
                print(f"Error on page {page} for query '{query}': {e}")
        self.driver.quit()
        return products