# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 08:20:48 2024

@author: Rajesh
"""
stack=[]
def push():
    element=int(input("enter the number:"))
    stack.append(element)
    print(stack)
def pop_element():
    if not  stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print("removered element:",e)
        print(stack)
def top():
    print("the top number:",max(stack))
def sizeofstack():
    print("the size of stack:",len(stack))
while True:
    print("select the operation 1.push 2.pop 3.top 4.size of stack 5.exit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        top()
    elif choice==4:
        sizeofstack()
    elif choice==5:
         print("enter the correct choice")
         break
    else:
        print("enter the another choice")