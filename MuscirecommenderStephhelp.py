'''
Created on Nov 13, 2017

@author: brand
'''
from cs115 import *

def readInData():
    try:
        handle = open("musicrecplus.txt" , 'r')
        lines = handle.read().splitlines()
        handle.close()
        for line in lines:
            #print('line: ', line)
            name, artists = line.split(':')
            print("name: '%s'  artists: '%s'" % (name, artists))
            datastuff[name] = artists.split(',')
        print
    except:
        return datastuff
    return datastuff

def getUser():
    print("Enter your name (put a $ symbol after your name if you wish your preferences to remain private):")
    username = input()
    return username

def myMap(fn, iterable):
    ret = [0]*len(iterable)
    i=0
    for thing in iterable:
        ret[i] = fn(thing)
        i+=1
    return ret
        
def printOnePerLine(iterable):
    for thing in iterable:
        print(thing)
def putInText():
    s = 'asdf'
    handle = open('file.txt', 'w')
    handle.write(s)
    handle.close()
    
def getRecs(user, datastuff):
    def compare(userArtists, otherArtists, otherU):
        iUser = 0
        iOther = 0
        score = 0
        while iUser < len(userArtists) and iOther < len(otherArtists):
            if otherUName[-1] == '$':
                return -1
            
            aUser = userArtist[iUser]
            aOther = otherArtists[iOther]
            if aUser == aOther:
                score +=1
                iUser +=1
                iOther +=1
            elif aUser < aOther:
                iUser +=1
            else:
                iOther +=1
        if len(userArtists) == score:
            return -1
        return score
    def diff(userArtists, otherArtists):
        iUser = 0
        iOther = 0
        diffs = []
        while iUser < len(userArtists) and iOther < len(otherArtists):
            aUser = userArtist[iUser]
            aOther = otherArtists[iOther]
            if aUser == aOther:
                iUser +=1
                iOther +=1
            elif aUser < aOther:
                iUser +=1
            else:
                iOther +=1
                diffs.append(aOther)
        if iOther < len(otherArtists):
            diffs.extend(otherArtists[iOther:])
        return diffs
    userArtists = database[user]
    ranked = sorted(myMap(lambda uname: (compare(userArtists, datastuff[uname], uname), uname), datastuff))
    if len(ranked) == 0:
        print('No recommendations available at this time')
        return
    if ranked[0][0] == -1:
        print('No recommendations available at this time')
        return
    maxScore = ranked[0][0]
    imax = -1
    for result in ranked:
        if maxScore != result[0]:
            break
        imax +=1
    artists = []
    for i in range(iMax):
        artists.extend(diff(userArtists, datastuff[ranked[0][1]]))
    artists = sorted(list(set(artists)))
    printOnePerLine(artists)
    print(artists)
    
            
    
    
    
def main():
    database = readInData()
    user = getUser()
    getRecs(user, datastuff)
    

    
""" splitlines and split """ 



