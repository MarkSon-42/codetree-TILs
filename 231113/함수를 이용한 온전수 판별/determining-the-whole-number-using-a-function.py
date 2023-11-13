def is_perfect_number(num):
    if num % 2 == 0 or num % 10 == 5 or (num % 3 == 0 and num % 9 != 0):
        return False
    return True

def count_perfect_numbers(a, b):
    count = 0
    for num in range(a, b + 1):
        if is_perfect_number(num):
            count += 1
    return count

a, b = map(int, input().split())

result = count_perfect_numbers(a, b)


print(result)