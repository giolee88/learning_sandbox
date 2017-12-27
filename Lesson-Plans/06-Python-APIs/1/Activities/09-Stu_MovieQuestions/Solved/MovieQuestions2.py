# Dependencies
import requests as req

url = "http://www.omdbapi.com/"

movies = [
	('Aliens', 'Director', 'The director of Aliens was '),
	('Gladiator', 'Rated', 'The rating of Gladiator was '),
	('50 First Dates', 'Year', 'The movie 50 First Dates was released in '),
	('Moana', 'Writer', 'The writer of Moana was '),
	('Sing', 'Plot', 'The plot of Sing was '),
]
# Who was the director of the movie Aliens?
for title, field, text in movies:
	response = req.get(
		url,
		params={'apikey': '40e9cece', 't': title})
	movie = response.json()
	value = movie[field]
	print(text + value + '.')
"""
print("The director of Aliens was " + movie["Director"] + ".")

# What was the movie Gladiator rated?
movie = req.get(url + "Gladiator").json()
print("The rating of Gladiator was " + movie["Rated"] + ".")

# What year was 50 First Dates released?
movie = req.get(url + "50 First Dates").json()
print("The movie 50 First Dates was released in  " + movie["Year"] + ".")

# Who wrote Moana?
movie = req.get(url + "Moana").json()
print("Moana was written by " + movie["Writer"] + ".")

# What was the plot of the movie Sing?
movie = req.get(url + "Sing").json()
print("The plot of Sing was: '" + movie["Plot"] + "'.")

# BONUS: Complete this activity with a loop.
"""