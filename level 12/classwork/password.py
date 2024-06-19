# Define the correct password
correct_password = "nika"

# Initialize user input
user_input = ""

# Loop until the user enters the correct password
while user_input != correct_password:
    # Prompt the user to enter the password
    user_input = input("Enter the password: ")
    
    # Check if the entered password is correct
    if user_input != correct_password:
        print("Password is wrong, please try again.")
    else:
        print("Authorization successful!")