# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 17:57:48 2020

@author: Matteo
"""

my_file = open("input.txt", "r")
content = my_file.read()
raw_forms = content.split("\n\n")
my_file.close()


#print(raw_forms)
#print('==================================')

group_counts = []

for group_form in raw_forms:
    check = []
    p1 = []
    p1.append(group_form)
    p2 = p1[0].split('\n')
    #print(p2)
    
    result = set(p2[0]).intersection(*p2)
    group_counts.append(len(result))
    
print(sum(group_counts))

