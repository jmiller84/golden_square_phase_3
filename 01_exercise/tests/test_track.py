from lib.track import *

"""
Initially create a new track and check it has a title
"""
def test_track_has_a_title():
    track_1 = Track("Three Little Birds", "Bob Marley")
    assert track_1.title == "Three Little Birds"
    

"""
Initially create a new track and check it has an artist
"""
def test_track_has_an_artist():
    track_1 = Track("Three Little Birds", "Bob Marley")
    assert track_1.artist == "Bob Marley"

"""
Initially create a new track and check it has a title and an artist
"""
def test_track_has_title_and_artist():
    track_1 = Track("Three Little Birds", "Bob Marley")
    assert track_1.title == "Three Little Birds" and track_1.artist == "Bob Marley"


"""
Add a track and check that when the correct keyword is given matches returns True
"""
def test_matches_returns_true():
    track_1 = Track("Three Little Birds", "Bob Marley")
    assert track_1.matches("Bob Marley") == True


"""
Add a track and check that when an incorrect keywordis given matches returns False
"""
def test_matches_returns_false():
    track_1 = Track("Three Little Birds", "Bob Marley")
    assert track_1.matches("Damian Marley") == False
