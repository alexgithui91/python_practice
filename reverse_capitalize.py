import math
import os
import random
import re
import sys


def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    pass


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)

    fptr.write(result + "\n")

    fptr.close()
