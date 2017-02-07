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

test_name_function.py
```python
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'"""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()
```

If the tests ran ok, we should get a result like this:

```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

### A failing test

What if now we want to change the method in order to accept an optional middle name?

```python
def get_formatted_name(first, middle, last):
    """Generate a neatly formatted full name."""
    full_name = first + ' ' + middle + ' ' + last
    return full_name.title()
```

We'll get an error:

```
E
======================================================================
ERROR: test_first_last_name (__main__.NamesTestCase)
Do names like 'Janis Joplin' work?
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_name_function.py", line 9, in test_first_last_name
    formatted_name = get_formatted_name('janis', 'joplin')
TypeError: get_formatted_name() takes exactly 3 arguments (2 given)

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
```

### Responding to a failing test

We know the test that failed actually used to work, so the problem is with the code, not the test.

We need a default value to middle name so it will be optional.

```python
def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()
```

### Adding new tests

Now we want to make sure that the function works when we have a middle name.

```python
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'"""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()
```

[<< Back](README.md)