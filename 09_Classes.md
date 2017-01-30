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

```python
class Car(object):
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statatement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
```

### Modifying attribute values

* You can change the value directly through an instance,
* You can set the value through a method,
* You can increment the value through a method.

#### Modifying an attribute's value directly

```python
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
```

#### Modifying an attribute's value through a method

```python
def update_odometer(self, mileage):
  """Set the odometer reading to the given value"""
  if mileage >= self.odometer_reading:
    self.odometer_reading = mileage
  else:
    print("You can't roll back an odometer!")

my_new_car.update_odometer(23)
my_new_car.read_odometer()
```

In this method we are checking for the value before setting it up.

#### Incrementing an attribute's value through a method

Sometimes you’ll want to increment an attribute’s value by a certain amount rather than set an entirely new value.

```python
class Car():
    --snip--

    def update_odometer(self, mileage):
        --snip--

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
```

## Inheritance

When one class inherits from another, it automatically takes on all the attributes and methods of the first class.
The child class inherits

### The `__init__()` method for a Child Class

The first task Python has when creating an instance from a child class is to assign values to all attributes in the parent class.

```python
class Car(object):
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statatement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of a parent class."""
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
```

In Python 2.7 it's slightly different:

```python
super(ElectricCar, self).__init__(make, model, year)
```

The `super()` function needs two arguments: a reference to the child class and the `self` object. These arguments are necessary to help Python make proper connections between the parent and child classes.

### Defining attributes and methods for the child class

Once you have a child class that inherits from a parent class, you can add any new attributes and methods necessary to differentiate the child class from the parent class.

```python
class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of a parent class.
        Then initialize attributes specific to an electric car.
        """
        super(ElectricCar, self).__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
```

### Overriding methods from the parent class

To override any method from the parent class that doesn't fit the child class, you define a method in the child class with the same name as the method you want to override in the parent class.

Python will disregard the parent class method and only pay attention to the method you define in the child class.

```python
def ElectricCar(Car):
    --snip--

    def fill_gas_tank():
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")
```

### Instances as attributes

You can break your large class into smaller classes that work together.

```python
class Battery(object):
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        super(ElectricCar, self).__init__(make, model, year)
        self.battery = Battery()

my_tesla.battery.describe_battery()
```

This looks like a lot of extra work, but now we can describe the battery in as much detail as we want without cluttering the `ElectricCar` class.

## Importing classes


[<< Back](README.md)
