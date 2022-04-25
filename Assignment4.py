# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 10:25:47 2022

@author: Lars Holen
Assignment 4

"""


#%% Task 1
"""
Given the following Graph, which set represents the Edge set of the Graph?
a) { (A,B), (B,C), (B,D), (C,A), (C,D) }
b) { (A,B), (B,C), (B,D), (C,A), (D,A) }
c) { (A,B), (B,C), (C,B), (C,A), (D,A) }
d) { (A,B), (B,C), (A,C), (C,A), (D,B) }
e) None of the above


Answer: b)
"""
def task1():
    print('Task 1. Answer: b')

#%% Task 2
"""
Extend the implementation of the solver for the N-queen problem by adding a new function
called is_solution() that receives as a parameter a candidate solution and checks if the
solution is valid (correct) or not. The candidate solution is in the form of a list of string,
indicating the position of the queens in the chessboard.

Note 1: You can find an example implementation of solver for N-queen problem in lecture 5.
Note 2: You can assume N=5.
7
You can change other functions if needed. Here is an example output for two candidate
solutions.




COLUMNS = "abcde"
NUM_QUEENS = len(COLUMNS)
ACCEPT = 1
CONTINUE = 2
ABANDON = 3
a,ll_solutions = []
def solve(partial_sol):...
def examine(partial_sol):...
def attacks(p1, p2):...
def extend(partial_sol):...
def is_solution(candidate_solution):
[your code here]
candidate_solution1 = ['d3', 'c1', 'e5', 'b4', 'a2']
candidate_solution2 = ['e4', 'a1', 'c5', 'd2', 'b1']
result1 = is_solution(candidate_solution1)
result2 = is_solution(candidate_solution2)
print("Candidate Solution 1:", result1)
print("Candidate Solution 2:", result2)
[Output]:
Candidate Solution 1: Valid!
Candidate Solution 2: Invalid!

"""
#  Making a class to contain the NQueen code
class NQueen():
# Takes n as the size of the board
    def __init__(self, n: int = 0):
        self.NUM_QUEENS = n
        # Make letters for the columns
        self.COLUMNS = [chr(97+x) for x in range(n)]
        self.ACCEPT = 1
        self.CONTINUE = 2
        self.ABANDON = 3
        # A list where the solves computed in the solve method are saved
        self.SOLVES = []
        self.HAS_SOLVED = False

    # From lecture
    def extend(self, partial_sol):
        results = []
        row = len(partial_sol) + 1
        for column in self.COLUMNS:
            new_solution = list(partial_sol)
            new_solution.append(column + str(row))
            results.append(new_solution)
        return results
    
    # From lecture
    def examine(self, partial_sol):
        for i in range(len(partial_sol)):
            for j in range(i + 1, len(partial_sol)):
                if self.attacks(partial_sol[i], partial_sol[j]):
                    return self.ABANDON
        if len(partial_sol) == self.NUM_QUEENS:
            return self.ACCEPT
        else:
            return self.CONTINUE
    # From lecture
    def attacks(self, p1, p2):
        column1 = self.COLUMNS.index(p1[0]) + 1
        row1 = int(p1[1])
        column2 = self.COLUMNS.index(p2[0]) + 1
        row2 = int(p2[1])
        return (
            row1 == row2 or
            column1 == column2 or
            abs(row1-row2) == abs(column1-column2)
        )
    # From lecture.  Modified only with an option to print or not
    def solve(self, partial_sol = [], printIt = True): 
        exam = self.examine(partial_sol)
        if exam == self.ACCEPT:
            if printIt:
                print(partial_sol)
            self.SOLVES.append(partial_sol)
        elif exam != self.ABANDON:
            for p in self.extend(partial_sol):
                self.solve(p,printIt)

    # Task solution
    def is_solution(self, candidate_solution):
        # Setting variables to fit with the canidate_solution
        self.NUM_QUEENS = len(candidate_solution)
        self.COLUMNS = [chr(97+x) for x in range(self.NUM_QUEENS)]
        self.SOLVES = []
        
        if self.examine(candidate_solution) == self.ACCEPT:
            return "Valid!"
        return "Invalid!"
        
        
#%% Task 3
"""
Cycle in a Graph is a path that starts from a vertex (node) and ends at the same vertex. The
Graph in the following figure shows a cycle.

<image>

Use the Graph class in Lecture notes 7, write a new method called find_cycle(node)
that receives a node as a parameter and traverses the Graph starting from the given node.
The method should print “Cycle found!” if it detects a cycle in the Graph and “Cycle not
found!”, otherwise. You can use either BFS or DFS algorithm.
"""
class Graph():
    def __init__(self):
        self.graph = dict()
        self.visited = set()
    
    def add_edge(self, node, neighbour):
        if node not in self.graph:
            self.graph[node] = [neighbour]
        else:
            self.graph[node].append(neighbour)
            
    def print_graph(self):
        print(self.graph)
        
    def find_cycle(self, node):
        # if node dont exist, return msg
        if node not in self.graph:
            return "Node does not exist"
        # loop the nodes neighbours
        for neighbour in self.graph[node]:
            # if neighbour is in visited, return Cycle found msg
            if neighbour in self.visited:
                return 'Cycle found!'
            # if neighbour is not in visited, add neighbour to visited and call find_cycle on neighbour
            self.visited.add(neighbour)
            # use recursion to find cycle in neighbour
            if self.find_cycle(neighbour):
                return 'Cycle found!'          
        return 'Cycle not found!'
                    



#%%
def main():
    print("Main running")
    task1()
    print()
    
    print('Task 2.')
    q = NQueen()
    candidate_solution1 = ['d3', 'c1', 'e5', 'b4', 'a2']
    candidate_solution2 = ['e4', 'a1', 'c5', 'd2', 'b1']
    result1 = q.is_solution(candidate_solution1)
    result2 = q.is_solution(candidate_solution2)
    print("Candidate Solution 1:", result1)
    print("Candidate Solution 2:", result2)
    print()
    
    print('Task 3.')
    my_graph = Graph()
    my_graph.add_edge('A', 'B')
    my_graph.add_edge('B', 'D')
    my_graph.add_edge('C', 'B')
    my_graph.add_edge('C', 'J')
    my_graph.add_edge('D', 'E')
    my_graph.add_edge('D', 'F')
    my_graph.add_edge('E', 'C')
    my_graph.add_edge('E', 'G')
    my_graph.add_edge('F', 'H')
    my_graph.add_edge('G', 'I')
    
    result = my_graph.find_cycle('A')
    print(result)
    print()
    print(my_graph.print_graph())

  


if __name__ == "__main__":
    main()