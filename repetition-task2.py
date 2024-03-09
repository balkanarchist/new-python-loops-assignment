'''
Convert the for loop from Task 1 into a while loop. Ensure it performs the
same function but also includes a condition to stop the loop if a certain
genre is played.

# Our playlist is still going
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
i = 0  # We start at the first track

# Keep the party alive until we've reached a specific genre
stop_genre = 'Hip-hop'

# Keep the party alive until we've reached the end or the stop_genre
while i < len(genres) and genres[i] != stop_genre:
    print("Remixing: " + genres[i])
    i += 1  # Move to the next track
'''

# Our playlist is still going
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
i = 0  # We start at the first track

# Keep the party alive until we've reached a specific genre
stop_genre = 'Hip-hop'

# Keep the party alive until we've reached the end or the stop_genre
while i < len(genres) and genres[i] != stop_genre:
    print("Remixing: " + genres[i])
    i += 1  # Move to the next track

# This is the same code that was provided on the assignment page - nothing was added but it runs
# as expected. If I'm meant to change the code somehow, that wasn't clear in the directions.