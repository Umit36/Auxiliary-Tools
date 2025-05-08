#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet MAC DEGISTIRME")
print("""
Mac Adresini Değiştirmeye Hoş Geldin Hacker : )

1) MAC Adresini Random Belirle
2) MAC Adresini Elle Belirle
3) MAC Adresini Orjinale Döndür

""")

islemno = input("İşlem numarası girin : ")

if (islemno=="1"):
	os.system("ifconfig eth0 down")
	os.system("macchanger -r eth0")
	os.system("ifconfig eth0 up")
	print("\033[92mYeni MAC Adresi Belirlendi.")
	
if (islemno=="2"):
	macadres = input("Yeni MAC Adresi girin : ")
	os.system("ifconfig eth0 down")
	os.system("macchanger --mac " + macadres + " eth0")
	os.system("ifconfig eth0 up")
	print("\033[92mYeni MAC Adresi Belirlendi.")
	
if (islemno=="3"):
	os.system("ifconfig eth0 down")
	os.system("macchanger -p eth0")
	os.system("ifconfig eth0 up")
	print("\033[92mMAC Orjinale Döndü.")
	
else:
	print("Hatalı seçim!")
	os.system("python mac_degistirme.py")
