import numpy as np
"""
Description
---
collection of functions used to do cluster calculations
"""
def euclidean_metric(point1, point2):
    """
    Description
    ---
    calculates the euclidean metric for some points

    Parameters
    ---
    point1, point2: np.array float
    represents the two points to be calculated

    Returns
    ---
    distance: np.float64
    you know what it is
    """
    sum = 0.0
    for i in range(len(point1)):
        sum += (point1[i] - point2[i])**2
    return np.sqrt(sum)

def cluster_distance(cluster1, cluster2):
    """
    Description
    ---
    calculate the distance between two disjoint clusters through
    average linkage clustering, also known as UPGMA
    the distance of ALL possible pairs of clusters must be calculated
    between two distinct clusters.

    Parameters
    ---
    cluster1, cluster2: list made up of np.array(dtype=np.float64)
    each element (array) in the cluster represents a subset of points
    initially these disjoint subsets would have a cardinality of 1

    Returns
    ---
    cluster_distance: np.float64

    Notes
    ---
    in the beginning all clusters will have a cardinality of at least 1

    """
    c1_cardinality = len(cluster1) #cluster 1 cardinality
    c2_cardinality = len(cluster2) #cluster 2 cardinality
    sum = 0.0
    for i in range(c1_cardinality):
        for j in range(c2_cardinality):
            sum += Clustering.euclidean_metric(cluster1[i], cluster2[j])

    constant = 1.0/(c1_cardinality*c2_cardinality)
    return sum*constant

def min_distance_clusters(partitioned_set):
    """
    Description
    ---
    determines the smallest cluster distance between any two disjoint
    clusters.

    Parameters
    ---
    partitioned_set: list of lists
    the nondominated population that has reached a size that is larger
    than the maximum.
    Returns
    ---
    nearest_clusters: list
    this list has the index of the two clusters in th partitioned_set that are the nearest
    this index will be used by some other function to merge the points within them together
    to form a larger cluster.

    Notes
    ---

    """
    min_distance = None
    nearest_clusters = list()
    penultimate = len(partitioned_set) - 1
    for i in range(penultimate):
        for j in range(i+1,len(partitioned_set)):
            d = Clustering.cluster_distance(partitioned_set[i], partitioned_set[j])
            if(min_distance is None):
                min_distance = d
                nearest_clusters = [i,j]
            elif(min_distance is not None and (d < min_distance)):
                min_distance = d
                nearest_clusters = [i,j]
    return nearest_clusters

def cluster_centroid(cluster):
    """
    Description
    ---
    find the centroid of a cluster by calculating the point with the smallest
    average distance between the other points in the cluster

    Parameters
    ---
    cluster: list
    a list of np.float64 np.arrays or any list of numbers

    Returns
    ---
    centroid: np.array

    """
    min_avg_dist = None
    index = None
    for i in range(len(cluster)):
        dist_sum = 0.0
        for j in range(len(cluster)):
            dist_sum +=Clustering.euclidean_metric(cluster[i],cluster[j])
        avg_dist = dist_sum / (len(cluster)-1)
        print('this is average_dist for ',avg_dist, i)
        if(i == 0):
            min_avg_dist = avg_dist
            index = i
        if(avg_dist < min_avg_dist):
            min_avg_dist = avg_dist
            index = i
    centroid = cluster[index]
    return centroid
                
