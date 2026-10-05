import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"

headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    response = requests.get(URL, headers=headers, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    headlines = []

    for heading in soup.find_all("h2"):
        title = heading.get_text(strip=True)

        if title:
            headlines.append(title)

    with open("headlines.txt", "w", encoding="utf-8") as file:
        for headline in headlines:
            file.write(headline + "\n")

    print(f"Successfully saved {len(headlines)} headlines.")

except requests.RequestException as error:
    print(f"Error fetching website: {error}")

except Exception as error:
    print(f"Unexpected error: {error}")
