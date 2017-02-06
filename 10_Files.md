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

[<< Back](README.md)
