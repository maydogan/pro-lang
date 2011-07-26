from Stack import *
import string

def show(frompole, withpole, topole):
	print "----"
	if frompole == []:
		print "kule 1 : bos" 
	else: 
		print "kule 1 :", string.join(frompole,"")
	if withpole == []: 
		print "kule 2 : bos"
	else: 
		print "kule 2 :", string.join(withpole,"")
	if topole == []: 
		print "kule 3 : bos"
	else: 
		print "kule 3 :", string.join(topole,"")
	print "----"
	
def moveTover(height, frompole, topole, withpole):
	if frompole.isEmpty() and withpole.isEmpty() and topole.isEmpty():
		str = "abcdefghijklmnoprstuvyz"
		for i in range(0, height):
			frompole.push(str[i])
		show(frompole.items, withpole.items, topole.items) 
	if height >= 1:
		
		moveTover(height -1 ,frompole,withpole,topole)
		moveDisk(frompole,topole)
		show(frompole.items, withpole.items, topole.items)
		moveTover(height -1 , withpole,topole,frompole)

		
def  moveDisk(frompole,topole):
	topole.push(frompole.pop())
	
kule1 = Stack()
kule2 = Stack()
kule3 = Stack()
moveTover(3, kule1, kule2, kule3)

