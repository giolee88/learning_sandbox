# Two Dictionaries
actress = {"name": "Angelina Jolie", "genre": "Action", "nationality": "United States"}
actor = {"name": "Adam Sandler", "genre": "comedy", "nationality": "United States"}

# Access all the keys
print(actor.keys())
# to make a list out of it
print (list(actor.keys())) 

# Access all values
print(actress.values())

# We can iterate through dictionaries with a for-loop
for key in actress.keys():
    print("This is a key:", key)

# Looping through values
for value in actress.values():
    print("This is a value:", value)

# Use items() to loop through both keys and values
for key, value in actress.items():
    print("This is a key:", key)
    print("This is a value:", value)

# ---------------------------------------------------------------
film = {"title": "Interstellar", "revenues": {"United States":360, "China":250, "United Kingdom":73}}
# Use del to delete a key-value pair from a dictionary
print("this is what it looks like before delete " )
print(film)

# now try delete 
del film["revenues"]
print("this is what it looks like after delete ")
print(film)

# ---------------------------------------------------------------

# Add a key-value pair to a dictionary
print ('this is the actor before adding key-val pair')
print(actor)
print ('this is the actor after adding key-val pair')
actor["hair"] = "brown"
actor["genre"] = "drama"
print(actor)

# adding to a field
actor["genre" ] += " & drama"
print(actor)