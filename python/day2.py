

""">more than  
<= less than or equal to  
>=greater than or equal to  
!= not equal to """

# selection is used to control the flow of the program
# Comparison using if statements
score = 25
userNum = int(input("Enter a user number:"))

if score > userNum:
    print("Score is greater than userNum")

# Using >= operator
score = 25
userNum = int(input("Enter a user number:"))

if score >= userNum:
    print("The score is greater than or equal to the user's number.")
else:
    print("The score is less than the user's number.")

# Correcting variable names
num1 = int(input('Enter Your first value:'))
num2 = int(input('Enter Your second value:'))

if num1 > num2:
    print(f"{num2} is the lowest value")
else:
    print(f"{num1} is the lowest value")



# First part of the code
cardValue = "King"
suitOfCards = "Hearts"

chkCardValue = input("Enter card value: ").title()
chkCardSuit = input("Enter card suit: ").title()

# Add the condition using the "and" operator to check card value & suit against user inputs
if chkCardValue == cardValue and chkCardSuit == suitOfCards:
    print("Winner!")
else:
    print("Try Again")

# Second part of the code
cardValue = "King"
suitOfCards = "Hearts"

chkCardValue = input("Enter card value: ").title()
chkCardSuit = input("Enter card suit: ").title()

# Add the condition to use the "and" operator to check card value & suit against predefined values
if chkCardValue == cardValue and chkCardSuit == suitOfCards:
    print("Winner!")
else:
    print("Try Again")

my_list = ['python', 'javascript', 'html', 'css']

user_number = input("Enter a user value to be found:")

if user_number in my_list:
    print('You found it!')
else:
    print("It is not in the list")



# Create a Menu program that allows user to select between three subject choices

# User must be presented with the value assoiciated with each choice

# for example 1. Music, 2. Maths ....

# A choice must also be available for the user to exit the program

# A message using the print function must be display as per the user choice

while True:
    # Display menu options
    print("Select a subject:")
    print("1. Music")
    print("2. Maths")
    print("3. Science")
    print("4. Exit")

    # Get user input
    choice = input("Enter your choice (1-4): ")

    # Check user choice and display corresponding message
    if choice == '1':
        print("You selected Music. Enjoy the Guitar super start!")
    elif choice == '2':
        print("You selected Maths. Get ready to solve some problems!")
    elif choice == '3':
        print("You selected Science. Explore the wonders of the world!")
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break  # Exit the loop if the user chooses to exit
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")


