# NearestNeighborClassifier
K-means clustering is a unsupervised machine learning algorithm that is used to divide a set of data pointsinto a predetermined number of clusters.
The process begins by defining a k (number of clusters) at random.
Finally, based on its distance to the nearest centroid, each data point is assigned to it's nearest cluster.
The centroid of each cluster is recalculated after each data point has been allocated to a cluster. 
This procedure of allocating data points to clusters and recalculating the centroids is repeated until the centroids stop changing or a predetermined number of iterations has been reached.

# Explaination
to create a program using Python that does the following:
1. Asks the user for the number of clusters. This is the parameter k that will be used for k-means.
 
2. Reads the input file (prog2-input-data.txt) and stores the points into a list
 
4. Applies the k-means algorithm to find the cluster for each point.
 
5. Displays the points that each cluster contains after each iteration of the algorithm
 
6. Writes the final cluster assignments to the screen and the output file (prog2-output-data.txt).
