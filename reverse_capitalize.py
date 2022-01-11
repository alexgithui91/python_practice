import math
import os
import random
import re
import sys


def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    new_sentence = sentence.split()
    new_sentence.reverse()

    new_string = ""
    new_list = []

    for elem in new_sentence:
        for letter in elem:
            if letter.isupper():
                new_string += letter.lower()
            else:
                new_string += letter.upper()

        new_list.append(new_string)
        new_string = ""

    return " ".join(new_list)


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    # sentence = input()
    sentence = "fUn"

    result = reverse_words_order_and_swap_cases(sentence)

    # fptr.write(result + "\n")

    # fptr.close()
    print(result)
