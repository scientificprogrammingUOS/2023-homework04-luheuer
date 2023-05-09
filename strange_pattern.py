import numpy as np

# implement the function strange pattern

def strange_pattern(shape):
    pattern = np.full(shape= shape, fill_value= False)
   
    for i in range(0,shape[0]):
        for k in range(((3 - (i%3))%3),shape[1],3):
            pattern[i,k ] = True

    return pattern


if __name__ == "__main__":
    print( strange_pattern((8,6)))

    pass
