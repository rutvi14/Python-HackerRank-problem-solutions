n = int(input())
s = set(map(int, input().split()))
c = int(input())
comand = []
n1 = int()
for _ in range(c):
    comand = input().split()
    if len(comand) == 1:
        s.pop()
    elif comand[0]=='remove' and int(comand[1]) in s:
        s.remove(int(comand[1]))
    elif comand[0]=='discard':
        s.discard(int(comand[1]))
print(sum(set(s)))