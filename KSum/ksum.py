# K Sum
# Author: Vinh Nguyen

def k_sum(numbers, k):
    # [10, 15, 3, 7] k=17
    # [ 7,  0, 0, 0]
    for i in range(len(numbers)):
        diff = k - numbers[i]
        if(diff in numbers):
            return True
    return False
