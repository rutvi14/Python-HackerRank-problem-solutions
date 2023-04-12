# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
numbers = set(map(int, input().split()))
N = int(input())
numbers1 = set(map(int, input().split()))
l = []
for i in numbers.difference(numbers1):
    l.append(i)
for i in numbers1.difference(numbers):
    l.append(i)
for i in sorted(l):
    print(i)

# Second way

M = int(input())
numbers = set(map(int, input().split()))
N = int(input())
numbers1 = set(map(int, input().split()))

sym_diff = sorted(numbers.symmetric_difference(numbers1))
for i in sym_diff:
    print(i)