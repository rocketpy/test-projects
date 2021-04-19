import requests
import threading
from bs4 import BeautifulSoup


class WebParser:
    
    def __init__(self, url):
        self.url = url
        
        
    def get_page(self):
        try:
            req = requests.get(self.url)
        except requests.ConnectionError:
            return
        if req.status_code < 400:
            return req.content  # text
          
          
    def get_data(self, html):
        html = self.page_source
        soup = BeautifulSoup(html, 'lxml')
        try:
            el = soup.find('')
        except (Indexerror, AttributeError):
            return


    def main(self):
        page = self.get_page()
        
        
if __name__ == '__main__':
    web_page = WebParse('https://...')
    # web_page.main()
    
    # using threading
    p_1 = WebParser('https://')
    p_2 = WebParser('https://')
    parser_1 = threading.Thread(target=p_1.main)
    parser_2 = threading.Thread(target=p_2.main)
    # parser_1.start()
    # parser_2.start()

