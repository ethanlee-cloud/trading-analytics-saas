import csv


def load_prices(file_path):
    prices = []

    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            prices.append({
                "date": row["date"],
                "open": float(row["open"]),
                "close": float(row["close"]),
            })

    return prices
