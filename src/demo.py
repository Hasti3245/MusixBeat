import tkinter as tk
from tkinter import messagebox
import os
from PIL import Image, ImageTk
import mysql.connector


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")   # artist images + logo
IMAGES_DIR = os.path.join(BASE_DIR, "images")   # ui icons


class MusicPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("1000x600")
        root.configure(bg="#2E3B4E")

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=3)
        self.root.grid_columnconfigure(1, weight=1)

        # ================= DATABASE =================
        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="music_player"
        )
        self.db_cursor = self.db_connection.cursor()

        self.create_content_area()
        self.create_sidebar()

    # ======================================================
    def create_content_area(self):
        content_frame = tk.Frame(self.root, bg="#2E3B4E")
        content_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.create_search_bar(content_frame)
        self.create_album_section(content_frame)

    # ======================================================
    def create_search_bar(self, parent_frame):
        search_frame = tk.Frame(parent_frame, bg="#2E3B4E")
        search_frame.pack(pady=10, padx=20, fill='x')

        try:
            logo_path = os.path.join(ASSETS_DIR, "logo22.jpg")
            logo_img = Image.open(logo_path)
            logo_img = logo_img.resize((70, 70), Image.LANCZOS)
            logo_img = ImageTk.PhotoImage(logo_img)

            logo_label = tk.Label(search_frame, image=logo_img, bg="#2E3B4E")
            logo_label.image = logo_img
            logo_label.pack(side="left", padx=10)

        except Exception as e:
            print("Logo load error:", e)
            placeholder = Image.new('RGB', (70, 70), color='grey')
            placeholder = ImageTk.PhotoImage(placeholder)
            tk.Label(search_frame, image=placeholder, bg="#2E3B4E").pack(side="left", padx=10)

        tk.Label(
            search_frame,
            text="MusixBeat",
            font=("Arial", 16, "italic", "bold"),
            fg="white",
            bg="#2E3B4E"
        ).pack(side="left", padx=8)

    # ======================================================
    def create_album_section(self, parent_frame):
        album_frame = tk.Frame(parent_frame, bg="#2E3B4E")
        album_frame.pack(pady=20, padx=20, fill='both', expand=True)

        canvas = tk.Canvas(album_frame, bg="#2E3B4E", width=550)
        canvas.pack(side="left", fill='both', expand=True)

        scrollable_frame = tk.Frame(canvas, bg="#2E3B4E")
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        self.db_cursor.execute("SELECT album_name, album_image FROM albums")
        albums = self.db_cursor.fetchall()

        for i in range(2):
            for j in range(5):
                if i * 5 + j < len(albums):
                    album_name, album_image = albums[i * 5 + j]
                    self.create_album_item(scrollable_frame, album_name, album_image, i, j)

        scrollable_frame.update_idletasks()

    # ======================================================
    def create_album_item(self, parent_frame, album_name, db_img_path, row, column):
        album_frame = tk.Frame(parent_frame, width=150, height=250, bg="#2E3B4E")
        album_frame.grid(row=row, column=column, padx=10, pady=10)

        try:
            # 🔑 Extract filename even if DB stores D:\MusixBeat\Shreya1.webp
            img_file = os.path.basename(db_img_path)
            img_path = os.path.join(ASSETS_DIR, img_file)

            img = Image.open(img_path)
            img = img.resize((200, 200), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)

            img_label = tk.Label(album_frame, image=img, bg="#2E3B4E")
            img_label.image = img
            img_label.pack()

        except Exception as e:
            print("Album image error:", e)
            placeholder = Image.new('RGB', (150, 150), color='grey')
            placeholder = ImageTk.PhotoImage(placeholder)
            tk.Label(album_frame, image=placeholder, bg="#2E3B4E").pack()

        tk.Button(
            album_frame,
            text=album_name,
            command=lambda: self.show_album_message(album_name),
            width=14,
            height=2,
            bg="#ADD8E6",
            fg="Black"
        ).pack(pady=10)

    # ======================================================
    def create_sidebar(self):
        sidebar_frame = tk.Frame(self.root, bg="#2E3B4E")
        sidebar_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        button_frame = tk.Frame(sidebar_frame, bg="#2E3B4E")
        button_frame.pack(pady=7)

        tk.Button(button_frame, text="Logout", command=self.logout,
                  width=6, height=2, bg="red", fg="white").pack(side="left", padx=5)

        tk.Button(button_frame, text="...", command=self.open_adminPanel,
                  width=3, height=2, bg="#2E3B4E").pack(side="left", padx=5)

        tk.Label(
            sidebar_frame,
            text="Categories",
            font=("Arial", 16),
            fg="white",
            bg="#2E3B4E"
        ).pack(pady=25)

        self.db_cursor.execute("SELECT category_name FROM categories")
        for (category_name,) in self.db_cursor.fetchall():
            tk.Button(
                sidebar_frame,
                text=category_name,
                command=lambda c=category_name: self.select_category(c),
                height=2,
                font=("Arial", 12),
                bg="#ddd",
                bd=0
            ).pack(pady=10, padx=10, fill="x")

    # ======================================================
    def select_category(self, category):
        if messagebox.askyesno(category, f"Play songs from {category}?"):
            scripts = {
                "Gujarati Songs": "gujaratiMusic.py",
                "Romantic Hits": "romanticMusic.py",
                "Trending Songs": "trendMusic.py",
                "Classical Songs": "classicalMusic.py",
                "English Songs": "englishSongs.py",
                "Punjabi Songs": "punjabiMusic.py",
                "Hip Hop Songs": "hiphopMusic.py",
                "Wedding Songs": "weddingMusic.py"
            }
            script = scripts.get(category)
            if script:
                self.root.quit()
                os.system(f"python {script}")

    # ======================================================
    def logout(self):
        if messagebox.askokcancel("Logout", "You have logged out!"):
            self.root.quit()
            os.system("python Register.py")

    def open_adminPanel(self):
        os.system("python AdminLogin.py")

    def show_album_message(self, album_name):
        if messagebox.askyesno(album_name, f"Play songs from {album_name}?"):
            scripts = {
                "Shreya Ghosal": "GhosalSongs.py",
                "Neha Kakkar": "nehaSongs.py",
                "Arijit Singh": "arijitSongs.py",
                "A.R. Rehman": "rehmanSongs.py",
                "Sachin-Jigar": "sachin_jigarSongs.py",
                "Diljit Dosanjh": "DosanjhSongs.py",
                "Badshah": "badshahSongs.py",
                "Yoyo Honey Singh": "honeySongs.py",
                "K.K.": "kkSongs.py",
                "Darshan Raval": "darshanSongs.py"
            }
            script = scripts.get(album_name)
            if script:
                self.root.quit()
                os.system(f"python {script}")



root = tk.Tk()
app = MusicPlayerApp(root)
root.mainloop()
