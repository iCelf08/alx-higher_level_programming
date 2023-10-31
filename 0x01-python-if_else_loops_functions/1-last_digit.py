#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
no = str(number)
lds = no[len(no)-1]
ld = int(lds)
if ld > 5:
  print(f"last digit of {number} is {ld} and is greater than 5")
elif ld == 0:
     print(f"last digit of {number} is {ld} and is zero")
else:
  print(f"last digit of {number} is {ld} and is less than 6 and not 0")
