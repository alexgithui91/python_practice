for i in range(int(input())):
    try:
        num1, num2 = map(int, input().split())
        print(num1 // num2)
    except BaseException as e:
        print("Error Code:", e)
