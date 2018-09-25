# Write a program that promps the user for the user for their five favourite
# movies. Store each movie in a list. If the user at any stage enters Quit at
# any stage, the program should stop prompting the user for the movie name and
# should print to the screen the movies captured in the list up to that point.

counter = 1
moviesList = []  # This makes an empty list
print("Enter up to 5 movies names or Quit to exit")

movieName = ""  # Starting with a blank variable to let us check in while

while counter <= 5 and movieName.lower() != "quit":
    movieName = input("Enter movie " + str(counter) + " name or Quit: ")
    if movieName.lower() != "quit":
        moviesList.append(movieName)
    counter += 1

print("Your movies are:")
for x in moviesList:
    print(x)
