# Product Array
# Author: Vinh Nguyen

# O(2n-1)
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

# O(2n)
def product_array_div(input_arr):
    size = len(input_arr)
    tot_prod = 1
    for i in range(size):
        tot_prod *= input_arr[i]
    output_arr = [tot_prod] * size
    for i in range(size):
        output_arr[i] /= input_arr[i]
    return output_arr

# O(2n-2)
def product_array(input_arr):
    # [1, 2, 3, 4, 5]
    # [(60/1)*2, (40/2)*3, (30/3)*4, (24/4)*5, 24=(120/5)*1]
    size = len(input_arr)
    output_arr = [1] * size
    for i in range(size - 1):
        output_arr[-1] *= input_arr[i]
    for i in range(1, size):
        # start from the end
        iOut = size - 1 - i
        iPrev = iOut + 1
        output_arr[iOut] = (output_arr[iPrev] / input_arr[iOut]) * input_arr[iPrev]
    return output_arr
