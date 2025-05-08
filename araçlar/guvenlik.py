#!/usr/bin/env python
# Detaylı bilgi için: https://yusuwyildirim.medium.com/kali-linux-tools-3-wafw00f-f5ef6e5f5cc1

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet GUVENLIK DUVARI")

print("""
Tespit Aracımıza Hoş Geldiniz...

""")

site = input("Site Adresini Girin : ")
os.system("wafw00f http://" + site)
