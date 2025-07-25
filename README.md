# 🧵 String Utility Module (with Pytest Test Coverage)

A simple yet robust Python mini-project that implements a utility module for common string operations. Each function is thoroughly tested using `pytest`, including edge cases and parameterized inputs.

---

## 📦 Module: `string_utils.py`

### ✅ Functions Implemented:

| Function Name           | Description                                    
|------------------------|--------------------------------------------
| `reverse_string(s)`     | Reverses the string                            
| `count_vowels(s)`       | Counts number of vowels (a, e, i, o, u)      
| `is_palindrome(s)`      | Checks if a string is a palindrome          
| `remove_special_chars(s)` | Removes non-alphanumeric characters  
| `capitalize_words(s)`   | Capitalizes the first letter of each word 

---

## 🧪 Testing with Pytest

Test cases for each function are written in `test_string_utils.py` using `pytest`.

### 🔍 What’s Covered:
- ✅ Basic unit tests with `assert`
- 🔁 Parametrized inputs via `@pytest.mark.parametrize`
- ⚠️ Edge/negative cases like empty strings and special symbols
- 🧪 Custom `print()` statements for clarity in test runs

---

## 🚀 How to Run

1. **Install Pytest** (if not already installed):
   ```bash
   pip install pytest
