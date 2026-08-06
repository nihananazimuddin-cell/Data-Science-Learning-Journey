# =================================================================
# Day 07 - Longest Common Prefix
# Date: 05 August 2026
#
# Problem:
# Given a list of strings, find the longest common prefix
# shared by all the strings. If there is no common prefix,
# return an empty string.
#
# Example:
    # Input:
         # ["flower", "flow", "flight"]
    # Output:
         # "fl"
#
# Concepts Practiced:
# - Strings
# - List traversal
# - Character comparison
# - Nested loops
# - String slicing
# - Algorithmic thinking
#
# Time Complexity: O(n × m)
# where n = number of strings,
#       m = length of the shortest string
#
# =================================================================

words = list(input("Enter the words : ").split())

def find_longest_prefix(words):
    if not words:
        return ""
    word1 = words[0]
    i=1
    while i<= len(word1):
        for j in range(1,len(words)):
            if not words[j].startswith(word1[0:i]):
                prefix = word1[0:i-1]
                return prefix
        i += 1
    return word1

print(f"Longest Common Prefix is : {find_longest_prefix(words)}")