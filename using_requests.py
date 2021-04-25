import csv
import requests
import datetime
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
from requests_jwt import JWTAuth
# import python_jwt as jwt


useragent = 'Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US)'
headers = {'User-Agent': useragent}
# headers = {'accept':'*/*', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
# head = {'Authorization': 'Bearer {}'.format(myToken)}
claims = {'consumerId': 'My App ID',
          'httpMethod': 'GET'}

jwtoken = jwt.generate_jwt(claims, 'My secret', 'HS256', datetime.timedelta(minutes=5))
response = requests.get('http://httpbin.org/get', jwtoken)
print(response.json())

# auth = JWTAuth('MySecretToken')
# requests.get("http://", auth=auth)
s = requests.Session()
req = s.get(url, headers=headers)

r = s.get("https://")

"""
s = requests.Session()
r = s.get(url, headers=heads)
cookie = r.headers['Set-Cookie']

heads_2 = {'authority': 'www.zooplus.de',
           'accept': 'application/json',
           'accept-encoding': 'gzip, deflate, br',
           'accept-language': 'ru,uk;q=0.9,ru-RU;q=0.8,en-US;q=0.7,en;q=0.6',
           'cookie': f'{cookie}',
           'referer': 'https://www.zooplus.de/tierarzt/results',
           'sec-ch-ua': 'Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
           'authorization': '',
           'x-site-id': '1'}
"""

"""
def get_req(url):
    try:
        res = requests.get(url)
        return json.dumps(res.json(), indent=4)
    except Exception as ex:
        return f"Message: {ex}"
  
  
def post_req(url, data):
    try:
        res = requests.post(url, json=data)
        return json.dumps(res.json(), indent=4)
    except Exception as ex:
        return f"Message : {ex}"
        
if __name__ == '__main__':
    main()
"""

"""
import python_jwt as jwt
# Create claims dictionary for generation of JwToken
claims = {'consumerId': 'My App ID',
          'httpMethod': 'GET'}

import datetime
# create JWToken
jwtoken = jwt.generate_jwt(claims, 'My secret', 'HS256', datetime.timedelta(minutes=5))

response = requests.get('http://httpbin.org/get', jwtoken)
print(response.json())
"""

"""
proxies = {
  'http': 'http://10.10.1.10:3128',
  'https': 'http://10.10.1.10:1080',
}
requests.get('http://', proxies=proxies)
"""
# using proxy
# session = requests.Session()
# session.proxies.update(proxies)
# session.get('http://')


def save_cookies(requests_cookiejar, filename):
    with open(filename, 'wb') as f:
        pickle.dump(requests_cookiejar, f)


def load_cookies(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)
    
    
"""
s = requests.Session()
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'\
           'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
           'Accept':'text/html,application/xhtml+xml,application/xml;'\
           'q=0.9,image/webp,*/*;q=0.8'}
url = 'https:'
req = session.get(url, headers=headers)

s.get('https://')
r = s.get("https://")
print(r.text)
"""

# save cookies
r = requests.get(url)
save_cookies(r.cookies, filename='cookies')        

# load cookies and do a request
r = requests.get(url, cookies=load_cookies(filename='cookies'))
# print(r.json())


def write_csv(data):
    with open('result.csv', 'a') as f:
        order = ['Doctor', 'Work time', 'Address', 'Rating']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)


def get_data():
        with open('data.txt') as json_file:
        data = json.load(json_file)
        # print(data)
        print(json.dumps(data, indent=4, sort_keys=True))


def main():
    # url = 'https://www.zooplus.de/tierarzt/results?animal_99=true'
    for i in range(1, 4):
        try:
            url = f'https://www.zooplus.de/tierarzt/results?animal_99=true%27&page={i}'
            response = requests.get(url)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            print('Success!')
        # print(get_data(get_html(url)))


if __name__ == '__main__':
    main()
    
    

"""
# for multiprocessing
def make_all(url):
    text = get_html(url)
    get_page_data(text)

def main():
    url = ''
    urls = [url.format(str(i)) for i in range(1, 4)]

    with Pool(20) as p:  # pools is a process
        p.map(make_all, urls)  # p.map to every func make_all
"""
