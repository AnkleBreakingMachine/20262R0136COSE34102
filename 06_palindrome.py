
def is_palindrome(text):
    cleaned = "".join(
        char.lower() for char in text if char.isalnum()
    )
    return cleaned == cleaned[::-1]

print(is_palindrome("racecar"))
print(is_palindrome("Hello"))
print(is_palindrome("A man a plan a canal Panama"))