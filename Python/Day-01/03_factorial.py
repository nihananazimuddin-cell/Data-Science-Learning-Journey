# Program: Factorial Calculator

# Description:
# Calculates the factorial of a given number.

# Day: 01
# Date: 30 July 2026
#============================================

n = int(input("Enter the number to be checked :"))

def factorial(n):
    if n < 0:
        return None
    if n==1 or n==0 :
        return 1
    return n * factorial(n-1)
   

result = factorial(n)

if result is None:
    print("Factorial isn't defined for negative numbers!")
else:
    print(f"Factorial is {result}")

