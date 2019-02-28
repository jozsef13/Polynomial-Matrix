import numpy as np

def readMatrix(n, matrix):
    #function for reading a matrix
    for i in range(n):
        for j in range(n):
            print("Enter the maximum power of the polynomial(can be smaller or equal with 10) from position ", i, j, " : ")
            power = int(input()) #reading the power of the polynomials from i,j position
            print("Enter the coefficients of the polynomial from position", i, j, " : ")
            #depending on the value we give to variable power, we read the coefficients and put them into a matrix in a polynomial form using poly1d from numpy module, we can read a maximum of 10 coefficients
            if power == 0:
                x0 = float(input())
                matrix[i][j] = np.poly1d([x0])
            if power == 1:
                x0, x1 = float(input()), float(input())
                matrix[i][j] = np.poly1d([x0, x1])
            if power == 2:
                x0, x1, x2 = float(input()), float(input()), float(input())
                matrix[i][j] = np.poly1d([x0, x1, x2])
            if power == 3:
                x0, x1, x2, x3 = float(input()), float(input()), float(input()), float(input())
                matrix[i][j] = np.poly1d([x0, x1, x2, x3])
            if power == 4:
                x0, x1, x2, x3, x4 = float(input()), float(input()), float(input()), float(input()), float(input())
                matrix[i][j] = np.poly1d([x0, x1, x2, x3, x4])
            if power == 5:
                x0, x1, x2, x3, x4, x5 = float(input()), float(input()), float(input()), float(input()), float(input()), float(input())
                matrix[i][j] = np.poly1d([x0, x1, x2, x3, x4, x5])
            if power == 6:
                x0, x1, x2, x3, x4, x5, x6 = float(input()), float(input()), float(input()), float(input()), float(input()), float(input()), float(input())
                matrix[i][j] = np.poly1d([x0, x1, x2, x3, x4, x5, x6])
            if power == 7:
                x0, x1, x2, x3, x4, x5, x6, x7 = float(input()), float(input), float(input()), float(input()), float(input()), float(input()), float(input()), float(input())
                matrix[i][j] = np.poly1d([x0, x1, x2, x3, x4, x5, x6, x7])
            if power == 8:
                x0, x1, x2, x3, x4, x5, x6, x7, x8 = float(input()), float(input()), float(input), float(input()), float(input()), float(input()), float(input()), float(input()), float(input())
                matrix[i][j] = np.poly1d([x0, x1, x2, x3, x4, x5, x6, x7, x8])
            if power == 9:
                x0, x1, x2, x3, x4, x5, x6, x7, x8, x9 = float(input()), float(input()), float(input()), float(input), float(input()), float(input()), float(input()), float(input()), float(input()), float(input())
                matrix[i][j] = np.poly1d([x0, x1, x2, x3, x4, x5, x6, x7, x8, x9])
            if power == 10:
                x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10 = float(input()), float(input()), float(input()), float(input()), float(input), float(input()), float(input()), float(input()), float(input()), float(input()), float(input())
                matrix[i][j] = np.poly1d([x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10])

def printMatrix(n, matrix):
    #function for printing a matrix, but not in a 2D form 
    for i in range(n):
        for j in range(n):
            print(matrix[i][j])
        print()

def matrixAddition(matrix1, matrix2, add, n):
    #function for the addition operation between two matrices
    for i in range(n):
        for j in range(n):
            add[i][j] = matrix1[i][j] + matrix2[i][j]

def matrixMultiplication(matrix1, matrix2, multi, n):
    #function for the multiplication operation between two matrices
    for i in range(n):
        for j in range(n):
            for k in range(n):
                multi[i][j] = multi[i][j] + (matrix1[i][k] * matrix2[k][j])

def matrixEvaluation(n, x, matrix, evaluation):
    #function for the evaluation of a matrix in a point x
    for i in range(n):
        for j in range(n):
            evaluation[i][j] = np.polyval(matrix[i][j], x) #we go through the matrix and we evaluate each i,j elements using polyval function imported from the numpy module
