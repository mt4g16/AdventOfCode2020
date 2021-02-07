# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 13:35:18 2020

@author: Matteo
"""
import operator

my_file = open("input.txt", "r")
content = my_file.read()
boarding_cards = content.split("\n")
my_file.close()


#boarding_cards = ['BFFFBBFRRR']

#print(boarding_cards)

seat_ids = []

all_seats = []
for row in range(0, 128):
    for col in range(0, 8):
        all_seats.append((row, col))
#print(all_seats)

booked_seats = []
for seat_pos in boarding_cards:
    rows = list(range(0, 128))
    columns = list(range(0,8))
    for i in range(0, 7):
        #print(seat_pos[i])
        if seat_pos[i] == 'F':
            rows = rows[:int(len(rows)/2)]
        if seat_pos[i] == 'B':
            rows = rows[int(len(rows)/2):]
    #print(rows)
    
    for i in range(7, 10):
        if seat_pos[i] == 'R':
            columns = columns[int(len(columns)/2):]
        if seat_pos[i] == 'L':
            columns = columns[:int(len(columns)/2)]
    #print(columns)
    
    booked_seats.append((rows[0], columns[0]))
    
    seat_id = rows[0] * 8 + columns[0]
    seat_ids.append(seat_id)

#print(booked_seats)
#print(max(seat_ids))
#print(booked_seats)
booked_seats.sort(key = operator.itemgetter(0, 1))
#print('========================================')

#print(booked_seats)
missing_seats = list(set(all_seats) - set(booked_seats))
missing_seats.sort(key = operator.itemgetter(0, 1))
print(missing_seats)

my_id = 69*8+5














