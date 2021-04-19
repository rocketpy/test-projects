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
        if req.status_code < 400:
            return req.content
          
          
    def get_data(self, html):
        html = self.page_source
        soup = BeautifulSoup(html, 'lxml')
        
        
    def main(self):
        while True:
            page = self.get_page()
            self.get_data(page)
        
        
if __name__ == '__main__':
    web_page = WebParse('https://...')
    web_page.main()
        
