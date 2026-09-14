import requests
from pprint import PrettyPrinter

BASE_URL = "http://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

printer = PrettyPrinter()  # for json format

response = requests.get(BASE_URL + ALL_JSON)
printer.pprint(response)
