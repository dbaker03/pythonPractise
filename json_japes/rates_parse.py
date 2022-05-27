import json


class RatesParser:
    def __init__(self, file_path):
        self._rates = self._open_json_file(file_path)
        self.base_rate = self._rates['base']
        self.date = self._rates['date']
        self.gpb = self._rates['rates']['GBP']
        self.usd = self._rates['rates']['USD']
        self.jpy = self._rates['rates']['JPY']

    def _open_json_file(self, file_path: str) -> dict:
        with open(file_path) as json_file:
            return json.load(json_file)

    def show_currency(self, currency_name):
        currency_name = currency_name.upper()

        print(f"On: {self.date}")
        print(f"1 {self.base_rate} will get you {self._rates['rates'][currency_name]} {currency_name}")
        print(f"1 {currency_name} will get you {1 / self._rates['rates'][currency_name]:.5f} {self.base_rate}")

    def convert(self, starting_currency, final_currency, amount):
        self._rates['EUR'] = 1
        starting_currency = starting_currency.upper()
        final_currency = final_currency.upper()
        amount_in_base = amount * self._rates[starting_currency]
        return amount_in_base * self._rates[final_currency]


if __name__ == '__main__':
    c = RatesParser("exchange_rates.json")
    while True:
        print("\n" * 50)
        c.show_currency(input("Enter currency: "))
        input()

