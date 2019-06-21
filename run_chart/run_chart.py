#! /usr/bin/env python3

import os
from sys import exit
import numpy
from matplotlib.pyplot import figure, plot, show


def read_data(file):
    try:
        with open(file, 'r') as file:
            data = [int(line.strip('\n').strip(' ').split(' ')[-1]) for line in file.readlines()]
            # print(data)
            return data
    except FileNotFoundError:
        print('Where the hell is the data file? :O')
        print(f'Given file path: {file}')
        exit(1)


def main():
    data_file = 'tasks_stat.txt'
    file = os.path.join(os.path.dirname(__file__), f'{data_file}')
    data = read_data(file)

    mean = numpy.mean(data)
    std_dev = numpy.std(data)
    green_range = (mean - std_dev, mean + std_dev)
    red_range = (mean - 2 * std_dev, mean + 2 * std_dev)
    time = []
    for i in range(len(data)):
        time.append(i)

    figure(1)
    plot(time, data, '-o')
    plot([mean for i in time], 'b')
    plot([green_range for i in time], 'g')
    plot([red_range for i in time], 'r')
    show()


if __name__ == '__main__':
    main()