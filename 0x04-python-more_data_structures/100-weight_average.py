#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    else:
        weighted_sum = 0
        total_weight = 0

        for item in my_list:
            value, weight = list(item)  # Convert tuple to list
            weighted_sum += value * weight
            total_weight += weight

        return weighted_sum / total_weight
