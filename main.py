from sources.airdropsio import scrape_airdropsio
from sources.cryptorank import scrape_cryptorank

items = []

items.extend(
    scrape_airdropsio()
)

items.extend(
    scrape_cryptorank()
)

print(
    len(items)
)
