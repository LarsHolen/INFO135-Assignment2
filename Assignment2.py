# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 16:15:00 2022

@author: Lars Holen

Assignment 2
Advanced Programming (INFO135)

"""


#%% Task 1.
"""
Suppose you have the following list of numbers to sort:
[ 1001, 1030, 1050, 1020, 300, 1080, 1100]
 What will be the partially sorted list after 3 passes of Selection Sort?
"""

def selectionSort(sortList):
    # Counting the passes with this variable
    passes = 0
    # Doing a nested loop to find the min value, and tuple swap it
    for i in range(len(sortList)):
        minValueIndex = i
        
        for j in range(i+1, len(sortList)):
            if sortList[minValueIndex] > sortList[j]:
                minValueIndex = j
                
                sortList[i], sortList[minValueIndex] = sortList[minValueIndex], sortList[i]
                
        # Count each pass, to stop it at the third run and return the partially sorted list.
        passes += 1
        if passes > 2:
            return sortList
    # If the list is sorted in less than 3 passes, it will return the sorted list
    return sortList


#%% Task 2.
"""
Suppose you have the following list of numbers to sort:
[ 210, 15, 111, 90, 45, 120, 150, 200, 100, 140 ]
 What will be the partially sorted list after 3 passes of Bubble Sort?
"""

def boubleSort(sortList):
    # Setting a bool that will test if any swaps has been made in each pass
    isSorted = False
    # Counting the passes with this variable
    passes = 0
    # While loop that wil run til it has done a pass without any swaps
    while (not isSorted):
        isSorted = True
        # Loops through the list, and swap if the item is bigger than the next 
        for i in range(len(sortList)-1):
            if sortList[i] > sortList[i+1]:
                sortList[i], sortList[i+1] = sortList[i+1], sortList[i]
                #  We have done a swap, and we set the isSorted to false
                isSorted = False
        # counting passes
        passes += 1
        # return list after 3 passes according to assignment
        if passes > 2:
            return sortList
    # If the list get sorted with less than 3 passes, it still return the sorted list
    return sortList

#%% Task 3.
"""
Write a function called sort_and_rem_dup() that receives a list of numbers and
returns a sorted list where the duplicates in the numbers are removed.
Please note that:
• you can choose and implement Selection sort, Insertion sort or Bubble sort.
• you cannot use Python Set data structure to remove the duplicates.
• you cannot use sort() or sorted() built-in functions for Python list.
"""
def sort_and_rem_dup(sortList):

    # Doing a nested loop to find the min value, and tuple swap it like I did in the selection sort
    # saving the number of duplicates
    numberOfDups = 0
    for i in range(len(sortList)):
        minValueIndex = i
        
        for j in range(i+1, len(sortList) - numberOfDups):
            # If I find a duplicate, I swap it for the last element in the list - the number of duplicates found
            if sortList[minValueIndex] == sortList[j]:
                numberOfDups += 1
                sortList[j], sortList[len(sortList) - numberOfDups] = sortList[len(sortList) - numberOfDups], sortList[j]
                #  I take one step back in the loop, to sort the item I just swapped from the end of the unsorted list
                j -= 1
            if sortList[minValueIndex] > sortList[j]:
                minValueIndex = j
                sortList[i], sortList[minValueIndex] = sortList[minValueIndex], sortList[i]
            
    del sortList[len(sortList) - numberOfDups : len(sortList)]

    # If the list is sorted in less than 3 passes, it will return the sorted list
    return sortList

#%% Task 4.
"""
Write a function check_palindrome(word) that receives a string variable called
word as an input parameter, and builds a Stack and a Queue where their elements are the
letters (characters) of that word. Then, the function should check and print if the word is
a Palindrome or not. 
"""
def check_palindrome(word):
    # Setting all characters in string to lower case 
    word = word.lower()
    for index in range(len(word)):
        if index > len(word)/2:
            break
        if word[index] != word[len(word)-index-1]:
            return "Not Palindrome"
    return "Palindrome"
    


#%% Main 
def main():
    # First task 
    print("1. The list after 3 passes of selection sort: ", end="")
    l1 = [ 1001, 1030, 1050, 1020, 300, 1080, 1100]
    print(selectionSort(l1) , "\n")
    
    # Second task
    print("2. The list after 3 passes of bouble sort: ", end="")
    l2 = [ 210, 15, 111, 90, 45, 120, 150, 200, 100, 140 ]
    print(boubleSort(l2), "\n")
    
    # Third task
    print("3. The list after sorting and removing duplicates: ", end="")
    my_list = [5,4,3,2,1,2,3,4,5]
    print(sort_and_rem_dup(my_list), "\n")
    
    #Fourth task
    print("4. Output from check_palindrome function with 'hello' and 'civic' input:")
    result = check_palindrome('hello')
    print("   Hello:" , result)
    result = check_palindrome('civic')
    print("   Civic:", result)
    
    
    
    
if __name__ == "__main__":
    main()