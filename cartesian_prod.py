from itertools import product

# break input down using map
a = list(map(int, input().split()))
b = list(map(int, input().split()))

my_list = [a, b]

my_tuple = tuple(product(*my_list))

for i in my_tuple:
    print(i, end=" ")
