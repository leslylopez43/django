NAME = "ADD YOUR FULL NAME HERE (LESLY)"
DATE = "ADD THE DATE HERE (e.g. 1/1/2020)"

print(NAME)

# Fixing the if and elif statements
condition = True  # Change this condition to what you need

if condition:
    print("IF STATEMENTS")
    print(DATE)
elif condition:  # Change this condition to what you need
    print("ELIF STATEMENTS")

# Fixing the while loop
# fro aChar in name:   
# if aChar == findchar:

name = "Abdul Malik"  # Add your name in between the speech marks 
findChar = input("Enter a character to search for: ")

"Method 1"

for aChar in name:  # loop and store every element inside the name variable in the aChar
    # aChar = A/b/d/u/l/ /M/a/l/i/k/
    if aChar == findChar:
        print(findChar)
    else:
        print(f"not found {findChar}")

"Method 1"
# if findChar in name:
#     print(findChar)
# else:
#     print("No character found")

# counter = 0  for aChar in searchStr:

# method   custom built function      list

# "To Do: Task 7: Refactor the code above by putting it into a subroutine and call/invoke it."

# def charCount(): # function definition with a name charCount
    # function body
    # local variables
    # searchStr = "Python is a great programming language"
    # findChar = input("Enter character to search for: ")

    # counter = 0
    # # loop through the entire string to search for the character entered
    # for aChar in searchStr:
    # # check if the character entered is a match with any character in the string
    #     if aChar == findChar:
    #     # increase the count by 1 every time you find the same character
    #         counter = counter + 1
    # print(f"Find the character : {findChar} {counter} times")  # display the result

