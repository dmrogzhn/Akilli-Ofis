import requests
from lxml import html

# Hedef web sitesinin URL'si
url = 'https://www.trthaber.com/denizli-hava-durumu.html'

# Web sitesinden içeriği çek
response = requests.get(url)
content = response.content

# HTML içeriğini parse et
doc = html.fromstring(content)

# XPath kullanarak belirli bir elementin içindeki metni al
result = doc.xpath('//*[@id="week_0_tab"]/span[2]')[0]  #bulut örtüsünün xpath i
result2 = doc.xpath('//*[@id="week_0_tab"]/span[3]/span[2]')[0]  # derecenin xpath i

bulut_ortusu= str(result.text_content())
bulut_ortusu= bulut_ortusu.replace(" ","_")
hava_derecesi= str(result2.text_content())#aldığımız değerler bi html tagı olarak geliyordu onu str formatına çevirdik ki işlem yapabilelim istersek int de yapardık

# hava derecesini alırken sonunda C olan kısmını ve baştaki birçok boşluğu almamız lazım o yüzden aşağıdaki işlemleri yapıyoruz
hava_derecesi = hava_derecesi.strip()           #burada str ifade içindeki tü boşluları kaldırdık
hava_derecesi=hava_derecesi[0:-2]               #burada da sonraki derece ifadesini kaldırdık sondaki iki ifadeye kadar al dedik
#hava_derecesi = hava_derecesi.replace(".",",")  #burada da bizim datasetimizde hava derecelerimiz nokta olarak değil virgül olarak bulunmakata o yüzden gelen veriyi de virgüllü hale çevirdik
hava_derecesi = float(hava_derecesi)
#print(hava_derecesi)
#print(bulut_ortusu)