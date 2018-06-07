import pytest
import sys
sys.path.insert(0,'../')
from clustering import Clustering as clustering
import numpy as np
import population as pop
from tests.fixtures.population_fixture import init_population_object

def test_euclidean_metric():
    point1 = 10*np.random.random(size=3)
    point2 = 10*np.random.random(size=3)
    point3 = np.ones(shape=10)
    point4 = np.zeros(shape=10)
    distance = clustering.euclidean_metric(point1, point2)
    distance_ones = clustering.euclidean_metric(point3, point4)
    distance_zero = clustering.euclidean_metric(point4, point4)
    assert type(distance) is np.float64
    assert np.floor(distance_ones) == 3
    assert distance_zero == 0
    assert np.floor(clustering.euclidean_metric(point1, point2)) <= 10

    for i in range(1000):
        n1 = 10*np.random.random(size=3)
        n2 = 10*np.random.random(size=3)
        assert clustering.euclidean_metric(n1, n2) > 0

#with random generated individuals to just test the function by itself
#def test_cluster_distance():#for pytest
def test_cluster_distance(mu_1, sigma_1, mu_2, sigma_2):#for python test
    """
    Description
    ---
    to test the distance between two clusters of different cardinality.
    this function plays a role in the reduction of the size of the 
    nondominate population if it were to exceed to predetermined max

    Parameters
    ---
    mu_1, mu_2: float
    the clusters are going to be randomly generated but be normally distributed around
    these two distinct values so as to better emulate clustering. we dont want true
    random distribution because the values will be all over the place and may overlap 
    and mess up the distance stuff because you may be measuring the distance between
    a cluster inside of a cluster.

    sigma_1, sigma_2: float
    these are the standard deviation values for these two clusters. keep that shit reasonably
    tight

    Returns
    ---
    the distance between two clusters as calculated by average linkage clustering, also known as UPGMA

    """
    cluster1 = list()
    cluster2 = list()
    #limit the cardinality to 10 for no reason. just because
    cluster1_cardinality = np.random.randint(low=1, high=10)
    cluster2_cardinality = np.random.randint(low=1, high=10)
  
  
    #create random points to populate the clusters
    #to do, limit the clusters around some normal so they act like clusters
    for i in range(cluster1_cardinality):
        cluster1.append(np.random.normal(loc=mu_1,scale=sigma_1,size=3))
    print('test_cluster_distance - cluster 1:')
    print(cluster1)
    print('test_cluster_distance cluster1 cardinality - ', cluster1_cardinality)
    
    for i in range(cluster2_cardinality):
        cluster2.append(np.random.normal(loc=mu_2, scale=sigma_2, size=3))
    print('test_cluster_distance - cluster 2:')
    print(cluster2)
    print('test_cluster_distance - cluster2 cardinality',cluster2_cardinality)
    
    distance = clustering.cluster_distance(cluster1, cluster2)
    print('test_cluster_distance return value',distance)
    assert type(distance) is np.float64
#test_cluster_distance(1,0.1, 10,2)

#with imported population object to test interaction 
def test_cluster_dis_with_pop(init_population_object):
    """
    Description
    ---
    determine the distance between clusters 
    
    Parameters
    ---
    init_population_object: population object
    this is a randomly generated population centered around some normal distribution. 
    the population can can be found in the test/fixture folder
    """
    population = init_population_object()
    population.partition()
    distance = clustering.cluster_distance(population.individuals[0], population.individuals[1])
    print('test_cluster_dis_with_population object', distance)
#test_cluster_dis_with_pop(init_population_object)

def test_min_distance_clusters(init_population_object):
    """
    Description
    ---
    find the minimum distance between two clusters
    """
    population = init_population_object()
    population.partition()
    closest_clusters = clustering.min_distance_clusters(population.individuals)
    print(closest_clusters)
    print(population.individuals[closest_clusters[0]])
    print(population.individuals[closest_clusters[1]])

#test_min_distance_clusters(init_population_object)

def test_cluster_centroid(init_population_object):
    population = init_population_object()
    centroid = clustering.cluster_centroid(population.individuals)
    print('population centroid is ', centroid[0])
    print('centroid index is ',centroid)
test_cluster_centroid(init_population_object)
    


