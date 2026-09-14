import comm
import requests
from pprint import PrettyPrinter

API_KEY = "57abd3885934f86b9b30378c48aadada2dc6"
BASE_URL = "https://currencyapi.net"
OUTPUT = "json"


printer = PrettyPrinter()


def get_currencies():
    endpoint = f"/api/v2/currencies?&output={OUTPUT}&key={API_KEY}"

    url = BASE_URL + endpoint
    data = requests.get(url).json()["currencies"]
    data = list(data.items())
    # data = data.sort()

    # printer.pprint(data)

    return data


def print_currencies(currencies):
    for currency in currencies:
        _id = currency[0]
        name = currency[1]
        print(f"{_id} - {name}")


def exchange_rate(currency1, currency2):
    endpoint = f"/api/v2/rates?base={currency1}&key={API_KEY}"

    url = BASE_URL + endpoint
    data = requests.get(url).json()["rates"]
    rate = data[currency2]

    if len(data) == 0:
        print("Invalid currencies")
        return

    print(f"{currency1} -> {currency2} = {rate}")

    # printer.pprint(data)
    return rate


def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)

    if rate is None:
        return

    try:
        amount = float(amount)

    except:
        print("Invalid amount.")
        return

    converted_amount = round(rate * amount, 3)
    print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")

    return converted_amount


def main():
    currencies = get_currencies()

    print("Welcome to the currency converter!")
    print("List - lists the different currencies")
    print("Convert - convert from one curreny to another")
    print("Rate - get the exchange rate of two currencies")
    print()

    while True:
        command = input("Enter a command (q to quit): ")

        if command == "q":
            break

        elif command == "list":
            print_currencies(currencies)

        elif command == "convert":
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to convert to: ").upper()
            amount = input(f"Enter a amount in {currency1}: ")
            convert(currency1, currency2, amount)

        elif command == "rate":
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to convert to: ").upper()
            exchange_rate(currency1, currency2)

        else:
            print("Unrecognized command!")


main()
