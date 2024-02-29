import random
import time

from python import algorithms
from python import constants
from python import data_generator


def take_execution_time(minimum_size, maximum_size, step, samples_by_size):
    return_table = []

    for size in range(minimum_size, maximum_size + 1, step):
        print("Processing size: " + str(size))
        table_row = [size]
        times = take_times(size, samples_by_size)
        return_table.append(table_row + times)

    return return_table


"""
    It will return three values, one for each algorithm: The execution time for that size on each algorithm
"""


def take_times(size, samples_by_size):
    samples = []
    for _ in range(samples_by_size):
        samples.append(data_generator.get_random_list(size))
    return [
        take_time_for_algorithm(samples, lambda arr: algorithms.linear_search(arr, random.randint(0, len(arr) - 1))),
        take_time_for_algorithm(order(samples), lambda arr: algorithms.binary_search(arr, random.randint(0, len(arr) - 1), 0,
                                                                              len(arr) - 1)),
        take_time_for_algorithm(samples, lambda arr: algorithms.ternary_search(arr, random.randint(0, len(arr) - 1), 0,
                                                                               len(arr) - 1)),
    ]

# Ordenar arreglos para binario y ter

def order(matrix):
    for array in matrix:
        array.sort()
    return matrix

"""
    Returns the median of the execution time measures for a sorting approach given in 
"""


def take_time_for_algorithm(samples_array, sorting_approach):
    times = []

    for sample in samples_array:
        start_time = time.time()
        sorting_approach(sample.copy())
        times.append(int(constants.TIME_MULTIPLIER * (time.time() - start_time)))

    times.sort()
    return times[len(times) // 2]
