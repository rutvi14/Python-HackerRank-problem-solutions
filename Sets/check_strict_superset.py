# Enter your code here. Read input from STDIN. Print output to STDOUT

s1=set(input().split(" "))
n2=int(input())
flag = True
for i in range(n2):
    s2=set(input().split(" "))
    if not s2.issubset(s1):
        flag = False
    if len(s2) >= len(s1):
        flag = False
print(flag)
