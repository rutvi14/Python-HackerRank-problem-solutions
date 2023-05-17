# Enter your code here. Read input from STDIN. Print output to STDOUT
n, x = map(int, input().split())
marks = []
for _ in range(x):
    marks.append(map(float, input().split()))
for i in zip(*marks):
    print(sum(i) / len(i))
