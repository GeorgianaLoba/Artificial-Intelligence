# -*- coding: utf-8 -*-
"""
Created on Sun May 10 13:18:58 2020

@author: Geo
"""

import numpy as np
from math import floor
import statistics
import matplotlib as mpl

class Data:
    def __init__(self, file_name):
        self.file_name = file_name
        
    def read_from_file(self):
        """
            Reads data from a given file with 6 floats on each line
            Returns 2 lists consisting on numpy arrays
        """
        x=[]
        y=[]
        with open(self.file_name, "r") as file:
            text = file.readlines()
            for line in text:
                line = line.strip('\n')
                if len(line) == 0:
                    continue
                line = line.split()
                line = [[float(x)] for x in line]
                x_temp = line[:-1]
                y_temp = line[-1]
                x.append(np.array(x_temp))
                y.append(np.array(y_temp))
        return x, y

    def split(self, data_x, data_y, split_coefficient):
        """
            Split available data into training and test sets based on a split coefficient (0.1, 1)
        """
        if split_coefficient>1:
            raise ValueError("The split coefficient must be in interval [0.1,1]")
        if split_coefficient<0.1:
            raise ValueError("The split coefficient must be in interval [0.1,1]")
        if split_coefficient==1:
            return data_x,data_y,data_x,data_y
        split = floor(len(data_y) * split_coefficient)
        return data_x[:split], data_y[:split], data_x[split:], data_y[split:]    
    
class NeuralNetwork:
    '''
        A two layer neural network
        
        layers = [int, int, int]
            Input - 5 neurons 
            Hidden Layer - abitrary number of neurons - try 5 or 6
            Output Layer - 1 neurons 
        w1,w2 = weights between input-hidden and hidden-output layers respectively
        b1,b2 = biases between input-hidden and hidden-output layers respectively
        
    '''
    def __init__(self, layers, learning_rate, fix_coefficient):
        self.layers = layers
        self.learning_rate = learning_rate
        self.fix_coefficient = fix_coefficient
        #weights
        self.w1 = np.random.rand(layers[0], layers[1])
        self.w2 = np.random.rand(layers[1], layers[2])
        #biases
        self.b1 = np.random.rand(layers[1])
        self.b2 = np.random.rand(layers[2])
    
        #helpful in backward propagation
        self.Z = None
        
        #for plotting the loss/iteration
        self.loss = []
        self.iterations = []
       
    
    def linear(self, z):
        '''
            Activation function
        '''
        return z
    
    def deriv_linear(self, z):
        '''
            Derivative of the activation function
        '''
        return 1

    
    def train_NN(self, x, y, iterations):
        '''
            Training the neural network using train data over a given number of iterations
            We compute the expected value and propagate backwords in order to train the NN
        '''
        pos=0
        for i in range(iterations):
            X=x[pos].T #x has the form (1,5)
            Y=y[pos] #y has the form (1,1)
            y_exp = self.forward_propagation(X)
            self.backward_propagation(X, Y, y_exp)
            
            #only needed for the plot
            self.loss.append(self.error(y_exp, Y)) 
            self.iterations.append(i)
            
            pos = (pos+1)%(len(x))
            
    def predict(self,x,y):
        '''
            To make predictions, you simply make a forward pass on the test data. 
        '''
        pos = 0
        errors=[]
        while (pos < len(x)):
            X=x[pos].T
            Y=y[pos]
            print("Predict for input: ", str(X[0]))
            output = self.forward_propagation(X[0])
            error = self.error(output, Y[0])
            print("Y predicted:", str(output))
            print("Y real:", str(Y))
            print("Error is: {:.3f}".format(error))
            print("\n")
            pos+=1
            errors.append(error)
        print("Average error while predicting is: {:.3f} ".format(statistics.mean(errors)))

    def error(self,predicted,actual):
        '''
            Computing the error, given the predicted value and the actual value.
        '''
        return np.sum((np.square(actual - predicted))/2)
        
    def forward_propagation(self, inp):
        '''
            Forward propagation consists of series of computations performed by
            the neural network before a prediction is made.
            
            y_predicted = activate(w2 * activate(w1 * x + b1) + b2)
        '''
        self.Z = self.linear(np.dot(inp, self.w1) + self.b1)
        return self.linear(np.dot(self.Z, self.w2)+ self.b2)
        
    def backward_propagation(self, X, Y, y_predicted):
        '''
            Backpropagation is the  process of training a neural network by 
            updating its weights and bias.
        '''
        first_back = (Y-y_predicted) * self.deriv_linear(y_predicted)
        second_back = np.dot(2*first_back, self.w2.T) * self.deriv_linear(self.Z)
        
        back_w2 = np.dot(self.Z.T, 2*first_back)
        back_w1 = np.dot(X.T, second_back)
        
        
        #it doesn't improve the accuracy if i change the biases as well
        #l_b1 = np.sum(wrt_z, axis=0)
        #l_b2 = np.sum(wrt_y, axis=0)

        self.w1 += self.learning_rate * back_w1 * (1 / self.fix_coefficient)
        self.w2 += self.learning_rate * back_w2 * (1 / self.fix_coefficient)
        #self.b1 += self.learning_rate * l_b1* (1 / 1000)
        #self.b2 += self.learning_rate * l_b2* (1 / 1000)
        

def initial():
    '''
        Data used for playing with the NN
    '''
    #file name
    file_name = 'data.txt'
    #split coefficient
    split = 0.75
    #hidden layer number of neurons
    hidden = 6
    #number of iterations for training the neural network
    iterations = 1000
    
    #Here I either have a really small learning rate or a fix coefficient in
    #order to get accurate results
    
    #learning rate
    learning_rate = 0.0001
    #fix coefficient
    fix_coefficient = 10
    
    return file_name, split, hidden, iterations, learning_rate, fix_coefficient


if __name__ == "__main__":
    file_name, split, hidden, iterations, learning_rate, fix_coefficient = initial()
    
    data = Data(file_name)
    x, y = data.read_from_file()
    x_train, y_train, x_predict, y_predict = data.split(x, y, split)
    layer = [x[0].shape[0],hidden,y[0].shape[0]]
        
    
    nn = NeuralNetwork(layer, learning_rate, fix_coefficient)
    nn.train_NN(x_train, y_train, iterations)
    nn.predict(x_predict, y_predict)
    
    
    mpl.pyplot.plot(nn.iterations, nn.loss, label='loss value vs iteration')
    mpl.pyplot.xlabel('Iterations')
    mpl.pyplot.ylabel('loss function')
    mpl.pyplot.legend()
    mpl.pyplot.show()
    