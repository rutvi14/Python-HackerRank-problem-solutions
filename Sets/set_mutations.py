a=int(input())
s=set(map(int,input().split()))
n=int(input())
for i in range(n):
    x,y=input().split()
    if x=='intersection_update':
       s.intersection_update(set(map(int,input().split())))
    
    elif x=='update':
        s.update(set(map(int,input().split())))    
    
    elif x=='symmetric_difference_update':
        s.symmetric_difference_update(set(map(int,input().split())))
    
    elif x=='difference_update':
        s.difference_update(set(map(int,input().split())))

print(sum(s))