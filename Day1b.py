#Advent of Code 2024
#Day 1: Historian Hysteria
#v1.0  12-1-2024

import re
Alist =[]
Blist=[]
    
with open('Day1in.txt') as f:
    read_data = f.readlines()
f.close()

for i in range(0,len(read_data)):
    line = read_data[i].strip().split("   ")
    Alist.append(int(line[0]))
    Blist.append(int(line[1]))

Alist.sort()
Blist.sort()
Counter = {}  #num: count of num
tot= 0

for n in range(0,len(Alist)):
    if Alist[n] not in Counter.keys() and Alist[n]in Blist:
        Counter[Alist[n]] = Blist.count(Alist[n])
    
print(Counter)

Score =0
for x in Alist:
    if x in Counter.keys():
        Score = Score + x * Counter[x]
    
print(Score)    


