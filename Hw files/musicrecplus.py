'''
Created on Nov 17, 2017

@author: brand
I pledge my Honor that I have abided by the Stevens Honor System - Bsoong 
'''

def readInData():
    try:
        handle = open("musicrecplus.txt" , 'r')
        lines = handle.read().splitlines()
        handle.close()
        for line in lines:
            #print('line: ', line)
            name, artists = line.split(':')
            print("name: '%s'  artists: '%s'" % (name, artists))
            database[name] = artists.split(',')
        print
    except:
        return database
    return database

def getPreferences(userName, uMap):
    ''' Returns a list of the uesr's preferred artists.
        If the system already knows about the user,
        it gets the preferences out of the userMap
        dictionary and then asks the user for additional 
        preferences.  If the user is new, it simply asks 
        the user for their preferences. '''
    newPref = ""
    if userName in uMap:
        prefs = uMap[userName]
        print("I see that you have used the system before.")
        print("Your music preferences include:")
        for artist in prefs:
            print(artist)
        print("Please enter another artist or band that you")
        print("like, or just press enter")
        newPref = input("to see your new preferences: ")
        for artist in prefs:
            print(artist)
    else:
        prefs = []
        print("I see that you are a new user.")
        print("Please enter the name of an artist or band")
        newPref = input("that you like: " )
        for artist in prefs:
            print(artist)
    while newPref != "":
        prefs.append(newPref.strip().title())
        print("Please enter another artist or band that you")
        print("like, or just press enter")
        newPref = input("to finish: ")
    prefs.sort()
    saveUserPreferences(userName, prefs, userMap, PREF_FILE)
    return prefs



