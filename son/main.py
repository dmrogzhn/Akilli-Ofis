'''''
# import yz2_predict as yz2
# import yz1_predict_2 as yz1
# import pyodbc


# # predict projelerinden gelen değerleri değişkenlere atayıp daha okunaklı ve erişilebilir hale getirdik
# # buradan gelen sonuçları da SQL e atarak C# ile oluşturulmuş arayüze veri gönderebileceğiz

# muzik = yz2.muzik
# koku = yz2.koku
# icecek = yz2.icecek
# klima = int(yz2.tahmin_edilen_klima_derecesi)
# duygu = yz1.predict_result

# # SQLCONNECTİON

# server = 'DESKTOP-S3S5IBG\SQLEXPRESS'
# database = 'lisans_tez'
# username = 'sa'
# password = 's'

# conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# try:
#     cursor = conn.cursor()
#     cursor.execute(f"INSERT INTO tbl_sonuclar (muzik,koku,icecek,klima,duygu) values {muzik},{koku},{icecek},{klima},{duygu}")
#     cursor.commit()
# finally:
#     conn.close()

# print(klima)

'''

import yz2_predict as yz2
import yz1_predict_2 as yz1
import pyodbc

# predict projelerinden gelen değerleri değişkenlere atayıp daha okunaklı ve erişilebilir hale getirdik
# buradan gelen sonuçları da SQL e atarak C# ile oluşturulmuş arayüze veri gönderebileceğiz

muzik = yz2.muzik
koku = yz2.koku
icecek = yz2.icecek
klima = int(yz2.tahmin_edilen_klima_derecesi)
duygu = yz1.predict_result

print(muzik)
print(koku)
print(icecek)
print(klima)
print(duygu)

# SQL Bağlantısı

server = 'DESKTOP-S3S5IBG\\SQLEXPRESS'
database = 'lisans_tez'
username = 'sa'
password = 's'

conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

try:
    cursor = conn.cursor()
    query = """
    INSERT INTO tbl_sonuclar (muzik, koku, icecek, klima, duygu)
    VALUES (?, ?, ?, ?, ?)
    """
    cursor.execute(query, (muzik, koku, icecek, klima, duygu))
    conn.commit()
    print("Veriler başarıyla eklendi.")
except pyodbc.Error as e:
    print("Hata oluştu:", e)
finally:
    conn.close()



