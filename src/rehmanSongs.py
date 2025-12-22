from tkinter import *
from tkinter import ttk, filedialog, messagebox
import os
import pygame
import time
import mysql.connector

# Initialize Pygame Mixer
pygame.mixer.init()

# --- Paths ---
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # src/ -> MusixBeat/
IMAGES_DIR = os.path.join(PROJECT_ROOT, "images")
SONGS_DIR = os.path.join(PROJECT_ROOT, "songs/A.R.Rehman")  # example album

# --- Tkinter Setup ---
root = Tk()
root.title("Music Player")
root.geometry("500x400")

# Master Frame
master_frame = Frame(root)
master_frame.pack(pady=20)

# Playlist Box
song_box = Listbox(master_frame, bg="black", fg="green", width=90, height=15,
                   selectbackground="green", selectforeground="black")
song_box.grid(row=0, column=0)

# --- Database functions ---
def fetch_songs():
    connection = mysql.connector.connect(host="localhost", user="root", password="", database="music_player")
    cursor = connection.cursor()
    cursor.execute("SELECT song_id, song_path FROM rehman_songs")
    songs = cursor.fetchall()
    connection.close()
    return songs

def get_song_path(song_name):
    connection = mysql.connector.connect(host="localhost", user="root", password="", database="music_player")
    cursor = connection.cursor()
    cursor.execute("SELECT song_path FROM rehman_songs WHERE song_path LIKE %s", (f"%{song_name}%",))
    song = cursor.fetchone()
    connection.close()
    return os.path.join(PROJECT_ROOT, song[0].replace("/", os.sep)) if song else None

# --- Load songs ---
songs_list = fetch_songs()
for song in songs_list:
    song_name = os.path.basename(song[1])
    song_box.insert(END, song_name)

# --- Controls ---
paused = False
stopped = False
current_song_index = 0

def play(song=None):
    global paused, stopped
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
    stopped = False
    paused = False
    show_time()
    if song is None:
        song = song_box.get(ACTIVE)
    song_path = get_song_path(song)
    if song_path:
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play(loops=0)

def stop():
    global stopped
    stopped = True
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)
    my_slider.config(value=0)
    status_bar.config(text="")

def pause():
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True

def next_song():
    global current_song_index
    if current_song_index < len(songs_list) - 1:
        current_song_index += 1
    else:
        current_song_index = 0
    song_box.selection_clear(0, END)
    song_box.activate(current_song_index)
    song_box.selection_set(current_song_index)
    my_slider.config(value=0)
    pygame.mixer.music.stop()
    play(os.path.basename(songs_list[current_song_index][1]))

def previous_song():
    global current_song_index
    if current_song_index > 0:
        current_song_index -= 1
    else:
        current_song_index = len(songs_list) - 1
    song_box.selection_clear(0, END)
    song_box.activate(current_song_index)
    song_box.selection_set(current_song_index)
    my_slider.config(value=0)
    pygame.mixer.music.stop()
    play(os.path.basename(songs_list[current_song_index][1]))

# --- Slider & Time ---
def show_time():
    if not pygame.mixer.music.get_busy():
        return
    current_time = pygame.mixer.music.get_pos() / 1000
    song_name = song_box.get(ACTIVE)
    song_path = get_song_path(song_name)
    if song_path:
        sound = pygame.mixer.Sound(song_path)
        song_length = sound.get_length()
        converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))
        converted_song_length = time.strftime('%M:%S', time.gmtime(song_length))
        my_slider.config(to=int(song_length), value=int(current_time))
        status_bar.config(text=f"Time Elapsed: {converted_current_time} of {converted_song_length}")
    status_bar.after(1000, show_time)

def slide(val):
    song_name = song_box.get(ACTIVE)
    song_path = get_song_path(song_name)
    if song_path and pygame.mixer.music.get_busy():
        pygame.mixer.music.set_pos(float(val))
        converted_time = time.strftime('%M:%S', time.gmtime(float(val)))
        status_bar.config(text=f"Time Elapsed: {converted_time}")

def control_vol(x):
    pygame.mixer.music.set_volume(volume_slider.get())

# --- GUI Controls ---
controls_frame = Frame(master_frame)
controls_frame.grid(row=1, column=0, pady=20)

volume_frame = LabelFrame(master_frame, text="Volume")
volume_frame.grid(row=0, column=1, padx=20)

back_btn_img = PhotoImage(file=os.path.join(IMAGES_DIR, "back50.png"))
forward_btn_img = PhotoImage(file=os.path.join(IMAGES_DIR, "forward50.png"))
play_btn_img = PhotoImage(file=os.path.join(IMAGES_DIR, "play50.png"))
pause_btn_img = PhotoImage(file=os.path.join(IMAGES_DIR, "pause50.png"))
stop_btn_img = PhotoImage(file=os.path.join(IMAGES_DIR, "stop50.png"))

back_button = Button(controls_frame, image=back_btn_img, borderwidth=0, command=previous_song)
forward_button = Button(controls_frame, image=forward_btn_img, borderwidth=0, command=next_song)
play_button = Button(controls_frame, image=play_btn_img, borderwidth=0, command=play)
pause_button = Button(controls_frame, image=pause_btn_img, borderwidth=0, command=pause)
stop_button = Button(controls_frame, image=stop_btn_img, borderwidth=0, command=stop)

back_button.grid(row=0, column=0, padx=10)
forward_button.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)
pause_button.grid(row=0, column=3, padx=10)
stop_button.grid(row=0, column=4, padx=10)

# Status Bar
status_bar = Label(root, text="", bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

# Slider
my_slider = ttk.Scale(master_frame, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=360)
my_slider.grid(row=2, column=0, pady=10)

# Volume
volume_slider = ttk.Scale(volume_frame, from_=0, to=1, orient=VERTICAL, value=1, command=control_vol, length=120)
volume_slider.pack(pady=10)

root.mainloop()
pygame.mixer.music.stop()
