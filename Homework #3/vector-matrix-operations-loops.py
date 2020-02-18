'''
    vector-matrix-operations-operations-loop.py
    Python script for practicing
    looping through vector and matrixes.

    Author: Mauricio A. De Leon Cardenas
    Email: mauricio.deleonc@udem.edu
    Institution: Universidad de Monterrey
    First created: Mon 15 Feb, 2020
'''
import numpy as np

def add_vectors(x,y,typeExec):
    '''
        Function that adds two vectors
        using the numpy library or iteratively.

        INPUTS
        :param x: numpy-type vector
        :param y: numpy-type vector
        :param typeExec: string defining whether to
            process the method using numpy or iterative

        OUTPUT
        :return z: vector with the result of x + y
    '''
    if typeExec == 'numpy':
        z = np.add(x,y)
        return z
    else:
        z = list()

        for xi, yi in zip(x,y):
            z.append(xi + yi)

        z = np.asarray(z)
        return z

def subtract_vectors(x,y,typeExec):
    '''
        Function that subtracts two vectors
        using the numpy library or iteratively.

        INPUTS
        :param x: numpy-type vector
        :param y: numpy-type vector
        :param typeExec: string defining whether to
            process the method using numpy or iterative

        OUTPUT
        :return z: vector with the result of x - y
    '''
    if typeExec == 'numpy':
        z = x.__sub__(y)
        return z
    else:
        z = list()
        
        for xi, yi in zip(x,y):
            z.append(xi - yi)

        z = np.asarray(z)
        return z

def transpose_vector(x,typeExec):
    '''
        Function that transposes a vector
        using the numpy library or iteratively.

        INPUTS
        :param x: numpy-type vector
        :param typeExec: string defining whether to
            process the method using numpy or iterative

        OUTPUT
        :return z: transpose of vector x
    '''
    if typeExec == 'numpy':
        z = x.T
        return z
    else:
        z = list()
        
        z = map(list, zip(*x))

        z = np.asarray(z)
        return z

def multiply_vectors_transpose(x,y,typeExec):
    '''
        Function that gets the transpose of a vector
        and then multiplies it to another vector
        using the numpy library or iteratively.

        INPUTS
        :param x: numpy-type vector
        :param y: numpy-type vector
        :param typeExec: string defining whether to
            process the method using numpy or iterative

        OUTPUT
        :return z: vector with the result of x.T * y
    '''
    if typeExec == 'numpy':
        a = transpose_vector(x,typeExec)
        z = a.__mul__(y)
        return z
    else:
        z = list()
        a = transpose_vector(x,typeExec)
        for xi, yi in zip(a,y):
            z.append(xi * yi)
        z = np.asarray(z)
        return z

def multiply_constant_vector(a,y,typeExec):
    '''
        Function that multiplies a constant and a vector
        using the numpy library or iteratively.

        INPUTS
        :param a: constant number
        :param x: numpy-type vector
        :param typeExec: string defining whether to
            process the method using numpy or iterative

        OUTPUT
        :return z: vector with the result of a * y
    '''
    if typeExec == 'numpy':
        z = y.__mul__(a)
        return z
    else:
        z = list()
        for i in y:
            z.append(i * a)
        z = np.asarray(z)
        return z

def add_matrices(X,Y,typeExec):
    '''
        Function that adds two matrices
        using the numpy library or iteratively.

        INPUTS
        :param X: numpy-type vector
        :param Y: numpy-type vector
        :param typeExec: string defining whether to
            process the method using numpy or iterative

        OUTPUT
        :return Z: matrix with the result of X + Y
    '''
    if typeExec == 'numpy':
        Z = np.add(X,Y)
        return Z
    else:
        Z = np.zeros_like(X)
        sizeX = X.shape
        sizeY = Y.shape

        for i in range(0, sizeX[0], 1):
            for j in range(0, sizeX[1], 1):
                Z[i][j] = X[i][j] + Y[i][j]

        Z = np.asarray(Z)
        return Z

def subtract_matrices(X,Y,typeExec):
    '''
        Function that subtracts two matrices
        using the numpy library or iteratively.

        INPUTS
        :param X: numpy-type vector
        :param Y: numpy-type vector
        :param typeExec: string defining whether to
            process the method using numpy or iterative

        OUTPUT
        :return Z: matrix with the result of X - Y
    '''
    if typeExec == 'numpy':
        Z = X.__sub__(Y)
        return Z
    else:
        Z = np.zeros_like(X)
        sizeX = X.shape
        sizeY = Y.shape

        for i in range(0, sizeX[0], 1):
            for j in range(0, sizeX[1], 1):
                Z[i][j] = X[i][j] - Y[i][j]

        Z = np.asarray(Z)
        return Z

def multiply_matrices(X,Y,typeExec):
    '''
        Function that multiplies two matrices
        using the numpy library or iteratively.

        INPUTS
        :param X: numpy-type vector
        :param Y: numpy-type vector
        :param typeExec: string defining whether to
            process the method using numpy or iterative

        OUTPUT
        :return Z: matrix with the result of X * Y
    '''
    if typeExec == 'numpy':
        Z = X.__mul__(Y)
        return Z
    else:
        Z = list()

        for xi,yi in zip(X,Y):
            Z.append(xi * yi)

        Z = np.asarray(Z)

        return Z

