import requests
from bs4 import BeautifulSoup

def main():
    url ='https://boxofficetw.tfai.org.tw/'
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print('失敗')   
    else:   
        with open('example.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
        print('成功')

    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.select('div')
    for title in titles:
        print(title)

main()