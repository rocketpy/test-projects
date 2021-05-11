import os
import pandas as pd
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
# https://chromedriver.chromium.org/downloads


driver = webdriver.Chrome()


def update_csv():
    df = pd.read_csv("file.csv", names=['Doctor', 'Work time', 'Address', 'Rating'])
    df.to_csv("result.csv", index=False)
    os.remove("file.csv")


# get data from a page
def get_data(drive):
    html = drive.page_source
    soup = BeautifulSoup(html, 'lxml')
    card_list = soup.find_all('article', class_='result-intro')

    data = []
    # get data from a card
    for card in card_list:
        name = card.find('h1', class_='result-intro__title').get_text().strip()
        try:
            subtitle = card.find('h2', class_='result-intro__subtitle').text
        except:
            subtitle = '  '
        work_time = card.find('span', class_='daily-hours').text
        address = card.find('p', class_='result-intro__address').text
        star_rating = len(soup.find('span', class_='star-rating'))
        rating = card.find('span', class_='result-intro__rating__note').text
        doctor_name = f"{name}   {subtitle}"
        ratings = f"{rating}   {star_rating} stars "
        new_data = {'Doctor': doctor_name, 'Work_Time': work_time,
                    'Address': address, 'Rating': ratings}

        data.append(new_data)

    df = pd.DataFrame(data)
    df.to_csv('file.csv', mode='a', index=False, encoding='utf-8', header=False)


# go to a website
driver.get("https://www...")
sleep(3)
# get a cookies
driver.find_element_by_id('onetrust-accept-btn-handler').click()
sleep(3)
# click on checkbox "Hunde"
driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div[4]/div[1]/section/div[1]/fieldset/div/div[1]/div[1]/label/input').click()
sleep(2)
# pages counter
counter = 3  # pages
while counter > 0:
    # scroll down a page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    sleep(2)
    get_data(driver)
    counter -= 1
    if counter > 0:
        # click on next page
        driver.find_element_by_css_selector('#search-results-pane-tab1 > div.pagination-group > nav > ul > li:nth-child(9) > a > span').click()
        sleep(3)
    else:
        # update a csv file
        update_csv()
        # driver quit
        driver.quit()

