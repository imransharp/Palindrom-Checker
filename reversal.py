def check_palindrome(input_string):
    reversed_string = input_string[::-1]
    if input_string == reversed_string:
        return f"'{input_string}' is a palindrome."
    else:
        return f"'{input_string}' is not a palindrome."

# Test the function
if __name__ == "__main__":
    test_string = input("Enter a string to check: ")
    print(check_palindrome(test_string))
