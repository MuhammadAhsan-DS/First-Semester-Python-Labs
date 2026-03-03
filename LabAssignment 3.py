                                    # NAME : MUHAMMAD AHSAN
                                    # ID   : SP25-BBD-093

# QUESTION NUMBER 1 :
Animals = ['Sheep','Cow','Buffalow']   # LIST OF ANIMALS
# USE A FOR LOOP 
for animal in Animals:         
    print(f"A {animal} eats grass.")
    print("These animals are all farm residents!")


# QUESTION NUMBER 2 :
Multiples_of_3  = list(range(3, 31, 3))
for value in Multiples_of_3:
    print(value)
Cubes = [a**3 for a in range(1, 11)]
print(Cubes)


# QUESTION NUMBER 3 :
# Step 1: Store the five foods in a tuple
menu = ('Fries', 'Burger', 'Pizza', 'Vegetable rice', 'Biryani')

# Step 2: Use a for loop to print each food the restaurant offers
print("Oiginal Menu:")
for food in menu:
    print(food)

    menu[0] = 'Steak' #Error: 'tuple' object does not support item assignment

# The restaurant changes its menu, replacing two items
menu = ('Steak', 'Shawarma', 'Pasta', 'Fruit Salad', 'Soup')
# Use a for loop to print each of the items on the revised menu
print("\nRevised Menu:")
for food in menu:
    print(food)

# Question Number 4 :
# List of usernames
usernames = ['Admin', 'Ahmad', 'Ali', 'Hassan', 'Burhan']

# Loop through the list of usernames
for username in usernames:
    if username == 'Admin':
        print(f"Hello {username}, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")

#  Question Number 5 :
# List of current usernames 
current_users = ['ahmed', 'sara', 'bilal', 'fatima', 'ali']

# List of new usernames 
new_users = ['Ali', 'ahmed', 'bilal', 'zainab', 'admin']

# Loop through the new_users list to check if each username has been used
for new_user in new_users:
    if new_user.lower() in [user.lower() for user in current_users]:
        print(f"{new_user} has already been used. You need to create a new one.")
    else:
        print(f"{new_user} is available.")


