num = 19  

for i in range(1, 11):

    answer = int(input(f"What is {i} x {num}? "))

    correct = i * num

    if answer == correct:

        print("Correct")

    else:

        print(f"No, the answer is {correct}")

print("Finished")

# # Complete the code below to display multiplication table of your choice
# num1 =any int(input("Enter any number for multplication: "))
# for i in range(1,11):
# #"block of code is missing here"
#     result = num1 * i
# print(f"{num1} x {i} = {result}")


