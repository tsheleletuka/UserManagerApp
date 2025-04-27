import json
import os

# Step 1: Define the file path
file_path = "users.json"

# Step 2: Function to load users from the file
def load_users():
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except:
        # Step 2a: If the file does not exist, start with an empty list
        return []

# Step 3: Function to save users to the file
def save_users(users):
    with open(file_path, "w") as file:
        json.dump(users, file, indent=4)

# Step 4: Function to display all users
def view_users(users):
    if not users:
        print("No users found.")
    else:
        print("\Current Users:")
        # Loop over the list 'users' with an index starting at 1
        for i, user in enumerate(users, start=1):
            # Print the user's position, name, and age in a formatted string
            print(f"{i}.{user['name']} - Age {user['age']}")
    print()     # Step 4a: Add an emply line for better spacing

# Step 5: Function to add a new user
def add_user(users):
    name = input("Enter the new user's name: ")
    age = input("Enter the new user's age: ")

    # Step 5a: Create a new user dictionary
    new_user = {
        "name": name,
        "age" : int(age)
    }

    # Step 5b: Add the new user to the list
    users.append(new_user)

    # Step 5c: Save the updated users list
    save_users(users)

    print(f"User {name} added successfully!\n")

# Step 6: Main program loop
def main():
    # Step 6a: Load existing uers
    users = load_users()

    while True:
        #Step 6b: Display menu options
        print("===== User Manager =====")
        print("1. View all users")
        print("2. Add a new user")
        print("3. Exit")

        # Step 6c: Get user choice
        choice = input("Enter your choice (1/2/3): ")

        # Step 6d: Perform action based on choice
        if choice == "1":
            view_users(users)
        elif choice == "2":
            add_user(users)
        elif choice == "3":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3.\n")

# Step 7: Start the program
if __name__ == "__main__":
    main()


# Step 5: Save the updated list back to the file
with open(file_path, "w") as file:
    json.dump(users, file, indent=4)

print(f"User {name} added successfully!")