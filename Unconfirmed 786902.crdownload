# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 09:13:50 2024

@author: Rajesh
"""

lower_range = int(input("Enter lower range: "))
upper_range = int(input("Enter upper range: "))
result = []
for num in range(lower_range, upper_range + 1):
    sqrt = int(num ** 0.5)
    print(sqrt)
    if sqrt * sqrt == num:
        print("i=",sqrt)
        digit_sum = sum(map(int, str(num)))
        print("i=",digit_sum)
        
        if digit_sum < 10:
            result.append(num)
print(result)