def divide_matrices(X,Y,typeExec):
    '''
        Function that divides two matrices
        using the numpy library or iteratively.

        INPUTS
        :param X: numpy-type vector
        :param Y: numpy-type vector
        :param typeExec: string defining whether to
            process the method using numpy or iterative

        OUTPUT
        :return Z: matrix with the result of X / Y
    '''
    if typeExec == 'numpy':
        Z = np.true_divide(X,Y)
        return Z
    else:
        Z = list()

        for xi, yi in zip(X,Y):
            Z.append(xi / yi)

        Z = np.asarray(Z)
        return Z

def multiply_constant_matrix(a,Y, typeExec):
    '''
        Function that multiplies a constant by a matrix
        using the numpy library or iteratively.

        INPUTS
        :param a: constant number
        :param Y: numpy-type vector
        :param typeExec: string defining whether to
            process the method using numpy or iterative

        OUTPUT
        :return Z: matrix with the result of a * Y
    '''
    if typeExec == 'numpy':
        Z = Y.__mul__(a)
        return Z
    else:
        Z = list()

        for yi, yj in zip(Y,Y):
            Z.append(yi * a)

        Z = np.asarray(Z)
        return Z

def transpose_matrix(X,typeExec):
    '''
        Function that obtains the trnaspose of a matrix
        using the numpy library or iteratively.

        INPUTS
        :param X: numpy-type vector
        :param typeExec: string defining whether to
            process the method using numpy or iterative

        OUTPUT
        :return Z: matrix with the result of X.T
    '''
    if typeExec == 'numpy':
        Z = X.T
        return Z
    else:
        Z = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]
        Z = np.asarray(Z)
        return Z

#Main driver method
def main():
    #initialice numpy type vectors
    x = np.array([[1],[2],[3]], dtype = np.int8)
    y = np.array([[4],[5],[6]], dtype = np.int8)

    #check size of vectors
    sizex = len(x)
    sizey = len(y)

    #intialice numpy type matrices
    X = np.array([[7,8,9],[10,11,12],[13,14,15]], dtype = np.int8)
    Y = np.array([[16,17,18],[19,20,21],[22,23,24]], dtype = np.int8)

    #check size of matrices
    sizeX = X.shape
    sizeY = Y.shape

    #defining type of method
    n = 'numpy'
    i = 'iterative'

    if sizex == sizey:
        #printing content of vectors
        print(28 * '-' + '\n' + 'OPERATIONS WITH VECTORS:\n' + 28 * '-' + '\n')
        print('contents of vector x:\n' + str(x) + '\n')
        print('contents of vector y:\n' + str(y) + '\n')
        print('x + y with numpy:\n' + str(add_vectors(x,y,n)) + '\n')
        print('x + y iterative:\n' + str(add_vectors(x,y,i)) + '\n')
        print('x - y numpy:\n' + str(subtract_vectors(x,y,n)) + '\n')
        print('x - y iterative:\n' + str(subtract_vectors(x,y,i)) + '\n')
        print('Transpose of x numpy:\n' + str(transpose_vector(x,n)) + '\n')
        print('Transpose of x iterative:\n' + str(transpose_vector(x,i)) + '\n')
        print('Transpose of x * y numpy:\n' + str(multiply_vectors_transpose(x,y,n)) + '\n')
        print('Transpose of x * y iterative:\n' + str(multiply_vectors_transpose(x,y,i)) + '\n')
        print('Constant a * vector y numpy:\n' + str(multiply_constant_vector(5,y,n)) + '\n')
        print('Constant a * vector y iterative:\n' + str(multiply_constant_vector(5,y,i)) + '\n')
    else:
        print('ERROR: Vectors are of different size')

    if sizeX[1] == sizeY[0]:
        #printing content of matrices
        print(28 * '-' + '\n' + 'OPERATIONS WITH MATRICES:\n' + 28 * '-' + '\n')
        print('contents of matrix X:\n' + str(X) + '\n')
        print('contents of matrix Y:\n' + str(Y) + '\n')
        print('X + Y with numpy:\n' + str(add_matrices(X,Y,n)) + '\n')
        print('X + Y iterative:\n' + str(add_matrices(X,Y,i)) + '\n')
        print('x - y numpy:\n' + str(subtract_matrices(X,Y,n)) + '\n')
        print('x - y iterative:\n' + str(subtract_matrices(X,Y,i)) + '\n')
        print('X * Y numpy:\n' + str(multiply_matrices(X,Y,n)) + '\n')
        print('X * Y iterative:\n' + str(multiply_matrices(X,Y,i)) + '\n')
        print('X/Y numpy:\n' + str(divide_matrices(X,Y,n)) + '\n')
        print('X/Y iterative:\n' + str(divide_matrices(X,Y,i)) + '\n')
        print('Constant a * matrix Y numpy:\n' + str(multiply_constant_matrix(5,Y,n)) + '\n')
        print('Constant a * matrix Y iterative:\n' + str(multiply_constant_matrix(5,Y,i)) + '\n')
        print('Transpose of X numpy:\n' + str(transpose_matrix(X,n)) + '\n')
        print('Transpose of X iterative:\n' + str(transpose_matrix(X,i)) + '\n')
    else:
        print('ERROR: Matrices are of different shape')

    return None;

#Calling driver method
main()
    