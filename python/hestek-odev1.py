#!/usr/bin/python
#-*- coding:utf-8 -*-
import csv , time
from sequential import *

def hash(s, base): #hash fonksiyonu 
	sum = 0
	for i in range(len(s)):
		if i%2 == 0:
			sum = sum  * (i+1) ^ ord(s[i])
		else:
			sum = sum ^ (i+1) * ord(s[i])
			
	return sum % base


N = 75
kisiler = csv.reader(open("ogrenci10.csv", "rb")) # csv dosyasindan kisileri okuma
top = [0] * N

tcler = []
for kisi in kisiler: 
 	tc = kisi[3] # kisilerin tc kimlik numaralarini alma
	tcler.append(tc)
	i = hash(tc, N) #hash fonksiyonunu cagirarak arguman olarak tc kimlik numarasini verip calistirma
	top[i] = top[i] + 1


sifirlar = 0
for i in top:
	if i == 0:
		sifirlar = sifirlar + 1                   # Kalan bos yer ve essiz yerlestirilen tc sayisi  
												  # Toplam 53 tane tc essiz bicimde yerlestirilebilmis
print sifirlar, "tane bos yerin/ ", 75 - sifirlar, "dolu yerin var"
 
 #arama algoritmalari

aranan = ["62116253084", "25280476970","34205183152","46864757568","46591768950","46576734230"]

start = time.clock()
for i in aranan:	
	print sequentialSearch(tcler, i)	
stop = time.clock()
print "sequential sort süresi %f" % (stop - start)


start = time.clock()
for i in aranan:	
	print orderedSequentialSearch(tcler, i)
stop = time.clock()
print "sequential sort süresi %f" % (stop - start)


start = time.clock()
for i in aranan:	
	print binarySearch(tcler, i)
stop = time.clock()
print "sequential sort süresi %f" % (stop - start)
