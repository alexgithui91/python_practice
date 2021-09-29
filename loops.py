def main():
    n = int(input())

    if n < 0:
        pass
    else:
        my_list = [*range(n)]
        for itm in my_list:
            print(itm ** 2)


if __name__ == "__main__":
    main()
