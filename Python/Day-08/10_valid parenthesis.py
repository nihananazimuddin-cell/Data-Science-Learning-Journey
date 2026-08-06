# =====================================================================
# Day 08 - Valid Parentheses
# Date: 06 August 2026

# Problem:
# Given a string containing only the characters
# '(', ')', '{', '}', '[' and ']',
# determine whether the input string is valid.

# A string is considered valid if:
#   1. Every opening bracket has a matching closing bracket.
#   2. Brackets are closed in the correct order.
#   3. Every closing bracket has a corresponding opening bracket.

# Example:
#   Input:()[]{}
#   Output: True

# Concepts Practiced:
# - Stack (using a Python list)
# - append() and pop()
# - while loop
# - Conditional statements
# - match-case
# - Algorithmic thinking
# - Input validation using a stack

# Learning Note:
# A stack follows the Last In, First Out (LIFO) principle.
# It is ideal for problems involving matching pairs,
# such as validating parentheses.

## Learning Note:
#   -A stack/list follows the Last In, First Out (LIFO) principle.
#   -It is ideal for problems involving matching pairs, such as validating parentheses.
# =====================================================================

brackets = input("Enter the string of brackets : ")

def check_valid_parenthesis(brackets):
    bracket_list = []
    i=0
    while i < len(brackets):
        if brackets[i] in ('(','{','['):
            bracket_list.append(brackets[i])
        else:
            if bracket_list :
                open_bracket = bracket_list.pop()  ##Note: pop() remove the last value added to the list, and return that value.
                match open_bracket:
                    case '(' :
                        if brackets[i] != ')':
                            return False
                    case '{':
                        if brackets[i] != '}':
                            return False
                    case _:
                        if brackets[i] != ']':
                            return False
            else:
                return False
        i += 1
    if bracket_list:
        return False
    return True

if check_valid_parenthesis(brackets):
    print("Valid parenthesis !")
else:
    print("Invalid Parenthesis !")
                
