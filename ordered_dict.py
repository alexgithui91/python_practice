# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

market_dict = OrderedDict()

for i in range(int(input())):
    name, blank, price = input().rpartition(" ")
    market_dict[name] = market_dict.get(name, 0) + int(price)

for i in market_dict.items():
    print(*i)
