#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet WORDLIST")
print("""
Wordlist Oluşturmaya Hoş Geldin Hacker : )

""")

minimum = input("Minimum karakter sayısını girin : ")
maximum = input("Maximum karakter sayısını girin : ")
karakter = input("İstediğiniz Karakterleri girin : ")

os.system("crunch " + minimum + " " + maximum + " " + karakter)

print("Başarıyla Tamamlandı.")
