# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 10:55:08 2020

@author: pocoloco
"""

from copy import deepcopy
from time import time

class Board:
    def __init__(self,n):
        self.__N = n
        self.__board = [[0 for col in range(0,n)] for row in range (0, n)]
    
    def getN(self):
        return self.__N
    
    def getBoard(self):
        return self.__board[:]
    
    def setBoard(self, vals):
        self.__board=vals[:]
    
    def get(self, i, j):
        return self.__board[i][j]
    
    def update(self, i, j, el):
        self.__board[i][j]=el
        
        
class State:
    def __init__(self, values):
        self.__values=values #a BOARD object
        self.__queens = 0 #number of queens placed on the board
        self.__myQueens = [] #positions of the queens in the board; pairs (row, col)

    def getQueens(self):
        return self.__queens
    
    def getMyQueens(self):
        return self.__myQueens
    
    def addQueen(self, i, j):
        self.__queens+=1
        self.__myQueens.append((i, j))
    
    def removeQueen(self):
        self.__queens-=1
        
    def get(self, i, j):
        return self.__values.get(i, j)
    
    def update(self, i, j, el):
        self.__values.update(i, j, el)
    
    def getN(self):
        return self.__values.getN()
    
    def get_values(self):
        return self.__values.getBoard()
     
    def set_values(self, vals):
        self.__values.setBoard(vals)
        
        
    def __str__(self):
        s=""
        for i in range (0, self.getN()):
            for j in range (0, self.getN()):
                s+=str(self.__values.get(i, j))
            s+="\n"
        return s

class Problem:
    def __init__(self):
        self.__initialState=None
        self.__finalState = None
        self.__values = None
        #TODO

        
    def isSafe(self, state):
        #checks if it can lead to sols
        board = state.get_values()
        for row in board:
            s=0
            for el in row:
                s+=el
                if s>1:
                    return False #sum on rows>1 already
        for j in range(0, state.getN()):
            s=0
            for i in range (0, state.getN()):
                s+=board[i][j]
                if s>1:
                    return False #sum on cols>1 already
        
        myQueens = state.getMyQueens()
        if len(myQueens)>=2:
            for i in range (0,len(myQueens)-1):
                for j in range (i+1, len(myQueens)):
                    deltaR = abs(myQueens[i][0]-myQueens[j][0])
                    deltaC = abs(myQueens[i][1]-myQueens[j][1])
                    if deltaR == deltaC:
                        return False #same diagonal
        return True

    def isSolution(self, state):
        if state.getN() == state.getQueens() and self.isSafe(state):
            return True
        else:
            return False
    
    def expand(self, state):
        #checks valid pos and adds a queen to a state  
        available=[]
        for i in range(0,state.getN()):
            for j in range(0, state.getN()):
                if state.get(i, j)==0:
                    available.append((i, j))
        
        states=[]
        for pair in available:
            auxState=deepcopy(state)
            auxState.update(pair[0], pair[1], 1)
            auxState.addQueen(pair[0], pair[1])
            states.append(auxState)
       
        return states
            
        
    def get_initialState(self):
        return self.__initialState
    
    def set_initialState(self, state):
        self.__initialState=state
             
    def readFromFile(self):
        with open('lab2.txt', 'r') as f:
            n=int(f.readline())
        return n
        
    def isUnderAttackPosition(self, state, row, col):
        #this function will check if a cell is under attack by other queens
        queens=state.getMyQueens()
        queenRows= [s[0] for s in queens]
        if row in queenRows:
            return True #same row
        queenCols =[s[1] for s in queens]
        if col in queenCols:
            return True #same col
        for pair in queens:
            deltaRow = abs(pair[0]-row)
            deltaCol = abs(pair[1]-col)
            if deltaRow == deltaCol:
                return True #same diagonal
        return False
    
    def validPositions(self, state):
        n=state.getN()
        score = n*n
        board = state.get_values()
        for i in range(0,n):
            for j in range(0,n):
                if not self.isUnderAttackPosition(state, i, j) and board[i][j]!=1:
                    score-=1
        return score
         
    def heuristic(self, state): 
        #this function gives a score to a state, the smaller the better
        
        score = 0 # this is equivalent to a state=solution
        if self.isSafe(state) == False:
            return float('inf')
        score = state.getN()-state.getQueens()
        score = score + self.validPositions(state)
        return score
                
        
class Controller:
    def __init__(self, problem):
        self.__problem = problem
        board=Board(problem.readFromFile())
        state = State(board)
        self.__problem.set_initialState(state) #initial state is an empty board
   
    def DFS(self, root):
        visited=[]
        stack = [] 
        stack.append(root)
        while len(stack)>0:
            state = stack.pop() #list in python can be used like stacks
            if self.__problem.isSolution(state):
                return state
            visited.append(state)
            if self.__problem.isSafe(state):
                states = self.__problem.expand(state)
                for st in states:
                    if st not in visited:
                        stack.append(st)
        return None
        
    
    def GBestFS(self, root):
        visited=[]
        queue=[]
        queue.append(root)
        while len(queue)>0:
            state=queue.pop(0) #use it as queue, FIFO
            visited=visited+[state]
            if self.__problem.isSolution(state):
                return state
            if self.__problem.isSafe(state):
                aux=[]
                states = self.__problem.expand(state)
                for st in states:
                    if st not in visited:
                        aux.append(st)
                aux = [(s,self.__problem.heuristic(s)) for s in aux]
                #SORT BY HEURISTIC WHATINTHEASSFAISTHAT
                self.orderStates(aux)
                aux = [st[0] for st in aux]
                queue = aux[:]+queue #place it at the start
        return None
    
    
    def Greedy(self, root):
        visited=[]
        queue=[]
        queue.append(root)
        while len(queue)>0:
            state=queue.pop(0) #use it as queue, FIFO
            visited=visited+[state]
            if self.__problem.isSolution(state):
                return state
            if self.__problem.isSafe(state):
                aux=[]
                states = self.__problem.expand(state)
                for st in states:
                    if st not in visited:
                        aux.append(st)
                aux = [(s,self.__problem.heuristic(s)) for s in aux]
                #SORT BY HEURISTIC WHATINTHEASSFAISTHAT
                self.orderStates(aux)
                aux = [st[0] for st in aux]
                queue = [aux[0]] #take only the first one, this is the greedy approach
                # even if it won't take us to a solution, we swing it
        return None
                
    
    def partition(self, array, low, high):
        i = low - 1 #idx of small el
        pivot = array[high][1]
        for j in range(low, high):
            if array[j][1]<=pivot:
                i=i+1
                array[i], array[j]=array[j],array[i]
        array[i+1], array[high]=array[high], array[i+1]
        return (i+1)
    
    def quickSort(self, array, low, high):
        if low<high:
            #pi partitioning index
            pi = self.partition(array, low, high)
            self.quickSort(array, low, pi-1)
            self.quickSort(array, pi+1, high)
    
    def orderStates(self, lst):
        self.quickSort(lst, 0, len(lst)-1)
        
    def getProblem(self):
        return self.__problem
    
        
        
class UI:
    def __init__(self, controller):
        self.__controller = controller
    
    def printMenu(self):
        s=""
        s+="App for solving a Latin Square similar to n-queen problem\n"
        s+="Press 1 in order to solve it using DFS\n"
        s+="Press 2 in order to solve it using Greedy BestFS\n"
        s+="Press 3 in order to solve it using Greedy\n"
        s+="Press 0 for exiting the application\n"
        print(s)
        
    def run(self):
        running=True
        self.printMenu()
        while running:
            try:
                print('You do you boo: ')
                command=int(input())
                print('\n')
                if command == 0:
                    running = False
                if command == 1:
                    self.DFS()
                if command == 2:
                    self.GBestFS()
                if command == 3:
                    self.Greedy()
            except:
                print('invalid command')
                
    def DFS(self):
        startClock = time()
        solution = self.__controller.DFS(self.__controller.getProblem().get_initialState())
        if solution is None:
            print("Couldn't find any solution, oopsie!")
        else:
            print(solution)
        print('execution time = ',time()-startClock, " seconds" )
        
    def GBestFS(self):
        startClock = time()
        solution = self.__controller.GBestFS(self.__controller.getProblem().get_initialState())        
        if solution is None:
            print("Couldn't find any solution, oopsie!")
        else:
            print(solution)
        print('execution time = ',time()-startClock, " seconds" )
         
    def Greedy(self):
        startClock = time()
        solution = self.__controller.Greedy(self.__controller.getProblem().get_initialState())
        if solution is None:
            print("Couldn't find any solution, oopsie!")
        else:
            print(solution)
        print('execution time = ',time()-startClock, " seconds" )
    
    
    
problem = Problem()
controller = Controller(problem)
ui = UI(controller)
ui.run()
    
    
    