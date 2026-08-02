# ---------------------------------------------------------
# Day 04 - Contains Duplicate
# Date: 02 August 2026
#
# Problem:
# Given an integer array, return True if any value appears
# at least twice, otherwise return False.
# 
# Learning Notes:
# 1. count() checks how many times an element appears by
#    scanning the entire list each time it is called.
#    Using count() inside a loop results in O(n²) time
#    complexity.
#
# 2. A set stores only unique elements. Converting a list
#    to a set automatically removes duplicates. If the
#    lengths of the list and the set are different,
#    duplicates are present.
#
# Best Approach: Set Approach.
#    Time Complexity: O(n)
#    Space Complexity: O(n)
# ---------------------------------------------------------

nums = list(map(int, input("Enter the numbers: ").split()))

#------------Initial Approach - using count()----------------
# def check_duplicates(nums):
#     for i in nums:
#         if nums.count(i) > 1:
#             return True
#     return False

# ------------ Optimized Approach - Using a Set and Comparing Lengths ------------
def check_duplicates(nums):
    nums_set = set(nums)
    return len(nums) == len(nums_set)

if check_duplicates(nums):
    print("No Duplicates !")
else:
    print("Contains Duplicates !")