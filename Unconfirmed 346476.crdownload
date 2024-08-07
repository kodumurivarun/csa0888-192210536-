# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 12:20:13 2024

@author: Rajesh
"""
def mean(number):
    sum=0
    count=len(number)
    for i in number:
        sum+=i
    mean_a=sum/count
    return mean_a
def median(number):
    n=len(number)
    if n%2!=0:
        median_a=number[(n)//2]
    else:
        median_a=number[(n//2)-1]+number[(n//2)]/2
    return median_a
def mode(number):
   freq={}
   for i in number:
       if i in freq:
           freq[i]+=1
       else:
           freq[i]=1
   max_freq=0
   mode_b=None
   for i,j in freq.items():
       print("i=",i)
       print("j=",j)
       if j>max_freq:
           #print("j=",j)
           max_freq=j
           mode_b=i
       elif j==max_freq:
             mode_b=None
   return mode_b
number=[1,3,3,6,7,8,9]
mean=mean(number)
median=median(number)
mode=mode(number)
print(mean)
print(median)
print(mode)