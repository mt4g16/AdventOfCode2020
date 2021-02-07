# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 22:25:19 2020

@author: Matteo
"""

my_file = open("input.txt", "r")
content = my_file.read()
path = content.split("\n")
my_file.close()

#print(path)

def slope_check(x, y):
    overflow = len(path[0])
    
    if y > 1:
        del path[1::2]
    
    start = 0
    trees = 0
    
    for row in path:
        if row[start] == '#':
            trees += 1
        start += x
        start = start%overflow
    
    return(trees)

a = slope_check(1, 1)
b = slope_check(3, 1)
c = slope_check(5, 1)
d = slope_check(7, 1)
e = slope_check(1, 2)

print(a*b*c*d*e)