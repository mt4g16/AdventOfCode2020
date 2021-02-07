# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 20:35:53 2020

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
    #print(key)
    range_list = raw_entry[:anchor-2].split('-')
    #print(range_list)
    pwd = raw_entry[anchor+2:]
    #print(pwd)
    key_count = pwd.count(key)
    #print(key_count)
    if int(range_list[0]) <= key_count <= int(range_list[1]):
        passed_pwds.append(raw_entry)

print(len(passed_pwds))