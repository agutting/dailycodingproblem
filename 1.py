# DailyCodingProblem.com Problem #1
#
# Problem short description:
# Given a list of numbers, determine whether any two add up to a third number.
#
# The problem as stated in the e-mail:
###############################################################################
#     This problem was recently asked by Google.                              #
#                                                                             #
#     Given a list of numbers and a number k, return whether any two numbers  #
#     from the list add up to k.                                              #
#                                                                             #
#     For example, given [10, 15, 3, 7] and k of 17, return true since        #
#     10 + 7 is 17.                                                           #
#                                                                             #
#     Bonus: Can you do this in one pass?                                     #
###############################################################################
#
# ##### Parameters & Usage ####################################################
# <arrayOfIntegersToSearch> - must be comma separated integers without spaces,
#       negative ints okay
# <integerSumToSearchFor> - must be an integer only, negative ints okay
# 
# Examples:
# .\1.py <arrayOfIntegersToSearch> <integerSumToSearchFor>
# .\1.py 2,4,6,3,5 8
# .\1.py 2,-4,6,3,5 -2

import sys
import re

def arrayContainsSum(arr, theSum):
    sumPresent = False
    matches = []
    
    for i in range(0, len(arr)):
        # beginning this 2nd loop at i + 1 means we never compare the same
        # two numbers twice or compare a number to itself, fulfilling the
        # 'in one pass' objective
        for j in range(i + 1, len(arr)):
            if int(arr[i]) + int(arr[j]) == int(theSum):
                sumPresent = True
                matches.append({
                    'firstNumber': arr[i],
                    'secondNumber': arr[j]
                })
    
    if sumPresent:
        return matches
    else:
        return False


if __name__ == "__main__":
    arr = sys.argv[1]
    theSum = sys.argv[2]

    usage = """Usage:
       Two parameters required, an array of integers input as a
       comma separated string without spaces and an integer representing
       the sum you're trying to find in the array.
       \r\nExample:
       .\\1.py 8,14,22,31 36"""

    # regex ensuring first argument is comma separated integers
    if not re.match(r'^(-?[0-9]+,)+-?[0-9]+$', arr):
        print(usage)
        exit()
    
    arr = arr.split(',')
    
    # regex ensuring second argument is integer only
    if not re.match(r'^[0-9]+$', theSum):
        print(usage)
        exit()

    result = arrayContainsSum(arr, theSum)
    if result: # at least one match found
        if len(result) > 1: # multiple matches found
            print("{} matches found:".format(len(result)))
            for i in result:
                print("{} + {} = {}".format(i['firstNumber'], i['secondNumber'], theSum))
        else: # exactly one match found
            print("1 match found:")
            for i in result:
                print("{} + {} = {}".format(i['firstNumber'], i['secondNumber'], theSum))
    else: # no matches found
        print("This array contains no two numbers which add up to {}".format(theSum))