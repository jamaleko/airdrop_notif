import requests

import json


def load_seen():

    try:

        with open(
            "seen.json",
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    except:

        return {}


def save_seen(data):

    with open(
        "seen.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=2,
        )
def build_message(item):

    return (
        f"🔥 AIRDROP BARU\n\n"
        f"📛 {item['title']}\n\n"
        f"🏷️ {item['source']}\n\n"
        f"🔗 {item['link']}"
    )
def send_message(
    token,
    chat_id,
    text
):

    url = (
        f"https://api.telegram.org"
        f"/bot{8934091180:AAGN0FcUM-LgyYvpHnlGlMBz6UBpQCQD57s}"
        f"/sendMessage"
    )

    payload = {
        "chat_id": chat_id,
        "text": text,
        "disable_web_page_preview": True,
    }

    r = requests.post(
        url,
        json=payload,
        timeout=30,
    )

    r.raise_for_status()
