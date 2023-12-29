def run_length_encoding(s):
    encoded_result = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded_result += s[i - 1] + str(count)
            count = 1

    encoded_result += s[-1] + str(count)  # Adding the last character and its count

    return len(encoded_result), encoded_result

if __name__ == "__main__":
    A = input().strip()

    length, result = run_length_encoding(A)

    print(length)
    print(result)