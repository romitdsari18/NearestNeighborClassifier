# -*- coding: utf-8 -*-

#Assignment information
print("Data 51100, Spring 2023")
print("Name: Marni Hari Krishna")
print("Programming Assignment #3")

#Importing the numpy package
import numpy as np

#Loading the data from the training and testing file into a numpy arrays
training_data = np.loadtxt('iris-training-data.csv', delimiter=',', dtype='<U15')
testing_data = np.loadtxt('iris-testing-data.csv', delimiter=',', dtype='<U15')

#Extracting the training and testing attributes (first four columns), training and testing labels (last column)
training_attributes = training_data[:, :4].astype(float)
training_labels = training_data[:, 4]

testing_attributes = testing_data[:, :4].astype(float)
testing_labels = testing_data[:, 4]

#Calculating the Euclidean Distance
differences = testing_attributes[:, np.newaxis] - training_attributes
squared_differences = np.square(differences)
sums = squared_differences.sum(axis=2)
distances = np.sqrt(sums)
 
#Predicting the labels based on the distance using argmin function in numpy
predicted_labels = training_labels[np.argmin(distances, axis=1)]

#Printing the number, actual label and predicted outputs in the requried format
print("\n#, True, Predicted")
for i in range(len(testing_labels)):
    print(f"{i+1},{testing_labels[i]},{predicted_labels[i]}")

#Calculating the accuracy and printing it to the console
accuracy = sum(predicted_labels == testing_labels) / len(predicted_labels)
print('Accuracy:',f"{accuracy:.2%}")

