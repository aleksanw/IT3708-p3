import numpy as np

input_count = 6
hidden_count = 0
output_count = 3

def random_genotype():
    """Generate random genotype with standard normal distributed weight values.
    """
    dims = (hidden_count + output_count
           ,input_count + hidden_count + output_count)
    #return np.zeros(dims)
    #return np.random.normal(0.4, 0.3, dims)
    return np.random.uniform(-0.4, 0.4, dims)
