# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

string, k = input().split()
for i in range(1, int(k) + 1):
    print(*["".join(i) for i in combinations(sorted(string), int(i))], sep="\n")
