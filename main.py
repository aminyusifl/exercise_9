import requests

def get_coin_price(coin):
    coin = coin.upper()
    url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={coin}"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return "False coin name or API is blocked"

    data = response.json()
    try:
        return data["lastPrice"]
    except KeyError:
        return "Cannot find coin."

coin = input("Enter the coin symbol: ")
result = get_coin_price(coin)
print("\nResult: ", result)
