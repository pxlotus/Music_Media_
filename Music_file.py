import tkinter
import pygame
from pygame import mixer
import os
import threading
import time
from Player_Themes import *


mixer.init()

# creating a playlist
playlist = []
def file_browse():
    global filename_path
    filename_path = filedialog.askopenfilename()
    add_to_playlist(filename_path)
    mixer.music.queue(filename_path)

# adding songs to the media player
def add_to_playlist(filename):
    filename = os.path.basename(filename)
    index = 0
    # if later it still not show, return back to playlistcontainer
    playlistcontainer.insert(index, filename)
    playlist.insert(index, filename_path)
    index += 1

# removing songs
def remove_song():
    sel_song = playlistcontainer.curselection()
    sel_song = int(sel_song[0])
    playlistcontainer.delete(sel_song)
    playlist.pop(sel_song)

# showing song details
def show_details(play_song):
    file_data = os.path.splitext(play_song)
    if file_data[1] == '.mp3':
        audio = MP3(play_song)
        total_length = audio.info.length
    else:
        a = mixer.Sound(play_song)
        total_length = a.get_length()
    mins, secs = divmod(total_length, 60)
    mins = round(mins)
    secs = round(secs)
    time_format = "{:02d}:(:02d}".format(mins, secs)
    lengthlabel["text"] = "Total Time " + "- " + time_format
    t1 = threading.Thread(target=start_count, args=(total_length,))
    t1.start()

# song count down (i think)
def start_count(t):
    global paused
    current_time = 0
    while current_time <= t and mixer.music.get_busy():
        if paused:
            continue
        else:
            mins, secs = divmod(current_time, 60)
            mins = round(mins)
            secs = round(secs)
            time_format = '{:02d}:{:02d}'.format(mins, secs)
            current_time_label['text'] = "Current_time " + "- " + time_format
            time.sleep(1)
            current_time += 1

# playing the music
def play_music():
    global paused
    if paused:
        mixer.music.unpause()
        statusbar['text'] = "Music Resumed"
        paused = False
    else:
        try:
            stop_music()
            time.sleep(1)
            sel_song = playlistcontainer.curselection()
            sel_song = int(sel_song[0])
            play_it = playlist[sel_song]
            mixer.music.load(play_it)
            mixer.music.play()
            statusbar['text'] = "playing music " + "- " + os.path.basename(play_it)
            show_details(play_it)
        except:
            import tkinter.messagebox
            tkinter.messagebox.showerror("File not Found", "sith MM player could not find the given file."
                                                           " please select again.")

def stop_music():
    mixer.music.stop()
    statusbar['text'] = "Music Stopped"
paused = False
def pause_music():
    global paused
    paused = True
    mixer.music.pause()
    statusbar['text'] = "music Paused"
def rewind_music():
    play_music()
    statusbar['text'] = "Music Repeat"

# setting volume for the music player
def set_vol(val):
    volume = float(val) / 100
muted = False
def mute_music():
    global muted
    if muted:
        mixer.music.set_volume(0.7)
        volumeBtn.configure(text="Volume")
        scale.set(70)
        muted = False
    else:
        mixer.music.set_volume(0)
        volumeBtn.configure(text="Volume")
        scale.set(0)
        muted = True
"""
def on_closing():
    stop_music()
    root.destroy()
root.protocol("WM_DElETE_WINDOW", on_closing)"""

