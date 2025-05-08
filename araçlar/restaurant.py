import os
import shutil
from datetime import datetime, timedelta

# Masaüstü yolunu belirleme ve proje klasörünü oluşturma
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
project_folder = os.path.join(desktop_path, "Restaurant_Uygulamasi")
if not os.path.exists(project_folder):
    os.makedirs(project_folder)

bakiye_dosya_yolu = os.path.join(project_folder, "bakiye.txt")
gunluk_gelir_dosya_yolu = os.path.join(project_folder, "anlik_gelir.txt")
onceki_ay_gelir_dosya_yolu = os.path.join(project_folder, "toplam_gelir.txt")

# Dosyaların oluşturulması (boş dosyalar)
for dosya_yolu in [bakiye_dosya_yolu, gunluk_gelir_dosya_yolu, onceki_ay_gelir_dosya_yolu]:
    if not os.path.exists(dosya_yolu):
        open(dosya_yolu, "w", encoding="utf-8").close()

masalar = {a: 0 for a in range(1, 21)}
rezervasyonlar = {a: None for a in range(1, 21)}
masa_durumlari = {a: "boş" for a in range(1, 21)}
toplam_gelir = 0
giris_yapildi = False
son_odeme_tarihi = datetime.now()
aylik_gelir = 0.0

# Kullanıcı bilgilerini tanımlama
kullanicilar = {"admin": {"şifre": "admin123", "rol": "yönetici"}}

def hesap_ekle(masa_no, eklenecek_ucret):
    if masa_no < 1 or masa_no > 20:
        print("Geçersiz masa numarası.")
        return
    if eklenecek_ucret < 0:
        print("Eklenebilir ücret negatif olamaz.")
        return
    bakiye = masalar[masa_no]
    guncel_bakiye = bakiye + eklenecek_ucret
    masalar[masa_no] = guncel_bakiye
    print(f"Masa {masa_no} için {eklenecek_ucret:.2f} TL eklendi. Yeni bakiye: {guncel_bakiye:.2f} TL")

def hesap_odeme():
    global son_odeme_tarihi
    try:
        masa_no = int(input("Masa numarası: "))
        if masa_no < 1 or masa_no > 20:
            print("Geçersiz masa numarası.")
            return
        bakiye = masalar[masa_no]
        print("Masa {}'in hesabı: {}".format(masa_no, bakiye))
        masalar[masa_no] = 0
        print("Hesap ödendi.")
        son_odeme_tarihi = datetime.now()
    except ValueError:
        print("Geçersiz giriş. Lütfen sayısal bir değer giriniz.")

def rezervasyon_ekle():
    masa_no = int(input("Rezervasyon yapılacak masa numarası: "))
    if masa_no < 1 or masa_no > 20:
        print("Geçersiz masa numarası.")
        return
    if rezervasyonlar[masa_no] is not None:
        print("Bu masa zaten rezerve edilmiş.")
        return
    isim = input("Rezervasyonu yapan kişinin adı: ")
    rezervasyonlar[masa_no] = isim
    print("Rezervasyon başarıyla eklendi.")

def rezervasyon_sil():
    masa_no = int(input("Rezervasyonu silinecek masa numarası: "))
    if masa_no < 1 or masa_no > 20:
        print("Geçersiz masa numarası.")
        return
    if rezervasyonlar[masa_no] is None:
        print("Bu masa için herhangi bir rezervasyon bulunmuyor.")
        return
    rezervasyonlar[masa_no] = None
    print("Rezervasyon başarıyla silindi.")

def rezervasyonlari_goruntule():
    for masa_no, isim in rezervasyonlar.items():
        if isim:
            print(f"Masa {masa_no}: {isim}")
        else:
            print(f"Masa {masa_no}: Boş")

def masa_durumu_guncelle():
    masa_no = int(input("Masa numarası: "))
    durum = input("Yeni durum (boş/dolu/rezerve): ")
    if masa_no < 1 or masa_no > 20 or durum not in ["boş", "dolu", "rezerve"]:
        print("Geçersiz giriş.")
        return
    masa_durumlari[masa_no] = durum
    print("Masa durumu başarıyla güncellendi.")

def masa_durumlari_goruntule():
    for masa_no, durum in masa_durumlari.items():
        print(f"Masa {masa_no}: {durum}")

def gunluk_gelir_kaydet():
    global toplam_gelir
    tarih = datetime.now().strftime("%Y-%m-%d")
    with open(gunluk_gelir_dosya_yolu, "a", encoding="utf-8") as dosya:
        dosya.write(f"{tarih}: {toplam_gelir:.2f}\n")

