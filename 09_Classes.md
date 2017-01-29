[<< Back](README.md)

# Classes

Making an object from a class is called instantiation, and you work with instances of a class.

## Creating and using a class

### Creating the Dog class

```python
class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")
```

By convention, capitalized names refer to classes in Python.
The parentheses in the class definition are empty because we're creating this class from scratch.

#### The `__init__()` method

A function that's part of a class is a method.
Everything you learned about functions applied to methods as well.

The `__init__()` method is a special method Python runs automatically whenever we create a new instance based on the `Dog`class.

The `self` parameter is required in the method definition, and it must come first before the other parameters.
It must be included in the definition because when Python calls this `__init__()` method later automatically passes `self`, which is a reference to the instance itself; it gives the individual instance access to the attributes and methods in the class.

#### Creating classes in Python 2.7

When you create a class in Python 2.7, you need to include the term `object` in parentheses when you create a class:

```python
class ClassName(object):
  """code"""
```

### Making an instance from a class

```python
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
```

The `__init__()` method creates an instance representing this particular dog and sets the `name` and `age` attributes using the values we provided.
The `__init__()` method has no explicit `return` statement, but Python automatically returns an instance representing this dog.

#### Accessing attributes

To access the attributes of an instance, you use dot notation.

```python
my_dog.name
```

#### Calling methods

```python
my_dog.sit()
my_dog.roll_over()
```

To call a method, give the name of the instance and the method you want to call, separated by a dot.

#### Creating multiple instances

You can create as many instances from a class as you need.

## Working with classes and instances

One of the first tasks you'll want to do is modify the attributes associated with a particular instance.
You can modify the attributes of an instance directly or write methods that update attributes in specific way.

### The Car class

```python
class Car(object):
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
```

Outputs: `2016 Audi A4`

To make the class more interesting, let's add an attribute that changes over time.

### Setting a default value for an attribute

Every attribute in a class needs an initial value, even if that value is 0 or an empty string.

[<< Back](README.md)
