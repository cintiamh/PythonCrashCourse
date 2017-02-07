[<< Back](README.md)

# Testing your code

In this chapter you'll learn to test your code using tools in Python's `unittest` module.

## Testing a function

A simple code: name_function.py
```python
def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = first + ' ' + last
    return full_name.title()
```

And a code that uses it (names.py):
```python
from name_function import get_formatted_name

print("Enter 'q' any time to quit.")
while True:
    first = raw_input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = raw_input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + ".")
```

### Unit tests and test cases

The module `unittest` from the Python standard library provides tools for testing your code.

* Unit test => verifies one specific aspect of a function's behavior is correct.
* Test case => is a collection of unit tests that together prove that the function behaves as it's supposed to.

### A passing test

To write a test case for a function, import the `unittest` module and the function you want to test.
Then create a class that inherits from `unittest.TestCase`, and write a series of methods to test different aspects of your function's behavior.

[<< Back](README.md)
