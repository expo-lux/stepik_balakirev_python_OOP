def input_int_numbers():
    try:
        return tuple(map(int, input().split()))
    except ValueError:
        raise TypeError('все числа должны быть целыми')

while True:
    try:
        res = input_int_numbers()
        print(*res)
    except:
        print("Введи целые числа, увалень")
    else:
        break