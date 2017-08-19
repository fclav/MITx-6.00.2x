#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 15:57:26 2017

@author: fequi
"""

def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    playlist = []
    remainingSize = max_size
    firstSong = songs[0]
    if firstSong[2] > remainingSize:
        return playlist
    else:
        playlist.append(firstSong[0])
        remainingSize -= firstSong[2]
    
    remainingSongs = sorted(songs[1:], key = lambda x: x[2])
    for song in remainingSongs:
        songSize = song[2]
        if songSize > remainingSize:
            break
        else:
            playlist.append(song[0])
            remainingSize -= songSize
    
    return playlist

def test_song_playlist():
    tests = []
    tests.append({"id":1, "songs":[('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)], "max_size":12.2, "output":['Roar','Wannabe','Timber']})
    tests.append({"id":2, "songs":[('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)], "max_size":11, "output":['Roar','Wannabe']})
    
    for test in tests:
        print("Test",test["id"])
        playlist = song_playlist(test["songs"], test["max_size"])
        print("Returned:", playlist)
        print("Expected:", test["output"])
    
#test_song_playlist()