import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower_bound, upper_bound):
    mean = 0
    std = 0
    values = np.empty(100)
    if ((type(loc) != int) and (type(loc) != float)) :
        raise  TypeError("Type Error: loc is not an integer or a float.") 
    elif((type(scale) != int) and (type(scale) != float)):
        raise  TypeError("Type Error: scale is not an integer or a float.")
    elif((type(lower_bound) != int) and (type(lower_bound) != float)):
        raise   TypeError("Type Error: lower_bound is not an integer or a float.")
    elif((type(upper_bound) != int) and (type(upper_bound) != float)):
        raise   TypeError("Type Error: upper_bound is not an integer or a float.")
    elif upper_bound <= lower_bound:
        raise TypeError("Type Error: lower_bound is not smaller that upper_bound.")
    
    for i in np.arange(100):
        values[i] = np.random.normal(loc,scale)
    
    mask = np.full(values.shape, fill_value= False)
    for k in np.arange(100):
        if((values[k] < lower_bound) or (values[k] > upper_bound)): 
            mask[k] = True
    
    values = np.delete(values, mask)
               
            
    print( lower_bound)
    print(upper_bound)
    print(values)
    mean = np.mean(values)
    std = np.std(values)    
    return (mean, std)


if __name__ == "__main__":
    # use this for your own testing!

    pass
