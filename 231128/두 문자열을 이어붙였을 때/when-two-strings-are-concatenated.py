def ispal(a, b):
    if a + b == b + a:
        return True
    else:
        return False

a = input()
b = input()

if ispal(a, b):
    print('true')
else:
    print('false')