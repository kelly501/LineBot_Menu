import requests as requests
from bs4 import BeautifulSoup
from linebot import LineBotApi
from linebot.models import TextSendMessage
import os


#休息
def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec;

#目標網站
url = "https://www.kurasushi.tw/products"
#請求網站
r = requests.get(url) #檢查回應。如果是200則成功請求
#將整個網站的程式碼爬下來
soup = BeautifulSoup(r.content, "html.parser")  # Python內建解析器

allname = soup.find_all('div', {'class':'ProductListItem__Name-ne7ga3-3 eUgBxf'}) #取得所有菜品
allprice = soup.find_all('div', {'class':'ProductListItem__Price-ne7ga3-4 hBIxQy'})

name = "藏壽司 本月Menu:\n\n"
price = ""
for n, p in zip(allname, allprice):
    name = name+n.getText()+" "+p.getText()+'\n'
print(name)

LINE_UUID = os.environ['LINE_UUID']
TOKEN = os.environ['TOKEN']

line_uuid = LINE_UUID
line_bot_api = LineBotApi(TOKEN)
line_bot_api.push_message(
    line_uuid,
    TextSendMessage(text=name))
