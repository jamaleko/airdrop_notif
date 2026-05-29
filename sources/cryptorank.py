import requests
from bs4 import BeautifulSoup

KEYWORDS = [
    "testnet",
    "points",
    "reward",
    "social",
    "liquidity",
    "hold",
    "nft",
    "role",
]


def get_detail_tags(url):

    try:

        html = requests.get(
            url,
            headers={
                "User-Agent":
                "Mozilla/5.0"
            },
            timeout=30,
        ).text.lower()

        tags = []

        for keyword in KEYWORDS:

            if keyword in html:
                tags.append(
                    keyword.upper()
                )

        return list(
            set(tags)
        )

    except:

        return []

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


if __name__ == "__main__":

    items = scrape_cryptorank()

    print(
        f"Found {len(items)}"
    )

    for item in items[:10]:
        print(item)
