import requests
from bs4 import BeautifulSoup


useragent = 'Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US)'
headers = {'User-Agent': useragent}


def get_html(url):
    useragent = {'User-Agent': choice(useragents)}
    r = requests.get(url, headers=headers, timeout=3)
    return r.text  #


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    # h1 = soup.find('div', id='home-welcome').find('header').find('h1').text
    return


def main():
    url = 'https://www.zooplus.de/tierarzt/results?animal_99=true'
    print(get_data(get_html(url)))


if __name__ == '__main__':
    main()

