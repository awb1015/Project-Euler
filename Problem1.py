#Project Euler Problem 1
#Sum multiples of 3 and 5 below 1000

threes = 0
fives = 0
fivess = 0

#Sum multiples of 3
for i in range (3, 1000, 3):
  threes = i + threes

#Sum multiples of 5 that are not also multiples of 3 to avoid double counts

for j in range (5, 1000,15):
   fives = fives + j
for k in range (10, 1000, 15):
   fivess = fivess + k

#Totals

total = fivess + fives + threes

print total