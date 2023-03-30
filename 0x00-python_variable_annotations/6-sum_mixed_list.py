#!/usr/bin/env python3
"""function sum_mixed_list which takes a
    list mxd_lst of integers and floats and returns their sum as a float
"""


def sum_mixed_list(mxd_list: [float | int]) -> float:

    total = 0.0
    for num in mxd_list:
        total = + num
    """returns their sum as a float"""
    return total
