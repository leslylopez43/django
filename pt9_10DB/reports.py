from connect import *

# create subroutine 
def songs_reports():

 dbCursor.execute("SELECT * FROM songs ORDER BY SongID DESC")
    # dbCursor.execute("")
    # dbCursor.execute("")
    # dbCursor.execute("")
    # dbCursor.execute("")
    # dbCursor.execute("")
    # dbCursor.execute("")
     # dbCursor.execute("")


reports = dbCursor.fetchall()

for aRecord in  reports:
        print(aRecord)

if __name__ == "__main__":
    songs_reports()

