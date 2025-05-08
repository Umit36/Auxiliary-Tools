#!/usr/bin/env python

import os
import py_compile

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet DERLEME")
print("""
Derlemeye Hoş Geldin Hacker : )

""")

derle = input("Program ismini girin : ")

py_compile.compile(derle)
