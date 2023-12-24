ch = input()
str_list = []
for c in ch:
    str_list.append(c)

str_list.sort()
a = ''.join(str_list)
print(a)