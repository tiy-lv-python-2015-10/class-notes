def square(x):
    int(x)
    return x * x

def fib(n):
    """Calculates the nth fibonacci number, given that n is positive"""

    prev = 0
    current = 1
    value = 0

    counter = 1

    if n == 0:
        return 0

    while counter < n:
        value = current + prev
        prev = current
        current = value
        counter += 1

    return value


if __name__ == '__main__':
    # Get a number
    my_number = int(input("Give me a number!"))
    print("Your number was ", my_number)

    print(square(my_number))
    print(fib(my_number))
