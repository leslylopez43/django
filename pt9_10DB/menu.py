import readsongs, addsongs, deletesongs, reports, updatesongs

#function to read the respective menu file.

def menuFile():
    with open("/Users/elenitayroy/Documents/GitHub/pythonjustit/pt9_10DB/songsMenu.txt") as songsFile: 
        userMenu = songsFile.read()
       
    
    return userMenu 

    print(menuFile())

