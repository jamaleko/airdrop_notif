import requests


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
