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


[<< Back](README.md)
