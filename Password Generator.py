import random
import string

def generate_password(password_length):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(password_length))
    return password

def main():
    print("Welcome to the Password Generator!")
    while True:
        try:
            password_length = int(input("Enter the desired length for the password: "))
            if password_length <= 0:
                print("Please enter a positive integer.")
                continue
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue
        
        password = generate_password(password_length)
        print(f"Generated password: {password}")

        other = input("Do you want to generate another password? (yes/no): ").lower()
        if other != 'yes':
            break
    
    print("Thank you for using the Password Generator!")

if __name__ == "__main__":
    main()
