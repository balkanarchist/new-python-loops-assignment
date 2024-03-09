'''
Loop through a slice of the genres list and print only the selected genres.
Use slicing to create a sublist of genres from the second to the fourth track.

# Selective playlist slice
selected_genres = genres[1:4]  # From Rock to Classical

# Loop through the selected slice
for genre in selected_genres:
    print("Selective play: " + genre)
'''

genres = ["Indie", "Britpop", "Surf Rock", "Raga Rock", "modern garbage"]
# Selective playlist slice
selected_genres = genres[1:4]

# Loop through the selected slice
for genre in selected_genres:
    print("Selective play: " + genre)

# Only added genres for the code to work as it should. If there was something else I was meant to do,
# the directions weren't clear.