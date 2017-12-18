"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

#Paolo Bergantino
def reverse(n):
    return str(n)[::-1]

def isPalindrome(n):
    if str(n) == reverse(n):
        return True
    return False

def findPalindromes(sequence):
    for n in sequence:
        if isPalindrome(n):
            yield n

def palindromeFactors():
    for m in range(100, 1000):
        for n in range(100, 1000):
            if isPalindrome(m * n):
                yield(m * n)
            
print(max(list(palindromeFactors())))
