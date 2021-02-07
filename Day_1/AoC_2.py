# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 20:24:02 2020

@author: Matteo
"""

my_file = open("input.txt", "r")
content = my_file.read()
expense_report = content.split("\n")
my_file.close()
#print(expense_report)

check = False

for index, value in enumerate(expense_report):
    if check == False:
        for index2, value2 in enumerate(expense_report):
            if check == False:
                for index3, value3 in enumerate(expense_report):
                    if index != index2 != index3:
                        if int(value)+int(value2)+int(value3) == 2020:
                            #print(value, value2, value3)
                            print(int(value)*int(value2)*int(value3))
                            check = True