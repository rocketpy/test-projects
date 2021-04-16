import csv
import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
# from multiprocessing import Pool


useragent = 'Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US)'
headers = {'User-Agent': useragent}




def save_cookies(requests_cookiejar, filename):
    with open(filename, 'wb') as f:
        pickle.dump(requests_cookiejar, f)


def load_cookies(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

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


def get_html(url):
    r = requests.get(url, headers=headers, timeout=3)
    # response.content
    # response.json()
    return r.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    # return


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
