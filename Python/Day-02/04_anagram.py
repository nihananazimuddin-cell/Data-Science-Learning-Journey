# ---------------------------------------------------------
# Day 02 - Valid Anagram
# Date: 31 July 2026

# Problem:
# Given two strings, determine whether they are anagrams.

# Example:
# listen, silent  -> True
# hello, world    -> False
# =============================================================

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    #-------------------VERSION 1 (Commented)------------------------------------
    # Initial Approach : Used range(len(s1)) to iterate through the string.
    # for i in range(len(s1)):
    #     if s1[i] not in s2:
    #         return False
    #     else:
    #         if s1.count(s1[i])!=s2.count(s1[i]):
    #             return False
    # return True

    #-------------------VERSION 2 (Improved)-------------------------------------- 
    # Iterate through the unique characters in s1 using sets.
    # This avoids checking the same characters multiple times
    # Eg: 
    #   "aaaaaaaaaaaab"
    #   "baaaaaaaaaaaa"
    for ch in set(s1):
        if ch not in s2:
            return False

        if s1.count(ch)!=s2.count(ch):
            return False
    return True


result = is_anagram(s1,s2)

if not result:
    print("Not an Anagram !")
else:
    print("Anagram !")

                
