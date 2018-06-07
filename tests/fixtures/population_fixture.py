import pytest
import numpy as np
import sys
sys.path.insert(0,'../')
import population

@pytest.fixture
def init_population_object():
    """
    Description
    ---
    initialize a population object to be used by subsequent tests
    """
    sample_nondominated_population = population.Population()
    assert type(sample_nondominated_population) is population.Population
    #fill the population with randon individuals
    for individuals in range(np.random.randint(low=2, high=100)):
        ind = np.random.normal(loc=10, scale=2.0, size=3)
        #todo: verify
        sample_nondominated_population.individuals.append(ind)
    return sample_nondominated_population
