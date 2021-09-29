def main():
    # method_one()
    # method_two()
    # method_three()
    method_four()
    # pass


def method_one():
    """
    Using a simple for loop to create a list
    """
    squares = []

    for i in range(10):
        squares.append(i * i)

    print(squares)


def method_two():
    """
    Using map() to create a list
    Returns:
        [type]: [description]
    """
    txns = [1.09, 23.56, 57.84, 4.56, 6.78]
    TAX_RATE = 0.08

    def get_price_with_tax(txn):
        return txn * (1 + TAX_RATE)

    final_prices = map(get_price_with_tax, txns)

    print(list(final_prices))


def method_three():
    """
    Using list comprehension we can write method_one in a single line
    """
    squares = [i * i for i in range(10)]
    print(squares)


def method_four():
    """
    Using list comprehension to create a list similar to method two
    Returns:
        [type]: [description]
    """
    txns = [1.09, 23.56, 57.84, 4.56, 6.78]
    TAX_RATE = 0.08

    def get_price_with_tax(txn):
        return txn * (1 + TAX_RATE)

    final_prices = [get_price_with_tax(i) for i in txns]

    print(list(final_prices))


if __name__ == "__main__":
    main()
