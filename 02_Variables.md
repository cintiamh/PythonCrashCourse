[<< Back](README.md)

# Variables And Simple Data Types

## Variables

Try changing `hello_world.py` code adding the string in a variable:

```python
message = "Hello World!"
print(message)
```

You can change the variable value at any time.

### Naming and using variables

* Variable names can contain letters, numbers, and underscores. They can start with a letter or an underscore, but not with a number.
* Spaces are not allowed in a variable names, but you can replace spaces with underscores.
* Avoid using Python reserved words on variable names.
* Variable names should be short but descriptive.
* Prefer to use lowercase letters for simple variables.

## Strings

Anything inside quotes is considered a string in Python, and you can use single or double quotes around your strings.

```python
"This is a string."
'This is also a string.'
```

This flexibility allows you to use quotes and apostrophes within your strings:

```python
'I told my friend, "Python is my favorite language!"'
"The language 'Python' is named after Monty Python, not the snake."
"One of Python's strengths is its diverse and supportive community."
```

### Changing case in a string with methods

#### Some String methods

`title()` displays each word in beginning with a capital letter.
`upper()` displays all letters uppercased.
`lower()` displays all letters lowercased. This method is particularly useful to store data.

```python
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())
```

The output is:
```
Ada Lovelace
ADA LOVELACE
ada lovelace
```


[<< Back](README.md)
