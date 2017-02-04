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

[<< Back](README.md)
