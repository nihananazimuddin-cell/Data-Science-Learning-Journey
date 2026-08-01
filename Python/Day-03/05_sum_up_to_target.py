# =======================X==============================X==============================
# Day 03 -  TWO SUM ----->  SUM UP TO TARGET (Brute Force)
# Date: 01 August 2026
# =======================X==============================X==============================
# Problem:
#       Given an array of integers and a target value,
#       return the indices of the two numbers that add up to the target.
#
# Concepts Practiced:
#      - Nested loops
#      - User input
#      - map()
#      - split()
#      - Tuple return values
#      - Tuple unpacking
#      - None
# =======================X==============================X==============================


# -------------------- HOW TO INPUT MULTIPLE NUMBERS --------------------
        # input() returns a string.
        # split() converts the string into a list of strings.
        #
        # Example:
        # Input:  "1 3 4 2"
        # split() -> ['1', '3', '4', '2']
        #
        # map(int, ...) applies int() to every element.
        # map() applies a function to every item in an iterable (like a list or tuple)
        #
        # Example:
        # ['1', '3', '4', '2']
        #        ↓
        # map(int, ...)
        #        ↓
        # [1, 3, 4, 2]
        #
        # split()    -> split by spaces
        # split(",") -> split by commas
nums = list(map(int,input("Enter the numbers : ").split()))

target = int(input("Enter the target value : "))

def sum_up_to_target(nums,target):
    length = len(nums)
    for i in range(length-1):
        j = i + 1   # Start from the next index to:
                            # 1. avoid comparing an element with itself.
                            # 2. avoid checking duplicate pairs.
                                # Example:
                                # (0,1) is checked, so (1,0) is unnecessary.                         
        while(j < length):    
            sum_result = nums[i] + nums[j]
            if sum_result == target:
                return(i,j)
            j+=1
    return None

result = sum_up_to_target(nums,target)  # result: tuple[int, int] | None 

if result is None:
    print("No combinations sum to the target! ")
else:
    i,j = result    # Tuple unpacking:
                            # result = (1, 3)
                            # becomes:
                                # i = 1
                                # j = 3
    print(f"The indices are {i} and {j} .")
