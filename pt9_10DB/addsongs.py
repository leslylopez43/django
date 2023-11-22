from connect import *

# create subroutine
def insert_songs():
    # Get user input
    songTitle = input("Enter song title: ")
    songArtist = input("Enter song artist: ")
    songGenre = input("Enter song genre: ")

    # Execute SQL command to insert a record into the "songs" table
    dbCursor.execute("INSERT INTO songs (Title, Artist, Genre) VALUES (?, ?, ?)", (songTitle, songArtist, songGenre))

    # Commit the changes
    dbCon.commit()

# Call the function to insert a song
insert_songs()

# Close the cursor and connection
dbCursor.close()
dbCon.close()
