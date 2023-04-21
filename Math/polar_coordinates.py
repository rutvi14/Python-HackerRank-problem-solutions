# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath

num = complex(input())
for i in cmath.polar(num):
    print(i)
