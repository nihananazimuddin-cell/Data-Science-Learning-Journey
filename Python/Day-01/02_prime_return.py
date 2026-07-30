# Program: Prime Number Checker

# Description:
# Checks whether a given number is a prime number, using return statements.

# Day: 01
# Date: 30 July 2026
#============================================

n = int(input("Enter the number to be checked:"))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        x = n%i
        if x == 0:
            return False
    return True

if is_prime(n):
    print("Prime Number!")
else:
    print("Not a Prime Number!")
