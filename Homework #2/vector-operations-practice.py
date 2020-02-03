'''
    vector-operations-practice.py
    Python script for practicing
    different type of basic operations 
    with vectors using the numpy library.

    Author: Mauricio A. De Leon Cardenas
    Email: mauricio.deleonc@udem.edu
    Institution: Universidad de Monterrey
    First created: Mon 03 Feb, 2020
'''

#import numpy library
import numpy as np

def add_vectors(x, y):
    '''
        Function that adds two 1-dimensional numpy arrays
        using the numpy library.

        INPUTS
        :param x: numpy-type vector
        :param y: numpy-type vector

        OUTPUT
        :return z: numpy-type vector with the result of x + y
    '''
    z = np.add(x,y)
    return z

def subtract_vectors(x, y):
    '''
        Function that subtracts two 1-dimensional numpy arrays
        using the numpy library.

        INPUTS
        :param x: numpy-type vector
        :param y: numpy-type vector

        OUTPUT
        :return z: numpy-type vector with the result of x - y
    '''
    z = x.__sub__(y)

    return z

def transpose_multiply_vectors(x, y):
    '''
        Function that multiplies two 1-dimensional numpy arrays
        using the numpy library. Where we make the transpose of x
        and then multiply it to y.

        INPUTS
        :param x: numpy-type vector
        :param y: numpy-type vector

        OUTPUT
        :return z: numpy-type vector with the result of xT * y
    '''
    a = x.T
    z = a.__mul__(y)

    return z

def multiply_vectors(a, y):
    '''
        Function that multiplies a 1-dimensional numpy arrays
        using the numpy library and a constant (number).

        INPUTS
        :param a: int number
        :param y: numpy-type vector

        OUTPUT
        :return z: numpy-type vector with the result of a * y
    '''
    z = y.__mul__(a)

    return z

def length_of_vector(y):
    '''
        Function that obtains the length of
        a 1-dimensional numpy array using the
        numpy library.

        INPUTS
        :param y: numpy-type vector

        OUTPUT
        :return z: integer value of the length of y
    '''
    z =  np.sqrt(y.dot(y.T))

    return z

def main():
    #initialice vectors x and y
    x = np.array([1,2,3], dtype = np.int8)
    y = np.array([4,5,6], dtype = np.int8)

    #initialice value a (used in multiply_vectors())
    a = 4

    #Printing results in the command linee
    print(28 * '-')
    print('OPERATIONS WITH VECTORS:')
    print(28 * '-')
    print('x = ' + str(x) + '\n')
    print('y = ' + str(y) + '\n')
    print('x + y = ' + str(add_vectors(x,y)) + '\n')
    print('x - y = ' + str(subtract_vectors(x,y)) + '\n')
    print('Transpose of x = ' + str(x.T) + '\n')
    print('xT * y =' + str(transpose_multiply_vectors(x,y)) + '\n')
    print('4 * y = ' + str(multiply_vectors(a,y)) + '\n')
    print('Length of y = ' + str(length_of_vector(y)) + '\n')

    return None

#Call main program
main()