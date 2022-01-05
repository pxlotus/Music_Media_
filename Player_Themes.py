import tkinter as tk
import tkinter.ttk
from tkinter import ttk
from tkinter import Menu, filedialog
from tkinter import *
from Music_file import file_browse, remove_song, play_music, stop_music, pause_music, rewind_music, mute_music, set_vol

root = tk.Tk()
root.title("Sith MM player")

# Exit action
def _quit():
    root.quit()
    root.destroy()
    exit()

# Creating a Menu Bar
menuBar = Menu(root)
root.config(menu=menuBar)
root["bg"] = "#FFC30B"

# Creating a File Menu
sub_menu = Menu(menuBar, tearoff=0)
sub_menu.add_command(label="New")
sub_menu.add_separator()
sub_menu.add_command(label="Open", command=file_browse)
sub_menu.add_separator()
sub_menu.add_command(label="Exit", command=_quit)
menuBar.add_cascade(label="File", menu=sub_menu)

# created a status bar
statusbar = ttk.Label(root, text="Sith Music, Media Player", anchor=W, font='Arial 8 italic')
statusbar.pack(side=BOTTOM, fill=X)
statusbar1 = ttk.Label(root, text="Sith Music, Media Player", anchor=W, font='Arial 8 italic')
statusbar1.pack(side=TOP, fill=X)

# mixer theme
lt_frame = Frame(root, bg="#FFFFFF")
lt_frame.pack(side=LEFT, pady=100, padx=30)

# play list
playlistcontainer = Listbox(lt_frame, selectmode=SINGLE, fg="black")  # can change back to playlistcontainer
playlistcontainer["bg"] = "#364C69"  # can change it back to playlist container
playlistcontainer.pack(pady=40)
# add button
addBtn = ttk.Button(lt_frame, text="+Add", command=file_browse)
addBtn.pack(side=LEFT)
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

root.mainloop()
