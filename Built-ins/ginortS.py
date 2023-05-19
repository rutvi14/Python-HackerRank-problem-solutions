# Enter your code here. Read input from STDIN. Print output to STDOUT
input_string = input()
lower = list(filter(lambda x: x.islower(), input_string))
upper = list(filter(lambda x: x.isupper(), input_string))
even = []
odd = []
for char in input_string:
    if char.isdigit():
        if int(char) % 2 == 0:
            even.append(char)
        else:
            odd.append(char)
print("".join(sorted(lower) + sorted(upper) + sorted(odd) + sorted(even)))
