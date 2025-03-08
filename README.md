# Akıllı Ofis

Akıllı Ofis, çalışanların duygusal durumlarını analiz ederek ofis ortamındaki konfor ayarlarını optimize eden bir yapay zeka destekli sistemdir.

## Proje Açıklaması

Bu proje, iki farklı yapay zeka modeli ile hiyerarşik olarak çalışmaktadır:
1. **İlk model**, çalışanların duygu durumunu tahmin eder.
2. **İkinci model**, tahmin edilen duygu durumuna göre ofis içi ortamın ayarlarını belirler.

### Duygu Durumu Tahmini İçin Kullanılan Parametreler
- Hava durumu
- Tuttuğu futbol takımı
- Evinden iş yerine kaç dakikada geldiği (trafik durumu)
- Borsadaki yatırımlarının durumu

Bu parametreler, Kaggle gibi platformlardan toplanan veriler ile eğitilmiştir. Modelin etiketlenmesi için gerçek kişi duyguları kullanılmıştır. Model tahminleme sırasında bu parametreleri internetten anlık olarak çekerek değerlendirme yapmaktadır.

### Ofis Ortamı Ayarları
İlk modelin duygu durumunu tahmin etmesinin ardından, çalışan için aşağıdaki ayarlar optimize edilir:
- Oda kokusu
- Dinleyeceği müzik türü
- Klima derecesi
- İçeceği (kahve, çay vb.)

Bu sayede ofis rutinleri tahmin edilerek çalışanların konfor seviyeleri artırılır ve verimlilik yükseltilir.

## Model Başarı Sonuçları

İlk modelin başlangıçta aldığı doğruluk oranı **%71** iken;
- Verilerin düzenlenmesi ve temizlenmesi,
- Hiperparametre optimizasyonu,
- Veri sayısının artırılması gibi iyileştirmelerle doğruluk **%82** seviyesine çıkartılmıştır.

Aşağıda modelin karışıklık matrisi (confusion matrix) verilmiştir:

![yz1_confusion](https://github.com/user-attachments/assets/648ae1f5-0fad-4655-81a2-bbdd0b670826)


## Kullanılan Teknolojiler
- **Python** (Makine Öğrenimi Modeli)
- **TensorFlow, Scikit-Learn** (Model Eğitimi)
- **C# (Form Arayüzü)**
- **MSSQL (Veri Kaydı ve Arayüz Entegrasyonu)**

## Kurulum ve Çalıştırma

### Python Modeli İçin:
1. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install tensorflow scikit-learn pandas numpy requests
   ```
2. Modeli çalıştırın:
   ```bash
   python model.py
   ```

### C# Uygulaması İçin:
- C# Form uygulaması doğrudan çalıştırılabilir.
- Python modeli bir **buton aracılığıyla** başlatılabilir.

### SQL Kullanımı:
- Projede basit bir SQL yapısı bulunmaktadır.
- Tek bir tablo vardır ve bu tablo duygu tahminleri ile ofis ortamı ayarlarını saklamaktadır.
- **SQL yalnızca arayüz için gereklidir**, Python projeleri kendi aralarında veri alışverişi yapmaktadır.


## Katkıda Bulunma
Eğer projeye katkıda bulunmak isterseniz, pull request gönderebilirsiniz! Görüş ve önerileriniz için issue açabilirsiniz.

---

📌 **Proje Sahibi:** [dmrogzhn](https://github.com/dmrogzhn)
