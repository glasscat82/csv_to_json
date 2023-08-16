# Иногда нужно сформировать json переменную из файла *.csv
бывает нужно для работы JavaScript фронтенд разработки (на react_js)

## ТЗ для работы с файлом /json/currency_transfers.csv
```
# Фильтруем список по стране. 
# Для этого в столбце «Страна» выбираем страну, выбранную валюту, + «Все страны валюта». 
# Если в таблице нет страны с карты, тогда по «Все страны»
```

```
# Группируем список полученных валют в столбце «Currency»:
# ▪ Если у валюты по всем строкам в столбце «Запрет» стоит «Да» - то валюту в списке не показываем
# ▪ В остальных случаях показываем буквенный код валюты из столбца «Currency»
```

## Результат /json/ два файла две переменные

запуск csv_to_json.py

```
# currency.json
{"AF": ["AED", "CNY", "EUR", "TRY", "USD", "UZS"], "AL": ["AED", "CNY", "EUR", "TRY", "UZS"], "AM": ["AED", "AMD", "CNY", "EUR", "TRY", "USD", "UZS"], "AO": ["AED", "CNY", "EUR", "TRY", "USD", "UZS"], "AT": ["AED", "CNY", "EUR", "TRY", "USD", "UZS"], "AZ": ["AED", "CNY", "EUR", "TRY", "USD", "UZS"], "BA": ["AED", "CNY", "EUR", "TRY", "UZS"], "BD": ["AED", "CNY", "TRY", "USD", "UZS"], "BY": ["AED", "BYN", "CNY", "EUR", "TRY", "USD", "UZS"], "CD": ["AED", "CNY", "TRY", "USD", "UZS"], "CN": ["AED", "CNY", "EUR", "TRY", "USD", "UZS"], "CZ": ["AED", "CNY", "EUR", "TRY", "UZS"], "DJ": ["AED", "CNY", "TRY", "USD", "UZS"], "DM": ["AED", "CNY", "EUR", "TRY", "USD", "UZS"], "EE": ["AED", "CNY", "TRY", "USD", "UZS"], "GE": ["AED", "CNY", "EUR", "GEL", "TRY", "USD", "UZS"], "GM": ["AED", "CNY", "EUR", "TRY", "USD", "UZS"], "HR": ["AED", "CNY", "EUR", "TRY", "UZS"], "HU": ["AED", "CNY", "EUR", "TRY", "UZS"], "IQ": ["AED", "CNY", "EUR", "TRY", "USD", "UZS"], "KG": ["AED", "CNY", "EUR", "KGS", "TRY", "USD", "UZS"], "KH": ["AED", "CNY", "EUR", "TRY", "USD", "UZS"], "KZ": ["AED", "CNY", "EUR", "KZT", "TRY", "USD", "UZS"], "LB": ["AED", "CNY", "TRY", "USD", "UZS"], "LT": ["AED", "CNY", "EUR", "TRY", "USD", "UZS"], "LV": ["AED", "CNY", "EUR", "TRY", "USD", "UZS"], "MD": ["AED", "CNY", "EUR", "TRY", "USD", "UZS"], "ME": ["AED", "CNY", "EUR", "TRY", "USD", "UZS"], "MN": ["AED", "CNY", "EUR", "TRY", "USD", "UZS"], "MT": ["AED", "CNY", "TRY", "USD", "UZS"], "MU": ["AED", "CNY", "EUR", "TRY", "USD", "UZS"], "MX": ["AED", "CNY", "TRY", "USD", "UZS"], "NA": ["AED", "CNY", "EUR", "TRY", "USD", "UZS"], "PR": ["AED", "CNY", "EUR", "TRY", "USD", "UZS"], "PS": ["AED", "CNY", "TRY", "USD", "UZS"], "RO": ["AED", "CNY", "EUR", "TRY", "UZS"], "RS": ["AED", "CNY", "EUR", "TRY", "USD", "UZS"], "RU": ["AED", "CNY", "EUR", "TRY", "USD", "UZS"], "SD": ["AED", "CNY", "EUR", "TRY", "USD", "UZS"], "SK": ["AED", "CNY", "EUR", "TRY", "UZS"], "SO": ["AED", "CNY", "TRY", "USD", "UZS"], "TJ": ["AED", "CNY", "EUR", "TRY", "USD", "UZS"], "TR": ["AED", "CNY", "EUR", "TRY", "USD", "UZS"], "TZ": ["AED", "CNY", "TRY", "USD", "UZS"], "UA": ["AED", "CNY", "EUR", "TRY", "USD", "UZS"], "UZ": ["AED", "CNY", "EUR", "TRY", "USD", "UZS"], "VU": ["AED", "CNY", "EUR", "TRY", "USD", "UZS"], "XK": ["AED", "CNY", "EUR", "TRY", "UZS"], "YE": ["AED", "CNY", "EUR", "TRY", "USD", "UZS"]}

# oll_country_currency.json
["AED", "CNY", "TRY", "UZS"]
```