## -----------DAY 06----------4/Aug/'26-----------------

1. What is the difference between a List and a Tuple?       
        | List                          | Tuple                                             |
        |-------------------|---------------------------------------------------------------|
        | Mutable                       | Immutable                                         |
        | Uses `[]`                     | Uses `()`                                         |
        | Created using `list()`        | Created using `tuple()`                           |
        | Can add,remove,update,delete elements | Cannot modify elements after creation |
        | Allows duplicate elements     | Allows duplicate elements                         |
        | Slightly slower               | Slightly faster                                   |
        | Uses slightly more memory     | More memory efficient                             |
        | Best for dynamic/changing data| Best for fixed/constant data                      |

    ### Example
        my_list = [1, 2, 3]
        my_list[0] = 10      # ✔ Allowed

        my_tuple = (1, 2, 3)
        # my_tuple[0] = 10   # ❌ TypeError

    # List Usage:
        - Shopping cart     - To-do list       - Employee records that change
    # Tuple Usage:
        - Coordinates (latitude, longitude)   - RGB color values   -Fixed configuration values

    ### Common Interview Follow-up
    **When would you use a tuple instead of a list?**
        - Data should not change (immutability)
        - Better memory efficiency
        - Slightly faster performance

---------------------------------------------------------------------------------

2. Why are tuples immutable? What are the advantages of immutability?

    Tuples are **immutable**, which means their elements **cannot be modified, added, or removed** once the tuple is created.

    ### Advantages of Immutability
        - Data remains unchanged after creation.
        - More memory efficient than lists.
        - Slightly faster than lists.
        - Suitable for storing constant or fixed data.
        - Can be used as dictionary keys (if all elements are hashable).
        - Reduces accidental modification of data.
    ### Examples
        - GPS coordinates → `(12.9716, 77.5946)`
        - RGB color values → `(255, 255, 255)`
        - Days of the week
        - Months of the year

3. What is List Comprehension? Give an example.

        List comprehension is a concise way of creating a new list from an existing iterable using a single line of code.
        
    ### Syntax
        new_list = [expression for item in iterable]

    ### Advantages
        - Shorter and cleaner code.
        - Easier to read for simple transformations.
        - Often slightly faster than using a `for` loop with `append()`.

    ### Example 1 : FIND SQUARES OF numbers
                numbers = [1, 2, 3, 4, 5]
                squares = [num**2   for num in numbers]
                print(squares)
        **Output**  : [1, 4, 9, 16, 25]

    ### Example 2 : FIND EVEN numbers
                numbers = [1, 2, 3, 4, 5, 6]
                even_numbers = [n   for n in numbers     if n % 2 == 0]
                print(even_numbers)
        **Output**  : [2, 4, 6]

----------------------------------------------------------------------------
4. What are *args and **kwargs?

    ### Definition
        - *args accepts any number of positional arguments.
        - **kwargs accepts any number of keyword arguments.

    ### Key Points
    |              *args                     |               **kwargs                        |
    |----------------------------------------|-----------------------------------------------|
    | Positional arguments                   | Keyword arguments                             |
    | Stored as a tuple                      | Stored as a dictionary                        |
    | Uses *                                 | Uses **                                       |
    | Useful when no.of arguments is unknown |Useful when no.of keyword arguments are unknown|

    ### Example 1 - `*args`
                def add(*args):
                    print(args)

                add(10, 20)
                add(10, 20, 30)
                add(10, 20, 30, 40)
                                        **Output**:
                                        (10, 20)
                                        (10, 20, 30)
                                        (10, 20, 30, 40)
    ### Example 2 - Sum of Numbers using `*args`
                def add(*args):
                    return sum(args)

                print(add(5, 10))
                print(add(5, 10, 15))
                print(add(5, 10, 15, 20))
                                        **Output**:
                                            15
                                            30
                                            50

    ### Example 3 - `**kwargs`
                def student_details(**kwargs):
                    print(kwargs)

                student_details(name="Nihana", age=31, city="Kochi")
                                                                     **Output**:
                                        {'name': 'Nihana', 'age': 31, 'city': 'Kochi'}
                
    ### Example 4 - Iterating through `**kwargs`
                def student_details(**kwargs):
                    for key, value in kwargs.items():
                        print(f"{key}: {value}")

                student_details(name="Nihana",age=31,city="Kochi",profession="Software Developer"
                                        **Output**:
                                            name: Nihana
                                            age: 31
                                            city: Kochi
                                            profession: Software Developer

    ### Example 5 - Using Both `*args` and `**kwargs`
                def display(*args, **kwargs):
                    print("Positional Arguments:", args)
                    print("Keyword Arguments:", kwargs)

                display(10,20,30,name="Nihana",city="Kochi")
                                    **Output**
                                        Positional Arguments: (10, 20, 30)
                                        Keyword Arguments: {'name': 'Nihana', 'city': 'Kochi'}
-------------------------------------------------------
5. What is the difference between a Shallow Copy and a Deep Copy?
    ### Definition:

    **copy** creates a new object from an existing object.

    - **Shallow Copy** creates a new object but shares references to nested (mutable) objects.
    - **Deep Copy** creates a completely independent copy, including all nested objects.

    ### Key Differences

        | Shallow Copy                             | Deep Copy                               |
        |------------------------------------------|-----------------------------------------|
        | Copies only the outer object             | Copies the outer object&all nested objs |
        | Nested objects are shared                |Nested objs are completely independent   |
        | Changes to nested objs affect both copies|Changes affect only the copied object    |
        | Faster                                   | Slightly slower                         |
        | Uses less memory                         | Uses more memory                        |
        | Created using `copy.copy()`              | Created using `copy.deepcopy()`         |

    ### Example 1 - Shallow Copy
        import copy
                    list1 = [[1, 2], [3, 4]]

                    list2 = copy.copy(list1)

                    list2[0][0] = 100

                    print("List1:", list1)
                    print("List2:", list2)
                                            **Output**:
                                            List1: [[100, 2], [3, 4]]
                                            List2: [[100, 2], [3, 4]]
                    **Explanation**
                    The outer list is copied, but the inner lists are shared.
                    Changing an inner list affects both copies.

    ### Example 2 - Deep Copy
        import copy

                    list1 = [[1, 2], [3, 4]]

                    list2 = copy.deepcopy(list1)

                    list2[0][0] = 100

                    print("List1:", list1)
                    print("List2:", list2)
                                                **Output**
                                                List1: [[1, 2], [3, 4]]
                                                List2: [[100, 2], [3, 4]]

                    **Explanation**
                    Both the outer list and all nested lists are copied.
                    Changing one copy does not affect the other.

        ------

    ### Common Interview Follow-up
     **When should you use Deep Copy?**
        Use **Deep Copy** when working with nested mutable objects (such as lists inside lists or dictionaries containing lists) and you need the copied object to be completely independent of the original.
        ---
        **Memory Tip**
        - ⭐ Shallow Copy → Shared nested objects
        - ⭐ Deep Copy → Independent nested objects
------------------------------------------------------------------------------

## ==========================Quick Revision (1 Minute)================================
### List vs Tuple
- Mutable vs Immutable
- [] vs ()
- Dynamic vs Fixed

### Tuple
- Immutable
- Faster
- Memory efficient

### List Comprehension
- One-line list creation

### *args
- Variable positional arguments
- Tuple

### **kwargs
- Variable keyword arguments
- Dictionary

### Shallow Copy
- Shared nested objects

### Deep Copy
- Independent nested objects
## =======================================================================================