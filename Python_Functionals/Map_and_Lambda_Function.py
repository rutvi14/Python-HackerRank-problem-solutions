cube = lambda x: x**3


def fibonacci(n):
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    if n==0:
        return []
    # Handle the base cases
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        result = [0, 1]
        for i in range(2, n):
            result.append(result[i - 1] + result[i - 2])
        return result[:n]


if __name__ == "__main__":
    n = int(input())
    print(list(map(cube, fibonacci(n))))
