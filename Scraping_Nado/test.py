import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"}

url = "https://edu.labs.go.kr/front/croom/examRecord.do"
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")


tables = soup.find_all("table", attrs={'class': 'soup.find('})


for table in tables:
    print(table.get_text())
