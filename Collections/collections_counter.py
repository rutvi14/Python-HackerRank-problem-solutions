shoes_count = int(input())
sizes = [int(i) for i in input().split()]
customers = int(input())
prices = []
for _ in range(customers):
    size, price = map(int, input().split())
    if size in sizes:
        prices.append(price)
        sizes.remove(size)
print(sum(prices))
