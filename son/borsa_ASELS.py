import requests
from lxml import html

# Hedef web sitesinin URL'si
url = 'https://uzmanpara.milliyet.com.tr/borsa/hisse-senetleri/aselsan-asels/'
# Web sitesinden içeriği çek
response = requests.get(url)
content = response.content

# HTML içeriğini parse et
doc = html.fromstring(content)

# XPath kullanarak belirli bir elementin içindeki değeri (inner HTML) al
result = doc.xpath('/html/body/div[13]/div[6]/div[3]/div[1]/table/tbody/tr[1]/td[2]/span[1]')[0]

# Elementin içindeki değeri ekrana yazdır
sonuc = str(result.text_content()).replace(",",".")
sonuc = sonuc.rstrip("%")
sonuc = float(sonuc)

#print(sonuc)
