import csv
import random
import string

def generate_password(length=12):
    """Generate a random password of specified length."""
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(characters) for i in range(length))

def create_users(num_users):
    """Create a list of users with unique passwords."""
    return [("user" + str(i + 1), generate_password()) for i in range(num_users)]

def export_to_csv(users, filename="users.csv"):
    """Export user data to a CSV file."""
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Username", "Password"])
        writer.writerows(users)

def main():
    try:
        num_users = int(input("Enter the number of users to create: "))
        users = create_users(num_users)
        export_to_csv(users)
        print(f"Generated {num_users} users and exported to CSV file.")
    except ValueError:
        print("Please enter a valid integer for the number of users.")

if __name__ == "__main__":
    main()
