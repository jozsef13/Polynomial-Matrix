"""

Homework problem for OOP course
Problem 13 - Operations on polynomial square matrices with real coefficients
Created by Simon Jozsef-Gabriel from CEN 2.3

"""

import module 
import numpy as np

n = int(input("Enter the number of rows and columns for the matrix A: ")) #reading the number of rows and columns for matrix A which is a square matrix
matrixA = [[0 for i in range(n)] for j in range(n)] #initialization of matrix A
module.readMatrix(n, matrixA) #calling the function for reading the matrix A
print()
print("This is the matrix A: ") 
module.printMatrix(n, matrixA) #calling the function for printing matrix A

m = int(input("Enter the number of rows and columns for the matrix B: ")) #reading the number of rows and columns for matrix B which is a square matrix
matrixB = [[0 for i in range(m)] for j in range(m)] #initialization of matrix B
module.readMatrix(m, matrixB) #calling the function for reading the matrix B
print()
print("This is the matrix B: ")
module.printMatrix(m, matrixB) #calling the function for printing matrix B

if n == m:
    #making the addition of two polynomials matrices
    additionMatrix = [[0 for i in range(n)] for j in range(n)] #initialization of addition matrix in which we make the addition between matrices A and B
    module.matrixAddition(matrixA, matrixB, additionMatrix, n) #calling the function for addition
    print("The addition between matrix A and matrix B is this matrix: ")
    module.printMatrix(n, additionMatrix) #calling the function for printing the addition matrix
else:
    #if we can't do the addition we print this message
    print("We can't do an addition, beacuse the number of rows and columns from matrix A isn't equal with the number of rows and columns from matrix B!")

if n == m:
    #making the multiplication of two polynomials matrices
    multiplicationMatrix = [[0 for i in range(n)] for j in range(n)] #initialization of multiplication matrix in which we make the multiplication between matrices A and B
    module.matrixMultiplication(matrixA, matrixB, multiplicationMatrix, n) #calling the function for multiplication
    print("The multiplication between matrix A and matrix B is this matrix: ")
    module.printMatrix(n, multiplicationMatrix) #calling the function for printing the multiplication matrix
else:
    #if we can't do the multiplication we print this message
    print("We can't do a multiplication, because the number of rows from matrix A is not equal with the number of columns from matrix B or vice-versa!")

evaluationMatrixA = [[0 for i in range(n)] for j in range(n)] #initialization of the evaluation matrix in which we make the evaluation for matrix A
print()
x = float(input("Enter the evaluation point x = ")) #reading the evaluation point
print()
module.matrixEvaluation(n, x, matrixA, evaluationMatrixA) #calling the function for evaluation of matrix A in the point x
print("This is the evaluation matrix for matrix A in the point x = ", x)
module.printMatrix(n, evaluationMatrixA) #calling the function for printing the evaluation matrix in point x for matrix A

evaluationMatrixB = [[0 for i in range(m)] for j in range(m)] #initialization of the evaluation matrix in which we make the evaluation for matrix B
print()
module.matrixEvaluation(n, x, matrixB, evaluationMatrixB) #calling the function for evaluation of matrix B in the point x
print("This is the evaluation matrix for matrix B in the point x = ", x)
module.printMatrix(m, evaluationMatrixB) #calling the function for printing the evaluation matrix in point x for matrix B