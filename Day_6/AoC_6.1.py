# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 17:37:34 2020

@author: Matteo
"""

my_file = open("input.txt", "r")
content = my_file.read()
raw_forms = content.split("\n\n")
my_file.close()

#print(raw_forms)
#print('==================================')

group_counts = []

for form in raw_forms:
    p1 = []
    p1.append(form)
    p2 = ''.join(p1[0].split('\n'))
    unique_answers = len(set(p2))
    group_counts.append(unique_answers)

print(sum(group_counts))
