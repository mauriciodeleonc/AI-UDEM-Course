'''
    matriz-operations-practice.py
    Python script for practicing
    different type of basic operations 
    with matrices using the numpy library.

    Author: Mauricio A. De Leon Cardenas
    Email: mauricio.deleonc@udem.edu
    Institution: Universidad de Monterrey
    First created: Mon 03 Feb, 2020
'''
import numpy as np

def add_matrices(X,Y):
    '''
        Function that adds two 2-dimensional numpy arrays
        using the numpy library.

        INPUTS
        :param X: numpy-type matrix
        :param Y: numpy-type matrix

        OUTPUT
        :return Z: numpy-type matrix with the result of X + Y
    '''
    Z = np.add(X,Y)

    return Z

def subtract_matrices(X,Y):
    '''
        Function that subtracts two 2-dimensional numpy arrays
        using the numpy library.

        INPUTS
        :param X: numpy-type matrix
        :param Y: numpy-type matrix

        OUTPUT
        :return Z: numpy-type matrix with the result of X - Y
    '''
    Z = X.__sub__(Y)

    return Z

def multiply_matrices(X,Y):
    '''
        Function that multiplies two 2-dimensional numpy arrays
        using the numpy library.

        INPUTS
        :param X: numpy-type matrix
        :param Y: numpy-type matrix

        OUTPUT
        :return Z: numpy-type matrix with the result of X * Y
    '''
    Z = X.__mul__(Y)
    return Z

def inverse_matrx(X):
    '''
        Function that multiplies two 2-dimensional numpy arrays
        using the numpy library and a constant (number).

        INPUTS
        :param Y: numpy-type matrix
        :param X: numpy-type matrix

        OUTPUT
        :return Z: numpy-type matrix with the result of X * Y
    '''
    Z = np.linalg.inv(X) 
    return Z

def divide_matrices(X,Y):
    '''
        Function that divides two 2-dimensional numpy arrays
        using the numpy library and a constant (number).

        INPUTS
        :param X: numpy-type matrix
        :param Y: numpy-type matrix

        OUTPUT
        :return Z: numpy-type matrix with the result of X / Y
    '''
    Z = np.true_divide(X,Y)
    return Z

def multiply_matrix_constant(a,X):
    '''
        Function that multiplies a 2-dimensional numpy array
        using the numpy library and a constant (number).

        INPUTS
        :param a: int number
        :param X: numpy-type matrix

        OUTPUT
        :return Z: numpy-type matrix with the result of a * X
    '''
    Z = X.__mul__(a)
    return Z

def transpose_matrix(X):
    '''
        Function that transposes a matrix (X) using numpy library.

        INPUTS
        :param X: numpy-type matrix

        OUTPUT
        :return Z: numpy-type matrix with the
            transposed matrix
    '''
    Z = X.T
    return Z

def identity_matrix(A):
    '''
        Function that generates an identity matrix
        of same size as A using numpy library.

        INPUTS
        :param A: numpy-type matrix

        OUTPUT
        :return I: numpy-type matrix with the
            identity matrix
    '''  
    I = np.identity(A.size)
    return I

def zero_matrix(A):
    '''
        Function that generates a zero matrix
        of same size as A using numpy library.

        INPUTS
        :param A: numpy-type matrix

        OUTPUT
        :return O: numpy-type matrix with
            the zero matrix
    '''
    O =  np.zeros(shape = A.shape,  dtype = np.int8)
    return O

def main():
    #Initialice 2-dimensional arrays x and y
    X = np.array([[1,2,3],[4,5,6],[7,8,9]], dtype = np.int8)
    Y = np.array([[10,11,12],[13,14,15],[16,17,18]], dtype = np.int8)

    #Initialice value a (used in multiply_matrix_constant())
    a = 5

    #Print results in command line
    print(28 * '-')
    print('OPERATIONS WITH MATRICES:')
    print(28 * '-')
    print('X:\n' +  str(X) + '\n')
    print('Y:\n' +  str(Y) + '\n')
    print('X + Y: \n' + str(add_matrices(X,Y)) + '\n')
    print('X - Y: \n' +  str(subtract_matrices(X,Y)) + '\n')
    print('XY: \n' + str(multiply_matrices(X,Y)) + '\n')
    print('YX: \n' + str(multiply_matrices(Y,X)) + '\n')
    print('X^-1: \n' + str(inverse_matrx(X)) + '\n')
    print('X/Y: \n' + str(divide_matrices(X,Y)) + '\n')
    print('Y/X: \n' + str(divide_matrices(Y,X)) + '\n')
    print('5 * X: \n' + str(multiply_matrix_constant(a,X)) + '\n')
    print('Transpose of X: \n' + str(transpose_matrix(X)) + '\n')
    print('Identity matrix of same size as X: \n' + str(identity_matrix(X)) + '\n')
    print('Zero matrix of same size as X: \n' + str(zero_matrix(X)) + '\n')

    return None

#Call main program
main()