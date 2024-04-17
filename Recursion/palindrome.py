def isPalindrome(s):
    '''tears apart user input words to determine if palindrome'''
    s = s.lower() #turns words to lower case
    l = len(s) #Grabs length of word
    if l < 2: #ensures the word is eligable to be a palindrome
        return True
    elif s[0] == s[l - 1]: #begins dissecting the word to check if palindrome
        return isPalindrome(s[1: l - 1])
    else:
        return False


def main():
    '''Lab 2, Problem 3: Palindromes'''
    print("A program to check for palindromes\n")
    s = input("Enter a possible palindrome:")
    ans = isPalindrome(s)
    if ans:
        print("Yes")
    else:
        print("No")

main()