import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

data = pd.read_csv("data_hatice2.csv")

data["duygu"] = data["duygu"].str.lower()
data["duygu"] = data["duygu"].str.strip()

label = LabelEncoder()
data["duygu"] = label.fit_transform(data["duygu"])

encoder = OneHotEncoder()

data_encoded = encoder.fit_transform(data[["durum"]]).toarray()

sutun_adi = "durum"

data_encoded = pd.DataFrame(data_encoded, columns=[f'{sutun_adi}_{i}' for i in range(data_encoded.shape[1])])
x_birlesim = pd.concat([data, data_encoded], axis=1)

Y = data["duygu"].values
X = pd.concat([data.drop(["duygu", "durum"], axis=1), data_encoded], axis=1)

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

x_train, x_test, y_train, y_test = train_test_split(X_scaled, Y, test_size=0.2, shuffle=True)

rfc = RandomForestClassifier(criterion="entropy", max_depth=15, min_samples_split=10, n_estimators=80)
rfc.fit(x_train, y_train)

print("skor = ", rfc.score(x_test, y_test))

# Tahminleri yapma
y_pred = rfc.predict(x_test)

# Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)
conf_matrix_display = ConfusionMatrixDisplay(confusion_matrix=conf_matrix, display_labels=label.classes_)

# Confusion Matrix'i görselleştirme
plt.figure(figsize=(10, 7))
conf_matrix_display.plot(cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
plt.show()

# Classification Report
class_report = classification_report(y_test, y_pred, target_names=label.classes_)
print("Classification Report:\n", class_report)

# Feature Importances
feature_importances = pd.DataFrame(rfc.feature_importances_, index=X.columns, columns=['importance']).sort_values('importance', ascending=False)

# Feature Importances'i görselleştirme
plt.figure(figsize=(12, 8))
sns.barplot(x=feature_importances.importance, y=feature_importances.index)
plt.title('Feature Importances')
plt.show()

# if rfc.score(x_test, y_test) >= 0.84:
#     joblib.dump(rfc, 'random_forest_model.pkl')
#     joblib.dump(scaler, 'scaler.pkl')  # Scaler'ı kaydedin
#     print("Model ve scaler başarıyla kaydedildi.")
# else:
#     print("Düşük skor")
