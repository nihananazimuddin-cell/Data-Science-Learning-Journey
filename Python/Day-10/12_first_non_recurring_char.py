# ============================================================
# DAY 10 — FIRST NON-RECURRING CHARACTER
# ============================================================
# Problem:
# Given a string, find the first character that appears only once.
#
# Example:
#   Input  : "swiss"
#   Output : "w"
#
# Approach:
# 1. Use a dictionary to count the frequency of each character.
# 2. Traverse the string again and return the first character
#    whose frequency is 1.
#
# ============================================================



# --------FIRST APPROACH:works, but 
# # word = input("Enter the string : ")

# def find_first_non_recurring_char(word):
#     for char in word:
#         if word.count(char) == 1:
#             return char
#     return None

# char = find_first_non_recurring_char(word)
# print(f"The first non-recurring character is : {char}")

# ------
word = input("Enter the string : ")

def find_first_non_recurring_char(word):
    count_dict = {}
    for char in word:
        if char not in count_dict:
            count_dict[char] = 1
        else:
            count_dict[char] += 1

    #------Below commented code also works: since dictionary preserve the INSERTION ORDER------
    #  for key in count_dict:
    #     if count_dict[key] == 1:
    #         return key
    
    for char in word:
        if count_dict[char] == 1:
            return char
    return None


char = find_first_non_recurring_char(word)
print(f"The first non-recurring character is : {char}")


