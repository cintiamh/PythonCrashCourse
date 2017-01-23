# Start with some designs that need to be printed.
unprinted_desings = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing
while unprinted_desings:
    current_design = unprinted_desings.pop()
    # Simulate creating a 3D print from the design
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# Display all completed models
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

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
