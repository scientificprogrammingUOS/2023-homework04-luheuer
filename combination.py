import numpy as np 

# implement your function to combine two numpy arrays 

def combination(array_1, array_2 , axis = 0):
    array_1 = np.squeeze(array_1)
    array_2 = np.squeeze(array_2)
    
    combination =  np.concatenate((array_1,array_2))
    return combination


if __name__ == "__main__":
    # use this for your own testing!

    pass
