#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from bs4 import BeautifulSoup
import urllib.request
import time
import datetime
from time import sleep

with open ('kur.txt', 'a') as f: f.write ('\n' + "-------------------------------------------------------------------------------")
with open ('kur.txt', 'a') as f: f.write ('\n' + "Dolar Kuru 	 	Saat                   Tarih")
with open ('kur.txt', 'a') as f: f.write ('\n' + "-------------------------------------------------------------------------------")

print("-------------------------------------------------------------------------------")
can = input("Alarm oluşturulacak yüksek kur değerinizi giriniz >> ")
print("-------------------------------------------------------------------------------")
cano = input("Alarm oluşturulacak düşük kur değerini giriniz >> ")
print("-------------------------------------------------------------------------------")

tarih = datetime.datetime.now().strftime("%Y-%m-%d")
zaman = datetime.datetime.now().strftime("%H:%M")
x = 1
yol = 'dikkat.vbs'
yolo = 'dikkat2.vbs'

while x==1:
	os.system('cls')
	print("-------------------------------------------------------------------------------")
	print("Dolar Kuru 	 	Saat                   Tarih")
	print("-------------------------------------------------------------------------------")
	url = "https://dolarrekorkirdimi.com/"
	url_oku = urllib.request.urlopen(url)
	soup = BeautifulSoup(url_oku, 'html.parser')
	ho = soup.find("h6")
	ho = ho.text
	b = "$1,Şimdi,=,₺, "
	for char in b:
		ho = str(ho).replace(char, "")
	if str(ho) > str(can):
		os.startfile(yol)
	if str(ho) < str(cano):
		os.startfile(yolo)
	baby = ho
	print(baby, "                ", zaman, "                ", tarih )
	with open ('kur.txt', 'a') as f: f.write ('\n' + baby + "                  " + zaman + "                  " + tarih)
	time.sleep(5)