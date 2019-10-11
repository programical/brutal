# Usage examples
Print every lowercase 4-character combination of the alphabet:
```python
import brutal

brutal.force("qwertyuiopasdfghjklzxcvbnm", 4, print)
```
Test for a specific combination and print the result:
```python
import brutal

def checker(guess):
    return guess == "pass"

print(brutal.force("qwertyuiopasdfghjklzxcvbnm", 4, checker))
```
