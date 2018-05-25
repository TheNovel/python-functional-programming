def isPalindrome(s):
    if (len(s) == 0):
        return True

    if s[0] == s[len(s) - 1]:
        return isPalindrome(s[1:len(s) - 1])
    else:
        return False
