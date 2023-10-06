def is_palindrome(s):
    s = s.lower() #convert into lower case
    reversed_s = s[::-1] #reverse the string
    return s == reversed_s #compare the original str and reversed str
print(is_palindrome('racecar'))
print(is_palindrome('python'))
