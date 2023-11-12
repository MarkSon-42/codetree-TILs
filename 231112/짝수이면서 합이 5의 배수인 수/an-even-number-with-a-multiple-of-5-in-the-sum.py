def is_even_and_sum_multiple_of_5(n):
    # Check if n is even
    is_even = n % 2 == 0

    # Calculate the sum of the digits
    digit_sum = sum(map(int, str(n)))

    # Check if the sum of the digits is a multiple of 5
    is_sum_multiple_of_5 = digit_sum % 5 == 0

    # Return "Yes" if both conditions are met, otherwise "No"
    return "Yes" if is_even and is_sum_multiple_of_5 else "No"

# Input: Read a two-digit number from the user
n = int(input())

# Output: Call the function and print the result
result = is_even_and_sum_multiple_of_5(n)
print(result)