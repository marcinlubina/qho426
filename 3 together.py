print("Welcome to the Adventure Game!")

#choose your path
print("You find yourself at a crossroads. Which path will you choose?")
print("1. The dark forest")
print("2. The mysterious cave")
path_choice = input("Enter the number of your choice (1/2): ")

if path_choice == "1":
    print("You venture into the dark forest.")

    # Ask the user to make another choice in the forest
    print("In the forest, you encounter a river. What will you do?")
    print("1. Attempt to swim across")
    print("2. Look for a bridge")
    river_choice = input("Enter the number of your choice (1/2): ")

    if river_choice == "1":
        print("You tried to swim but got caught in a strong current. Game over!")
    elif river_choice == "2":
        print("You found a hidden bridge and safely crossed the river. Well done!")
    else:
        print("Invalid choice. Game over!")

elif path_choice == "2":
    print("You enter the mysterious cave.")

    # Ask the user to make another choice in the cave
    print("Inside the cave, you see two tunnels. Which one will you choose?")
    print("1. The left tunnel")
    print("2. The right tunnel")
    tunnel_choice = input("Enter the number of your choice (1/2): ")

    if tunnel_choice == "1":
        print("You chose the left tunnel and discovered a treasure chest. Congratulations!")
    elif tunnel_choice == "2":
        print("You entered the right tunnel but encountered a dead-end. Game over!")
    else:
        print("Invalid choice. Game over!")

else:
    print("Invalid choice. Game over!")

print("Thanks for playing!")
