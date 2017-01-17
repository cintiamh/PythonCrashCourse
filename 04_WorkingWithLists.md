[<< Back](README.md)

# Working with Lists

## Looping through an entire List

Let's use a `for` loop to print out each name in a list of magicians.

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
```

### A closer look at looping

The set of steps is repeated once for each item in the list, no matter how many items are in the list.

### Doing more work within a for loop

You can write as many lines of code as you like in the `for` loop. Every indented line following the line `for magician in magicians` is considered inside the loop.

```python
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
```

### Doing something after a for loop

Any lines of code after the `for` loop that are not indented are executed once without repetition.

```python
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show!")
```

## Avoiding Indentation Errors

Python uses indentation to determine when one line of code is connected to the line above it.

Some common errors are:

* Forgetting to indent
* Forgetting to indent additional lines - logical error
* Indenting unnecessarily
* Indenting unnecessarily after the loop - logical error
* Forgetting the colon

## Making Numerical Lists

### Using the `range()` function

Python's `range()` function makes it easy to generate a series of numbers.

```python
for value in range(1, 5):
    print(value)
# 1
# 2
# 3
# 4
```

This code doesn't print the number `5`. The `range()` function causes Python to start counting at the first value you give it, and it stops when it reaches the second value you provide.

### Using `range()` to make a list of numbers

If you want to make a list of numbers, you can convert the results of `range()` directly into a list using the `list()` function.

```python
numbers = list(range(1, 6))
print(numbers)
# [1, 2, 3, 4, 5]
```

We can also use the `range()` function to tell Python to skip numbers in a given range.

```python
even_numbers = list(range(2, 11, 2))
print(even_numbers)
# [2, 4, 6, 8, 10]
```

In this example, the `range()` function starts with the value 2 then adds 2 until it reaches or passes the end value 11.

### Simple statistics with a list of numbers

A few Python functions are specific to lists of numbers:

* `min(list)` - finds the minimum of a list of numbers
* `max(list)` - finds the maximum of a list of numbers
* `sum(list)` - calculates the sum of a list of numbers

### List comprehensions

A list comprehension combines the `for` loop and the creation of new elements into one line, and automatically appends each new element.

```python
squares = [value**2 for value in range(1,11)]
print(squares)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

Inside the square brackets define the expression for the values you want to store in the new list (`value**2`). Then write a `for` loop to generate the numbers you want to feed into the expression (`for value in range(1,11)`), and close the square brackets. Notice that no colon is used at the end of the `for` statement.

## Working with part of a list

### Slicing a List

To make a slice, you specify the index of the first and last elements you want to work with.

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
# ['charles', 'martina', 'michael']
```

If you omit the first index in a lice, Python automatically starts you slice at the beginning of the list:

```python
print(players[:4])
# ['charles', 'martina', 'michael', 'florence']
```

A similar syntax works if you want a slice that includes the end of a list.

```python
print(players[2:])
# ['michael', 'florence', 'eli']
```

You can also use the negative index as in:

```python
print(players[-2:])
# ['florence', 'eli']
```

### Looping through a slice

```python
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
# Here are the first three players on my team:
# Charles
# Martina
# Michael
```

### Copying a List

To copy a list, you can make a slice that includes the entire original list by omitting the first and second indexes (`[:]`). This tells Python to make a slice that starts at the first item and ends with the last item, producing a copy of the entire list.

```python
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')

print('My favorite foods are:')
print(my_foods)
print('My friends favorite foods are:')
print(friend_foods)
# My favorite foods are:
# ['pizza', 'falafel', 'carrot cake', 'cannoli']
# My friends favorite foods are:
# ['pizza', 'falafel', 'carrot cake', 'ice cream']
```

## Tuples

Tuples are immutable lists.

### Defining a Tuple

A tuple looks just like a list except you use parentheses instead of square brackets. Once you define a tuple, you can access individual elements by using each item's index, just as you would for a list.

```python
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# 200
# 50
```

If we try to assign a new value to `dimensions[0]`, for example, Python would throw and error.

### Writing over a Tuple

Although you can't modify a tuple, you can assign a new value to a variable that holds a tuple.

```python
dimensions = (200, 50)
print('Original dimensions:')
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print('\nModified dimensions:')
for dimension in dimensions:
    print(dimension)
# Original dimensions:
# 200
# 50

# Modified dimensions:
# 400
# 100
```

[<< Back](README.md)
