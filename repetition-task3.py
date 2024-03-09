'''
Using the range() function, loop through the genres list by index. For each genre,
print out the track number and a message that the light show is ready. Modify the
loop to skip a genre if it's not suitable for the light show.

# Our playlist needs a light show
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
unsuitable_genre = 'Classical'

for index in range(len(genres)):
    if genres[index] == unsuitable_genre:
        continue  # Skip the light show for this genre
    print(f"Track {index + 1}: {genres[index]} - Light show is on!")
'''

# Our playlist needs a light show
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
unsuitable_genre = 'Classical'

for index in range(len(genres)):
    if genres[index] == unsuitable_genre:
        continue  # Skip the light show for this genre
    print(f"Track {index + 1}: {genres[index]} - Light show is on!")

# This is the same code that was provided on the assignment page - nothing was added but it runs
# as expected. If I'm meant to change the code somehow, that wasn't clear in the directions.