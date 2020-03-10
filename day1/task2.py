for num in range(1, 31):
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 5 == 0 and num % 15 != 0:
        print("Buzz")
    elif num % 3 == 0 and num % 15 != 0:
        print("Fizz")
    else:
        print(num)
