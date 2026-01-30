# Zatürre(Pneumonia) Teşhis Destek Sistemi

Bu projeyi, göğüs röntgenlerini analiz ederek zatürre (pneumonia) belirtisi olup olmadığını tahmin eden bir karar destek mekanizmasıdır. Sağlık çalışanlarının iş yükünü hafifletmek ve teşhis sürecine dijital bir yardımcı eklemek amacıyla geliştirilmiştir. 

### Nasıl Kullanılır?
* **Hızlıca denemek için:** [https://huggingface.co/spaces/boveric/zaturre-tespit-araci]
* **Bilgisayarda çalıştırmak için:** **Releases** bölümünden ZIP dosyasını indirin. 

### Teknik Detaylar
* **Model:** DenseNet121 mimarisi kullanıldı.
* **Dil:** Python 3.13 & TensorFlow.
* **Başarı Oranı** 
Genel Doğruluk:%91
Recall:%97

**Önemli Not:** Bu yazılım tıbbi bir teşhis aracı değildir. Yalnızca eğitim ve destek amaçlı hazırlanmıştır. Herhangi bir sağlık kararı vermeden önce mutlaka uzman doktor görüşü alınmalıdır.
