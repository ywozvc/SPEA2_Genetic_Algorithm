##Clustering
this is collection of functions used soley for the purpose of reducing a population that has exceeded its
maximum size. it's a collection of functions for calculating distance of points and clusters of points, centroid, etc.
all functions are generalized for arbitrary dimensions. (x), (x1,x2), (x1,x2,x3), (x1,x2...x_n)

###euclidean_metric
basic euclidean distance formula

###cluster_distance
distance between two clusters. not generalized for any metric right now but can be easily modified

###min_distance_clusters
find the two closests point clusters. each cluster can be of arbitrary size

###cluster_centroid
find the centroid of some particular cluster by finding the point with teh smallest average distance
