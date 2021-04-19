import requests
from bs4 import BeautifulSoup


class WebParser:
    def __init__(self, url):
        self.url = url
        
        
    def get_page(self):
        try:
            req = requests.get(self.url)
        except requests.ConnectionError:
            pass
        if req.stsus_code < 400:
            return req.content
          
          
    def get_data(self, html):
        html = self.page_source
        soup = BeautifulSoup(html, 'lxml')
        
        
    def main(self):
        pass
        
        
if __name__ == '__main__':
    web_page = WebParse('https://...')
    web_page.main()
        
