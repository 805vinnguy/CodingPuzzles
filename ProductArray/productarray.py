# Product Array
# Author: Vinh Nguyen

def product_array_no_div(input_arr):
    # [1, 2, 3, 4, 5]
    # [1, 1, 1, 1, 1]
    # looping slice
    size = len(input_arr)
    output_arr = [1] * size
    i = 0
    while(i < size):
        j = (i + 1) % size
        while(j % size != i):
            output_arr[i] *= input_arr[j % size]
            j += 1
        i += 1
    return output_arr

def product_array_div(input_arr):
    size = len(input_arr)
    tot_prod = 1
    for i in range(size):
        tot_prod *= input_arr[i]
    output_arr = [tot_prod] * size
    for i in range(size):
        output_arr[i] /= input_arr[i]
    return output_arr
