from collections import Counter

number_of_shoes = int(input())

shoe_sizes = list(map(int, input().split()))
shoe_size_dict = dict(Counter(shoe_sizes))

number_of_customers = int(input())

money_earned = 0

for i in range(number_of_customers):
    shoe_order = list(map(int, input().split()))
    stock_count = shoe_size_dict.get(shoe_order[0])
    if stock_count == 0:
        pass
    else:
        try:
            shoe_size_dict[shoe_order[0]] -= 1
            money_earned += shoe_order[1]
        except Exception as e:
            pass

print(money_earned)
