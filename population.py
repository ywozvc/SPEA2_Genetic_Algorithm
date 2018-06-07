
class Error(Exception):
    pass

class PopulationError(Error):
    def __init__(self, message):
        self.message = message

class Partition(list):
    """
    Description
    ---
    partition class that extends python list so as to have
    extra descriptive properties
    
    Properties
    ---
    centroid: list
    is the centroid of the partition if it has one
    """
    def __init__(self, individual=None):
        self.centroid = None
        self.append(individual)

    def __call__(self):
        return self
        
class Population(list):
    """
    Description
    ---
    populations represent the set of individuals (potential solutions)
    or the set of nondominated individuals
    
    """
    def __init__(self):
        self.partitioned = False
        self.centroid_found = False
        """
        partitioning takes a list object of individuals and partitions them
        into a list object of list obects with each internal list object
        constituting a single member at first. 
        population objects can have a partitioned or nonpartioned list of 
        individuals. if a nondominated set were to exceed its maximum limit
        then it will be partitioned and cluster analysis will be conducted
        so as to continuous merge the closest clusters. afterwards some
        centroid calcuation will be conducted to reduce the cardinality of
        the cluster to 1. then the population will be departitioned.
        """

    def __call__(self):
        """
        added this so it can work with pytest fixture. kept saying object
        not callable.
        """
        return self

    def partition_population(self):
        """
        Description
        ---
        this will take a population and seperate it into disjoint partitions
        representing clusters. each partition will be a list that contains
        at least one individual

        Parameters
        ---
        self.individuals: list
        list of individuals can be partitioned or unpartitioned
        """
        if(len(self) > 0):
            for i in range(len(self)):
                singleton_partition = Partition(self[i])
                self[i] = singleton_partition
            self.partitioned = True

    def departition_pop(self):
        """
        Description
        ---
        departition a partitioned individuals list
        Parameters
        ---
        self.individuals: list
        the list of individuals can be partitioned but if you're here it's
        gonna be unpartitioned
        """
        if(self.partitioned):
            for partition in range(len(self)):
                self[partition] = self[partition][0]
            self.partitioned = False
        else:
            raise PopulationError('population is not partitioned')

    
    
