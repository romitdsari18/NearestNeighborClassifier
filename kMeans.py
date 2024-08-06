# -*- coding: utf-8 -*-


#Defining the function for k-means clustering
def k_means_cluster(input_data, centroids, data_points):
    # Initializing the clusters dictionary with empty lists for each cluster index
    clusters = {i: [] for i in range(k)}

    for point in input_data:
        #Calculating distances from the point to each centroid
        distances = [((centroids[c] - point) ** 2) ** 0.5 for c in centroids]

        #Placing the point in the closest cluster based on distance
        closest_index = distances.index(min(distances))
        clusters[closest_index].append(point)
        data_points[point] = closest_index

    return clusters

#Promting for user input
while True:
    try:
        k = int(input("\nEnter the number of clusters: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

#Importing the data from file and insert into input_data list
input_data = []
for num in open("prog2-input-data.txt"):
    input_data.append(float(num.rstrip()))

#Defining the initial centroid as per first k data points and using zip function to remove list out of index error
centroids = {i: point for i, point in zip(range(k), input_data)}

#Creating the dictionaries to store updated and previous centroids
updated_centroids = {i: value for i, value in zip(range(k), input_data)}
previous_centroids = {}

#Creating the dictionary to store each data point and its assigned cluster
data_points = {}
for i in range(len(input_data)):
    data_points[input_data[i]] = i

#Intilizing the iterator_count
iterator_count = 1

#The loop ends when if condition becomes true
while True:
    print(f"\nIteration: {iterator_count}")

    #Assigning the data points to clusters based on current centroids using k_means_cluster function and updating the centroid
    clusters = k_means_cluster(input_data,centroids,data_points)
    for cluster in clusters:
            updated_centroids[cluster] = float(sum(clusters[cluster]) / len(clusters[cluster]))
    
    #Printing the cluster and data point to the console and increasing the iterator_count by 1
    for key,value in clusters.items():
           print(key,value)  

    iterator_count+=1

    if updated_centroids == previous_centroids:
            break
    else:
        previous_centroids=centroids
        centroids = updated_centroids
               
#Printing the each data point and its assigned cluster to the console
print('')
for key, value in data_points.items():
    print(f"Point {key} in cluster {value}")

#Writing each data point and its assigned cluster to an output file
output_file = open("prog2-output-data.txt", "w")
for key, value in data_points.items():
    output_file.write(f"Point {key} in cluster {value}\n")
output_file.close()
