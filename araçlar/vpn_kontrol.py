#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet VPN KONTROL")
print("""
Vpn Kontrole Hoş Geldin Hacker : )

""")

hedefip = input("Hedef Ip girin : ")
os.system("ike-scan " + hedefip)

