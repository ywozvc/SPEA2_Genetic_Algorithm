import sys
sys.path.insert(0,'../')
import pytest
import population
from fixtures.population_fixture import init_population_object


def test_partition(init_population_object):
    """
    Description
    ---
    test the population parititioning function
    the partitioning function should return a list of lists
    """
    pop = init_population_object()
    pop.partition_population()
    for cluster_index in range(len(pop)):
        assert type(pop[cluster_index]) is population.Partition

def test_departition(init_population_object):
    """
    Description
    ---
    make sure that the departitioning function works
    """
    sample_pop = init_population_object()
    sample_pop.partition_population()
    sample_pop.departition_pop()
    for index in range(len(sample_pop)):
        assert type(sample_pop[index]) is not population.Partition
    with pytest.raises(population.PopulationError):
        sample_pop.departition_pop()



        
