# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

num = int(input())
d = deque()
for _ in range(num):
    action = input().split()
    if action[0] == "append":
        d.append(action[1])
    elif action[0] == "appendleft":
        d.appendleft(action[1])
    elif action[0] == "pop":
        d.pop()
    elif action[0] == "popleft":
        d.popleft()
print(*d)
