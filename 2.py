# DailyCodingProblem.com Problem #2
#
# Problem short description:
# Given an array of integers, produce an array where newArray[i] equals
# the product of all elements in originalArray except originalArray[i]
#
# The problem as stated in the e-mail:
###############################################################################
#     Given an array of integers, return a new array such that each element   #
#     at index i of the new array is the product of all the numbers in the    #
#     original array except the one at i.                                     #
#                                                                             #
#     For example, if our input was [1, 2, 3, 4, 5], the expected output      #
#     would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the         #
#     expected output would be [2, 3, 6].                                     #
#                                                                             #
#     Follow-up: what if you can't use division?                              #
###############################################################################
#
# ##### Parameters & Usage ####################################################
# <inputSet> - must be comma separated integers without spaces, negative ints
#              are okay
#
# Example:
# .\2.py <inputSet>
# .\2.py 1,2,3,4,5
# .\2.py 1,-2,3,4,5

import sys
import re

def transformSet(inputSet):
    outputSet = []

    for i in range(0, len(inputSet)):
        # Make a copy of inputSet, remove this iteration's value,
        # get the product, and append it to outputSet
        multiplicands = inputSet[:]
        multiplicands.remove(multiplicands[i])
        j = 1
        for multiplicand in multiplicands:
            j = j * multiplicand
        outputSet.append(j)
    
    return outputSet


if __name__ == '__main__':
    inputSet = sys.argv[1]
    
    usage = """Usage:
       One parameter required - an array of integers input as a
       comma separated string without spaces
       \r\nExample:
       .\\1.py 1,2,4,9,7"""
    
    # regex ensuring argument is comma separated integers
    if not re.match(r'^(-?[0-9]+,)+-?[0-9]+$', inputSet):
        print(usage)
        exit()
    
    # convert list of strings (e.g. ['1', '2']) to list of ints ([1, 2])
    inputSet = list(map(int, inputSet.split(',')))
    
    outputSet = transformSet(inputSet)

    print('With input set:')
    print(inputSet)
    print('You get output set:')
    print(outputSet)