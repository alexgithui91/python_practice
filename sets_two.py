num_stamps = int(input())
country_list = []

for i in range(num_stamps):
    country = input()
    country_list.append(country)

new_list = set(country_list)

print(len(new_list))
