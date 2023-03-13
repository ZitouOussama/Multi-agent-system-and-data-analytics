import random

from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import random


def scrap_moroccan_news(numOfPages):
  website='moroccoworldnews'
  news_dict=[]
  numOfPages=int(numOfPages)

  # Create a headless Chrome browser
  chrome_options = Options()
  chrome_options.add_argument("--headless")
  chrome_options.add_argument("--log-level=3")
  browser = webdriver.Chrome(chrome_options=chrome_options)

 
  for i in range(1, numOfPages+1):
      url="https://www.moroccoworldnews.com/news-2/{}".format(i)
      # response = requests.get(url)
      # time.sleep(10)
      # soup = BeautifulSoup(response.content,"html.parser")
      # # for div in soup.findAll("div", {'class':'td-ss-main-sidebar'}): 
      # #   div.decompose() 
      # # for div1 in soup.findAll("div", {'class':'td-subcategory-header'}):
      # #   div1.decompose() 
      # print('card__post__body' in str(soup))
      # print('scrap..')
      # h3_elements = soup.findAll("div", {'class':'card__post__body'})
      # print(len(h3_elements))
      # for head in h3_elements:
      #   headl=head.getText()
      #   news_dict.append({'website':website,'url': url,'headline': headl})
      # Load the webpage
      browser.get(url)
      time.sleep(3)
      h3_elements = browser.find_elements(by=By.CSS_SELECTOR,value='#app > div > section.bg-content > div > div > div > div.wrapper__list__article.mt-10 > div > div.wrapper__list__article > div > div.col-md-8 > div.mb-4 > div > div > div > div > div > div.card__post__title > h3')
      for head in h3_elements:
        headl=head.text
        news_dict.append({'website':website,'url': url,'headline': headl, 'result': random.choice(['POSITIVE','POSITIVE','NEGATIVE'])})

  # Quit the browser
  browser.quit()

  news_df=pd.DataFrame(news_dict)
  news_df.to_csv("myScrapedData.csv" ,index=False, encoding='utf8')

""" def covid19TSdataScrapingMA():
    json_url ="./MA-times_series.csv"
    df = pd.read_csv(json_url,index_col=0)
    df.reset_index(level=0, inplace=True)
    df = df.rename(columns={'Dates / التواريخ': 'Dates', 'Cases / الحالات': 'Cases', 'Recovered / تعافى': 'Recovered', 'Deaths / الوفيات': 'Deaths'})
    df.to_csv("MA-times_series.csv", index=False) """

""" def regionDataScraping():
    json_url ="./regions.csv"
    df = pd.read_csv(json_url,index_col=0)
    df.reset_index(level=0, inplace=True)
    df = df.rename(columns={'Region / الجهة': 'Region', 'Total Cases / إجمالي الحالات': 'Confirmed', 'Active Cases / الحالات النشطة': 'Active','Total Deaths / إجمالي الوفيات': 'Deaths', 'Total Recovered / إجمالي المعافين': 'Recovered'})
    df.to_csv("MA-regions_data.csv", index=False)
 """


