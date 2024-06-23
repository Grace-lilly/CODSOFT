import string
import random

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                print("Please enter a positive number.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        password = generate_password(length)
        print(f"Generated password: {password}")

        another = input("Do you want to generate another password? (yes/no): ")
        if another.lower() != 'yes':
            print("Thank you for using the Password Generator. Goodbye!")
            break

if __name__ == "__main__":
    main()
