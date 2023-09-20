from lib.music_library import *
from unittest.mock import Mock

"""
Unit Test the MusicLibrary Class using mocks
"""

"""
Add 3 mock tracks and return 3 tracks
"""
def test_add_three_mock_tracks_return_three_tracks():
    music_lib = MusicLibrary()
    track_1_mock = Mock()
    track_2_mock = Mock()
    track_3_mock = Mock()
    music_lib.add(track_1_mock)
    music_lib.add(track_2_mock)
    music_lib.add(track_3_mock)
    assert music_lib.tracks == [track_1_mock, track_2_mock, track_3_mock]


"""
Add 3 mock tracks and return 1 track using search
"""
def test_search_returns_one_mock_track():
    music_lib = MusicLibrary()

    track_1_mock = Mock()
    track_1_mock.matches.return_value = False

    track_2_mock = Mock()
    track_2_mock.matches.return_value = True

    track_3_mock = Mock()
    track_3_mock.matches.return_value = False

    music_lib.add(track_1_mock)
    music_lib.add(track_2_mock)
    music_lib.add(track_3_mock)

    assert music_lib.search("Test") == [track_2_mock]

"""
Add 3 mock tracks and return empty list from search
"""
def test_mocks_search_returns_empty_list():
    music_lib = MusicLibrary()

    track_1_mock = Mock()
    track_1_mock.matches.return_value = False

    track_2_mock = Mock()
    track_2_mock.matches.return_value = False

    track_3_mock = Mock()
    track_3_mock.matches.return_value = False

    music_lib.add(track_1_mock)
    music_lib.add(track_2_mock)
    music_lib.add(track_3_mock)

    assert music_lib.search("Test") == []
