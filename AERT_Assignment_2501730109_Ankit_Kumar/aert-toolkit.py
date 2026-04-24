class StackADT:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.data.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)


def factorial(n):
    if n < 0:
        return "Invalid input"
    if n == 0:
        return 1
    return n * factorial(n - 1)


naive_count = 0
memo_count = 0


def fib_naive(n):
    global naive_count
    naive_count += 1

    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


def fib_memo(n, memo):
    global memo_count
    memo_count += 1

    if n in memo:
        return memo[n]

    if n <= 1:
        memo[n] = n
        return n

    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


def hanoi(n, source, helper, destination, stack):
    if n == 1:
        stack.push("Move disk 1 from " + source + " to " + destination)
        return

    hanoi(n - 1, source, destination, helper, stack)
    stack.push("Move disk " + str(n) + " from " + source + " to " + destination)
    hanoi(n - 1, helper, source, destination, stack)


def binary_search(arr, key, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, key, low, mid - 1)
    else:
        return binary_search(arr, key, mid + 1, high)


def main():
    print("Factorial Test Cases")
    print("0! =", factorial(0))
    print("1! =", factorial(1))
    print("5! =", factorial(5))
    print("10! =", factorial(10))
    print()

    print("Fibonacci Test Cases")

    for n in [5, 10, 20, 30]:
        global naive_count, memo_count

        naive_count = 0
        memo_count = 0

        memo = {}

        print("n =", n)
        print("Naive:", fib_naive(n), "Calls:", naive_count)
        print("Memoized:", fib_memo(n, memo), "Calls:", memo_count)
        print()

    print("Tower of Hanoi (N = 3)")
    stack = StackADT()
    hanoi(3, "A", "B", "C", stack)

    while not stack.is_empty():
        print(stack.pop())
    print()

    print("Binary Search Test Cases")
    arr = [1, 3, 5, 7, 9, 11, 13]

    print("Search 7 ->", binary_search(arr, 7, 0, len(arr) - 1))
    print("Search 1 ->", binary_search(arr, 1, 0, len(arr) - 1))
    print("Search 13 ->", binary_search(arr, 13, 0, len(arr) - 1))
    print("Search 2 ->", binary_search(arr, 2, 0, len(arr) - 1))

    empty = []
    print("Search in empty list ->", binary_search(empty, 5, 0, len(empty) - 1))


if __name__ == "__main__":
    main()