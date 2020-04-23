# Type 1
class NotPalindromeError(Exception):
    pass

def palindrome(word):
    if word == word[::-1]:
        print(word)
    else:
        raise NotPalindromeError('회문이 아닙니다.')

try:
    word = input()
    palindrome(word)
except NotPalindromeError as e:
    print(e)


# Type 2
class NotPalindromeError2(Exception):
    def __init__(self):
        super().__init__('회문이 아닙니다.')

def palindrome2(word):
    if word == word[::-1]:
        print(word)
    else:
        raise NotPalindromeError2

try:
    word = input()
    palindrome2(word)
except NotPalindromeError2 as e:
    print(e)