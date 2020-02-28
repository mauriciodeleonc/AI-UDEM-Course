'''
    gradient-descent.py
    Python script for showing how the
    gradient descent algorithm works
    in order to predict the best line that
    represents a group/cluster of data.

    Author: Mauricio A. De alpha_trainingeon Cardenas
    Email: mauricio.deleonc@udem.edu
    Institution: Universidad de Monterrey
    First created: Mon 22 Feb, 2020
'''
import matplotlib.pyplot as plt
import pandas as pd

def plottingGraph(X, Y, line, w0, w1, mse, graph_number, dot_color, line_color, type):
    '''
        Function that graphs the data given,
        in this case, a linear regression function
        and its respective data.

        INPUTS
        :param X: vector with the actual values of X from the dataset (Celsius)
        :param Y: vector with the actual values of Y from the dataset (Fahrenheit)
        :param line: Vector with the predicted values of y for each x
        :param n: length of vector/ amount of data in the X vector
        :param mse: value of the Mean Squared Error
        :param w0: optimal value of w0
        :param w1: optimal value of w1
        :param graph_number: Number of the graph
        :param dot_color: in case of points of data, the color they will be presented
        :param line_color: in this case, the color of the param line

        OUTPUT
        :Y_pred: Vector with the predicted values of y for each x
        :w0: the optimal value of w0
        :w1: the optimal value of w1
    '''
    plt.figure(graph_number)
    plt.plot(X, Y, dot_color, label=('{} data').format(type))
    plt.plot([min(X), max(X)], [min(line), max(line)], color=line_color, label='regression line')
    plt.xlabel('Celsius')
    plt.ylabel('Fahrenheit')
    plt.legend()
    plt.grid(True)
    plt.title(('W0 = {:f}, W1 = {:f}, MSE ({}) = {:f}').format(w0,w1,type,mse), fontsize = 7)

def calcGradientDescent(X, Y, n, alpha, w0, w1):
    '''
        Function that calculates the
        gradient descent function to achieve
        the best values w0 and w1 that represent
        the data given.

        INPUTS
        :param X: vector with the actual values of X from the dataset (Celsius)
        :param Y: vector with the actual values of Y from the dataset (Fahrenheit)
        :param n: length of vector/ amount of data in the X vector
        :param alpha: learning rate of the function
        :w0: initial value of w0 (in this case is 0)
        :w1: initial value of w1 (in this case is 0)

        OUTPUT
        :Y_pred: Vector with the predicted values of y for each x
        :w0: the optimal value of w0
        :w1: the optimal value of w1
    '''

    iterations = 10000
    for i in range(iterations): 
        Y_pred = w1 * X + w0
        D_w1 = (-2/n) * sum(X * (Y - Y_pred))
        D_w0 = (-2/n) * sum(Y - Y_pred)
        w1 = w1 - alpha * D_w1
        w0 = w0 - alpha * D_w0


    return Y_pred, w0, w1

def calcMSE(Y, Y_pred, n):
    '''
        Function that calculates the
        Mean Square Error.

        INPUTS
        :param Y: vector with the actual values from the given data
        :param Y_pred: vector with the predicted values of a function
        :param n: length of vector/ amount of data in the Y vector

        OUTPUT
        :mse: result of the MSE
    '''
    mse = (sum((Y - Y_pred)**2))/n

    return mse

def main():
    #Get training dataset
    training_file = pd.read_csv('trainingdata.csv')

    #Fill training arrays
    Tc_training = training_file.iloc[:, 0]
    Tf_training = training_file.iloc[:, 1]

    #amount of training data
    n_training = float(len(Tc_training))

    #Alpha value (learning rate)
    alpha = 0.001

    #Calculate the optimal values for w0, w1 and the function that describes the linear regression of the training data
    Y_pred, w0, w1 = calcGradientDescent(Tc_training, Tf_training, n_training, alpha, 0, 0)
    
    #Calculate the Mean Square Error of the training data
    mse_training = calcMSE(Tf_training, Y_pred, n_training)

    #printing training data
    print(32*'-' + '\n' + 'Data set statistics:\n' + 32*'-')
    print('Number of samples [training]: ' + str(len(Tc_training)) + '\nNumber of samples [testing]: '+ str(len(Tc_training)) + '\n\n')
    print(32*'-' + '\n' + 'Training Data:\n' + 32*'-')
    print(" Tc      Tf")
    for x,y in zip(Tc_training,Tf_training):
        print(str(x) + "   " + '{:f}'.format(y))
    print('\n' + 32*'-' + '\n' + 'Estimated parameters:\n' + 32*'-')
    print(('intercept (b): {:f}').format(w0))
    print(('slope (m): {:f}\n').format(w1))
    print(32*'-' + '\n' + 'Performance metric [training]:\n' + 32*'-')
    print(('Mean Squared Error: {:f}').format(mse_training))

    #Get testing dataset
    testing_file = pd.read_csv('testingdata.csv')

    #Fill testing arrays
    Tc_testing = testing_file.iloc[:, 0]
    Tf_testing = testing_file.iloc[:, 1]

    #Amount of testing data
    n_testing = float(len(Tc_testing))

    #Calculate the optimal values for w0, w1 and the function that describes the linear regression of the testing data
    #Y_pred_testing, w0_testing, w1_testing = calcGradientDescent(Tc_testing, Tf_testing, n_testing, alpha, 0, 0)
    
    #Calculate the Mean Square Error of the testing data
    Y_pred = w0 + w1 * Tc_testing
    mse_testing = calcMSE(Tf_testing, Y_pred, n_testing)

    #Printing testing data
    print('\n'+32*'-' + '\n' + 'Testing Data:\n' + 32*'-')
    print(" Tc      Tf")
    for x, y in zip(Tc_testing, Tf_testing):
       print(str(x) + "   " + '{:f}'.format(y))
    print('\n' + 32*'-' + '\n' + 'Estimated parameters:\n' + 32*'-')
    print(('intercept (b): {:f}').format(w0))
    print(('slope (m): {:f}\n').format(w1))
    print(32*'-' + '\n' + 'Performance metric [testing]:\n' + 32*'-')
    print(('Mean Squared Error: {:f}').format(mse_testing))

    #Plotting both training and testing data
    plottingGraph(Tc_training,Tf_training, Y_pred, w0, w1, mse_training,1, 'ok', 'green','training')
    plottingGraph(Tc_testing,Tf_testing, Y_pred, w0, w1, mse_testing,2, 'ok', 'red','testing')
    plt.show()

    

main()