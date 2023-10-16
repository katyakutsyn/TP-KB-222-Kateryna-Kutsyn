import requests


response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
exchange_rates = response.json()


currency_rates = {}
for rate in exchange_rates:
    currency_rates[rate['cc']] = rate['rate']


supported_currencies = ["EUR", "USD", "PLN"]


while True:
    currency = input("Введіть валюту (EUR, USD, PLN): ").upper()
    if currency not in supported_currencies:
        print("Ця валюта не підтримується. Спробуйте ще раз.")
    else:
        break

amount = float(input("Введіть кількість валюти: "))


converted_amount = amount * currency_rates[currency]


print(f"{amount} {currency} = {converted_amount} ukrainian hryvnia")
