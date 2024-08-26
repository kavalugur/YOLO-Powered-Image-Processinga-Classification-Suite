YOLO-Powered Image Processing and Classification Suite
Proje Tanımı
YOLO-Powered Image Processing and Classification Suite projesi, gelişmiş görüntü işleme ve sınıflandırma tekniklerini kullanarak çeşitli nesneleri (fil, uçak, dinozor) otomatik olarak algılamayı ve sınıflandırmayı amaçlamaktadır. YOLO modellerinin (YOLOv8 ve YOLO-NAS) güçlü yönlerinden yararlanan bu proje, veri artırma ve segmentasyon teknikleriyle model doğruluğunu artırmaktadır. Proje, nesne algılama ve sınıflandırma alanında araştırmalar yapmak isteyenler için sağlam bir temel sunar.


Özellikler
Gelişmiş Görüntü İşleme: Fil, uçak ve dinozor gibi nesnelerin tespiti için YOLO modelleri kullanılır.
Otomatik Sınıflandırma: YOLOv8 ve YOLO-NAS modelleri ile yüksek doğruluk oranında sınıflandırma yapılır.
Veri Artırma ve Segmentasyon: Veri setlerinin çeşitlendirilmesi ve segmentasyon işlemleri için gelişmiş teknikler kullanılır.
Performans Değerlendirme: Model performansı, "Precision", "Recall" ve "F1-Score" gibi metriklerle değerlendirilir.
Kullanıcı Dostu Arayüz: Kolay kullanım için optimize edilmiş betikler ve kullanıcı talimatları.
Kullanılan Teknolojiler ve Kütüphaneler
Python - Proje ana dili
YOLOv8 ve YOLO-NAS - Nesne algılama ve sınıflandırma modelleri
PIL (Python Imaging Library) - Görüntü işleme ve dönüştürme işlemleri için
OpenCV - Görüntü işleme ve video analizi için
PyTorch - Derin öğrenme modellerinin eğitimi ve değerlendirilmesi için
Kurulum
Projeyi yerel makinenize klonlamak ve gerekli kütüphaneleri kurmak için şu adımları izleyin:

Depoyu Klonlayın:

git clone https://github.com/kavalugur/YOLO-Powered-Image-Processinga-Classification-Suite.git

cd YOLO-Powered-Image-Processinga-Classification-Suite

Gereksinimleri Yükleyin:

pip install -r requirements.txt

Kullanım
Proje betiklerini çalıştırarak görüntüleri işleyebilir ve sınıflandırabilirsiniz:

Modeli Yükleyin ve Görüntüleri İşleyin:

python StajProjesi.py

Sonuçları Görüntüleyin:

results/ klasöründe işlemden geçmiş ve sınıflandırılmış görüntüleri bulabilirsiniz.
Eğitim ve Test Verileri
Eğitim Verileri: 40 fil, 40 uçak ve 40 dinozor görüntüsünden oluşan bir veri seti kullanılmıştır.
Veri Artırma: Eğitim verilerini çoğaltmak ve modelin genel performansını artırmak için veri artırma teknikleri kullanılmıştır.
Sonuçlar ve Performans Metrikleri
Proje sonuçları, aşağıdaki performans metrikleri ile değerlendirilmiştir:

Precision: Modelin doğru pozitif tespit oranı.
Recall: Modelin toplam pozitif tespit oranı.
F1-Score: Precision ve Recall'un harmonik ortalaması.
Model, test verileri üzerinde %85 doğruluk oranına ulaşmıştır.
