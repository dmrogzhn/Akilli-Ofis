import pickle
import joblib
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import pandas as pd
import hava_durum as hva
import yz1_predict_2 as yz1 

# Pickle ile kaydedilmiş model dosyasını yükleme
with open('yz2_model.pkl', 'rb') as pickle_file:
    model_data = pickle.load(pickle_file)

# HDF5 dosyasını geçici olarak kaydedip model olarak yükleme
with open('yz2_temp_model.h5', 'wb') as model_file:
    model_file.write(model_data)

# Modeli custom_objects ile yükleme
model = load_model('yz2_temp_model.h5', custom_objects={'mse': tf.keras.losses.mse})

# Scaler'ı yükleme
scaler = joblib.load('yz2_scaler.save')

derece = hva.hava_derecesi
duygu = yz1.predict_result


# Sütun isimlerini tanımlıyoruz
columns = ["duygu_Keyifli", "duygu_Keyifsiz", "duygu_Mutlu", "duygu_Sinirli","duygu_Üzgün"]

# Örnek veri çerçevesi oluşturuyoruz (boş)
df = pd.DataFrame(columns=columns)

# Fonksiyonumuzu tanımlıyoruz
def set_emotion(df, emotion):
    # Tüm sütunları 0 olarak ayarlıyoruz
    df.loc[0, columns] = 0
    # Gelen duygu durumuna göre ilgili sütunu 1 yapıyoruz
    df.loc[0, f"duygu_{emotion}"] = 1

# Örnek olarak duygu durumu "sinirli" olan bir veri ekliyoruz
set_emotion(df, duygu)

print(df.values)

liste = df.values.flatten().tolist()

liste.insert(0, derece)

print(liste)

# # Girdi özellikleri
input_features = liste

input_features = np.array(input_features).reshape(1,-1)


# # Veriyi ölçeklendirme
X_new = scaler.transform(input_features)

# # Tahmin yapma
predictions = model.predict(X_new)

# # Tahminleri DataFrame olarak gösterme
output_targets = ["klima_derecesi","muzik_caz_piyano","muzik_electric_blues","muzik_klasik_meditasyon","muzik_metallica","icecek_cay","icecek_filtre","icecek_latte","koku_dag_esintisi","koku_deniz","koku_orman","koku_papatya"]
pred_df = pd.DataFrame(predictions, columns=output_targets)

# En yüksek tahmin değerini bulma ve çıktıyı oluşturma
muzik_columns = ["muzik_caz_piyano", "muzik_electric_blues", "muzik_klasik_meditasyon", "muzik_metallica"]
icecek_columns = ["icecek_cay", "icecek_filtre", "icecek_latte"]
koku_columns = ["koku_dag_esintisi", "koku_deniz", "koku_orman", "koku_papatya"]

en_yuksek_muzik = pred_df[muzik_columns].idxmax(axis=1).iloc[0]
en_yuksek_icecek = pred_df[icecek_columns].idxmax(axis=1).iloc[0]
en_yuksek_koku = pred_df[koku_columns].idxmax(axis=1).iloc[0]
tahmin_edilen_klima_derecesi = pred_df["klima_derecesi"].iloc[0]



# Sonuçları daha okunabilir bir biçimde yazdırma


# print(f"Tahmin edilen klima derecesi: {tahmin_edilen_klima_derecesi}")
# print(f"Tahmin edilen müzik türü: {en_yuksek_muzik.replace('muzik_', '').replace('_', ' ')}")
# print(f"Tahmin edilen içecek türü: {en_yuksek_icecek.replace('icecek_', '').replace('_', ' ')}")
# print(f"Tahmin edilen koku: {en_yuksek_koku.replace('koku_', '').replace('_', ' ')}")

muzik = en_yuksek_muzik.replace('muzik_', '').replace('_', ' ')
icecek = en_yuksek_icecek.replace('icecek_', '').replace('_', ' ')
koku = en_yuksek_koku.replace('koku_', '').replace('_', ' ')

def add_underscore_after_first_word(s):
    # Split the string into words
    words = s.split()
    # Check if there are at least two words
    if len(words) >= 2:
        # Join the first word with the rest of the string with an underscore
        return words[0] + '_' + ' '.join(words[1:])
    else:
        # If there is only one word or the string is empty, return it as is
        return s
muzik = add_underscore_after_first_word(muzik)

print(muzik)

#print(pred_df)