def gelir_analizi():
    global toplam_gelir, aylik_gelir
    global son_odeme_tarihi

    # Günlük gelir hesapla
    if datetime.now() - son_odeme_tarihi > timedelta(days=1):
        toplam_gelir = 0  # 24 saat dolmuş, gelir sıfırlanacak
    toplam_gelir = sum(masalar.values())
    gunluk_gelir_kaydet()

    print(f"Anlık gelir : {toplam_gelir:.2f} TL")

    try:
        # Son 30 günün gelirini hesapla
        with open(gunluk_gelir_dosya_yolu, "r", encoding="utf-8") as dosya:
            satirlar = dosya.readlines()
            son_30_gun = datetime.now() - timedelta(days=30)
            aylik_gelir = 0.0
            for satir in satirlar:
                tarih_str, gelir = satir.strip().split(": ")
                tarih = datetime.strptime(tarih_str, "%Y-%m-%d")
                if tarih > son_30_gun:
                    aylik_gelir += float(gelir)
            print(f"Toplam gelir(Aylık) : {aylik_gelir:.2f} TL")

            # Önceki ayın gelirini dosyaya kaydet
            if datetime.now().day == 1:  # Ayın ilk günü
                with open(onceki_ay_gelir_dosya_yolu, "a", encoding="utf-8") as dosya:
                    dosya.write(f"{datetime.now().strftime('%Y-%m')}: {aylik_gelir:.2f}\n")
                aylik_gelir = 0.0  # Yeni ayda aylık gelir sıfırlanacak
    except FileNotFoundError:
        print("Henüz gelir verisi kaydedilmedi.")

def kullanici_giris():
    global giris_yapildi
    if not giris_yapildi:
        kullanici_ad = input("Kullanıcı adı: ")
        sifre = input("Şifre: ")
        if kullanici_ad in kullanicilar and kullanicilar[kullanici_ad]["şifre"] == sifre:
            print("Giriş başarılı.")
            giris_yapildi = True
            return kullanicilar[kullanici_ad]["rol"]
        else:
            print("Geçersiz kullanıcı adı veya şifre.")
            return None
    return "yönetici"  # Varsayılan olarak "yönetici" rolü ile devam ediyoruz.

def dosya_kontrolu(dosya_adi):
    try:
        with open(dosya_adi, "r", encoding="utf-8") as dosya:
            veri = dosya.read().strip().split("\n")
            for satir in veri:
                if satir:
                    parcalar = satir.split(": ")
                    if len(parcalar) == 2:
                        masa_no = int(parcalar[0].split()[1])
                        bakiye = float(parcalar[1])
                        masalar[masa_no] = bakiye
    except FileNotFoundError:
        with open(dosya_adi, "w", encoding="utf-8"):
            pass
        print("Kayıt dosyası oluşturuldu.")

def dosya_guncelle(dosya_adi):
    with open(dosya_adi, "w", encoding="utf-8") as dosya:
        for a in range(1, 21):
            bakiye = str(masalar[a])
            dosya.write("Masa {}: {}\n".format(a, bakiye))

def ekran_temizle():
    """Konsolu temizle."""
    os.system('cls' if os.name == 'nt' else 'clear')

def ana_islemler():
    dosya_kontrolu(bakiye_dosya_yolu)
    if not kullanici_giris():
        print("Giriş başarısız. Çıkılıyor.")
        return

    while True:
        try:
            ekran_temizle()  # Ana menüye dönmeden önce ekranı temizle
            print("""
                Ümit Çelik restaurant uygulaması

            1) Masaları Görüntüle 🪑
            2) Hesap Ekle ➕
            3) Hesap Ödeme 💰
            4) Rezervasyon Ekle 📅
            5) Rezervasyon Sil 🗑️
            6) Rezervasyonları Görüntüle 👁️
            7) Masa Durumunu Güncelle 🔄
            8) Masa Durumlarını Görüntüle 🗂️
            9) Gelir Analizi 📊
            Q) Çıkış ❌

            """)

            secim = input("Yapılacak İşlemi Giriniz: ")
            if secim == "1":
                for a in range(1, 21):
                    print("Masa {} için hesap: {}".format(a, masalar[a]))
            elif secim == "2":
                masa_no = int(input("Hesap eklemek istenen masa numarası: "))
                eklenecek_ucret = float(input("Eklenmek istenen ücret: "))
                hesap_ekle(masa_no, eklenecek_ucret)
            elif secim == "3":
                hesap_odeme()
            elif secim == "4":
                rezervasyon_ekle()
            elif secim == "5":
                rezervasyon_sil()
            elif secim == "6":
                rezervasyonlari_goruntule()
            elif secim == "7":
                masa_durumu_guncelle()
            elif secim == "8":
                masa_durumlari_goruntule()
            elif secim == "9":
                gelir_analizi()
            elif secim.lower() == "q":
                print("Çıkış Yapılıyor. İyi günler.")
                break
            else:
                print("Hatalı seçim yaptınız.")
            dosya_guncelle(bakiye_dosya_yolu)
            input("Ana menüye dönmek için enter'a basınız.")
        except EOFError:
            print("Geçersiz işlem. Lütfen tekrar deneyin.")

ana_islemler()
