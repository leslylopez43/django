from connect import *

# create subroutines
def read_songs():

    #select all record from songs
    dbCursor.execute("select * from songs")

    #fetch/get all from the songs table 
    allRecords =dbCursor.fetchall()

    # loop through all records
    for eachRecord in allRecords:
        print(eachRecord)
if __name__ == "__main__":
    read_songs()
    
