def palindrome(s):
    return s == s[::-1]
 
s = "kajak"
a = palindrome(s)
 
if a:
    print(bool(s == s[::-1]))
else:
    print(bool(s == s[::-1]))