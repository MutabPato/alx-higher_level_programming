#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    total_sum = 0
    total_weight = 0

    for item in my_list:
        value, weight = item
        total_sum += value * weight
        total_weight += weight

    if total_weight == 0:
        return (0)

    return (total_sum / total_weight)
