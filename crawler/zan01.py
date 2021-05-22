import requests
import re
from bs4 import BeautifulSoup
import time
from random import randint
import json


base_url = 'https://zan01.com/lotto649/history/'
page_rage = range(1, 49)
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

def big_lottery():

    record_list = []

    for idx in page_rage:

        to_sleep = randint(3, 13)
        print('sleep %s secs to avoid frequent query...next page: %s' % (to_sleep, idx))
        time.sleep(to_sleep)

        url = base_url + str(idx)
        res  = requests.get(url, headers=headers)
        #soup = BeautifulSoup(res.text,'html.parser')
        soup = BeautifulSoup(res.text,'lxml')
        table = soup.find_all('body')[0].find_all('table', recursive=False)[0]
        tbody = table.find_all('tbody', recursive=False)[0]
        tr_array = tbody.find_all('tr', recursive=False)
        for tr in tbody.find_all('tr', recursive=False):
            th_array = tr.find_all('th')
            if not len(th_array) == 2:
                continue
            record = {
                'identity': None,
                'date': None,
                'ordered_numbers': [],
                'special_number': None,
            }
            record['identity'] = th_array[0].text.strip()
            record['date'] = th_array[1].text.strip()
            td_array = tr.find_all('td', recursive=False)
            for td in td_array:
                text = str(td.text).strip()
                if len(text) == 12:
                    numbers = re.findall('..', text)
                    record['ordered_numbers'] = numbers
                else:
                    record['special_number'] = text
                    break # got all we need, exit loop
            # check before add to list
            if record['ordered_numbers'] and record['special_number']:
                record_list.append(record)

    record_list = sorted(record_list, key=lambda k: k['identity']) 
    return record_list

record_list = big_lottery()

# write to file
'''
with open('tw_lottery_649.json', 'w') as outfile:
    json.dump(record_list, outfile)
'''