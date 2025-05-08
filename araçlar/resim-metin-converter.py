import easyocr
from fpdf import FPDF
from tkinter import Tk, filedialog
import os
from googletrans import Translator

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Metin Belgesi', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Sayfa {self.page_no()}', 0, 0, 'C')

def goruntu_yukle():
    """
    Kullanıcıdan görüntü dosyasını seçmesini ister.
    """
    Tk().withdraw()  # Tkinter'ın ana penceresini gizler
    dosya_yolu = filedialog.askopenfilename(
        title="Görüntü Dosyası Seçin",
        filetypes=[("Görüntü Dosyaları", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")]
    )
    if dosya_yolu:
        print(f"Seçilen dosya: {dosya_yolu}")
        return dosya_yolu
    else:
        print("Hiçbir dosya seçilmedi.")
        return None

def metni_ayikla_easyocr(goruntu_yolu, dil="en"):
    """
    EasyOCR kullanarak görüntüden metin ayıklar ve metnin düzenini koruyarak çıkarır.
    """
    try:
        reader = easyocr.Reader([dil])  # Belirtilen dilde destek
        metin_detayli = reader.readtext(goruntu_yolu, detail=1, paragraph=True)  # Metni detaylı çıkar
        
        # Metni düzgün bir şekilde çıkartabilmek için blokları ve satırları düzenliyoruz
        metin = ""
        son_koordinatlar = None
        satir_yuksekligi = 10  # Satırlar arasındaki boşluk

        for parca in metin_detayli:
            # Her metin parçasının pozisyonlarına bakıyoruz, eğer çok farklıysa yeni satıra geçiyoruz
            if son_koordinatlar:
                # Eğer önceki metnin bitişiyle şu anki metnin başlangıcı arasında yeterli mesafe varsa, yeni satır başlatıyoruz
                if abs(parca[0][0][1] - son_koordinatlar[1]) > satir_yuksekligi:
                    metin += "\n"
            
            metin += parca[1] + " "  # Metni birleştiriyoruz
            son_koordinatlar = parca[0][2]  # Son metnin sağ alt köşesinin koordinatlarını kaydediyoruz

        return metin.strip()
    except Exception as e:
        print(f"Hata: {e}")
        return ""

def turkceye_cevir(metin):
    """
    Google Translate ile metni İngilizceden Türkçeye çevirir.
    """
    translator = Translator()
    try:
        cevrilen_metin = translator.translate(metin, src='en', dest='tr')
        return cevrilen_metin.text
    except Exception as e:
        print(f"Çeviri hatası: {e}")
        return metin  # Çeviri hatası durumunda orijinal metni döndür

def pdf_olustur(metin, cikti_yolu):
    """
    Ayıklanan metni bir PDF dosyasına yazar.
    """
    pdf = PDF()
    pdf.add_page()
    
    # Türkçe karakterler için Arial Unicode fontu kullanıyoruz
    pdf.add_font('Arial', '', 'C:/Windows/Fonts/arial.ttf', uni=True)
    pdf.set_font("Arial", size=12)
    
    # Metni PDF'ye yazıyoruz
    pdf.multi_cell(0, 10, metin)
    
    pdf.output(cikti_yolu)
    print(f"PDF başarıyla kaydedildi: {cikti_yolu}")

def menu():
    """
    Kullanıcıya seçim yapması için bir menü sunar.
    """
    print("*****************************")
    print("1. Görüntüyü metne çevirip PDF oluştur")
    print("2. Görüntüyü Türkçeye çevirip PDF oluştur")
    print("q. Çıkış")
    print("*****************************")

def main():
    while True:
        menu()
        secim = input("Bir seçenek girin (1, 2, q): ").strip().lower()
        
        if secim == "1":
            print("Görüntü dosyasını seçin...")
            goruntu_yolu = goruntu_yukle()
            
            if goruntu_yolu:
                # Dosya adını al ve uzantısını pdf ile değiştir
                dosya_adı, _ = os.path.splitext(os.path.basename(goruntu_yolu))
                cikti_pdf_yolu = f"{dosya_adı}_metin.pdf"
                
                print("Metin ayıklanıyor...")
                metin = metni_ayikla_easyocr(goruntu_yolu, dil="en")  # İngilizce dilinde ayıkla
                
                if metin.strip():  # Ayıklanan metin boş değilse
                    print("PDF oluşturuluyor...")
                    pdf_olustur(metin, cikti_pdf_yolu)
                else:
                    print("Görüntüden herhangi bir metin ayıklanamadı.")
        
        elif secim == "2":
            print("Görüntü dosyasını seçin...")
            goruntu_yolu = goruntu_yukle()
            
            if goruntu_yolu:
                # Dosya adını al ve uzantısını pdf ile değiştir
                dosya_adı, _ = os.path.splitext(os.path.basename(goruntu_yolu))
                cikti_pdf_yolu = f"{dosya_adı}_turkce.pdf"
                
                print("Metin ayıklanıyor...")
                metin = metni_ayikla_easyocr(goruntu_yolu, dil="en")  # İngilizce dilinde ayıkla
                
                if metin.strip():  # Ayıklanan metin boş değilse
                    print("Türkçeye çevriliyor...")
                    metin_turkce = turkceye_cevir(metin)  # İngilizce metni Türkçeye çevir
                    print("PDF oluşturuluyor...")
                    pdf_olustur(metin_turkce, cikti_pdf_yolu)
                else:
                    print("Görüntüden herhangi bir metin ayıklanamadı.")
        
        elif secim == "q":
            print("Çıkış yapılıyor...")
            break
        
        else:
            print("Geçersiz seçenek. Lütfen 1, 2 veya q girin.")

if __name__ == "__main__":
    main()
