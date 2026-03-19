import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

os.makedirs("data", exist_ok=True)

def scrape_ecommerce(pages=5):
    all_books = []
    base_url = "https://books.toscrape.com"  # DEMO SITE
    # REAL JUMIA ADAPTATION (uncomment when ready):
    # base_url = "https://www.jumia.com.ng" 
    # Use Playwright for JS-heavy pages (code in comments at bottom)

    for page in range(1, pages + 1):
        url = f"{base_url}/catalogue/page-{page}.html"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        
        for article in soup.find_all("article", class_="product_pod"):
            title = article.h3.a["title"]
            price = article.find("p", class_="price_color").text.replace("£", "").strip()
            all_books.append({"title": title, "price": float(price), "category": "Books"})

    df = pd.DataFrame(all_books)
    print(f"Scraped {len(df)} records")
    return df
