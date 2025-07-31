
# Helper function to check if a word is a palindrome
# Palindromes are words that are the same forwards and backwards
# "racecar" is a palindrome since when reversed, it still spells "racecar"
# "hello" wouldn't be a palindrome since backwards it is spelt "olleh"
def is_palindrome(word):
    backwards = ""
    for i in word:
        backwards = i + backwards
    if word == backwards:
        return True
    else:
        return False
    

# Input for test cases (racecar is a palindrome, hello is not a palindrome.)
word = input("Enter a word to check if it is a palindrome: ")

# Test case
checked_word = is_palindrome(word)
print(checked_word)

