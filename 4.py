# DailyCodingProblem.com Problem #4
#
# Problem short description:
# Given an array of integers, find the lowest positive integer that does
# not exist in the array.
#
# The problem as stated in the e-mail:
###############################################################################
#     Given an array of integers, find the first missing positive integer in  #
#     linear time and constant space. In other words, find the lowest         #
#     positive integer that does not exist in the array. The array can        #
#     contain duplicates and negative numbers as well.                        #
#                                                                             #
#     For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] #
#     should give 3.                                                          #
#                                                                             #
#     You can modify the input array in-place.                                #
###############################################################################
#
# ##### Parameters & Usage ####################################################
# <inputSet> - must be comma separated integers without spaces, negative ints
#              are okay
#
# Example:
# .\4.py <inputSet>
# .\4.py 1,2,3,4,5
# .\4.py 1,-2,3,4,5

import sys
import re

def findFirstMissingPositiveInt(inputSet):
    counter = 1
    found = False

    while found == False:
        if counter not in inputSet:
            found = True
            return counter
        else:
            counter = counter + 1

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

    theNumber = findFirstMissingPositiveInt(inputSet)

    print("The first missing positive integer is {}.".format(theNumber))