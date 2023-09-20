from lib.music_library import *
from lib.track import *

"""
Adding 3 tracks using the add method we return one track using the search method
"""
def test_search_returns_single_track():
    lib = MusicLibrary()
    track_1 = Track("Three Little Birds", "Bob Marley")
    track_2 = Track("Mathematics", "Mos Def")
    track_3 = Track("Voodoo Child", "Jimmy Hendricks")
    lib.add(track_1)
    lib.add(track_2)
    lib.add(track_3)
    assert lib.search("Mos Def") == [track_2]

"""
Adding 3 tracks we return an empty list if search keyword does not match any of the tracks
"""

def test_search_returns_single_track_return_empty_list():
    lib = MusicLibrary()
    track_1 = Track("Three Little Birds", "Bob Marley")
    track_2 = Track("Mathematics", "Mos Def")
    track_3 = Track("Voodoo Child", "Jimmy Hendricks")
    lib.add(track_1)
    lib.add(track_2)
    lib.add(track_3)
    assert lib.search("The Liberteens") == []