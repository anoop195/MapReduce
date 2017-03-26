#!/usr/bin/python
import sys

'''
The data is stored in the format data time store item cost payment
This is a mapper function to calculate sales for each product category 
The mapping here is store ->  cost
Also once mapper gets executed hadoop will sort and shuffle and send the key -> value pair to corresponding reducer function based on the 
partitioner.
'''


def mapper():
    for line in sys.stdin:
        data = line.strip().split('\t')
        if len(data) == 6:
            data, time, store, item, cost, payment = data
            print "{0}\t{1}".format(store, cost)


mapper()
