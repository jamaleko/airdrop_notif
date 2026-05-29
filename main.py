from sources.airdropsio import scrape_airdropsio
from sources.cryptorank import scrape_cryptorank

from telegram import send_message
from telegram import load_seen
from telegram import save_seen
from telegram import build_message

from config import BOT_TOKEN
from config import CHANNEL_ID


def main():

    seen = load_seen()

    items = []

    items.extend(
        scrape_airdropsio()
    )

    items.extend(
        scrape_cryptorank()
    )

    sent = 0

    for item in items:

        link = item["link"]

        if link in seen:
            continue

        msg = build_message(item)

        try:

            send_message(
                BOT_TOKEN,
                CHANNEL_ID,
                msg,
            )

            seen[link] = True

            sent += 1

            print(
                "sent:",
                item["title"]
            )

        except Exception as e:

            print(
                "telegram error:",
                e
            )

    save_seen(seen)

    print(
        f"new sent: {sent}"
    )


if __name__ == "__main__":
    main()
