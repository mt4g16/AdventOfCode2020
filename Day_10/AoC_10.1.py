# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 19:16:58 2020

@author: Matteo
"""
from collections import Counter

my_file = open("input.txt", "r")
content = my_file.read()
adapters = content.split("\n")
my_file.close()

adapters = [int(x) for x in adapters]

adapters.insert(0, 0)

adapters.sort()

adapters.append(adapters[-1]+3)

print(adapters)


diff = []
for index_a in range(1, len(adapters)):
    diff.append(adapters[index_a]-adapters[index_a-1])
    
#print(diff)

f1 = list(Counter(diff).keys()) # equals to list(set(words))
f2 = list(Counter(diff).values()) # counts the elements' frequency

for i in range(len(f1)):
    print(str(f2[i]) + ' instances of ' + str(f1[i]))



