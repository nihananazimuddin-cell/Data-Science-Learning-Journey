# 📚 Learning Notes – Group Anagrams & Dictionaries
===================================================================
## 1. Dictionary
    - A **dictionary** stores data as **key : value** pairs.
    - Example:
            student = {
                "name": "Nihana",
                "age": 31
                }
    **Key** → Used to identify or look up data.
    **Value** → The data stored for that key.

## 2. Creating an Empty Dictionary
    my_dict = {}
        OR
    my_dict = dict()

    The most commonly used method is: my_dict = {}

## 3. Dictionary vs Set
    Although both use curly braces `{}`, they are different.
    ### Dictionary
        Stores **key : value** pairs.
            student = {
            "name": "Nihana",
            "age": 31
            }
    ### Set
        Stores only **unique values**.
        fruits = {"apple", "banana", "orange"}
    ### Important:
        {} creates an **empty dictionary**, **not** an empty set.
        To create an empty set: my_set = set()
---
## 4. Checking if a Key Exists

    To check whether a key already exists in a dictionary:
    Example: if "name" in student:
                print("Found")
    This checks only the **keys**, not the values.
---
## 5. Adding Data to a Dictionary
    To add a new key-value pair:
        student["city"] = "Kochi"

    General syntax:
    dictionary[key] = value
---
## 6. Dictionary with Lists
    A dictionary value can also be a list.
    Example:
        groups = {  "aet": ["eat", "tea"]  }
    To add another word:
        groups["aet"].append("ate")
    Output:
    {    "aet": ["eat", "tea", "ate"]   }
---
## 7. Why did I get this error?
    -Error:  AttributeError: 'str' object has no attribute 'append'
    -Reason: I initially wrote:
            anagram_dict[key] = word
            which stores a **string**.
    -Later I tried: anagram_dict[key].append(word)
    -But strings cannot use `append()`.
    -Correct approach:
                anagram_dict[key] = [word]
        Now the value is a **list**, and lists support `append()`.
---
## 8. Sorting a String
    - Strings do not have a `.sort()` method because strings are **immutable** (cannot be modified after creation).
    - This does **not** work:  word.sort()
    - Instead, use:            sorted(word)
    - Output:    ['a', 'e', 't']
    - Since `sorted()` returns a list, convert it back to a string:  
                                                            "".join(sorted(word))
    Example:    word = "eat"
                key = "".join(sorted(word))
                print(key)
    Output: aet
---
## 9. Why use `"".join()`?
    `sorted()` returns a list of characters.
    sorted("eat")----->RETURNS ---> ['a', 'e', 't']

    To make it a string again:    "".join(['a', 'e', 't'])
    Output: aet
    This sorted string becomes the dictionary key.
---
    ## 10. Printing Only Dictionary Values
    To print only the values:    print(my_dict.values())
    Output: dict_values(...)
    To convert it into a list:   print(list(my_dict.values()))
    
    Output:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    This is also what the Group Anagrams problem expects as the final output.
---

## 11. When to Use `for` vs `while`
    ### Use `for` when:
        * Iterating through a list
        * Iterating through a string
        * Iterating through a dictionary
        * Iterating a fixed number of times
        * Example:  for word in words:

    ### Use `while` when:
        * Repeating until a condition changes
        * Number of iterations is unknown
        * Waiting for user input
        * Binary Search
        * Queue/Stack based algorithms

    Simple rule:
        `for` → Iterate over data.
        `while` → Continue until a condition changes.

---

# What is a Hash Map?
    - A **Hash Map** is a data structure that stores information as **key → value** pairs and allows very fast lookup, insertion, and updates.
    - In Python, a **dictionary (`dict`) is implemented as a hash map**.

    Example:  student = {
                        "name": "Nihana",
                        "age": 31
                        }
    - Instead of searching through every item one by one, Python uses a special process called **hashing** to calculate where a key should be stored. 
    - This allows it to find values very quickly—typically in **O(1)** (constant) time.
    
    * A **dictionary** in Python is implemented using a **hash map**.
    * Hash maps provide **fast lookup, insertion, and update** operations.
    * They are ideal when you need to search for data using a unique key.

    This is why the **Group Anagrams** solution uses a dictionary (hash map): it lets us quickly check whether a sorted word already has a group and either create a new group or add the word to an existing one.

---
===================================================================================
# Key Takeaways

* Dictionary = **Key → Value** storage.
* Hash Map = The data structure Python uses to implement dictionaries.
* Lists are **mutable** → can use `.append()` and `.sort()`.
* Strings are **immutable** → use `sorted()` instead of `.sort()`.
* `sorted()` returns a **list**, so use `"".join()` to convert it back into a string.
  eg: "".join(sorted(string_name))
* Use `if key in dictionary` to check whether a key already exists.
* Use `list(dictionary.values())` when only the grouped values are needed.
* Group Anagrams works by using the **sorted version of each word as the dictionary key**, so all anagrams naturally end up in the same group.
