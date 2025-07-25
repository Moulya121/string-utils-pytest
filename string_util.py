import re

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    return sum(1 for char in s.lower() if char in 'aeiou')

def is_palindrome(s):
    cleaned = re.sub(r'[^A-Za-z0-9]','',s.lower())
    return cleaned == cleaned[::-1]

def remove_special_char(s):
    return re.sub(r'[^A-Za-z0-9]','',s)

def capitalize_word(s):
    return ' '.join(word.capitalize() for word in s.split())