# DailyCodingProblem.com Problem #5
#
# The problem as stated in the e-mail:
###############################################################################
#     cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the   #
#     first and last element of that pair. For example, car(cons(3, 4))       #
#     returns 3, and cdr(cons(3, 4)) returns 4.                               #
#                                                                             #
#     Given this implementation of cons:                                      #
#                                                                             #
#     def cons(a, b):                                                         #
#       def pair(f):                                                          #
#         return f(a, b)                                                      #
#       return pair                                                           #
#                                                                             #
#     Implement car and cdr.                                                  #
###############################################################################
#
# ##### Parameters & Usage ####################################################
# <inputSet> - must be exactly two comma separated integers without spaces, negative ints
#              are okay
#
# Example:
# .\5.py <inputSet>
# .\5.py 1,2
# .\5.py 1,-2

import sys
import re

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(f):
    def left(a, b):
        return a
    return f(left)

def cdr(f):
    def right(a, b):
        return b
    return f(right)

if __name__ == '__main__':
    inputSet = sys.argv[1]

    usage = """Usage:
       One parameter required - a pair of integers input as a
       comma separated string without spaces
       \r\nExample:
       .\\5.py 1,2"""

    # regex to validate input
    if not re.match(r'^(-?[0-9]+,)-?[0-9]+$', inputSet):
        print(usage)
        exit()
    
    # convert input string to list of ints
    inputSet = list(map(int, inputSet.split(',')))

    print("car(cons({}, {})) is {}".format(inputSet[0], inputSet[1], car(cons(inputSet[0], inputSet[1]))))
    print("cdr(cons({}, {})) is {}".format(inputSet[0], inputSet[1], cdr(cons(inputSet[0], inputSet[1]))))