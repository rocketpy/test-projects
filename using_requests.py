import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError


useragent = 'Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US)'
headers = {'User-Agent': useragent}


def write_csv(data):
    with open('result.csv', 'a') as f:
        order = ['Doctor', 'Work time', 'Address', 'Rating']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)


def get_html(url):
    useragent = {'User-Agent': choice(useragents)}
    r = requests.get(url, headers=headers, timeout=3)
    # response.content
    return r.text  #


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    # h1 = soup.find('div', id='home-welcome').find('header').find('h1').text
    return


def main():
    url = 'https://www.zooplus.de/tierarzt/results?animal_99=true'
    for url in 
    try:
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

