[<< Back](README.md)

# User Input and While Loops

## How the `input()` function works

The `input()` function pauses your program and waits for the user to enter some text. Once Python receives the user's input, it stores it in a variable to make it convenient for you to work with.

```python
message = raw_input("Tell me something, and I will repeat it back to you: ")
print(message)
```

The `input()` function takes one argument: the prompt.

### Writing clear prompts

Each time you use the `input()` function, you should include a clear, easy-to-follow prompt that tells the user exactly what kind of information you're looking for.

```python
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = raw_input(prompt)
print("\nHello, " + name + "!")
```

### Using `int()` to accept numerical input

When you use the `input()` function, Python interprets everything the user enters as a string.

We can use the `int()` function that converts a string representation of a number to a numerical representation.

```python
>>> age = input("How old are you? ")
> How old are you? 21
>>> age = int(age)
>>> age >= 18
> True
```

When you use numerical input to do calculations and comparisons, be sure to convert the input value to a numerical representation first.

### The modulo operator

The modulo operator (`%`) divides the number by another number and returns the remainder.

```python
>>> 4 % 3
> 1
>>> 5 % 3
> 2
>>> 6 % 3
> 0
>>> 7 % 3
> 1
```

### Accepting input in Python 2.7

If you are using Python 2.7, you should use the `raw_input()` function when propting for user input.

Python 2.7 has an `input()` function as well, but this function interprets the user's input as Python code and attempts to run the input.

## Introducing while loops

The `while` loop runs as long as, or while, a certain condition is true.

### The while loop in action

```python
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
```

Python repeats the loop as long as the condition `current_number <= 5` is true.

### Letting the user choose when to quit

In the following program, it will keep running as long as the user has not entered the 'quit' value.

```python
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != "quit":
    message = raw_input(prompt)
    print(message)
```

### Using a flag

For a program that should run only as long as many conditions are true, you can define one variable (flag) that determines whether or not the entire program is active.

```python
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = raw_input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
```

### Using `break` to exit a loop

To exit a `while` loop immediately without running any remaining code in the loop, regardless of the results of any conditional test, use the `break` statement. The `break` statement directs the flow of your program.

```python
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
```

### Using `continue` in a loop

You can use the `continue` statement to return to the beginning of the loop based on the result of a conditional test.

```python
# Print only odd numbers
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)
```

### Avoiding infinite Loops

Every `while` loop needs a way to stop running so it won't continue to run forever.

To avoid writing infinite loops, test every `while` loop and make sure the loop stops when you expect it to.

To end an infinite loop, press CTRL-C or close the window displaying the output.

## Using a while loop with lists and Dictionaries

A `for` loop is effective for looping through a list, but you shouldn't modify a list inside a `for` loop because Python will have trouble keeping track of the items in the list. To modify a list as you work through it, use a `while` loop. Using `while` loops with lists and dictionaries allows you to collect, store, and organize lots of input to examine and report on later.

### Moving items from one list to another

```python
# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
```

### Removing all instances of specific values from a list

What if you want to remove all instances of a value from a list?

You can run a `while` loop until a value is not longer in the list.

```python
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print pets

while 'cat' in pets:
  pets.remove('cat')

print pets
```

[<< Back](README.md)
