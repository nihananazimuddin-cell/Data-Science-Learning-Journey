
# Program: Palindrome Checker

# Description:
# Checks whether a given number is a palindrome.

# Day: 01
# Date: 30 July 2026
#============================================

n=int(input("Enter the number to be checked: "))

def palindrome(n):
    original=n
    reversedNum=0

    while n>0:
        digit=n%10
        n=n//10
        reversedNum = reversedNum*10 + digit

    if(original == reversedNum):
        print("PALINDROME !")
    else:
        print("NOT A PALINDROME !")


palindrome(n)