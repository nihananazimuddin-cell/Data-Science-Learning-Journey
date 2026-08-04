# ---------------------------------------------------------
# Day 06 - Merge Two Sorted Lists (Two Pointer Technique)
# Date: 04 August 2026
#
# Problem:
# Given two sorted lists, merge them into a single sorted list
# without using Python's built-in sorting functions.
#
# Approach:
# - Use two pointers (i and j), one for each list.
# - Compare the current elements of both lists.
# - Append the smaller element to the merged list.
# - Move only the pointer of the element that was appended.
# - Continue until one list is completely traversed.
# - Finally, append the remaining elements from the other list.
#
# Concepts Practiced:
# - Two Pointer Technique
# - While Loops
# - List Operations (append)
# - Edge Case Handling (empty lists)
# ---------------------------------------------------------

list1 = list(map(int, input("Enter the first sorted list : ").split()))
list2 = list(map(int, input("Enter the next sorted list : ").split()))

# ---------Using BUILT IN sort() function---------
#   merged_list = list1 + list2
#   merged_list.sort()
#   print(f"Merged Sorted List : {merged_list} ")

def merge_two_lists(list1, list2):
    i = 0
    j = 0
    length1 = len(list1)
    length2 = len(list2)
    merged_list = []

    #If list1 is empty
    if length1 == 0: 
        merged_list = list2.copy()
        return merged_list
    
    # list2 is empty
    if length2 == 0: 
        merged_list = list1.copy()
        return merged_list

    # Compare elements from both lists until one of the lists is completed.
    # Append the smaller element to the merged list and move only that list's pointer.
    while i<length1 and j<length2:
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # If list2 still has remaining elements, append all of them.
    # No further comparison is needed because list1 has already been completely processed.
    while j<length2:
        merged_list.append(list2[j])
        j += 1

    #If list2 still has remaining elements, append all of them.
    # No further comparison is needed because list1 has already been completely processed.
    while i<length1:
        merged_list.append(list1[i])
        i += 1       

    return merged_list


merged_list = merge_two_lists(list1, list2)

print(f"Merged Sorted List : {merged_list} ")

