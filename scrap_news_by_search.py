from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import os
import win32com.client

import news_paper_List as pp

nn=input()
driver = webdriver.Firefox()
driver.implicitly_wait(3)
driver.get('https://www.google.com/')
g_s_button = driver.find_element(By.XPATH,"//*[@class='gLFyf']")
g_s_button.send_keys(nn)
g_s_button.send_keys(Keys.ENTER)

try:
    driver.find_element(By.LINK_TEXT, "News").click()
except:
    driver.find_element(By.LINK_TEXT, "সংবাদ").click()
href_values = []
for pages in range(20):
    channel_name =driver.find_elements(By.XPATH,"//a[@class='WlydOe']") 

    href_values += [{x.get_attribute('href').split('/')[2]:x.get_attribute('href')} for x in channel_name]

    # Print the result
    print(len(href_values))

    try:
        driver.find_element(By.XPATH,"(//*[@class='d6cvqb BBwThe'])[2]").click()
    except:
        break


enableList =[pp.dhaka_tribune,
             pp.bangla_dhaka_tribune,
             pp.amar_songbad,
             pp.prothom_alo,
             pp.kaler_kontho,
             pp.new_diganta,
             pp.ittefaq,
             pp.jugantor,
             pp.buiseness_standard,
             pp.daily_star,
             pp.en_prothom_alo,
             pp.bd_news]

newsList = []
newsLink = []

def button_click(url):
    # This function is called when a button is clicked
    print(f"Opening link: {url['url']}")
    # You can implement logic to open the link in a browser here
    driver.get(url['url'])
    try:
        headline = driver.find_element(By.XPATH, url['head_line']).text
    except:
        headline = ''

    try:
        news_author = driver.find_element(By.XPATH, url['news_author_xpath']).text
    except:
        news_author =''

    try:
        news_time = driver.find_element(By.XPATH,url['news_time_xpath']).text
    except:
        news_time = ''

    try:
        news_text_ele = driver.find_elements(By.XPATH,url['news_text_xpath'])
        news_text = ' '.join([element.text for element in news_text_ele])
    except:
        news_text =''
    
    news = {
    'source': url['newspaper_url'].split('.')[1],
    'headline': headline,
    'news_author': news_author,
    'news_time': news_time,
    'news_text': news_text
}
    newsList.append(news)
    print(news_author)

# Create buttons dynamically based on the data_list
for data_dict in href_values:
    key = list(data_dict.keys())[0]
    for up in enableList:
        if key in up['newspaper_url']:
            up['url'] = data_dict[key]
            print(up['url'])
            try:
                button_click(up)
            except:
                continue
driver.quit()
df = pd.DataFrame(newsList)
try:
    excel = win32com.client.GetActiveObject("Excel.Application")
    excel.Quit()
except:
    pass
df.to_excel(nn+'.xlsx',index=False, header=True)
    
