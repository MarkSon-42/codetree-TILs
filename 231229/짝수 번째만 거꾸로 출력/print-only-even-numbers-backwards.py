# Function to reverse even-numbered characters of a string
def reverse_even_characters(input_string):
    even_characters = input_string[1::2]  # Extract even-numbered characters
    reversed_even_characters = even_characters[::-1]  # Reverse the even-numbered characters
    print(reversed_even_characters)

# Input
input_string = input().strip()

# Output
reverse_even_characters(input_string)