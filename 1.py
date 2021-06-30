"""
Question 1:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: 
Consider use range(#begin, #end) method
"""

seven = []
for a in range(2000,3201):
    if (a%7 == 0):
        seven.append(a)

five = []
for b in range(2000,3201):
    if (b%5 == 0):
        five.append(b)

result = []
for c in seven:
    if c not in five:
        result.append(c)
return_string = '' 

for res in result:
    return_string += str(res) + ', '

print(return_string[:-2])
