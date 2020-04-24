# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 16:36:08 2020

@author: Geo
"""
from math import floor
import numpy

class Data:
    def __init__(self):
        pass
    
    def read_data(self, file):
        """
            Reads data from a given file with 6 floats on each line,
            5 floats corresponding to independent values (x) and 1
            corresponding to the dependend value
            Returns 2 lists:
                one containing [[x11...x1n], [x21,...,x2n], ...]
                another [y1,y2,...,yn]
        """
        data_x=[]
        data_y=[]
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line.strip('\n')
                line = line.split()
    
                if len(line) == 0:
                    continue
                x = [float(val) for val in line[:-1]]
                y = float(line[-1])
                data_x.append(x)
                data_y.append(y)
        return data_x, data_y
    
    def data_matrix(self, data_x, data_y):
        """
            X(feature matrix): [[1 x11,x12,...,x15],[1 x21,x22,...,x25], ...]
            Y(response vector): [y1,y2, ...]
            Return corresponding numpy arrays for dependend values (y)
            and independent values(x)
            Used numpy arrays since the library provides matrix operations 
            such as inverse, matrix multiplication, transpose

        """
        X=[]
        Y=[]
        for i in range(len(data_x)):
            new_x = [1] + data_x[i]
            X.append(new_x)
            Y.append(data_y[i])
        return numpy.array(X), numpy.array(Y)


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


class Regression:
    def __init__(self):
        self.Beta = None
    
    def beta_coefficients(self, X, Y):
        """
            Beta = inverse(transpose(X)*X) * transpose(X)*Y
        """
        transpose_X = X.transpose()
        first_multiplication = numpy.dot(transpose_X, X)
        second_multiplication = numpy.dot(transpose_X, Y)
        inverse = numpy.linalg.inv(first_multiplication)
        beta = numpy.dot(inverse, second_multiplication)
        self.Beta = beta
        
    def prediction(self, x_vals):
        """
            Predict a value for y having the independent vals given
            Y = X * Beta
        """
        total = 0
        for i in range(len(x_vals)):
            total+=self.Beta[i]*x_vals[i]
        return total
    
    def loss_of_regression(self, X, Y):
        """
            Compare the predicted value for y to the actual value of y

        """
        loss = 0
        for i in range(len(X)):
            prediction = self.prediction(X[i])
            current = (Y[i]-prediction)*(Y[i]-prediction)
            loss += current
        return loss
    
    def analyze(self, X, Y):
        """
            Analysis of the test data after beta values are found in training
        """
        for i in range(len(X)):
            y_predicted = self.prediction(X[i])
            y = Y[i]
            print("For X= " + str(X[i])+ ": ")
            print("Predicted Y: " + str(y_predicted))
            print("Actual Y: " + str(y))
            print("Error of regression: {:.2f} ".format(abs(y-y_predicted)))
        
        print("\n\nFound beta values: " + str(self.Beta))
        print("Total loss of regression: {:.2f}".format(self.loss_of_regression(X, Y)))
    
    
"""
        inspiration: https://www.geeksforgeeks.org/linear-regression-python-implementation/
        h(xi)=Beta0 + Beta1*xi1+Beta2*xi2+...+Beta5*xi5 predicted response
        then we can write:
            yi = Epsi + Beta0 + Beta1*xi1+Beta2*xi2+...+Beta5*xi5
        where Epsi is the residual error
        Beta = inverse(transpose(x)*x) * transpose(x)*y 
        y = x*Beta
            where x is the feature matrix and y the response vector
 """
if __name__ == "__main__":
    data = Data()
    x,y = data.read_data('data.txt')
    X,Y = data.data_matrix(x,y)
    print("Regression problem solved using Least Square Method")
    split =float(input("Enter the coefficient of splitting the data into training-test sets: "))
    training_X, training_Y, test_X, test_Y = data.split(X, Y, split)
    regression = Regression()
    regression.beta_coefficients(training_X, training_Y)
    regression.analyze(test_X, test_Y)
    