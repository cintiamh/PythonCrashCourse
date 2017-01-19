[<< Back](README.md)

# Functions

## Defining a function

The simplest structure of a function looks like this:

```python
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()
```

We use the keyword `def` to inform Python that we're defining a function.
This is the function definition, which tells Python the name of the function, and if applicable, what kind of information the function needs to do its job (inside the parenthesis).
The parentheses are required. Finally, the definition ends in a colon.

`Docstring` is a type of comment that describes what the function does. `Docstrings` are enclosed in triple quotes, which Python looks for when it generates documentation for the functions in your programs.

### Passing information to a function

```python
def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")

greet_user('jesse')
# Hello, Jesse!
```

### Arguments and Parameters

A parameter is a piece of information the function needs to do its job. In the case above, the variable `username`.

An argument is a piece of information that is passed from a function call to a function. In the case above, the name we passed in when calling `greet_user`, `jesse`.

## Passing Arguments



[<< Back](README.md)
