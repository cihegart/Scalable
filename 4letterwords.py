#!/usr/bin/python

import itertools
import enchant

d = enchant.Dict("en_US")
f = open('4words.txt', 'w')
res = itertools.product('abcdefghijklmopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYNZ', repeat=4)
count=0
for i in res:
    if d.check(''.join(i)):
    	count+=1
    	f.write(''.join(i) + '\n')

f.close()
print count