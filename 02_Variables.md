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

* `title()` displays each word in beginning with a capital letter.
* `upper()` displays all letters uppercased.
* `lower()` displays all letters lowercased. This method is particularly useful to store data.

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

#### Combining or Concatenating Strings

Python uses the plus (`+`) symbol to concatenate strings.

```python
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
message = "Hello, " + full_name.title() + "!"
print(message)
```

Which outputs:
```
Hello, Ada Lovelace!
```

#### Adding whitespace to strings with tabs or newlines

* `/t` is used to add a new tab in your string.
* `/n` is used to add a newline in your string.

```python
print("Languages:\n\tPython\n\tC\n\tJavaScript")
```

Outputs:
```
Languages:
	Python
	C
	JavaScript
```

#### Stripping Whitespace

* `.rstrip()` returns a string with the white spaces stripped from the right edges. It doesn't change the variable value.
* `.lstrip()` does the same as `.rstrip()`, but on the left side of the string.
* `.strip()` strips the white spaces from both sides of a string.

```python
favorite_language = ' python '
print(favorite_language.rstrip())
# ' python'
print(favorite_language.lstrip())
# 'python '
print(favorite_language.strip())
# ' python '
```

## Numbers

### Integers

You can add (`+`), subtract (`-`), multiply (`*`), and divide (`/`) integers in Python.

```
>>> 2 + 3
5
>>> 3 - 2
1
>>> 2 * 3
6
>>> 3 / 2
1.5
```

Python uses two multiplication symbols (`**`) to represent exponents:

```
>>> 3 ** 2
9
>>> 3 ** 3
27
>>> 10 ** 6
1000000
```

You can also use parenthesis:

```
>>> 2 + 3*4
14
>>> (2 + 3) * 4
20
```

### Floats

Python calls any number with a decimal point a float.

```
>>> 0.1 + 0.1
0.2
>>> 0.2 + 0.2
0.4
>>> 2 * 0.1
0.2
>>> 2 * 0.2
0.4
```

### Avoiding type errors with the `str()` method

If you try to concatenate a variable containing a number to a string using `+`, Python is going to throw a type error.
You can avoid this by converting the contents of the variable to string using `.str()` method before doing the concatenation.

```python
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)
```

### Integers in Python 2

In Python 2, if you do Math only with Integers, the result will be an Integer as well, ignoring decimals.
In order to avoid imprecise results, at least one of the numbers needs to be a Float so the result will be a Float as well.

```
>>> 3 / 2
1
>>> 3.0 / 2
1.5
>>> 3 / 2.0
1.5
>>> 3.0 / 2.0
1.5
```

## Comments

In Python use `#` to write comments.

```python
# Say hello to everyone.
print("Hello Python people!")
```


[<< Back](README.md)
