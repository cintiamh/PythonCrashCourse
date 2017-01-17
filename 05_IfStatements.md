[<< Back](README.md)

# If Statements

## A simple example

Print just 'bmw' with all capital letters:

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
```

## Conditional Tests

Python uses the values `True` and `False` to decide whether the code in an `if` statement should be executed.

### Checking for Equality (`==`)

```python
>>> car = 'bmw'
>>> car == 'bmw'
True

>>> car = 'audi'
>>> car == 'bmw'
False
```

### Ignoring case when checking for equality

Testing for equality is case sensitive in Python.

If case doesn't matter, you can convert the variable's value to lowercase before doing the comparison:

```python
>>> car = 'Audi'
>>> car.lower() == 'audi'
True
>>> car
'Audi'
```

### Checking for Inequality (`!=`)

```python
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print('Hold the anchovies!')
```

### Numerical Comparisons (`<, <=, >, >=`)

```python
>>> age = 18
>>> age == 18
> True
>>> age != 42
> True
>>> age < 21
> True
>>> age <= 21
> True
>>> age > 21
> False
>>> age >= 21
> False
```

### Checking multiple conditions (`and` and `or`)

#### Using `and` to check multiple conditions

To check whether two conditions are both `True` simultaneously, use the keyword `and` to combine the two conditional tests. If either test fails or if both tests fail, the expression evaluates to `False`.

```python
>>> age_0 = 22
>>> age_1 = 18
>>> age_0 >= 21 and age_1 >= 21
> False
>>> age_1 = 22
>>> age_0 >= 21 and age_1 >= 21
> True
```

To improve readability, you can use parentheses around the individual tests, but they are not required.

```python
(age_0 >= 21) and (age_1 >= 21)
```

#### Using `or` to check multiple conditions

The keyword `or` allows you to check multiple conditions as well, but it passes when either or both of the individual tests pass.

```python
>>> age_0 = 22
>>> age_1 = 18
>>> age_0 >= 21 or age_1 >= 21
> True
>>> age_0 = 18
>>> age_0 >= 21 or age_1 >= 21
> False
```

### Checking whether a value is in a list (`in`)

To find out whether a particular value is already in a list, use the keyword `in`.

```python
>>> requested_toppings = ['mushrooms', 'onions', 'pineapple']
>>> 'mushrooms' in requested_toppings
True
>>> 'pepperoni' in requested_toppings
False
```

### Checking whether a valid is not in a list (`not in`)

```python
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
```

### Boolean Expressions

A Boolean Expression is just another name for a conditional test. A Boolean value is either `True` or `False`, just like the value of a conditional expression after it has been evaluated.

```python
game_active = True
can_edit = False
```

## `if` Statements

### Simple `if` statements

```python
if conditional_test:
    do something
```

All indented lines after an `if` statement will be executed if the test passes, and the entire block of indented lines will be ignored if the test does not pass.

### `if-else` Statements

Often, you'll want to take one action when a conditional test passes and a different action in all other cases. The `else` statement allows you to define an action or set of actions that are executed when the conditional test fails.

```python
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
```

### The `if-elif-else` Chain

Often, you'll need to test more than two possible situations. Python executes only one block in a `if-elif-else` chain.

```python
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
```

### Using multiple elif Blocks

You can use as many `elif` blocks in your code as you like.

```python
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
elif age < 65:
    print("Your admission cost is $10.")
else:
    print("Your admission cost is $5.")
```

### Omitting the `else` block

Python does not require an `else` block at the end of an `if-elif` chain.

The `else` block is a catchall statement. If you have a specific final condition you are testing for, consider using a final `elif` block and omit the `else` block. As a result, you'll gain extra confidence that your code will run only under the correct conditions.

### Testing multiple conditions

Sometimes it's important to check all of the conditions of interest. In this case, you should use a series of simple `if` statements with no `elif` or `else` blocks.

```python
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")
```

## Using `if` statements with Lists

### Checking for special items

```python
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")
```

### Checking that a list is not empty

```python
requested_toppings = []
# Python returns True only if there is at least one element in the list
# Empty lists return False
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
```

### Using multiple lists

```python
available_toppings = ['mushrooms', 'olives', 'green peppers',
                         'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")
```

[<< Back](README.md)
