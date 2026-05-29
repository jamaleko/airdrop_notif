import requests
from bs4 import BeautifulSoup

KEYWORDS = {
    "testnet": 50,
    "galxe": 20,
    "quest": 20,
    "discord": 10,
    "twitter": 10,
    "social": 10,
    "faucet": 20,
    "swap": 20,
    "liquidity": 30,
    "bridge": 30,
    "stake": 30,
    "hold": 10,
}

def get_detail_info(url):

    html = requests.get(
        url,
        headers=HEADERS,
        timeout=30
    ).text.lower()

    score = 0
    tags = []

    for word, pts in KEYWORDS.items():

        count = html.count(word)

        if count > 0:

            tags.append(
                word.upper()
            )

            score += pts

    return {
        "tags": tags,
        "extra_score": score
    }
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

        tags = get_detail_tags(
            link
        )
        
        result.append({
            "title": title,
            "link": link,
            "source": "CryptoRank",
            "tags": tags,
        })

    return result


if __name__ == "__main__":

    items = scrape_cryptorank()

    print(
        f"Found {len(items)}"
    )

    for item in items[:10]:
        print(item)
