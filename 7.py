# DailyCodingProblem.com Problem #7
#
# The problem as stated in the e-mail:
###############################################################################
#     Good morning! Here's your coding interview problem for today.           #
#                                                                             #
#     This problem was asked by Facebook.                                     #
#                                                                             #
#     Given the mapping a = 1, b = 2, ... z = 26, and an encoded message,     #
#     count the number of ways it can be decoded.                             #
#                                                                             #
#     For example, the message '111' would give 3, since it could be decoded  #
#     as 'aaa', 'ka', and 'ak'.                                               #
#                                                                             #
#     You can assume that the messages are decodable. For example, '001' is   #
#     not allowed.                                                            #
###############################################################################
#
# ##### Parameters & Usage ####################################################
# <message> - must be a string of integers that can be separated into a list
#             of integers containing only the numbers 1 through 26
#
# Example:
# .\5.py <inputSet>
# .\5.py 419122531549147161815212513192131119

import sys

translationDict = {
    1: "a",
    2: "b",
    3: "c",
    4: "d",
    5: "e",
    6: "f",
    7: "g",
    8: "h",
    9: "i",
    10: "j",
    11: "k",
    12: "l",
    13: "m",
    14: "n",
    15: "o",
    16: "p",
    17: "q",
    18: "r",
    19: "s",
    20: "t",
    21: "u",
    22: "v",
    23: "w",
    24: "x",
    25: "y",
    26: "z"
}

def decodeMessage(message):
    messageSequence = list(message)

    workingChar = ''

    for i in messageSequence:
        if int(i) >= 1 and int(i) <= 26 and len(workingChar) < 2:
            workingChar = workingChar + i
            if len(workingChar) = 1 and int(workingChar) > 0:
                


if __name__ == '__main__':
    message = sys.argv[1]

    usage = """Usage:
       One parameter required - a string of integers that can be separated into
       a list containing only the numbers 1 through 26
       \r\nExample:
       .\\5.py 1,2"""

    