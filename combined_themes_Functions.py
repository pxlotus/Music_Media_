import tkinter
import tkinter.ttk
import os
import time
import threading
from tkinter import ttk, filedialog, Menu
from pygame import mixer
from tkinter import *


root = tkinter.Tk()

# Features for the music player

# exit action
def _quit():
    root.quit()
    root.destroy()
    exit()
root.protocol("sith_Delete_window", _quit)

# creating a menu Bar
menuBar = Menu(root)
root.config(menu=menuBar)
root["bg"] = "#FCE205"

# created a status bar
statusbar = ttk.Label(root, text="Sith Music, Media Player", anchor=W, font='Arial 8 italic')
statusbar.pack(side=BOTTOM, fill=X)
statusbar1 = ttk.Label(root, text="Sith Music, Media Player", anchor=W, font='Arial 8 italic')
statusbar1.pack(side=TOP, fill=X)

# mixer theme
lt_frame = Frame(root, bg="#FFFFFF")
lt_frame.pack(side=LEFT, pady=100, padx=30)


# functions for the music player

mixer.init()

# creating a file menu
sub_menu = Menu(menuBar, tearoff=0)
playlist = []
def file_browse():
    global filename_path
    filename_path = filedialog.askopenfilename()
    add_to_playlist(filename_path)
    mixer.music.queue(filename_path)

def add_to_playlist(filename):
    filename = os.path.basename(filename)
    index = 0
    playlistcontainer.insert(index, filename)
    playlist.insert(index, filename_path)
    index += 1

sub_menu.add_command(label="New")
sub_menu.add_separator()
sub_menu.add_command(label="Open", command=file_browse)
sub_menu.add_separator()
sub_menu.add_command(label="Exit", command=_quit)
menuBar.add_cascade(label="File", menu=sub_menu)

# play list
playlistcontainer = Listbox(lt_frame, selectmode=SINGLE, fg="black")  # can change back to playlistcontainer
playlistcontainer["bg"] = "#364C69"  # can change it back to playlist container
playlistcontainer.pack(pady=40)

# add button
addBtn = ttk.Button(lt_frame, text="+Add", command=file_browse)
addBtn.pack(side=LEFT)

# removing songs
def remove_song():
    sel_song = playlistcontainer.curselection()
    sel_song = int(sel_song[0])
    playlistcontainer.delete(sel_song)
    playlist.pop(sel_song)

# deleting / removing a song button
root.style = ttk.Style()
root.style.theme_use("clam")
remBtn = ttk.Button(lt_frame, text="- Del", command=remove_song)
remBtn.pack(side=LEFT)

# Not sure
root.style.configure('TButton', background="#12936F")
rt_frame = Frame(root, bg="#364C69")
rt_frame.pack(pady=30, padx=20)

# Top Frame
top_frame = Frame(rt_frame, bg="#FEE227")
top_frame.pack()
root.style = ttk.Style()

# status bar theme
root.style.theme_use("clam")
root.style.configure('TLabel', background="#364C69")

# time label
lengthlabel = ttk.Label(top_frame, text='Total Time :--:--')
lengthlabel.pack(pady=5)

current_time_label = ttk.Label(top_frame, text='Current Time :--:--')
current_time_label.pack()

# showing the song details
def show_details(play_song):
    file_data = os.path.splitext(play_song)
    if file_data[1] == ".mp3":
        audio = MP3(play_song)
        total_length = audio.info.length
    else:
        a = mixer.Sound(play_song)
        total_length = a.get_length()
    mins, secs = divmod(total_length, 60)
    mins = round(mins)
    secs = round(secs)
    time_format = "{:02d}:{:02d}".format(mins, secs)
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
        except EXCEPTION:
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

middle_frame = Frame(rt_frame, bg="#364C69")
middle_frame.pack(pady=30, padx=30)
playBtn = tkinter.Button(middle_frame, text="Play", command=play_music)
playBtn.grid(row=0, column=0, padx=10)
stopBtn = tkinter.Button(middle_frame, text="Stop", command=stop_music)
stopBtn.grid(row=0, column=1, padx=10)
pauseBtn = tkinter.Button(middle_frame, text="Pause", command=pause_music)
pauseBtn.grid(row=0, column=2, padx=10)

bottom_frame = Frame(rt_frame,bg="gray")
bottom_frame.pack(pady=10,padx=5)
rewindBtn = tkinter.Button(bottom_frame, text="Rewind", command=rewind_music)
rewindBtn.grid(row=0, column=0,padx=10)
volumeBtn = tkinter.Button(bottom_frame, text="Mute", command=mute_music)
volumeBtn.grid(row=0, column=1)
scale = tkinter.Scale(bottom_frame, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(70)

if __name__ == mainloop():
    root.mainloop()

