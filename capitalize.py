import os


def solve(s):
    new_string = ""
    string_list = s.split(" ")
    for itm in string_list:
        new_string += itm.capitalize() + " "
    return new_string


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = solve(s)

    fptr.write(result + "\n")

    fptr.close()
