from rates_parse import RatesParser

rp = RatesParser("exchange_rates.json")
print(rp.date)
print(rp.base_rate)
rp.show_currency('jpy')
print(rp.convert('gbp', 'eur', 5.99))
