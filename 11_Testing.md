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

## Testing a class

### A variety of assert methods

Python provides a number of assert methods in the `unittest.TestCase` class.

* `assertEqual(a, b)` - Verify that `a == b`
* `assertNotEqual(a, b)` - Verify that `a != b`
* `assertTrue(x)` - Verify that `x` is `True`
* `assertFalse(x)` - Verify that `x` is `False`
* `assertIn(item, list)` - Verify that `item` is in `list`
* `assertNotIn(item, list)` - Verify that `item` is in `list`

### A class to test

Testing a class is similar to testing a function - much of your work involves testing the behavior of the methods in the class.

survey.py
```python
class AnonymousSurvey():
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print("- " + response)
```

Then a code that uses that class:

language_survey.py
```python
from survey import AnonymousSurvey

# Define a question, and make a survey.
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = raw_input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show the survey results.
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
```

### Testing the AnonymousSurvey Class



[<< Back](README.md)
