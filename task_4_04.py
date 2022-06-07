import utils

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
print(utils.currency_rates(url, 'USd'))
print(utils.currency_rates(url, 'GBP2'))

print(utils.currency_rates_advanced(url, 'USd'))
print(utils.currency_rates_advanced(url, 'GBP2'))

