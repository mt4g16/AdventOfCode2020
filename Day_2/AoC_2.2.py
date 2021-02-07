# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 21:09:30 2020

@author: Matteo
"""

my_file = open("input.txt", "r")
content = my_file.read()
passwords = content.split("\n")
my_file.close()

passed_pwds = []

for index, raw_entry in enumerate(passwords):
    #print(raw_entry)
    anchor = raw_entry.find(':')
    key = raw_entry[anchor-1]
    #print(type(key))
    key_positions = raw_entry[:anchor-2].split('-')
    #print(range_list)
    pwd = raw_entry[anchor+2:]
    #print(pwd)
    if (pwd[int(key_positions[0])-1] == key) != (pwd[int(key_positions[1])-1] == key):
        passed_pwds.append(raw_entry)
print(len(passed_pwds))

