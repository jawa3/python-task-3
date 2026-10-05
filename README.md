# Task 3 - News Headlines Web Scraper

## Objective

The objective of this project is to scrape top news headlines
from a public news website using Python.

## Technologies Used

- Python
- Requests
- BeautifulSoup

## How It Works

1. Sends an HTTP GET request to the news website.
2. Receives the HTML response.
3. Uses BeautifulSoup to parse the HTML.
4. Finds headline elements using h2 tags.
5. Saves the headlines into headlines.txt.

## Installation

```bash
pip install requests beautifulsoup4
