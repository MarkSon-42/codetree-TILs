string_a = input()
string_b = input()
result_a = ''.join(char for char in string_a if not char.isalpha())
result_b = ''.join(char for char in string_b if not char.isalpha())

print(int(result_a) + int(result_b))