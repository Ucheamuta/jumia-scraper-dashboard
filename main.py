**File: main.py**
```python
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pandas as pd
from scraper import scrape_ecommerce

app = FastAPI(title="Jumia Scraper Dashboard")
templates = Jinja2Templates(directory="templates")

# Serve static files if you add CSS later
# app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home():
    return {"message": "Jumia Scraper API running"}

@app.get("/scrape")
def run_scrape(pages: int = 5):
    df = scrape_ecommerce(pages)
    df.to_csv("data/products.csv", index=False)
    df.to_json("data/products.json", orient="records")
    return {"records": len(df), "message": "Scraped & exported successfully"}

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    df = pd.read_csv("data/products.csv") if pd.io.common.file_exists("data/products.csv") else pd.DataFrame()
    stats = {
        "total_products": len(df),
        "avg_price": round(df["price"].mean(), 2) if not df.empty else 0,
        "categories": df["category"].nunique() if not df.empty else 0
    }
    return templates.TemplateResponse("dashboard.html", {"request": request, "stats": stats, "data": df.to_dict(orient="records")})
