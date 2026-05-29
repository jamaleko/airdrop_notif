import requests
from bs4 import BeautifulSoup


def scrape_cryptorank():

    url = "https://cryptorank.io/drophunting"

    html = requests.get(
        url,
        headers={
            "User-Agent":
            "Mozilla/5.0"
        },
        timeout=30
    ).text

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    result = []

    for a in soup.select(
        'a[href*="/drophunting/"]'
    ):

        p = a.select_one("p")

        if not p:
            continue

        title = p.get_text(
            strip=True
        )

        link = (
            "https://cryptorank.io"
            + a["href"]
        )

        result.append({
            "title": title,
            "link": link,
            "source": "CryptoRank",
        })

    return result


if name == "__main__":

    items = scrape_cryptorank()

    print(
        f"Found {len(items)}"
    )

    for item in items[:10]:
        print(item)
