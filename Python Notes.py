# Certainly! Let's break down the syllabus into key points and generate coding practice questions for each topic.

# ### Functions:
# 1. **Function Definition**
#    ```python
#    def func(a, b):
#        print("Sum:", a + b)
#    ```
#    - **Coding Practice Question 1:**
#      Write a function that takes two parameters, multiplies them, and prints the result.

# 2. **Function with Pass**
#    ```python
#    def func3(a, b):
#        if a > b:
#            pass
#        else:
#            return a + b
#    ```
#    - **Coding Practice Question 2:**
#      Create a function that checks if a given number is even. If it is, do nothing; otherwise, print "Odd number."

# 3. **Sending Arr**
#    ```python
#    def func4(*num):
#        for i in num:
#            sum = sum + i
#        print(sum / len(numbers))
#    ```
#    - **Coding Practice Question 3:**
#      Write a function that receives a variable number of arguments and calculates their product.

# 4. **Sending Dict**
#    ```python
#    def func5(**num):
#        # Check this func.
#    ```
#    - **Coding Practice Question 4:**
#      Implement a function that accepts a dictionary and prints key-value pairs.

# 5. **Function with Return**
#    ```python
#    def func2(a, b):
#        return a + b

#    for i in range(1, 10):
#        print(func2(i, i + 1))
#    ```
#    - **Coding Practice Question 5:**
#      Develop a function that takes two numbers and returns their difference. Use it in a loop to print the differences for a range of numbers.

# ### Break and Continue:
# 6. **Break and Continue Tutorial**
#    ```python
#    for i in range(1, 12):
#        if i == 10:
#            break
#        print(i)
#    ```
#    - **Coding Practice Question 6:**
#      Implement a loop that prints numbers from 1 to 20, but skips multiples of 3 using 'continue'.

# ### While Loop:
# 7. **While Loop**
#    ```python
#    i = 0
#    while i < 4:
#        print(i)
#        i = i + 1
#    ```
#    - **Coding Practice Question 7:**
#      Write a while loop that prints the Fibonacci series up to the 10th term.

# 8. **While-Else**
#    ```python
#    i = 5
#    while i < 4:
#        print(i)
#        i = i + 1
#    else:
#        print("i > 4")
#    ```
#    - **Coding Practice Question 8:**
#      Create a program that prompts the user to guess a number. Use a while loop with an else statement to provide feedback on the guess.

# 9. **Implementing Do-While**
#    ```python
#    i = 5
#    while i < 4:
#        i = i + 1
#        print(i)
#    else:
#        print("i > 4")
#    ```
#    - **Coding Practice Question 9:**
#      Write a do-while loop that asks the user to enter a positive number until they do so.

# ### Loops:
# 10. **For Loops and Nested Loops**
#     ```python
#     arr = {1, 2, 3, 4}
#     for i in arr:
#         print(i)

#     arr2 = "csds"
#     for i in arr2:
#         if i == "s":
#             print(i)

#     arr3 = {"red", "Blue"}
#     for i in arr3:
#         for x in i:
#             print(x)

#     for k in range(1, 5):
#         print(k)

#     for k in range(1, 9, 3):
#         print(k)
#     ```
#     - **Coding Practice Question 10:**
#       Create a nested loop to print a pattern of asterisks where the number of asterisks in each row is equal to the row number.

# ### Match Case (Switch):
# 11. **Match Case (Switch)**
#     ```python
#     n = int(input("Enter choice"))
#     match n:
#         case 1:
#             print("Choice 1")
#         case _ if n == 23:
#             print("okay")
#         case _:
#             print("Invalid")
#     ```
#     - **Coding Practice Question 11:**
#       Write a function that simulates a calculator using a match case for different operations.

# ### If-Elif with Time Library:
# 12. **If-Elif with Time Library**
#     ```python
#     import time
#     time = time.strftime('%H,%M,%S')
#     print(time)
#     if time > '21,0,0':
#         print("Jey")
#     ```
#     - **Coding Practice Question 12:**
#       Create a program that uses the time library to print a greeting message depending on the time of the day.

# ### Strings:
# 13. **String Manipulation**
#     ```python
#     a = "moiz!!!"
#     # ... (various string manipulation operations)
#     ```

#     - **Coding Practice Question 13:**
#       Develop a function that takes a string and returns the reverse of the string.

# ### Strings Are Immutable:
# 14. **Strings Are Immutable**
#     ```python
#     a = "moiz!!!"
#     # ... (various string methods)
#     ```

#     - **Coding Practice Question 14:**
#       Implement a function that receives a string and returns a new string with every second character in uppercase.

# String functions:
# # Strings are immutable
# a="moiz!!!"
# print(len(a))
# print(a.upper())
# print(a.lower())
# # Removes trailing characters
# print(a.rstrip("!"))
# print(a.replace("Moiz","Sarah"))
# print(a.split("o"))
# # Converts all to lower first to upper
# print(a.capitalize())
# print(a.center(50))
# print(a.count("m"))
# # See if str ends with +++
# print(a.endswith("+++"))
# # Give range
# print(a.endswith("oi",1,3))
# # Finds  first occurence
# print(a.find("oi"))
# # Find(Returns error if not found)
# print(a.index("o"))
# str="J2erfw"
# print(str.isalnum())

# print(str.isalpha())
# print(str.islower())
# # e.g. \n hai str me tou false
# print(str.isprintable())
# # Spaces
# print(str.isspace())
# # To check title
# print(str.istitle())
# print(str.startswith("M"))
# # Upper to lower and vice versa
# print(str.swapcase())
# print(str.title())