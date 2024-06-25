import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Reshape,Input
import matplotlib.pyplot as plt

data = pd.read_csv('yz2-datas.csv')

print(data.head())

#hepsini küçük harf aptık ve baştaki sondaki boşlukları komple temizledik
data[["duygu","muzik","icecek","koku"]] = data[["duygu","muzik","icecek","koku"]].applymap(lambda x: x.lower())
data[["duygu","muzik","icecek","koku"]] = data[["duygu","muzik","icecek","koku"]].applymap(lambda x: x.strip())

#ENCODİNG İŞLEMLERİ UYGULAYACAĞIMIZ SÜTUNLARI SEÇTİK
sutunlar = ["duygu", "muzik", "icecek", "koku"]
df_encoded = pd.get_dummies(data, columns=sutunlar)

#df_encoded.to_excel("yz2_encoded.xlsx")

print(df_encoded)

input_features = ["derece","duygu_keyifli","duygu_keyifsiz","duygu_mutlu","duygu_sinirli","duygu_üzgün"]
output_targets = ["klima_derecesi","muzik_caz_piyano","muzik_electric_blues","muzik_klasik_meditasyon","muzik_metallica","icecek_cay","icecek_filtre","icecek_latte","koku_dag_esintisi","koku_deniz","koku_orman","koku_papatya"]

train_data, test_data = train_test_split(df_encoded, test_size=0.2, random_state=42)

train_data, val_data = train_test_split(train_data, test_size=0.2, random_state=42)


scaler = MinMaxScaler()

X_train = scaler.fit_transform(train_data[input_features])
X_val = scaler.transform(val_data[input_features])
X_test = scaler.transform(test_data[input_features])

y_train = train_data[output_targets].values
y_val = val_data[output_targets].values
y_test = test_data[output_targets].values

model = Sequential()
model.add(Input(shape=(len(input_features),)))# dens katmanını değiştir // relu yerine bir de farklı kullan

model.add(Reshape((1, 6)))
model.add(LSTM(6, activation='tanh'),1)# burayı 6 yap
model.add(Dense(len(output_targets)))

# Optimizasyon algoritması seçimi (Gradyan İniş)
#optimizer = tf.keras.optimizers.SGD(learning_rate=0.001)

# Optimizasyon algoritması seçimi (Adam Optimizasyonu)
optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)

model.compile(optimizer=optimizer, loss='mse')

history= model.fit(X_train, y_train, epochs=1000, batch_size=32, validation_data=(X_val, y_val))#validation için ayrıca train verisinden bir daha bö

loss = model.evaluate(X_test, y_test)
print("Test Loss:", loss)

plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Training and Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

y_pred = model.predict(X_test)

# Gerçek ve tahmin edilen değerleri karşılaştırma
plt.figure(figsize=(14, 7))
plt.plot(y_test[:, 0], label='Gerçek Klima Derecesi')
plt.plot(y_pred[:, 0], label='Tahmin Edilen Klima Derecesi')
plt.title('Gerçek ve Tahmin Edilen Klima Derecesi')
plt.xlabel('Örnek')
plt.ylabel('Klima Derecesi')
plt.legend()
plt.show()

# import joblib
# import pickle

# # Modeli HDF5 formatında kaydetme
# model.save('yz2_model.h5')

# # HDF5 dosyasını binary formatta okuyup pickle ile kaydetme
# with open('yz2_model.h5', 'rb') as model_file:
#     model_data = model_file.read()

# with open('yz2_model.pkl', 'wb') as pickle_file:
#     pickle.dump(model_data, pickle_file)

# # Scaler'ı kaydetme
# scaler_filename = "yz2_scaler.save"
# joblib.dump(scaler, scaler_filename)
