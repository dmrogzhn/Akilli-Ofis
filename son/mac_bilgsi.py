import socket , time, requests
from bs4 import BeautifulSoup
import tkinter as tk
import pandas as pd

# BeautifulSoup kullandık ve verileri aldık
url = "https://www.sporx.com/galatasaray-fiksturu-ve-mac-sonuclari"

r = requests.get(url)
html = r.text
soup = BeautifulSoup(html,"html.parser")

# bugünden bir öncekine bakıyor ki dün maç var  mıydı bunun için de aşağıdaki tarih düzenlemesini yaptık
from datetime import datetime as dt
an = dt.now()

ay = an.month

gun = an.day
gun = gun - 1

aystr = str(ay)
gunstr = str(gun)

birles= gunstr + "." + aystr
#print(type(birles))

mac_bilgisi= "bulunamadı"

# burada class ı text-nowrap olanların hepsini yani tarihlerin hepsine erişiyor. daha sonra da bunların tectini bir trh değişkenine atıyor
# bu tarih değişkeni bizim dünki tarihimize yani birles değişkenimize eşit ise soucu getiriyor değil ise devam ediyor.
# burada getirdiği sonuca göre bir deictionary oluşturulacak ve 1-0 şekilnde karşılığı olacak
for k in soup.find_all("td", {'class':'text-nowrap'}):
    trh = str(k.text)
    if trh == birles:
        next1 = k.find_next('img')
        mac_bilgisi = next1['src']
        mac_bilgisi = mac_bilgisi[6:9]
        #print(mac_bilgisi[6:9])
        # print("oldu")
        # next1 = k.find_next('img')
        # print(type(next1))
        # print(next1['alt'])
        # print("BULUNDU" + " "+trh)
        # durum = next1['src']
        # print(durum)
        # print(durum[6:9])
        break  

mac_var_mi = 0
kazandi_mi = 0

#biz programda kazanıp kazanmamasına bakıyoruz o yüzden berabere de olsa kazanmadığı için kazandı mı kısmı 0 oluyor.
#burad da kontrolleri sağladık ve artık değişkenlerimiz hazır. yukarıdaki for döngüsünden gelen değere göre aşağıdaki if ler ile 1-0 atamalarını gerçekleştireceğiz
if  mac_bilgisi == "win":
    mac_var_mi = 1
    kazandi_mi = 1
elif mac_bilgisi == "los" or mac_bilgisi == "dra":
    mac_var_mi = 1
    kazandi_mi = 0

'''''
print(mac_var_mi)
print(kazandi_mi)
print(mac_bilgisi)
print("maç bilgisi bulunamadı")
'''