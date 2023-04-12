# Enter your code here. Read input from STDIN. Print output to STDOUT
test_cases = int(input())
for i in range(test_cases):
    elementsA = int(input())
    A = set(input().split(" "))
    elementsB = int(input())
    B = set(input().split(" "))
    print(A.issubset(B))