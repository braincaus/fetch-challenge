import math
from datetime import datetime


def get_points(receipt):
    points = 0

    # One point for every alphanumeric
    points += len([x for x in receipt['retailer'] if x.isalnum()])

    total = float(receipt['total'])

    if not total % 1:
        points += 50

    if not total % .25:
        points += 25

    points += (int(len(receipt['items']) / 2) * 5)

    for item in receipt['items']:
        if len(item['shortDescription'].strip()) % 3 == 0:
            points += math.ceil(float(item['price']) * 0.2)

    if datetime.strptime(receipt['purchaseDate'], "%Y-%m-%d").day % 2 != 0:
        points += 6

    if 14 <= datetime.strptime(receipt['purchaseTime'], "%H:%M").hour <= 16:
        points += 10

    return points
