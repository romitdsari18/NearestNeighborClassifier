# NearestNeighborClassifier
K-means clustering is a unsupervised machine learning algorithm that is used to divide a set of data pointsinto a predetermined number of clusters.
The process begins by defining a k (number of clusters) at random.
Finally, based on its distance to the nearest centroid, each data point is assigned to it's nearest cluster.
The centroid of each cluster is recalculated after each data point has been allocated to a cluster. 
This procedure of allocating data points to clusters and recalculating the centroids is repeated until the centroids stop changing or a predetermined number of iterations has been reached.

# Explaination - KMeans
to create a program using Python that does the following:
1. Asks the user for the number of clusters. This is the parameter k that will be used for k-means.

2. Reads the input file (prog2-input-data.txt) and stores the points into a list
 
4. Applies the k-means algorithm to find the cluster for each point.
 
5. Displays the points that each cluster contains after each iteration of the algorithm
 
6. Writes the final cluster assignments to the screen and the output file (prog2-output-data.txt).


# Explaination - NearestNeighbhorClassifier
To program a python code that predicts the iris flower type based on the petal length and width, sepal length and width using Euclidean distance.

1.Importing the NumPy Library as np for mathematical equation and fetching the data.

2.Fetching the data from the csv files (iris-training-data.csv and iris-testing-data.csv) into the NumPy arrays (training_data and testing_data) using load function from numpy.

3.Extracting the first four columns into training and testing attributes as float from the respective NumPy array.

4.Extracting the fifth column into training and testing labels from the respective NumPy array.

5.The Euclidean distance between each testing instance and each training instance is calculated using the formula sqrt(sum((x-y)^2)), which involves calculating the differences, squaring them, summing them and then taking the square root. This is done using numpy functions such as np.square, np.sum, and np.sqrt.

6.The predicted label for each testing instance is determined using the argmin function from numpy. This function returns the index of the smallest distance value for each testing instance, which is used to extract the corresponding label from the training_labels array.

7.Print function and for loop is used to print the number, true label and predicted label in the required format.

8.Accuracy is calculated by comparing the predicted labels to the true labels. Printing the accuracy in the float format and percentage.
