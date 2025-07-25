import pytest

from string_util import reverse_string, count_vowels, is_palindrome, remove_special_char, capitalize_word

@pytest.mark.parametrize("input_str, expected",[
    ("abc", "cba"),
    ("Hello", "olleH"),
    ("", ""),
    ("A man a plan a canal Panama", "amanaP lanac a nalp a nam A"),
])
def test_reverse_string(input_str, expected):
    print(f"Testing reverse_string with input: {input_str}")
    assert reverse_string(input_str) == expected

@pytest.mark.parametrize("input_str, expected",[
    ("abc", 1),
    ("Hello", 2),
    ("moulya", 3),
    ("", 0),
])
def test_count_vowels(input_str,expected):
    print(f"Testing count_vowels with input: {input_str}")
    assert count_vowels(input_str) == expected

@pytest.mark.parametrize("input_str, expected",[
    ("abc", False), 
    ("racecar", True),
    ("mom", True),
    ("Hello", False),
])
def test_is_palindrome(input_str, expected):
    print(f"Testing is_palindrome with input: {input_str}")
    assert is_palindrome(input_str) == expected

@pytest.mark.parametrize("input_str, expected",[
    ("abc!@#", "abc"),
    ("Hello, World!", "HelloWorld"),
    ("", ""),
    ("A man a plan a canal Panama", "AmanaplanacanalPanama")
])
def test_remove_special_char(input_str, expected):
    print(f"Testing remove_special_char with input: {input_str}")
    assert remove_special_char(input_str) == expected

@pytest.mark.parametrize("input_str, expected",[
    ("hello world", "Hello World"),
    ("python programming", "Python Programming"),
    ("", ""),
    ("a b c", "A B C"),
])
def test_capitalize_word(input_str, expected):
    print(f"Testing capitalize_word with input: {input_str}")
    assert capitalize_word(input_str) == expected