[<< Back](README.md)

# Dictionaries

Dictionaries can store an almost limitless amount of information.

## A Simple Dictionary

```python
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])
```

## Working with dictionaries

A dictionary in Python is a collection of key-value pairs. In Python, a dictionary is wrapped in braces, `{}`.

### Accessing values in a dictionary

To get the value associated with a key, give the name of the dictionary and then place the key inside a set of square brackets:

```python
print(alien_0['color'])
```

### Adding new key-value pairs

Dictionaries are dynamic structures, and you can add new key-value pairs to a dictionary at any time.

```python
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)
# {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
```

Python doesn't care about the order in which you store each key-value pair, it cares only about the connection between each key and its value.

### Starting with an empty dictionary

Typically, you'll use empty dictionaries when storing user-supplied data in a dictionary or when you write code that generate a large number of key-value pairs automatically.

```python
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
# {'color': 'green', 'points': 5}
```

### Modifying values in a dictionary

To modify a value in a dictionary, give the name of the dictionary with the key in square brackets and then the new value you want associated with that key.

```python
alien_0['color'] = 'yellow'
```

A more interesting example:

```python
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

# Original x-position: 0
# New x-position: 2
```

### Removing key-value pairs

You can use the `del` statement to completely remove a key-value pair. All `del` needs is the name of the dictionary and the key that you want to remove.

```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)
# {'color': 'green', 'points': 5}
# {'color': 'green'}
```

## Looping through a dictionary

### Looping through all key-value pairs

You can loop through the dictionary using a `for` loop:

```python
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}
for key, value in user_0.items():
    print("Key: " + key)
    print("Value: " + value)
```

To write a `for` loop for a dictionary, you create names for the two variables that will hold the key and value in each key-value pair. You can choose any names you want for these two variables.

The method `items()` returns a list of key-value pairs. The `for` loop then stores each of these pairs in the two variables provided.

### Looping through all the keys in a dictionary

The `keys()` method is useful when you don't need to work with all of the values in a dictionary.

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
for name in favorite_languages.keys():
    print(name.title())
```

Looping through the keys is actually the default behavior when looping through a dictionary, so this code would have the same output as:

```python
for name in favorite_languages:
```

The `keys()` method actually returns a list of all keys.

```python
if 'erin' not in favorite_languages.keys():
    print('Erin, please take our poll!')
```

### Looping through a dictionary's keys in order

The dictionary doesn't return its items in order. One way to return items in a certain order is to sort the keys as they're returned in the `for` loop. You can use the `sorted()` function to get a copy of the keys in order:

```python
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")
```

### Looping through all values in a dictionary

You can use `values()` method to return a list of values without any keys.

```python
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
```

This approach pulls all the values from the dictionary without checking for repeats.

To see each language chosen without repetition, we can use a `set`. A `set` is similar to a list except that each item in the `set` must be unique:

```python
for language in set(favorite_languages.values()):
    print(language.title())
```

When you wrap `set()` around a list that contains duplicate items, Python identifies the unique items in the list and builds a set from the items.

## Nesting

You can nest a set of dictionaries inside a list, a list of items inside a dictionary, or a dictionary inside another dictionary.

### A list of dictionaries

We can make a list of aliens in which each alien is a dictionary of information about that alien.

```python
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
```

In a more realistic example, we can dynamically generate a fleet of aliens, using `range()`.

```python
aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print('...')

# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))
```

These aliens all have the same characteristics, but Python considers each one a separated object, which allows us to modify each alien individually.

All of the dictionaries in the list should have an identical structure so you can loop through the list and work with each dictionary object in the same way.

### A list in a dictionary

```python
# Store information about a pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}
# Summarize the order
print("You ordered a " + pizza['crust'] + "-crust pizza " +
    "with the following toppings:"
)
for topping in pizza['toppings']:
    print("\t" + topping)
```

### A dictionary in a dictionary

You can nest a dictionary inside another dictionary, but your code can get complicated quickly when you do.

```python
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
```

[<< Back](README.md)
