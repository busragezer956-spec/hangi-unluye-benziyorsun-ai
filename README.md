# 🎬 Hangi Türk Ünlüye Benziyorsun?

Bu proje, yapay zekâ destekli yüz tanıma teknolojileri kullanılarak geliştirilmiş bir yüz benzerlik analiz uygulamasıdır.  
Kullanıcıdan alınan fotoğraf analiz edilerek veri setindeki Türk ünlüler ile karşılaştırılır ve en çok benzeyen kişi belirlenir.

---

# 🚀 Proje Özeti

Bu uygulama Python tabanlı geliştirilmiş olup:

- Yüz algılama
- Yüz embedding çıkarımı
- Benzerlik hesaplama
- Kamera desteği
- Modern kullanıcı arayüzü

özelliklerine sahiptir.

Uygulama eğlence amaçlı geliştirilmiş olsa da bilgisayarlı görü ve yapay zekâ tekniklerini gerçek bir senaryoda uygulamaktadır.

---

# 🧠 Kullanılan Teknolojiler

| Teknoloji | Açıklama |
|---|---|
| Python | Ana programlama dili |
| Streamlit | GUI arayüzü |
| face_recognition | Yüz tanıma sistemi |
| OpenCV | Görüntü işleme |
| NumPy | Matematiksel işlemler |
| Pillow | Görsel işleme |
| Pickle | Eğitilmiş verileri saklama |

---

# 📂 Proje Yapısı

```bash
face_recognition_project/
│
├── dataset/
│   ├── Afra_Saracoglu/
│   ├── Burak_Ozcivit/
│   ├── Kivanc_Tatlitug/
│   └── ...
│
├── train.py
├── recognize.py
├── modern_gui.py
├── encodings.pkl
├── requirements.txt
└── README.md
```

---

# 📸 Uygulama Özellikleri

## ✅ Fotoğraf Yükleme
Kullanıcı bilgisayardan fotoğraf yükleyebilir.

## ✅ Kamera Desteği
Kullanıcı kamera ile canlı fotoğraf çekebilir.

## ✅ Yüz Analizi
Fotoğraf içerisindeki yüz otomatik algılanır.

## ✅ Benzerlik Hesaplama
Veri setindeki ünlüler ile karşılaştırma yapılır.

## ✅ Benzerlik Oranı
En yüksek eşleşme yüzdesel olarak gösterilir.

---

# 🧠 Sistem Nasıl Çalışıyor?

## 1. Veri Seti Oluşturma
Türk ünlülere ait fotoğraflar klasörler halinde dataset içine eklenir.

Örnek:

```bash
dataset/
 ├── Burak_Ozcivit/
 ├── Serenay_Sarikaya/
 └── Kivanc_Tatlitug/
```

---

## 2. Model Eğitimi

`train.py` dosyası çalıştırılır.

Bu işlem:

- tüm fotoğrafları okur
- yüzleri algılar
- yüz embedding vektörleri çıkarır
- `encodings.pkl` dosyasına kaydeder

Çalıştırma:

```bash
python3 train.py
```

---

## 3. GUI Arayüzü Çalıştırma

Modern arayüzü başlatmak için:

```bash
streamlit run modern_gui.py
```

---

# 🖥️ Arayüz Özellikleri

- Modern koyu tema
- Kamera açma/kapatma
- Fotoğraf önizleme
- Yüz tanıma sonucu
- Benzerlik progress bar
- Kullanıcı dostu tasarım

---

# 📊 Kullanılan Yapay Zekâ Yaklaşımı

Bu projede:

- HOG tabanlı yüz algılama
- Face Encoding
- Euclidean Distance
- Similarity Matching

teknikleri kullanılmıştır.

---

# 📦 Kurulum

## Gerekli Kütüphaneler

```bash
pip install -r requirements.txt
```

---

# ▶️ Çalıştırma

## Eğitimi Başlat

```bash
python3 train.py
```

## GUI Başlat

```bash
streamlit run modern_gui.py
```

---

# 📷 Örnek Kullanım

1. Fotoğraf yükle
2. Kamera ile fotoğraf çek
3. Yapay zekâ yüzü analiz etsin
4. En çok benzediğin Türk ünlüyü öğren

---

# ⚡ Gelecek Geliştirmeler

- Yaş tahmini
- Duygu analizi
- Gerçek zamanlı video analizi
- Mobil uygulama
- Daha büyük veri seti
- Daha hızlı inference sistemi

---

# 👩‍💻 Geliştirici

Büşra Gezer  
Bilgisayar Mühendisliği Öğrencisi

---

# 📄 Lisans

Bu proje eğitim ve araştırma amaçlı geliştirilmiştir.
