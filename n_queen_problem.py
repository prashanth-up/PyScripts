# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 09:05:32 2021

@author: mahesh
"""

import numpy as np
def printSolution(board): 
    print(f"---------------------------SOLUTION FOR {N} queen problem ----------------------------------------")
    for i in range(N): 
        for j in range(N): 
            print (board[i][j], end = " ") 
        print()
    print("f--------------------------------------------------------------------------------------------------")

def isSafe(board, row, col): 
    
    for i in range(col): 
        if board[row][i] == 1: 
            return False
  
    for i, j in zip(range(row, -1, -1),range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False

    for i, j in zip(range(row, N, 1),range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
  
    return True

def solveNQUtil(board, col): 
    if col >= N: 
        return True
    
    for i in range(N): 
        if isSafe(board, i, col): 
            board[i][col] = 1
            if solveNQUtil(board, col + 1) == True: 
                return True
            
            board[i][col] = 0
    return False

def solveNQ(): 
    board = np.zeros((N,N),dtype = int).tolist()
  
    if solveNQUtil(board, 0) == False: 
        print ("No solution bruh!") 
        return False
  
    printSolution(board) 
    

if __name__ == "__main__":    
    global N 
    N = int(input("enter the N, stranger, heh heh: "))
    solveNQ() 