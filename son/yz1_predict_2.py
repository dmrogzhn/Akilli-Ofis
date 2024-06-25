import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, LabelEncoder, OneHotEncoder
import joblib

# Borsa ve hava durumu verilerini çekme kısmı
import borsa_ASELS as asel
import borsa_FROTO as froto
import borsa_THY as thy
import mac_bilgsi as mac
import hava_durum as hva
#import trafik_bilgi as trf

asels = asel.sonuc
ford = froto.sonuc
tr_hava = thy.sonuc
macvarmi = mac.mac_var_mi
mackazandimi = mac.kazandi_mi
derece = hva.hava_derecesi
bulut = hva.bulut_ortusu
#trafik = trf.sonuc

durum_encoded = {
    "Az_Bulutlu": "durum_1",
    "Açık": "durum_2",
    "Dolu": "durum_3",
    "Hafif_Kar_Yağışlı": "durum_4",
    "Hafif_Yağmurlu": "durum_5",
    "Kar_Yağışlı": "durum_6",
    "Karla_Karışık_Yağmur": "durum_7",
    "Kırağı": "durum_8",
    "Parçalı_Bulutlu": "durum_9",
    "Pus": "durum_10",
    "Sağnak_Yağışlı": "durum_11",
    "Sisli": "durum_12",
    "Tipi": "durum_13",
    "Yağmurlu": "durum_14",
    "Çok_Bulutlu": "durum_15"
}

duygu_encoded = {
    0: "Keyifli",
    1: "Keyifsiz",
    2: "Mutlu",
    3: "Sinirli",
    4: "Üzgün"
}

gelen_deger = durum_encoded[bulut]
veriler = [derece, macvarmi, mackazandimi, tr_hava, asels, ford,20]

# Tüm durum değişkenlerini başlangıçta 0 olarak ayarla
durumlar = [0] * len(durum_encoded)

# Gelen değere karşılık gelen durum değişkenini 1 olarak ayarla
for key, value in durum_encoded.items():
    if value == gelen_deger:
        durumlar[int(value.split('_')[-1]) - 1] = 1

# Verileri ve durumları birleştir
birlesim = veriler + durumlar
birlesim = np.array(birlesim).reshape(1, -1)  # Tek örnek olduğundan dolayı reshape gerekli

# Modeli ve scaler'ı yükle
loaded_model = joblib.load('random_forest_model.pkl')
scaler = joblib.load('scaler.pkl')  # Scaler'ı kaydettiğiniz isimle yükleyin

# Scale işlemi
birlesim_scaled = scaler.transform(birlesim)

# Tahmin yap
prediction = loaded_model.predict(birlesim_scaled)
print("Tahmin edilen duygu: ", duygu_encoded[prediction[0]])

predict_result = duygu_encoded[prediction[0]]