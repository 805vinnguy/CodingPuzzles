# Max Sum Non Adjacent
# Author: Vinh Nguyen

def max_sum_non_adjacent(list):
    largest_sum_excluding_last = 0
    largest_sum_including_last = 0

    for i in range(len(list)):
        tmp = largest_sum_excluding_last
        largest_sum_excluding_last = max(largest_sum_excluding_last, largest_sum_including_last)
        largest_sum_including_last = tmp + list[i] 

    return max(largest_sum_excluding_last, largest_sum_including_last)
