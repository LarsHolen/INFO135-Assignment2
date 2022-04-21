# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 16:33:22 2022

@author: Lars Holen

INFO135
Assignment 1

"""

#%% Task 1.
"""
Suppose you’re looking for a word in the following dictionaries. In the worst case how
many steps do you think the search will take with Binary Search?
a) Persian dictionary with 171476 words
b) English dictionary with 1100373 words
c) Chinese dictionary with 260000 words

"""
def WorstCaseStepsInBinarySearch(name, words):
    """
    Parameters
    ----------
    name : String
        Name of list/dictionary one would search.
    words : int
        Number of items/word in the list.

    Returns
    -------
    None. Prints how many steps binary search would do to find ine item/word 
    in a worst case scenario.

    """
    
    # Divides the words til its >=1 and counts how many times it takes
    steps = 0
    while(words >= 1):
        words = words // 2
        steps += 1
    print("Worst case scenario with binary search for", name, "is", steps, "steps.")
    

#%% Task 2.
"""
Write a class called Student that has two following methods:
• Method 1: __init__() that receives name, age and country of a student and sets
them as instance variables.
• Method 2: greeting() that prints the following message for a student whose name
is Sara, 25 years old and from Norway:
student = Student("Sara", 25, "Norway")
student. greeting()
[Output]
Hei! my name is Sara
I am 25 years old.
I am from Norway.
"""
class Student:
    """
        Student class with name, age and country.
        One Method greeting, that print 3 lines of info
    """
    
    def __init__(self, name, age, country):
        """
        Parameters
        ----------
        name : String
            Name of student.
        age : int
            Age of student.
        country : String
            Students country of origin.
        Returns
        -------
        None.
        """
        self.name = name
        self.age = age
        self.country = country
        
        
    def greeting(self):
        """
        Returns
        -------
        None. Prints 3 lines of information.
        """
        print("Hei! my name is", self.name, "\nI am", self.age, "years old.\nI am from", self.country + ".")
        
#%% Task 3.
"""
Given the following linked-list class, write a method called print_list() that loops
over and prints the entire contents of a linked-list starting from head.
class LinkedList:
 def __init__(self):
 self.head = None
"""
class LinkedList:
    """
    Linked list class.  Contain the head node 
    """
    def __init__(self):
        """
        Init Function.  Set head to None
        Returns
        -------
        None.

        """
        self.head = None
    
    def print_list(self):
        """
        Print all the items in the linked list

        Returns
        -------
        None.

        """
        item = self.head
        while item:
            print(item.data)
            item = item.next


class Node:
    """
    Node class for the Linked list
    """
    def __init__(self, data):
        """
        Init function.  Setting the data, and Next node to None
        Parameters
        ----------
        data : Whatever data one want in the list
        Returns
        -------
        None.
        """
        self.data = data
        self.next = None
        

#%% Task 4.
"""
Write a function reverse_list() that receives a Python list, builds a Stack with the
same elements, and prints the reversed list.
[Hint]: you can find the implementation of Stack in the slides of Lecture 2.
my_list = [1,2,3,4,5]
reverse_list(my_list)
[Output]: [5,4,3,2,1]
"""
class Stack():
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    

def reverse_list(inputList):
    stack = Stack()
    for i in inputList:
        stack.push(i)
    # Not relly sure why I should build the stack since printing the reverse
    # can be done like this, without changing the list at all.
    print(stack.items[::-1])

    



#%% Main



def main():
    # TASK 1
    print("Task 1.")
    print("a) ", end="")
    WorstCaseStepsInBinarySearch("Persian dictionary", 171476)
    print("b) ", end="")    
    WorstCaseStepsInBinarySearch("English dictionary", 1199373)
    print("c) ", end="")
    WorstCaseStepsInBinarySearch("Chinese dictionary", 260000)
    print("")
    
    # TASK 2
    student = Student("Sara", 25, "Norway")
    student.greeting()
    print("")
    
    # TASK 3
    print("Printing the linked list in from head to tail(Added data to the class to see the order")
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    linkedList = LinkedList()
    linkedList.head = n1
    linkedList.print_list()
    
    # TASK 4
    print("Reversing a list")
    my_list = [1,2,3,4,5]
    print("Reversing this list:", my_list)
    print("And get: ", end="")
    reverse_list(my_list)
    
if __name__ == "__main__":
    main()