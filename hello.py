print("We need to get some basic information from you.")

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age < 21:
    print("Sorry, you're too young to visit this site.")
else:
    print(f"Welcome {name}, thanks for visiting!")