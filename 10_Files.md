[<< Back](README.md)

# Files and Exceptions

## Reading from a file

When you want to work with the information in a text file, the first step is to read the file into memory.
You can read the entire contents of a file, or you can work through the file one line at a time.

### Reading an entire file

We have the following text file (pi_digits.txt):

```
3.1415926535
  8979323846
  2643383279
```

Here's the program that opens this file, reads it, and prints the contents of the file to the screen:

file_reader.py
```python
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
```

The `open()` function opens the file to access it. It needs one argument: the name of the file you want to open.
Python looks for this file in the directory where the program that's currently being executed is stored.

The `open()` function returns an object representing the file.
Python stores this object in `file_object`.

The keyword `with` closes the file once access to it is no longer needed.
You could also use `close()`.

Once we have a file object representing the file, we use the `read()` method to read the entire contents of the file.
The `read()` method returns an empty string when it reaches the end of the file.

### File Paths

When you pass a simple file name like `pi_digits.txt` to the `open()` function, Python looks in the directory where the file that's currently being executed is stored.

To get Python to open files from a directory other than the one where your program file is stored, you need to provide a file path.

```python
with open('text_files/filename.txt') as file_object:
```

In Windows systems you use a backslash (`\`) instead of a forward slash (`/`) in the file path.

You can also tell Python exactly where the file is on your computer. This is called absolute file path.

```python
file_path = '/home/higashi/other_files/text_files/filename.txt'
with open(file_path) as file_object:
```

### Reading line by line

You can use a `for` loop on the file object to examine each line from a file one at a time:

```python
file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    for line in file_object:
        # rstrip removes the new line from the file.
        print(line.rstrip())
```

To examine the file's contents, we work through each line in the file by looping over the file object.

### Making a list of lines from a file

When you use `with`, the file object returned by `open()` is only available inside the `with` block that contains it.
If you want to retain access to a file's contents outside the `with` block, you can store the file's lines in a list inside the block and then work with that list.

```python
file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    # stores lines from file in lines
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
```

The `readlines()` method takes each line from the file and stores it in a list.

### Working with a file's contents

```python
file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))
```

output:
```
3.1415926535  8979323846  2643383279
36
```

To avoid these spaces, replace `rstrip()` with `strip()`

```python
pi_string += line.strip()
```

When Python reads from a text file, it interprets all text in the file as a string.
If you read in a number and want to work with that value in a numerical context, you'll have to convert it to an integer using the `int()` function or convert it to a float usign the `float()` function.

### Is your birthday contained in pi?

```python
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
```

You can use `replace()` method to replace any word in a string with a different word.

```python
>>> message = "I really like dogs."
>>> message.replace('dog', 'cat')
> 'I really like cats.'
```

## Write to a file

### Writing to an empty file

To write text to a file, you need to call `open()` with a second argument telling Python that you want to write to the file.

```python
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write('I love programming.')
```

You can open a file in:

* `r` => read mode
* `w` => write mode
* `a` => append mode
* `r+` => read and write mode

If you omit the mode argument, Python opens the file read-only mode by default.

The `open()` function automatically creates the file you’re writing to if it doesn’t already exist.
However, be careful opening a file in write mode (`'w'`) because if the file does exist, Python will erase the file before returning the file object.

Python can only write strings to a text file. If you want to store numerical data in a text file, you'll have to convert the data to string format first using the `str()` function.

### Writing multiple lines

The `write()` function doesn't add any newlines to the text you write.
So if you write more than one line without including newline characters, your file may not look the way you want it to:

```python
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write('I love programming.')
    file_object.write('I love creating new games.')
```

Writes:

```
I love programming.I love creating new games.
```

Including newlines in your `write()` statements makes each string appear on its own line:

```python
file_object.write("I love programming.\n")
file_object.write("I love creating new games.\n")
```

### Append to a file

If you want to add content to a file instead of writing over existing content, you can open the file in append mode.
When you open a file in append mode, Python doesn't erase the file before returning the file object.
Any lines you write to the file will be added at the end of the file.
If the file doesn't exist yet, Python will create an empty file for you.

```python
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
```

## Exceptions

Exceptions are handled with `try-except` blocks.

### Handle the ZeroDivisionError Exception

division.py
```python
print(5/0)
```

This fires an exception.

```
Traceback (most recent call last):
  File "division.py", line 1, in <module>
    print(5/0)
ZeroDivisionError: integer division or modulo by zero
```

### Using `try-except` blocks

```python
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

Output:

```
You can't divide by zero!
```

If more code followed the `try-except` block, the program would continue running because we told Python how to handle the error.
Let’s look at an example where catching an error can allow a program to continue running.

### Using Exceptions to prevent crashes

Handling error correctly is specially important when the program has more work to do after the error occurs.

```python
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break

    second_number = input("Second number: ")
    if second_number == 'q':
        break

    answer = int(first_number) / int(second_number)
    print(answer)
```

If the user inputs a division by 0, the program will crash.

### The else block

The `try-except-else` block works like this: Python attempts to run the code in the `try` statement.
The only code that should go in a `try` statement is code that might cause an exception to be raised.
Sometimes you’ll have additional code that should run only if the `try` block was successful; this code goes in the `else` block.
The `except` block tells Python what to do in case a certain exception arises when it tries to run the code in the `try` statement.

```python
try:
  answer = int(first_number) / int(second_number)
except ZeroDivisionError:
  print("You can't divide by zero!")
else:
  print(answer)
```

By anticipating likely sources of errors, you can write robust programs that continue to run even when they encounter invalid data and missing resources. Your code will be resistant to innocent user mistakes and malicious attacks.

### Handling the FileNotFoundError Exception

One common issue when working with files is handling missing files.

```python
filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")
```

### Failing silently

To make a program fail silently, you write a `try` block as usual, but you explicitly tell Python to do nothing in the `except` block. Python has a `pass` statement that tells it to do nothing in a block.

```python
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        --snip--
    except FileNotFoundError:
        pass
    else:
        --snip--

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
```

The `pass` statement also acts as a placeholder. It's a reminder that you're choosing to do nothing at a specific point in your program's execution and that you might want to do something there later.

## Storing data

The `json` module allows you to dump simple Python data structures into a file and load the data from that file the next time the program runs.
You can also use `json` to share data between different Python programs.

### Using `json.dump()` and `json.load()`

Let's write a short program that stores a set of numbers and another program that reads these numbers back into memory.

The `json.dum()` function takes two arguments: a piece of data to store and a file object it can use to store the data.

number_writer.py
```python
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
```

Now we'll write a program that uses `json.load()`:

number_reader.py
```python
import json

filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)
```

The full code (works with Python3)

```python
import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()
```

[<< Back](README.md)
