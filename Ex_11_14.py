# print("how old are you?:", end=" ")
# age = int(input())

# age = int(input("how old are you?:"))

# print(f"You are {age} old")

from sys import argv
#unpacking
_, name, last_name, age = argv
# print(_)
print(f"Name: {name} {last_name}, \nAge: {age}")

city = input("City:")
print(f"City: {city}")