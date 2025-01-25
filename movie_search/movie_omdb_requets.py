from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulStoneSoup
import time
import json
import requests


def omdb_get():
    #針對movie_id進行請求
    url = 'http://www.omdbapi.com/?i=tt8373206'
    headers = {
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    #需要api key才能請求成功
    if response.status_code == 200:
        print('成功取得資料')
    else:
        print(f'失敗，狀態碼: {response.status_code}')
        # 顯示伺服器返回的錯誤訊息
        print(f'錯誤資訊: {response.text}') 

def omdb_selenium_get():#進行擬人點擊取得資料
    try:
        service = Service(executable_path=r'C:\Users\User\Desktop\my-repo\chromedriver-win64\chromedriver.exe')
        options = webdriver.ChromeOptions()
        #建立chromedriver
        driver = webdriver.Chrome(service=service, options=options)
        #目標網站
        url = 'https://www.omdbapi.com/'
        driver.get(url)
        time.sleep(3)
        #找到對話框並輸入movier_id
        input_text = driver.find_element(By.ID, 'i')
        input_text.send_keys('tt8373206')
        #輸入後進行點擊
        button_search = driver.find_element(By.ID, "search-by-id-button")
        button_search.click()
        #等待動態畫面載入
        movie_text = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'alert-success'))
        )
        #當前的html
        html_content = driver.page_source
        #跳出pre標籤，用beautifulsoup下標籤取內容
        soup = BeautifulSoup(html_content, 'html.parser')
        movie_content_pre = soup.find('pre', class_='alert alert-success').text
        print(movie_content_pre)

    except:
        print('錯誤')

    finally:
        time.sleep(5)
        driver.quit()

omdb_selenium_get()