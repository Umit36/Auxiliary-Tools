#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet PORT TARAMA")
print("""
Port Tarama Aracına Hoşgeldiniz :)

1) Hızlı Tarama
2) Servis ve Versiyon Bilgisi
3) İşletim Sistemi Bilgisi

""")

islemno = input("İşlem Numarasını Girin : ")

if(islemno=="1"):
	hedefip = input("Hedef IP Girin : ")
	os.system("nmap " + hedefip)
elif(islemno=="2"):
	hedefip = input("Hedef Ip Girin : ")
	os.system("nmap -sS -sV " + hedefip)
elif(islemno=="3"):
	hedefip = input("Hedef Ip Girin : ")
	os.system("nmap -o " + hedefip)
else:
	print("Hatalı Secim Yaptın Be Bro :(")
