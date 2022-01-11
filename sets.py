def average(array):
    set_list = set(array)
    result = sum(set_list) / len(set_list)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
