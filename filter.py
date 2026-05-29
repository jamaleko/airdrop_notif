def calculate_score(item):

    score = 0

    source = item.get(
        "source",
        ""
    ).lower()

    title = item.get(
        "title",
        ""
    ).lower()

    action = item.get(
        "action",
        ""
    ).lower()

    temp = item.get(
        "temperature",
        ""
    )

    if source == "cryptorank":
        score += 20

    try:

        degree = int(
            temp.replace(
                "°",
                ""
            )
        )

        if degree >= 200:
            score += 30

        elif degree >= 100:
            score += 20

    except:
        pass

    keywords = (
        title
        + " "
        + action
    )

    if "testnet" in keywords:
        score += 50

    if "points" in keywords:
        score += 40

    if "reward" in keywords:
        score += 30

    if "liquidity" in keywords:
        score += 20

    if "hold" in keywords:
        score += 10

    return score


def filter_airdrops(items):

    result = []

    for item in items:

        score = calculate_score(
            item
        )

        item["score"] = score

        if score >= 50:
            result.append(item)

    result.sort(
        key=lambda x:
        x["score"],
        reverse=True
    )

    return result
