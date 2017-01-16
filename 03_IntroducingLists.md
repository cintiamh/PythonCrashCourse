[<< Back](README.md)

# Introducing Lists

## What is a list?

A list is a collection of items in a particular order.

In Python, square brackets `[]` indicate a list, and individual elements in the list are separated by commas.

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
```

### Index positions starts at 0

By asking for the index `-1`, Python always returns the last item in the list.

```python
print(bicycles[-1])
```

This convention exteds to other negative index values as well. The index `-2` returns the second item from the end of the list, the index `-3` returns the third item from the end, and so forth.

### Modifying elements in a list

To change an element, use the name of the list followed by the index of the element you want to change, and then provide the new value you want that item to have.

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)
```

### Adding elements to a List

#### Appending elements to the end of a list

You can use `append()` method to add a new element to the end of a List.

```python
motorcycles.append('ducati')
print(motorcycles)
```

It's a common practice to start with an empty List `[]` and then just keep using `append()` to add elements to the list.

#### Inserting elements into a List

You can add a new element at any position in your list by using the `insert()` method. You do this by specifying the index of the new element and the value of the new item.

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
```

### Removing element from a List

#### Removing an item using the `del` statement

If you know the position of the item you want to remove from a list, you can use the `del` statement.

```python
del motorcycles[0]
print(motorcycles)
```

In this example, you can no longer access the value that was removed from the list after the `del` statement is used.

#### Removing an item using the `pop()` method

The `pop()` method removes the last item in a list, but it lets you work with that item after removing it.

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
# ['honda', 'yamaha']
# suzuki
```

#### Popping items from any position in a List

You can actually use `pop()` to remove an item in a list at any position by including the index of the item you want to remove in parentheses.

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')
# The first motorcycle I owned was a Honda.
```

#### Removing an item by value

If you only know the value of the item you want to remove, you can use the `remove()` method.

```python
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print('\nA ' + too_expensive.title() + " is too expensive for me.")
# ['honda', 'yamaha', 'suzuki']
#
# ADucati is too expensive for me.
```

#### Sorting a List permanently with the `sort()` method

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
# ['audi', 'bmw', 'subaru', 'toyota']
```

The `sort()` method changes the order of the list permanently.

You can also sort this list in reverse alphabetical order by passing the argument `reverse=True`.

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
# ['toyota', 'subaru', 'bmw', 'audi']
```

#### Sorting a List temporarily with the `sorted()` function

The `sorted()` function lets you display your list in a particular order but doesn't affect the actual order of the list.

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))
```

The `sorted()` function can also accept a `reverse=True` argument if you want to display a list in reverse alphabetical order.

#### Printing a List in Reverse order

To reverse the original order of a list, you can use the `reverse()` method.

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)
# ['subaru', 'toyota', 'audi', 'bmw']
```

Notice that `reverse()` doesn't sort backward alphabetically; it simply reverses the order of the list.

The `reverse()` method changes the order of a list permanently, but you can revert to the original order anytime by applying `reverse()` to the same list a second time.

#### Finding the length of a List

You can quickly find the length of a list by using the `len()` function.

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
# 4
```

[<< Back](README.md)
