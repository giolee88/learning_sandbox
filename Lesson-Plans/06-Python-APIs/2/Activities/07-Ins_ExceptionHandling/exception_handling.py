students = {
    # Name  : Age
    "James": 27,
    "Sarah": 19,
    "Jocelyn": 28
}

student = input("Which student?")

# Try to access key that doesn't exist
try:
    print(students[student])
except KeyError:
    print("Oops, that student doesn't exist.")

# "Catching" the error lets the rest of our code execute
print("...But the program doesn't die early!")
