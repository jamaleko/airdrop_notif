from sources.airdropsio import scrape_airdropsio
from sources.cryptorank import scrape_cryptorank
from filter import (
    filter_airdrops
)
from telegram import (
    send_message,
    load_seen,
    save_seen,
)

from config import (
    BOT_TOKEN,
    CHANNEL_ID,
)

import time


def chunk_list(data, size):

    for i in range(0, len(data), size):
        yield data[i:i + size]


def build_batch_message(items):

    text = "🔥 AIRDROP UPDATE\n\n"

    for i, item in enumerate(items, 1):

        tag_text = ""

        if item.get("tags"):

            tag_text = (
                "🏷️ "
                + ", ".join(
                    item["tags"]
                )
                + "\n"
            )

        text += (
            f"{i}. {item['title']}\n"
            f"⭐ Score: {item['score']}\n"
            f"{tag_text}"
            f"📦 {item['source']}\n"
            f"🔗 {item['link']}\n\n"
        )

    return text


def main():

    print("loading seen.json...")

    seen = load_seen()

    items = []

    print("scraping airdrops.io...")

    try:
        items.extend(
            scrape_airdropsio()
        )
    except Exception as e:
        print(
            "airdrops.io error:",
            e
        )

    print("scraping cryptorank...")

    try:
        items.extend(
            scrape_cryptorank()
        )
    except Exception as e:
        print(
            "cryptorank error:",
            e
        )

    print(
        f"total scraped: {len(items)}"
    )
    items = filter_airdrops(
        items
    )
    
    print(
        f"after filter: {len(items)}"
    )
    new_items = []

    for item in items:

        link = item["link"]

        if link in seen:
            continue

        seen[link] = True

        new_items.append(item)

    print(
        f"new items: {len(new_items)}"
    )

    if not new_items:

        print(
            "no new airdrops"
        )

        return

    batch_count = 0

    for batch in chunk_list(
        new_items,
        10,
    ):

        msg = build_batch_message(
            batch
        )

        try:

            send_message(
                BOT_TOKEN,
                CHANNEL_ID,
                msg,
            )

            batch_count += 1

            print(
                f"batch {batch_count} sent "
                f"({len(batch)} items)"
            )

            time.sleep(1)

        except Exception as e:

            print(
                "telegram error:",
                e
            )

    save_seen(seen)

    print(
        f"done. "
        f"{len(new_items)} new items "
        f"sent in "
        f"{batch_count} batches"
    )


if __name__ == "__main__":
    main()
