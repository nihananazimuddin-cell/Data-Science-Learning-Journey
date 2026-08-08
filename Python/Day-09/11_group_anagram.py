#==================================================================================
# Problem Name : Group Anagrams
#
# Problem:
# Given a list of strings, group all the anagrams together.
#
# Example:
# Input : ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
#
# Logic Used:
# 1. Create an empty dictionary to store grouped anagrams.
# 2. Iterate through each word in the input list.
# 3. Sort the characters of each word and use the sorted string as the dictionary key.
#    - Example:
#        "eat" -> "aet"
#        "tea" -> "aet"
#        "ate" -> "aet"
#    Since all anagrams produce the same sorted string,
#    they will have the same dictionary key.
# 4. If the key already exists, append the current word to
#    the existing list.
# 5. Otherwise, create a new list with the current word as
#    its first element.
# 6. Finally, return only the dictionary values, which
#    represent the grouped anagrams.
#
# Data Structures Used:
# - Dictionary (Hash Map)
# - List
#
#REFER TO FILE "11_group_anagram_Dictionary_Concepts.md" for explanation of concepts in detail.
#=================================================================================================

words = input("Enter the words :").split()

def group_anagram(words):
    anagram_dict = {}
    for w in words:
        # generate sorted key 
        # Note: Strings are immutable, so cannot use w.sort()
        sorted_key = "".join(sorted(w))
        if sorted_key in anagram_dict:
            # key:value ==> sorted_key:[list]
            # to add to this dict;  dict_name[key].append(value)
            anagram_dict[sorted_key].append(w)
        else:
            anagram_dict[sorted_key]=[w]
    return anagram_dict

result = group_anagram(words)

if result:
    print(list(result.values()))
