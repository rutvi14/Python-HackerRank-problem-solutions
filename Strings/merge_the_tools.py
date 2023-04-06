def merge_the_tools(s, k):
    # your code goes here
    
    n = len(s)
    parts = [s[i:i+k] for i in range(0, n, k)]
    for part in parts:
        distinct_chars = []
        for char in part:
            if char not in distinct_chars:
                distinct_chars.append(char)
        print(''.join(distinct_chars))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)