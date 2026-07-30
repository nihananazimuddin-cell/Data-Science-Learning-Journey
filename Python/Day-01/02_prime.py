
# Program: Prime Number Checker

# Description:
# Checks whether a given number is a prime number, using print statements in the function.

# Day: 01
# Date: 30 July 2026
#============================================

n= int(input("Enter the number to be checked:"))

def prime(n):
    if n<=1:
        print("Not a Prime Number!")
        return
    
    primeFlag=True
    for i in range(2,n,1):
           x=n%i
           if x==0:
               primeFlag=False
               print("Not a Prime Number!")
               break
    if primeFlag == True:
        print("Prime Number !")
            

prime(n)
