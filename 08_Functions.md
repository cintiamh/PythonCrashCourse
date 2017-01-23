[<< Back](README.md)

# Functions

## Defining a function

The simplest structure of a function looks like this:

```python
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()
```

We use the keyword `def` to inform Python that we're defining a function.
This is the function definition, which tells Python the name of the function, and if applicable, what kind of information the function needs to do its job (inside the parenthesis).
The parentheses are required. Finally, the definition ends in a colon.

`Docstring` is a type of comment that describes what the function does. `Docstrings` are enclosed in triple quotes, which Python looks for when it generates documentation for the functions in your programs.

### Passing information to a function

```python
def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")

greet_user('jesse')
# Hello, Jesse!
```

### Arguments and Parameters

A parameter is a piece of information the function needs to do its job. In the case above, the variable `username`.

An argument is a piece of information that is passed from a function call to a function. In the case above, the name we passed in when calling `greet_user`, `jesse`.

## Passing Arguments

### Positional arguments

When you call a function, Python must match each argument in the function call with a parameter in the function definition.

Positional arguments is when we match those based on the order of the arguments provided.

In this case the order of the arguments matter.

```python
def describe_pet(animal_type, pet_name):
    """Display information about pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
# I have a hamster.
# My hamster's name is Harry.
```

### Keyword arguments

A keyword argument is a name-value pair that you pass to a function. You directly associate the name and the value within the argument, so when you pass the argument to the function, there's no confusion.

In this case the order of the arguments doesn't matter.

```python
describe_pet(pet_name = 'penny', animal_type = 'dog')
# I have a dog.
# My dog's name is Penny.
```

Note that in this example the `describe_pet()` method itself didn't change, but even though the arguments order is not right, Python knows what assign to the right parameter.

### Default values

You can set default values for the arguments to make some of the function calls simpler.

```python
def describe_pet(pet_name, animal_type = 'dog'):
    """Display information about pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# Now you can call the same function just with the pets name, if you have a dog.
describe_pet('penny');
describe_pet('meow', 'cat');
```

When you use default values, the parameters with default values are listed after all parameters that don't have any default values.

## Return values

The `return` statement takes a value from inside a function and sends it back to the line that called the function.

### Returning a simple value

```python
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
# Jimi Hendrix
```

When you call a function that returns a value, you need to provide a variable where the return value can be stored.

### Making an argument optional

You can use default values to make an argument optional.

```python
def get_formatted_name(first_name, last_name, middle_name = ''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else :
        full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
```

Optional values allow functions to handle a wide range of use cases while letting function calls remain simple as possible.

### Returning a dictionary

A function can return any kind of value you need it to, including lists and dictionaries.

```python
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)
# {'last': 'hendrix', 'first': 'jimi'}
```

## Passing a list

When you pass a list to a function, the function gets direct access to the contents of the list.

```python
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
```

### Modifying a list in a function

When you pass a list to a function, the function can modify the list. Any changes made to the list inside function's body are permanent.

```python
def print_models(unprinted_desings, completed_models):
    """Simulate printing each design, until none are left.
    Move each design to completed_models after printing."""
    while unprinted_desings:
        current_design = unprinted_desings.pop()

        # Simulate creating a 3D print from the design
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_desings = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_desings, completed_models)
show_completed_models(completed_models)
```

#### Preventing a function from modifying a list

Sometimes you won't want to change the list when going through a function, in this case, you can pass in a copy of the list to the function.

```python
def function_name(list_name[:]):
```

Even though you can preserve the contents of a list by passing a copy of it to your functions, you should pass the original list to functions unless you have a specific reason to pass a copy.

## Passing an arbitrary number of arguments

Python allows a function to collect an arbitrary number of arguments from the calling statement.

```python
def make_pizza(*toppings):
    """Print the list of toppings that have been requested"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
# ('pepperoni',)
# ('mushrooms', 'green peppers', 'extra cheese')
```

The asterisk in the parameter name `*toppings` tells Python to make an empty tuple called `toppings` and pack whatever values it receives into this. tuple.

### Mixing positional and arbitrary arguments

If you want a function to accept several different kind of arguments, the parameter that accepts an arbitrary number of arguments must be placed last in the function definition.

```python
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

## Storing your functions in modules

You can store your functions in a separated file called module and then importing that module into your main program. An `import` statement tells Python to make the code in a module available in the currently running program file.

### Importing an entire module

A `module` is a file ending in `.py` that contains the code you want to import into your program.

pizza.py
```python
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
```

Now we make a separated file called `making_pizzas.py` with the following content:

```python
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

This first approach to importing, in which you simply write `import` followed by the module's name, makes every function from the module available in your program.

### Importing specific functions

You can also import a specific function from a module.

```python
from module_name import function_name
```

You can import as many functions as you want from a module by separating each function's name with a comma:

```python
from module_name import function_0, function_1, function2
```

```python
from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

### Using `as` to give a function an alias

If the name of a function you're importing might conflict with an existing name in your program or if the function name is long, you can use an unique alias.

```python
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
```

### Using `as` to give a module an alias

You can also provide an alias for a module name.

```python
import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

### Importing all functions in a module

You can tell Python to import every function in a module by using the asterisk `*` operator:

```python
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

Because every function is imported, you can call each function by name without using the dot notation.

Python may see several functions or variables with the same name, and instead of importing all the functions separately, it will overwrite functions.

The best approach is to import the function or functions you want, or import the entire module and use the dot notation.

[<< Back](README.md)
