#!/usr/bin/python

f = open('allwords.txt', 'r')

lines = f.readlines()
allperms = ['none']
#place =0
for index, i in enumerate(lines):
	for count, j in enumerate(lines):
		#temp = i[:-1]
		#temp2 = j[:-1]
		allperms.append(i[:-1]+j[:-1])
		#allperms[place]=temp+temp2
		#place+=1
for k in allperms:
	print k