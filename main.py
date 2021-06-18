from requests import post
from bs4 import BeautifulSoup
from html_table_parser import parser_functions as parser

url = 'https://findip.opendocs.co.kr/find'

def get_ip():
    return '119.196.25.64'

def make_data():
    return {'ip' : get_ip()}

def request(data):
    res = post(url, data=data)

    soup = BeautifulSoup(res.text, 'html.parser')

    location = soup.select('#location')[0]

    my_ip = location.p.text

    tables = soup.find_all('table')

    p = parser.make2d(tables[0])
    sort_of_ip =  p[1][1]
    nation_code = p[2][1]

    p = parser.make2d(tables[1])
    name_of_network = p[2][1]
    name_of_org = p[3][1]
    address_of_org = p[4][1]
    num_of_address = p[6][1]

    p = parser.make2d(tables[2])
    name_of_real_org = p[2][1]
    address_of_real_org = p[3][1]
    num_of_real_address = p[5][1]

    return {'ip' : my_ip,
            'sort' : sort_of_ip,
            'code' : nation_code,
            'name' : name_of_real_org,
            'address' : address_of_real_org,
            'num' : num_of_real_address}

print(request(make_data()))
