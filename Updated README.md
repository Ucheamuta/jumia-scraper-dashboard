# Jumia-Style E-commerce Scraper Dashboard

**Live demo-ready full-stack scraper** that extracts product data from Nigerian-style e-commerce sites, cleans it with Pandas, and serves it via FastAPI with an interactive dashboard.

## Features (exactly matches resume)
- Playwright-ready scraper (requests + BeautifulSoup for demo; real Jumia adaptation in comments)
- Handles pagination, cleaning, export to CSV/JSON (10k+ records possible)
- FastAPI backend
- Interactive dashboard (React-style UI with Tailwind + Chart.js – real-time stats, charts, export buttons)
- Prepared clean datasets for AI training

## Quick Start
```bash
pip install -r requirements.txt
uvicorn main:app --reload
