num=input("Enter a number:")
if num==num[::-1]:
    print("The number is palindrome.")
else:
    print("The number is not palindrome.")

    # Function to check if a string is palindrome

def is_palindrome(s):
    s = s.lower().replace(" ", "")  # ignore spaces and case
    return s == s[::-1]             # reverse check

# Example
word = input("Enter a word: ")
if is_palindrome(word):
    print("It's a palindrome!")
else:
    print("Not a palindrome.")
