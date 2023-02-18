"""
    Detect and save the chorus of a song
"""
from pychorus import find_and_output_chorus


chorus_start_sec = find_and_output_chorus("./data/uplink.wav", "output.wav", clip_length = 15)