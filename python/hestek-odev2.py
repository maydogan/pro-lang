#!/usr/bin/python
#-*- coding:utf-8 -*-
import csv

def hash(tc): 
	sum = 0
	for i in range(len(tc)):
		if i % 2 == 0:
			sum = sum  * (i+1) ^ ord(tc[i])
		else:
			sum = sum ^ (i+1) * ord(tc[i])
	return sum % 75

def hash_chain():
	kisiler = csv.reader(open("ogrenci10.csv", "rb")) # csv default olarak ";" yerine "," kullanıyor.
	tc_zincir = [None] * 75
	
	tcler = []
	for kisi in kisiler: 
		tcler.append(kisi[3])

	for tc in tcler :
		i = hash(tc)
		if tc_zincir[i] == None:
			tc_zincir[i] = tc
		elif type(tc_zincir[i]) != type([]):
			temp = tc_zincir[i]
			tc_zincir[i] = []
			tc_zincir[i].append(temp)
			tc_zincir[i].append(tc)
		else:
			tc_zincir[i].append(tc)
	return tc_zincir
	
def hash_name(tc_numara):
	tc_zincir = hash_chain()
	
	kisiler = csv.reader(open("ogrenci10.csv", "rb")) # csv default olarak ";" yerine "," kullanıyor.
	bilgi_zincir = [None] * 75
	
	for kisi in kisiler:
		tc = kisi[3]
		i = hash(tc)
		if bilgi_zincir[i] == None and type(tc_zincir[i]) == str:
			bilgi_zincir[i] = kisi[1:3]
		elif type(tc_zincir[i]) == list and bilgi_zincir[i] == None:
			bilgi_zincir[i] = [[]] * len(tc_zincir[i])
			index = tc_zincir[i].index(tc)
			bilgi_zincir[i][index] = kisi[1:3]
		elif type(tc_zincir[i]) == list and bilgi_zincir[i] != None:
			index = tc_zincir[i].index(tc)
			bilgi_zincir[i][index] = kisi[1:3]
	
	i = hash(tc_numara)
	if type(tc_zincir[i]) == list:
		index = tc_zincir[i].index(tc_numara)
		print bilgi_zincir[i][index]
	else:
		print bilgi_zincir[i]
		
print hash_chain()			
hash_name("51940591790")
