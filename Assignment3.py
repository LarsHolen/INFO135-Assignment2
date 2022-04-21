# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 09:04:02 2022

@author: Lars Holen

INFO135
Assignment 3

"""


#%% Task 1.
"""
What is the printed output of the following code snippet? 

def hash_function(input_string, table_size):
    total = 0
    length = len(input_string)
    for pos in range(length):
        total = total + ord(input_string[pos]) + length
    return total % table_size

my_list = ['a1b2c3', 'CiTiBnk', '232323', 'myLaptop']
my_choice = 19

for item in my_list:
    print(hash_function(item, my_choice), end='')


This function will return 59166 with the given list.  Which is
an integer in the range of slots.

"""

def hash_function(input_string, table_size):
    total = 0
    length = len(input_string)
    for pos in range(length):
        total = total + ord(input_string[pos]) + length
    return total % table_size


#%% Task 2.
"""
Write a class HashClass that has:
• a constructor method to receive the id number of a person as parameter.
• a method called hash_it() that generates a random integer number called salt
(ranging from 1 to 1000), adds the value of salt to the id number, and then hashes the
result using SHA algorithm (see Lecture 6).
• a method called print_it()that prints out the generated hash number.
• Use random.randint() to generate a random integer number.
"""
import hashlib as hl
import random

class HashClass:
    def __init__(self, id_num):
        self.id_num = id_num
        self.hash_id_num = ""
        

    def hash_it(self):
       salt = random.randint(1,1000) 
       id_num_salted = self.id_num + salt
       self.hash_id_num = hl.sha1(str(id_num_salted).encode()).hexdigest()
       
      
    def print_it(self):
        print(self.hash_id_num)


#%% Task 3.
"""
The following image shows the IMDB Top movies in 2020. You are given a List of Tuples,
each representing (title, budget) of movies. Budgets are given in $ Million.
Write a Python function, called sort_and_print(), that first sorts the movies based
on their budgets and then prints the title of the movie with the largest budget.
[Note]: You can implement any sorting algorithm you prefer.
"""
def sort_and_print(list_to_sort):
    # Making a tuple to save the item with the highest number in the second slot 
    largest_budget = ("Placeholder", 0.0)
    for item in list_to_sort:
        #  Test if item's budget is larger than the one we have
        if item[1] > largest_budget[1]:
            # Set current largest to item
            largest_budget = item
    # Print the name to screen
    print(largest_budget[0])

#%% Task 4.
"""
Write a “recursive” function called magic_function() that receives as input a string
variable and computes and returns a list of all permutations of a given input. See the
example below:
"""

       
def magic_function(input_string, output_string = " "):
    output_list = []
    # If we are at the first letter, return an empty list
    if len(input_string) == 0:
        output_list.append(output_string)
        return output_list
    for i in range(len(input_string)):
        character = input_string[i]
        left_side = input_string[0:i]
        right_side = input_string[i+1:]
        combined = left_side + right_side
        output_list = output_list + magic_function(combined, output_string + character)
    return output_list


#%% Main func

def main():
    print("Task 1.")
    my_list = ['a1b2c3', 'CiTiBnk', '232323', 'myLaptop']
    my_choice = 19

    for item in my_list:
        print(hash_function(item, my_choice), end='')
    print("\n")
    
    print("Task 2.")
    print("Using HashClass to salt and hash id = 11011999 and print the hashed id to screen:")
    h = HashClass(11011999)
    h.hash_it()
    h.print_it()
    
    print("\nTask 3.")
    list_of_tuples = [('Birds of prey', 97.1),
                  ("Dolittle", 175.0),
                  ("The Gentlemen", 7.0),
                  ("Falling", 22.0)]
    print("The movie with largest budget is:")
    sort_and_print(list_of_tuples)
    
    print("\nTask 4.")
    i_string = "abcd"
    tList = magic_function(i_string, "")
    print(tList)

    
#%% Start
    
if __name__ == "__main__":
    main()