def describe_pet(animal_type, pet_name):
    """Display information about pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet(pet_name = 'penny', animal_type = 'dog')

def describe_pet(pet_name, animal_type = 'dog'):
    """Display information about pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('penny');
describe_pet('meow', 'cat');
