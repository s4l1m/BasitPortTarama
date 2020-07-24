#!/usr/bin/env python

import os

os.system("apt install figlet")
os.system("clear")
os.system("figlet Basit Düzey Port Tarama")
print("Bu araç, nmap komutlarını kullanarak port taraması yapar.")

print(""" 
1) Hızlı Tarama
2) Servis ve Versiyon Bilgileri 
3) İşletim Sistemi Bilgileri
""")

while True:
    islem = input("Yapmak istediğiniz işlemin numarasını yazınız: ")
    if islem == "1":
        print("""Hızlı Tarama Yapılıyor...       
        """)
        hedef_ip_adresi = input("Hedef ip adresini giriniz: ")
        os.system("nmap " + hedef_ip_adresi)

    elif islem == "2":
        print("""Servis ve Versiyon Bilgileri Taranıyor... """)
        hedef_ip_adresi = input("Hedef ip adresini giriniz: ")
        os.system("nmap -sS -sV" + hedef_ip_adresi)

    elif islem == "3":
        print("İşletim Sistemi Bilgileri Taranıyor... ")
        hedef_ip_adresi = input("Hedef ip adresini giriniz: ")
        os.system("nmap -A " + hedef_ip_adresi)
    
    else:
        print("Yanlış Seçim! ")
