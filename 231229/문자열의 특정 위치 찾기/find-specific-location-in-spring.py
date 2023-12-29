string, find_str = input().split()
if find_str in string:    
    print(string.index(find_str))
else:
    print('No')