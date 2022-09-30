# Christian Hart 001-68-3628

import math

# ~~~~~~~~~~ TASK 1 ~~~~~~~~~~
# 1. Write a function that takes a string as input and does the following:
#   Returns True if the input string has more vowels than consonants
#   Returns False if the input string has more consonants than vowels
#   Returns None (this is the Python equivalent of null) if the input
#       string has an equal number of consonants and vowels. We’ll ignore
#       type safety for now!

# Resources used:
#   https://appdividend.com/2022/05/30/python-list-contains/
#   https://realpython.com/python-strings/


def task_1(input):
    # define 2 lists, one of all vowels and the other of all consenants
    vowels = ['a', 'e', 'i', 'o', 'u']
    consenants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                  'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']

    # define a vowel counter and a consenants counter
    v = 0  # vowels counter
    c = 0  # consenants counter
    i = 0  # char iterator

    # write a while loop that iterates over input string
    # when a char in the string exists in the vowel list, v += 1
    # when a char in the string exists in the consenant list, c += 1
    while i < len(input):
        letter = input[i].lower()
        if letter in vowels:
            v += 1
        if letter in consenants:
            c += 1
        i += 1

    if v > c:  # if vowels > consenants return true
        return True
    if v < c:  # if vowels < consenants return false
        return False
    if v == c:  # if vowels = consenants return none
        return None

# Examples:
#   print(task_1("Cracking Toast, Gromit!!!"))
#   print(task_1("HELLOOOOOOOO!"))
#   print(task_1("Helloo"))


# ~~~~~~~~~~ TASK 2 ~~~~~~~~~~
# 2. The volume of a sphere is given by the formula V = (4/3)πr^3.
# Given an input R, return the volume of a sphere with radius R.
# You can assume R is positive.

# Resources used:
#   https://docs.python.org/3/library/math.html

def task_2(R):
    return (4/3)*math.pi*math.pow(R, 3)

# Examples:
#   print(task_2(6))


# ~~~~~~~~~~ TASK 2 ~~~~~~~~~~
# 3. Comma-separated values (CSV) is a popular format for storing data.
# For the first step of the CSV portion of this assignment, write a
# function that takes a list of strings as inputs, and returns a single
# string created by joining all the input strings together, with a comma
# separating them. Example: ["I", "Love", "Python"] -> "I,Love,Python"

# Resources used:
#   https://www.w3schools.com/python/python_for_loops.asp
#   https://geekflare.com/python-remove-last-character/


def task_3(input):
    # declare an emply string, strung
    strung = ""

    # write a for loop that concatenates each element to the end of strung
    for word in input:
        strung = strung + word + ","

    strung = strung[:-1]  # remove the last comma
    return strung

# Examples:
#   print(task_3(["I", "Love", "Python"]))
#   print(task_3(["Minions:", "Rise", "of", "Gru"]))


# ~~~~~~~~~~ TASK 4 ~~~~~~~~~~
# 4. Now write another function that takes two arguments: a list of lists
# of strings, and a filepath. The function should apply the operation
# from question 3 to each list in the list, and write the result as a row
# of the file at filepath. The function doesn't need to return anything.

# Recources used:
#   https://www.w3schools.com/python/python_file_write.asp

def task_4(input, filepath):

    # open a file path and append to the file
    f = open(filepath, "a")

    # write a for loop that iterates over each list in the input list
    # declare empty string, strung
    for list in input:
        strung = ""

        # write an inner for loop that concatenates each element of the
        #   list to the end of strung
        for word in list:
            strung = strung + word + ","

        strung = strung[:-1]  # remove the last comma
        f.write(strung + "\n")

# Example:
#   print(task_4([["Java", "Is", "To", "JavaScript"], [
#      "As", "Car", "Is", "To", "Carpet"], ["HmmHmmHmm", "Programming", "Humor"]], "./test.txt"))


# ~~~~~~~~~~ TASK 5 ~~~~~~~~~~
# 5. Finally, write the reverse of question 4: write a function that takes in
# a filename (which we will assume is a CSV), and returns a list of lists
# of strings, where one row in the file corresponds to one list in the
# output list (and each value between the commas in the file row is one
# element in the list). To see an example, just flip the input and output
# above.


# ~~~~~~~~~~ TASK 6 ~~~~~~~~~~
# 6. Error-handling is an important part of writing web apps, especially when
# your app talks to potentially unreliable third-party APIs. This problem
# will have you practice the try and except keywords in Python. Write a
# function that takes two arguments, adds them together, and returns the
# result. Your function should be resilient to mismatched input types -- you
# should catch the error if the user submits a string and an integer, for
# example.

# ~~~~~~~~~~ TASK 7 ~~~~~~~~~~
# 7. Write a function that takes a list of integers and returns the same list,
# but with all values that occur only once removed (for example, [1,2,3,1]
# would become [1,1])
