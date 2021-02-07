# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 21:55:45 2020

@author: Matteo
"""

my_file = open("input.txt", "r")
content = my_file.read()
path = content.split("\n")
my_file.close()

#print(path)

overflow = len(path[0])

start = 0
trees = 0
for row in path:
    if row[start] == '#':
        trees += 1
    start += 3
    start = start%31

print(trees)