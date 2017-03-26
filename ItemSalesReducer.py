#!/usr/bin/python
import sys

'''
The data is stored in the format data time store item cost payment
This is a reducer function to calculate sales for each product category 
The mapping here is item -> cost
'''


def reducer():
    salesTotal = 0
    oldKey = 0
    for line in sys.stdin:
        data = line.strip().split('\t')

        if len(data) != 2:
            continue
        thisKey, thisSale = data
        if oldKey and oldKey != thisKey:
            print "{0}\t{1}".format(oldKey, salesTotal)
            salesTotal = 0
        oldKey = thisKey
        salesTotal += float(thisSale)


reducer()
