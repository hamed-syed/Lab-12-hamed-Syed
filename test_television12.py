import pytest
from television import Television

def test_init():
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_power():
    tv = Television()
    tv.power()
    assert "Power = True" in str(tv)
    tv.power()
    assert "Power = False" in str(tv)

def test_mute():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert "Volume = 1" in str(tv)
    tv.mute()
    assert "Volume = 1" in str(tv)

def test_channel_up():
    tv = Television()
    tv.power()
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert "Channel = 0" in str(tv)

def test_channel_down():
    tv = Television()
    tv.power()
    tv.channel_down()
    assert "Channel = 3" in str(tv)

def test_volume_up():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_up()
    assert "Volume = 2" in str(tv)

def test_volume_down():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    tv.volume_down()
    tv.volume_down()
    assert "Volume = 0" in str(tv)
    