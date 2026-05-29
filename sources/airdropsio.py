import requests
from bs4 import BeautifulSoup
from datetime import datetime

BASE_URL = "https://airdrops.io/latest/"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/136.0.0.0 Safari/537.36"
    )
}


def parse_date(value):
    if not value:
        return None

    try:
        return datetime.strptime(value, "%Y%m%d")
    except Exception:
        return None

def filter_items(items):
    result = []

    for item in items:

        title = item["title"].lower()

        keywords = [
            "testnet",
            "points",
            "reward",
            "campaign",
            "quest",
        ]

        if any(k in title for k in keywords):
            result.append(item)
            continue

        temp = item["temperature"]

        try:
            score = int(
                temp.replace("°", "")
            )

            if score >= 100:
                result.append(item)

        except:
            pass

    return result
    
def scrape_airdropsio():

    response = requests.get(
        BASE_URL,
        headers=HEADERS,
        timeout=30,
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser",
    )

    results = []

    articles = soup.select(
        "article.airdrop-click"
    )

    for article in articles:

        try:

            title_el = article.select_one("h3")

            if not title_el:
                continue

            title = title_el.get_text(
                strip=True
            )

            link_el = article.select_one(
                "a[href]"
            )

            if not link_el:
                continue

            link = link_el.get("href")

            status_el = article.select_one(
                ".status-indicator"
            )

            status = (
                status_el.get_text(strip=True)
                if status_el
                else "Unknown"
            )

            action_el = article.select_one(
                ".est-value span"
            )

            action = (
                action_el.get_text(strip=True)
                if action_el
                else ""
            )

            temp_el = article.select_one(
                ".droptemp span"
            )

            temperature = (
                temp_el.get_text(strip=True)
                if temp_el
                else ""
            )

            published_raw = article.get(
                "data-published"
            )

            ends_raw = article.get(
                "data-ends"
            )

            results.append(
                {
                    "id": link,
                    "title": title,
                    "link": link,
                    "source": "Airdrops.io",
                    "status": status,
                    "action": action,
                    "temperature": temperature,
                    "published": published_raw,
                    "ends": ends_raw,
                }
            )

        except Exception as e:

            print(
                f"[Airdrops.io] error: {e}"
            )

    return results


if __name__ == "__main__":

    items = scrape_airdropsio()

    print(
        f"Found {len(items)} items"
    )

    for item in items[:10]:

        print("-" * 50)

        print(
            item["title"]
        )

        print(
            item["temperature"]
        )

        print(
            item["status"]
        )

        print(
            item["link"]
        )
