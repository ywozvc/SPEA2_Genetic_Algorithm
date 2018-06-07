import sys
import pytest
import numpy as np
sys.path.insert(0,'../')
import population
from clustering import Clustering as clustering
from fixtures.population_fixture import init_population_object


def test_partition(init_population_object):
    """
    Description
    ---
    test the population parititioning function
    the partitioning function should return a list of lists
    """
    pop = init_population_object()
    print(pop)
    pop.partition_pop()
    for cluster in range(len(pop.individuals)):
        assert type(pop.individuals[cluster]) is list
#test_partition(init_population_object)

def test_departition(init_population_object):
    """
    Description
    ---
    make sure that the departitioning function works
    """
    sample_pop = init_population_object()
    sample_pop.partition_pop()
    print(sample_pop.individuals)
    sample_pop.departition_pop()
    print(sample_pop.individuals)

    with pytest.raises(population.PopulationError):
        sample_pop.departition_pop()
#test_departition(init_population_object)

def test_merge_partition(init_population_object):
    """
    Description
    ---
    Test merging
    """
    population = init_population_object()
    population.partition_pop()
    print('population size premerge ', len(population.individuals))
    print('first individual cluster ', len(population.individuals[0]))
    print(population.individuals[0])
    print(population.individuals[1])
    population.merge_partitions(0,1)
    print('population size post merge ', len(population.individuals))
    print('first individual cluster post merge ', len(population.individuals[0]))
    print(population.individuals[0])
    print(population.individuals[1])

#test_merge_partition(init_population_object)


        
