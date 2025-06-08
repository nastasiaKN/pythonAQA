#Task1
def even_numbers(n):
    for number in range(0, n + 1, 2):
        yield number


def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

# Task 2
class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        result = self.current
        self.current += 2
        return result

# Task 3
def log_arguments_and_result(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper


def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred: {e}")
    return wrapper


if __name__ == "__main__":
    print("Even numbers:")
    for num in even_numbers(10):
        print(num, end=' ')

    print("\n\nFibonacci sequence:")
    for num in fibonacci(15):
        print(num, end=' ')

    print("\n\nReverse list:")
    rev = ReverseIterator([1, 2, 3, 4, 5])
    for item in rev:
        print(item, end=' ')

    print("\n\nEven numbers with iterator:")
    even = EvenIterator(10)
    for num in even:
        print(num, end=' ')

    @log_arguments_and_result
    def add(a, b):
        return a + b

    print("\n\nDecorated add function:")
    add(5, 3)

    @handle_exceptions
    def divide(a, b):
        return a / b

    print("\nDivision with exception handling:")
    divide(10, 0)
