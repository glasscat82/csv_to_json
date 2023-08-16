''' csv to json '''
import csv
import json
from datetime import datetime
from art import tprint

def get_country(currecy):   
    return set(i[6].strip() for i in currecy if len(i[6].strip())>0)

def get_oll_country_currency(currecy):
    gc = []
    for r in currecy:
        if r[7] != 'Все страны':
            continue
        
        if r[5].strip() == 'Да':
            continue
        
        gc.append(r[2].strip())
    
    return sorted(set(gc))

def get_currency(country_code, currecy):
    gc = []
    for r in currecy:
        if r[6] != country_code:
            continue
        
        if r[5].strip() == 'Да':
            continue
        
        gc.append(r[2].strip())
    
    return sorted(set(gc))

def open_csv(patch):
    currecy = []
    with open(patch, encoding='cp1251') as f:
        reader = csv.reader(f, delimiter=';')
        for index, row in enumerate(reader, 0):
            if index == 0:
                continue
            # print(row)
            currecy.append(row)
    
    return currecy

def write_json(data, path = None):
    path = './json/currency.json' if path is None else path
    with open(path, 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)  # indent=2, 

def main():
    start = datetime.now()
    
    #---start
    tprint('CSV >> JSON', font='bulbhead')
    currecy = open_csv(patch = './json/currency_transfers.csv')
    country = sorted(get_country(currecy))
    gcc = get_oll_country_currency(currecy)  # валюта для всех стран и т.д.
    print(f'[+] oll currency country {gcc}')
    print(f'[+] count country {len(country)}')
    print(f'[+] code countrys {country}')
    # print(country)
    
    json = {}
    for code in country:
        # тут мы объединяем список валют со списком валют "всех стран"
        json[code] = sorted(set([*get_currency(code, currecy), *gcc]))
        # print(code)
        # print(json[code])
    
    write_json(gcc, './json/oll_country_currency.json')
    write_json(json, './json/currency.json')

    # print(json)
    #---end
    
    end = datetime.now()
    print(f'[+] lead time {str(end-start)}')

if __name__ == '__main__':
    main()