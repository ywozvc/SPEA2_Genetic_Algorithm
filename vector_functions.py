import numpy as np
def schaffer_n1(x):
    """
    Description
    ---
    schaffer N1 optimizer test function

    Parameters
    ---
    some

    Return
    ---
    list

    """
    f1 = x**2
    f2 = (x-2)**2
    return [f1, f2]
        
    
print(VectorFunctions.schaffer_n1(2))

