import math
import os
import random
import re
import sys
import string


def transformSentence(sentence):
    # Write your code here
    new_string = sentence.split()
    res_str = ""

    for i in new_string:
        res_str += i[0]
        for j in range(1, len(i)):
            if i[j - 1].lower() < i[j].lower():
                res_str += i[j].upper()
            elif i[j - 1].lower() < i[j].lower():
                res_str += i[j].lower()
            else:
                res_str += i[j]

        res_str += " "
    return res_str[:-1:]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    sentence = input()

    result = transformSentence(sentence)

    fptr.write(result + "\n")

    fptr.close()
