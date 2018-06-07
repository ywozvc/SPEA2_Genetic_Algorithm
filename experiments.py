import numpy as np
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
    distance: float
    you know what it is
    """
    sum = 0.0
    for i in range(len(point1)):
        sum += (point1[i] - point2[i])**2

    return np.sqrt(sum)
