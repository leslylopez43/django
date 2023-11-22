import logging
import time

# [09:54] Abdul Jalloh

# # D.items() -> a set-like object providing a view on D's items

# dItems = dict1.items()

# print(dItems)



# # D.keys() -> a set-like object providing a view on D's keys

# dKeys = dict1.keys()

# print(dKeys)



# # D.values() -> an object providing a view on D's values

# dVals = dict1.values()

# print(dVals)

# # Loop through the keys ansd/values

# for aKey in dKeys:

#     print(aKey)



# for aVal in dVals:

#     print(aVal)



# for aKey, aVal in dItems:

#     print(f"Key: {aKey} , Value: {aVal}")



# direct = {2: "python" , 3: "html" , 4: "css"}
# print (f"Dictionary 2 {direct2}")   

# direct1.update(dict2)

# create a dictionary with keys but no values

dict1 = {"fName":"", "age":"", "interests":"", "level":""}

# create a dictionary with keys but no values

userDetails1 = {"fName":"", "age":"", "interests":"", "level":""}

print(userDetails1)


userDetails1["fName"] = input("Enter value for fName: ")

userDetails1["age"] = input("Enter value for age: ")

userDetails1["interests"] = input("Enter value for interests: ")

userDetails1["level"] = input("Enter value for level: ")



print(userDetails1)


userDetails1["fName"] = input("Enter value for fName: ")

userDetails1["age"] = input("Enter value for age: ")

userDetails1["interests"] = input("Enter value for interests: ")

userDetails1["level"] = input("Enter value for level: ")



print(userDetails1)


# create a dictionary with  no keys and no values

userDetails2 = {}

print(userDetails2)

dKey1 = input("Enter a key: ")

userDetails2[dKey1] = input(f"Enter the value for key {dKey1}")



dKey2 = input("Enter a key: ")

userDetails2[dKey2] = input(f"Enter the value for key {dKey2}")

print(userDetails2)

userDetails3 = {}

print(userDetails3)

for keyVal in range('numOfKeyValPairs'):

    aKey = input("Enter a key: ")

    aVal = input(f"Enter a value for {aKey}")



    # add all key value pairs to the userDetails3 dictionary

    userDetails3[aKey]=aVal

print(userDetails3)




#create a dictionary 
# dict1 = {"fName":"James Smith", "age":21, "interests":"coding", "gamer":True}


# create a dictionary with keys but no values 
# userDetails1 = {"fName":"", "age":"", "interests":"", "level":""}
# print(userDetails1)

# add values to the respective dictionary keys
# userDetails1["fName"] = "Some name" 
# userDetails1["fName"] = input("Enter value for fName: ")
# userDetails1["age"] = input("Enter value for age: ")
# userDetails1["interests"] = input("Enter value for interests: ")
# userDetails1["level"] = input("Enter value for level: ")
# print(userDetails1)

# create a dictionary with no keys and no values 
# userDetails2 = {}
# print(userDetails2)

# dKey1 = input("Enter a key: ")
# userDetails2[dKey1] = input(f"Enter the value for key {dKey1}")

# dKey2 = input("Enter a key: ")
# userDetails2[dKey2] = input(f"Enter the value for key {dKey2}")
# print(userDetails2)


# userDetails3 = {}
# numOfKeyValPairs = int(input("Enter the number of key value pairs you want to add: "))

# for keyVal in range(numOfKeyValPairs):
#     aKey = input("Enter a key: ")
#     aVal = input(f"Enter a value for {aKey}: ")

#     add all key value pairs to the userDetails3 dictionary
#     userDetails3[aKey]=aVal
# print(userDetails3)
# print(userDetails3)

# Collapse



# has context menu

# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(filename="week10\pt8_Exceptions_CollectionsCodebase\1_Exceptions/file1.log", level=logging.DEBUG

# """"""group exception python""""""