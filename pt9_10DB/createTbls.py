from connect import * #import the connect.py module 

# Assuming you have already connected to the database and created a cursor (dbCursor)

# Execute SQL command to create a table
dbCursor.execute("""
CREATE TABLE IF NOT EXISTS members (
    MemberID INTEGER PRIMARY KEY,
    Firstname TEXT,
    Lastname TEXT,
    Email TEXT
)
""")

# Commit the changes
dbCon.commit()

# Execute SQL command to create another table (fixing the comments and AUTOINCREMENT)
dbCursor.execute("""
CREATE TABLE IF NOT EXISTS songs (
    SongID INTEGER PRIMARY KEY,
    Title TEXT,
    Artist TEXT,
    Genre TEXT
)
""")

# Commit the changes
dbCon.commit()

# Create the table with foreign keys (fixing the comments and AUTOINCREMENT)
dbCursor.execute("""
CREATE TABLE IF NOT EXISTS downloads (
    DownlID INTEGER PRIMARY KEY,
    SongID INTEGER,
    MemberID INTEGER,
    Date TEXT,
    FOREIGN KEY(SongID) REFERENCES songs(SongID),
    FOREIGN KEY(MemberID) REFERENCES members(MemberID)
)
""")

# Commit the changes
dbCon.commit()

# Close the cursor and connection
dbCursor.close()
dbCon.close()


# has context menuCompose

# from * squiles3 import connect  
# dbContest + connect(.  
