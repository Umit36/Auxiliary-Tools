#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet WORDPRESS TARAMA")
print("""
Wordpress taramaya Hoş Geldin Hacker : )

1) Hızlı tarama
2) Eklenti tarama
3) Tema tarama
4) Yönetici Kullanıcı adı tarama

""")

islemno = input("İşlem Numarası girin : ")

if(islemno=="1"):
	site = input("Site Adresi girin: ")
	os.system("wpscan --url " + site)
	
elif(islemno=="2"):
	site = input("Site Adresi girin: ")
	os.system("wpscan --url " + site + " --enumerate p" )
	
elif(islemno=="3"):
	site = input("Site Adresi girin: ")
	os.system("wpscan --url " + site + " --enumerate t" )
	
elif(islemno=="4"):
	site = input("Site Adresi girin: ")
	os.system("wpscan --url " + site + " --enumerate u" )
	
else:
	print("Hatalı Seçim!!!")
