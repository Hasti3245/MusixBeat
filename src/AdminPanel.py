import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter import ttk
import re
import mysql.connector

class MusicPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player Admin Panel")
        self.root.geometry("1000x600")
        self.root.configure(bg='#2E3B4E')

        # Connect to MySQL Database
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="music_player"
            
        )
        self.cursor = self.conn.cursor()

        self.create_admin_panel()

    def create_admin_panel(self):
    # Clear window if any existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()
            
        self.image = Image.open(r"D:/MusixBeat/assets/AdminPhoto.png")
        self.image = self.image.resize((200, 200))  # Resize image to 400x400
        self.image = ImageTk.PhotoImage(self.image)  #

        # Create the sidebar image on the left side of the window
        self.sidebar_image_label = tk.Label(self.root, image=self.image, bg="#2E3B4E")
        self.sidebar_image_label.place(relx=0.01, rely=0.1, relwidth=0.2)   # Sidebar image on the left

        # Create the title "Admin" under the image
        admin_title = tk.Label(self.root, text="Admin Panel", font=("Arial", 24, "bold"), fg="#FF6F61", bg="#2E3B4E")
    
        # Position "Admin" label directly under the image and centered
        admin_title.place(relx=0.003 + 0.2/2 - 0.05, rely=0.37)
   
        # Navigation Buttons for Albums, Categories, Songs, and Users (aligned to the right)
        button_style = {"font": ("Arial", 14), "bg": "#4F81BD", "fg": "white", "relief": "flat", "width": 23, "height": 2}

        # Using place method to align buttons to the right side with more vertical space
        button_y = 0.02
        # Start Y-position for the buttons
        tk.Button(self.root, text="Manage Albums", command=self.manage_albums, **button_style).place(relx=0.87, rely=button_y, anchor="ne")
        button_y += 0.10  # Increased space between buttons
        tk.Button(self.root, text="Manage Categories", command=self.manage_categories, **button_style).place(relx=0.87, rely=button_y, anchor="ne")
        button_y += 0.10 # Increased space between buttons
        tk.Button(self.root, text="Manage Users", command=self.manage_users, **button_style).place(relx=0.87, rely=button_y, anchor="ne")

        button_z = 0.02
        tk.Button(self.root, text="Manage Songs of Neha", command=self.manage_songs_of_neha, **button_style).place(relx=0.43, rely=button_z, anchor="ne")
        button_z += 0.10  # Increased space between buttons
        tk.Button(self.root, text="Manage Songs of Shreya", command=self.manage_songs_of_shreya, **button_style).place(relx=0.43, rely=button_z, anchor="ne")
        button_z += 0.10  # Increased space between buttons
        tk.Button(self.root, text="Manage Songs of Arijit ", command=self.manage_songs_of_arijit, **button_style).place(relx=0.43, rely=button_z, anchor="ne")
        button_z += 0.10  # Increased space between buttons
        tk.Button(self.root, text="Manage Songs of Rehman", command=self.manage_songs_of_rehman, **button_style).place(relx=0.43, rely=button_z, anchor="ne")
        button_z += 0.10  # Increased space between buttons
        tk.Button(self.root, text="Manage Songs of Sachin Jigar", command=self.manage_songs_of_sachJig, **button_style).place(relx=0.43, rely=button_z, anchor="ne")
        button_z += 0.10 # Increased space between buttons
        tk.Button(self.root, text="Manage Songs of Diljit", command=self.manage_songs_of_diljit, **button_style).place(relx=0.43, rely=button_z, anchor="ne")
        button_z += 0.10  # Increased space between buttons
        tk.Button(self.root, text="Manage Songs of Badshah", command=self.manage_songs_of_badshah, **button_style).place(relx=0.43, rely=button_z, anchor="ne")
        button_z += 0.10  # Increased space between buttons
        tk.Button(self.root, text="Manage Songs of Honey Singh", command=self.manage_songs_of_honey, **button_style).place(relx=0.43, rely=button_z, anchor="ne")
        button_z += 0.10  # Increased space between buttons
        tk.Button(self.root, text="Manage Songs of K.K.", command=self.manage_songs_of_kk, **button_style).place(relx=0.43, rely=button_z, anchor="ne")
        button_z += 0.10  # Increased space between buttons
        tk.Button(self.root, text="Manage Songs in Darshan", command=self.manage_songs_of_darshan, **button_style).place(relx=0.43, rely=button_z, anchor="ne")




        button_m = 0.02 # Increased space between buttons
        tk.Button(self.root, text="Manage Gujarati Songs", command=self.manage_gujarati_songs, **button_style).place(relx=0.65, rely=button_m, anchor="ne")
        button_m += 0.10 # Increased space between buttons
        tk.Button(self.root, text="Manage Romantic Songs", command=self.manage_romantic_songs, **button_style).place(relx=0.65, rely=button_m, anchor="ne")
        button_m += 0.10 # Increased space between buttons
        tk.Button(self.root, text="Manage Trending Songs", command=self.manage_trending_songs, **button_style).place(relx=0.65, rely=button_m, anchor="ne")
        button_m += 0.10 # Increased space between buttons
        tk.Button(self.root, text="Manage Classical Songs", command=self.manage_classical_songs, **button_style).place(relx=0.65, rely=button_m, anchor="ne")
        button_m += 0.10 # Increased space between buttons
        tk.Button(self.root, text="Manage english Songs", command=self.manage_english_songs, **button_style).place(relx=0.65, rely=button_m, anchor="ne")
        button_m += 0.10 # Increased space between buttons
        tk.Button(self.root, text="Manage Punjabi Songs", command=self.manage_punjabi_songs, **button_style).place(relx=0.65, rely=button_m, anchor="ne")
        button_m += 0.10 # Increased space between buttons
        tk.Button(self.root, text="Manage Hip Hop Songs", command=self.manage_hiphop_songs, **button_style).place(relx=0.65, rely=button_m, anchor="ne")
        button_m += 0.10 # Increased space between buttons
        tk.Button(self.root, text="Manage Wedding Songs", command=self.manage_wedding_songs, **button_style).place(relx=0.65, rely=button_m, anchor="ne")


        


    def manage_users(self):
        self.create_management_window("users")

    def manage_albums(self):
        self.create_management_window("albums")

    def manage_categories(self):
        self.create_management_window("categories")

    def manage_songs_of_neha(self):
        self.create_management_window("songs_of_neha")

    def manage_songs_of_shreya(self):
        self.create_management_window("songs_of_shreya")

    def manage_songs_of_arijit(self):
        self.create_management_window("songs_of_arijit")

    def manage_songs_of_rehman(self):
        self.create_management_window("songs_of_rehman")

    def manage_songs_of_sachJig(self):
        self.create_management_window("songs_of_sach-jig")

    def manage_songs_of_diljit(self):
        self.create_management_window("songs_of_diljit")

    def manage_songs_of_badshah(self):
        self.create_management_window("songs_of_badshah")

    def manage_songs_of_honey(self):
        self.create_management_window("songs_of_honey")

    def manage_songs_of_kk(self):
        self.create_management_window("songs_of_kk")

    def manage_songs_of_darshan(self):
        self.create_management_window("songs_of_darshan")

    def manage_gujarati_songs(self):
        self.create_management_window("gujarati_songs")

    def manage_romantic_songs(self):
        self.create_management_window("romantic_songs")

    def manage_trending_songs(self):
        self.create_management_window("trending_songs")

    def manage_classical_songs(self):
        self.create_management_window("classical_songs")

    def manage_english_songs(self):
        self.create_management_window("english_songs")

    def manage_punjabi_songs(self):
        self.create_management_window("punjabi_songs")

    def manage_hiphop_songs(self):
        self.create_management_window("hiphop_songs")

    def manage_wedding_songs(self):
        self.create_management_window("wedding_songs")

    def create_management_window(self, entity):
        # Clear window if any existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # Title
        title = tk.Label(self.root, text=f"Manage {entity.capitalize()}", font=("Arial", 20,"bold"),fg="#FF6F61", bg="#2E3B4E")
        title.pack(pady=10)

        # Add Button
        add_button = tk.Button(self.root, text=f"Add {entity.capitalize()}", command=lambda: self.add_entity(entity), font=("Arial", 14), bg="#4F81BD", fg="white", relief="flat", width=20, height=2)
        add_button.pack(pady=10)

        # List Button
        list_button = tk.Button(self.root, text=f"List {entity.capitalize()}", command=lambda: self.list_entity(entity), font=("Arial", 14), bg="#4F81BD", fg="white", relief="flat", width=20, height=2)
        list_button.pack(pady=10)
        

        # Go Back Button
        back_button = tk.Button(self.root, text="Back to Admin Panel", command=self.create_admin_panel, font=("Arial", 14), bg="#FF6F61", fg="white", relief="flat", width=20, height=2)
        back_button.pack(pady=10)

    def add_entity(self, entity):
        if entity == "albums":
            self.add_album()
        elif entity == "categories":
            self.add_category()
        elif entity == "songs_of_neha":
            self.add_song_of_neha()
        elif entity == "songs_of_shreya":
            self.add_song_of_shreya()
        elif entity == "songs_of_arijit":
            self.add_song_of_arijit()
        elif entity == "songs_of_rehman":
            self.add_song_of_rehman()
        elif entity == "songs_of_sachJig":
            self.add_song_of_sachJig()
        elif entity == "songs_of_diljit":
            self.add_song_of_diljit()
        elif entity == "songs_of_badshah":
            self.add_song_of_badshah()
        elif entity == "songs_of_honey":
            self.add_song_of_honey()
        elif entity == "songs_of_kk":
            self.add_song_of_kk()
        elif entity == "songs_of_darshan":
            self.add_song_of_darshan()
        elif entity == "gujarati_songs":
            self.add_gujarati_songs()
        elif entity == "romantic_songs":
            self.add_romantic_songs()
        elif entity == "trending_songs":
            self.add_trending_songs()
        elif entity == "classical_songs":
            self.add_classical_songs()
        elif entity == "english_songs":
            self.add_english_songs()
        elif entity == "punjabi_songs":
            self.add_punjabi_songs()
        elif entity == "hiphop_songs":
            self.add_hiphop_songs()
        elif entity == "wedding_songs":
            self.add_wedding_songs()
        elif entity == "users":
            self.add_user()

    def list_entity(self, entity):
        if entity == "albums":
            self.list_albums()
        elif entity == "categories":
            self.list_categories()
        elif entity == "songs_of_neha":
            self.list_songs_of_neha()
        elif entity == "songs_of_shreya":
            self.list_songs_of_shreya()
        elif entity == "songs_of_arijit":
            self.list_songs_of_arijit()
        elif entity == "songs_of_rehman":
            self.list_songs_of_rehman()
        elif entity == "songs_of_sachJig":
            self.list_songs_of_sachJig()
        elif entity == "songs_of_diljit":
            self.list_songs_of_diljit()
        elif entity == "songs_of_badshah":
            self.list_songs_of_badshah()
        elif entity == "songs_of_honey":
            self.list_songs_of_honey()
        elif entity == "songs_of_kk":
            self.list_songs_of_kk()
        elif entity == "songs_of_darshan":
            self.list_songs_of_darshan()
        elif entity == "gujarati_songs":
            self.list_gujarati_songs()
        elif entity == "romantic_songs":
            self.list_romantic_songs()
        elif entity == "trending_songs":
            self.list_trending_songs()
        elif entity == "classical_songs":
            self.list_classical_songs()
        elif entity == "english_songs":
            self.list_english_songs()
        elif entity == "punjabi_songs":
            self.list_punjabi_songs()
        elif entity == "hiphop_songs":
            self.list_hiphop_songs()
        elif entity == "wedding_songs":
            self.list_wedding_songs()
        elif entity == "users":
            self.list_users()

    def add_user(self):
        self.open_user_input_window("Add User", self.insert_user)

    def open_user_input_window(self, title, insert_method):
        def validate_inputs():
            username = username_entry.get()
            password = password_entry.get()
            email = email_entry.get()
            phone = phone_entry.get()

        # Username validation: must contain at least a number and a special symbol
            if not re.match(r'^(?=.*\d)(?=.*[!@#$%^&*])', username):
                messagebox.showerror("Error", "Username must contain at least one number and one special symbol.")
                return False

        # Password validation: must be at least 6 characters long
            if len(password) < 6:
                messagebox.showerror("Error", "Password must be at least 6 characters long.")
                return False

        # Email validation: must match the basic email pattern
            if not re.match(r'\S+@\S+\.\S+', email):
                messagebox.showerror("Error", "Invalid email address.")
                return False

        # Phone number validation: must be exactly 10 digits
            if len(phone) != 10 or not phone.isdigit():
                messagebox.showerror("Error", "Phone number must be 10 digits.")
                return False

        # If all validations pass, call the insert method
            insert_method(username, password, email, phone)
            return True

        input_window = tk.Toplevel(self.root)
        input_window.title(title)

    # Username input
        username_label = tk.Label(input_window, text="Username:", font=("Arial", 12), bg="#FFFFFF")
        username_label.grid(row=0, column=0, padx=10, pady=10)
        username_entry = tk.Entry(input_window, font=("Arial", 12))
        username_entry.grid(row=0, column=1, padx=10, pady=10)

    # Password input
        password_label = tk.Label(input_window, text="Password:", font=("Arial", 12), bg="#FFFFFF")
        password_label.grid(row=1, column=0, padx=10, pady=10)
        password_entry = tk.Entry(input_window, font=("Arial", 12), show="*")
        password_entry.grid(row=1, column=1, padx=10, pady=10)

    # Email input
        email_label = tk.Label(input_window, text="Email:", font=("Arial", 12), bg="#FFFFFF")
        email_label.grid(row=2, column=0, padx=10, pady=10)
        email_entry = tk.Entry(input_window, font=("Arial", 12))
        email_entry.grid(row=2, column=1, padx=10, pady=10)

    # Phone number input
        phone_label = tk.Label(input_window, text="Phone Number:", font=("Arial", 12), bg="#FFFFFF")
        phone_label.grid(row=3, column=0, padx=10, pady=10)
        phone_entry = tk.Entry(input_window, font=("Arial", 12))
        phone_entry.grid(row=3, column=1, padx=10, pady=10)

    # Submit button
        submit_button = tk.Button(input_window, text="Submit", command=validate_inputs, font=("Arial", 14), bg="#4F81BD", fg="white")
        submit_button.grid(row=4, columnspan=2, pady=20)

    def insert_user(self, username, password, email, phone):
        self.cursor.execute("INSERT INTO users (username, password, email, phone_number) VALUES (%s, %s, %s, %s)", (username, password, email, phone))
        self.conn.commit()
        messagebox.showinfo("Success", "User Added Successfully")
        self.create_admin_panel()

    def list_users(self):
        self.cursor.execute("SELECT * FROM users")
        users = self.cursor.fetchall()

        user_list_window = tk.Toplevel(self.root)
        user_list_window.title("Users List")

        tk.Label(user_list_window, text="Users", font=("Arial", 16, "bold"), fg="#FF6F61", bg="#2E3B4E").pack(pady=10)

        

        # Create treeview for displaying users
        tree = ttk.Treeview(user_list_window, columns=("ID", "Username", "Password", "Email", "Phone"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Username", text="Username")
        tree.heading("Password", text="Password")
        tree.heading("Email", text="Email")
        tree.heading("Phone", text="Phone")
        
        
        tree.column("ID", width=100, anchor="center")
        tree.column("Username", width=100, anchor="center")
        tree.column("Password", width=200, anchor="center")
        tree.column("Email", width=200, anchor="center")
        tree.column("Phone", width=200, anchor="center")
        

        for user in users:
            tree.insert("", tk.END, values=(user[0], user[1], user[2], user[3], user[4]))

        tree.pack(pady=10)  # Use pack instead of grid for the tree

    # Create frame to hold the update and delete buttons
        button_frame = tk.Frame(user_list_window)
        button_frame.pack(pady=10)  # Use pack for the button frame

    # Function to update the selected user
        def update_selected_user():
            selected_item = tree.selection()
            if selected_item:
                user_id = tree.item(selected_item, "values")[0]
                self.update_user(user_id)  # You can use your existing update_user function

    # Function to delete the selected user
        def delete_selected_user():
            selected_item = tree.selection()
            if selected_item:
                user_id = tree.item(selected_item, "values")[0]
                self.delete_user(user_id)  # You can use your existing delete_user function

    # Create update and delete buttons for the selected user
        update_button = tk.Button(button_frame, text="Update Selected", command=update_selected_user)
        update_button.pack(side="left", padx=10, pady=5)

        delete_button = tk.Button(button_frame, text="Delete Selected", command=delete_selected_user)
        delete_button.pack(side="left", padx=10, pady=5)

    # Create close button at the bottom of the window
        close_button = tk.Button(user_list_window, text="Close", command=user_list_window.destroy, font=("Arial", 14))
        close_button.pack(pady=5)

    def update_user(self, user_id):
        # Open a new window to update user details
        update_window = tk.Toplevel(self.root)
        update_window.title("Update User")

        # Get user details
        self.cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = self.cursor.fetchone()

        # Create fields to update user details
        username_label = tk.Label(update_window, text="Username:", font=("Arial", 12), bg="#FFFFFF")
        username_label.grid(row=0, column=0, padx=10, pady=10)
        username_entry = tk.Entry(update_window, font=("Arial", 12))
        username_entry.insert(0, user[1])  # Pre-fill with current username
        username_entry.grid(row=0, column=1, padx=10, pady=10)

        password_label = tk.Label(update_window, text="Password:", font=("Arial", 12), bg="#FFFFFF")
        password_label.grid(row=1, column=0, padx=10, pady=10)
        password_entry = tk.Entry(update_window, font=("Arial", 12), show="*")
        password_entry.insert(0, user[2])  # Pre-fill with current password
        password_entry.grid(row=1, column=1, padx=10, pady=10)

        email_label = tk.Label(update_window, text="Email:", font=("Arial", 12), bg="#FFFFFF")
        email_label.grid(row=2, column=0, padx=10, pady=10)
        email_entry = tk.Entry(update_window, font=("Arial", 12))
        email_entry.insert(0, user[3])  # Pre-fill with current email
        email_entry.grid(row=2, column=1, padx=10, pady=10)

        phone_label = tk.Label(update_window, text="Phone Number:", font=("Arial", 12), bg="#FFFFFF")
        phone_label.grid(row=3, column=0, padx=10, pady=10)
        phone_entry = tk.Entry(update_window, font=("Arial", 12))
        phone_entry.insert(0, user[4])  # Pre-fill with current phone number
        phone_entry.grid(row=3, column=1, padx=10, pady=10)

        def save_update():
            username = username_entry.get()
            password = password_entry.get()
            email = email_entry.get()
            phone = phone_entry.get()

            # Call the method to update the user data in the database
            self.cursor.execute("""
                UPDATE users
                SET username = %s, password = %s, email = %s, phone_number = %s
                WHERE id = %s
            """, (username, password, email, phone, user_id))
            self.conn.commit()
            messagebox.showinfo("Success", "User Updated Successfully")
            update_window.destroy()  # Close the update window

        save_button = tk.Button(update_window, text="Save", command=save_update, font=("Arial", 14), bg="#4F81BD", fg="white")
        save_button.grid(row=4, columnspan=2, pady=20)

    def delete_user(self, user_id):
        confirm = messagebox.askyesno("Delete User", "Are you sure you want to delete this user?")
        if confirm:
            self.cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
            self.conn.commit()
            messagebox.showinfo("Success", "User Deleted Successfully")
            self.create_admin_panel()  # Refresh admin panel after deletion



    
    # Manage Albums
    def add_album(self):
        self.open_album_input_window("Add Album", self.insert_album)

    def open_album_input_window(self, title, insert_method):
        input_window = tk.Toplevel(self.root)
        input_window.title(title)

        # Album Name input
        album_name_label = tk.Label(input_window, text="Album Name:", font=("Arial", 12))
        album_name_label.grid(row=0, column=0, padx=10, pady=10)
        album_name_entry = tk.Entry(input_window, font=("Arial", 12))
        album_name_entry.grid(row=0, column=1, padx=10, pady=10)

        # Release Year input
        album_image_label = tk.Label(input_window, text="Album Image Path:", font=("Arial", 12))
        album_image_label.grid(row=2, column=0, padx=10, pady=10)
        album_image_entry = tk.Entry(input_window, font=("Arial", 12))
        album_image_entry.grid(row=2, column=1, padx=10, pady=10)

        # Submit button
        submit_button = tk.Button(input_window, text="Submit", command=lambda: insert_method(album_name_entry.get(), album_image_entry.get()), font=("Arial", 14))
        submit_button.grid(row=3, columnspan=2, pady=20)

    def insert_album(self, album_name, album_image):
        if not album_image:
            album_image = None
        self.cursor.execute("INSERT INTO albums (album_name, album_image) VALUES (%s, %s)", (album_name,album_image))
        self.conn.commit()
        messagebox.showinfo("Success", "Album Added Successfully")
        self.create_admin_panel()

    def list_albums(self):
        self.cursor.execute("SELECT * FROM albums")
        albums = self.cursor.fetchall()

        album_list_window = tk.Toplevel(self.root)
        album_list_window.title("Albums List")

        tk.Label(album_list_window, text="Albums", font=("Arial", 16, "bold"), fg="#FF6F61", bg="#2E3B4E").pack(pady=10)

    # Create treeview for displaying albums
        tree = ttk.Treeview(album_list_window, columns=("ID", "Name", "Image"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("Image", text="Image")

        tree.column("ID", width=100, anchor="center")
        tree.column("Name", width=100, anchor="center")
        tree.column("Image", width=200, anchor="center")

    # Insert albums into the treeview
        for album in albums:
            tree.insert("", tk.END, values=(album[0], album[1], album[2] if album[2] else "No Image"))

        tree.pack(pady=10)

    # Create frame to hold the update and delete buttons
        button_frame = tk.Frame(album_list_window)
        button_frame.pack(pady=10)

    # Function to update the selected album
        def update_selected_album():
            selected_item = tree.selection()
            if selected_item:
                album_id = tree.item(selected_item, "values")[0]
                self.update_album(album_id)  # Use your existing update_album function

    # Function to delete the selected album
        def delete_selected_album():
            selected_item = tree.selection()
            if selected_item:
                album_id = tree.item(selected_item, "values")[0]
                self.delete_album(album_id)  # Use your existing delete_album function

    # Create update and delete buttons for the selected album
        update_button = tk.Button(button_frame, text="Update Selected", command=update_selected_album)
        update_button.pack(side="left", padx=10, pady=5)

        delete_button = tk.Button(button_frame, text="Delete Selected", command=delete_selected_album)
        delete_button.pack(side="left", padx=10, pady=5)

    # Create close button at the bottom of the window
        close_button = tk.Button(album_list_window, text="Close", command=album_list_window.destroy, font=("Arial", 14))
        close_button.pack(pady=5)

    def update_album(self, album_id):
    # Open a new window to update album details
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Album")

    # Get album details
        self.cursor.execute("SELECT * FROM albums WHERE album_id = %s", (album_id,))
        album = self.cursor.fetchone()

    # Create fields to update album details
        name_label = tk.Label(update_window, text="Album Name:", font=("Arial", 12), bg="#FFFFFF")
        name_label.grid(row=0, column=0, padx=10, pady=10)
        name_entry = tk.Entry(update_window, font=("Arial", 12))
        name_entry.insert(0, album[1])  # Pre-fill with current album name
        name_entry.grid(row=0, column=1, padx=10, pady=10)

        image_label = tk.Label(update_window, text="Image:", font=("Arial", 12), bg="#FFFFFF")
        image_label.grid(row=1, column=0, padx=10, pady=10)
        image_entry = tk.Entry(update_window, font=("Arial", 12))
        image_entry.insert(0, album[2])  # Pre-fill with current album image (or empty if none)
        image_entry.grid(row=1, column=1, padx=10, pady=10)

        def save_update():
            name = name_entry.get()
            image = image_entry.get()

        # Call the method to update the album data in the database
            self.cursor.execute("""
                UPDATE albums
                SET album_name = %s, album_image = %s
                WHERE album_id = %s
            """, (name, image, album_id))
            self.conn.commit()
            messagebox.showinfo("Success", "Album Updated Successfully")
            update_window.destroy()  # Close the update window

        save_button = tk.Button(update_window, text="Save", command=save_update, font=("Arial", 14), bg="#4F81BD", fg="white")
        save_button.grid(row=2, columnspan=2, pady=20)

    def delete_album(self, album_id):
        confirm = messagebox.askyesno("Delete Album", "Are you sure you want to delete this album?")
        if confirm:
            self.cursor.execute("DELETE FROM albums WHERE album_id = %s", (album_id,))
            self.conn.commit()
            messagebox.showinfo("Success", "Album Deleted Successfully")
            self.create_admin_panel()  # Refresh admin panel after deletion

    # Manage Categories
    def add_category(self):
        self.open_category_input_window("Add Category", self.insert_category)

    def open_category_input_window(self, title, insert_method):
        input_window = tk.Toplevel(self.root)
        input_window.title(title)

        # Category Name input
        category_name_label = tk.Label(input_window, text="Category Name:", font=("Arial", 12))
        category_name_label.grid(row=0, column=0, padx=10, pady=10)
        category_name_entry = tk.Entry(input_window, font=("Arial", 12))
        category_name_entry.grid(row=0, column=1, padx=10, pady=10)

        # Submit button
        submit_button = tk.Button(input_window, text="Submit", command=lambda: insert_method(category_name_entry.get()), font=("Arial", 14))
        submit_button.grid(row=1, columnspan=2, pady=20)

    def list_categories(self):
        self.cursor.execute("SELECT * FROM categories")
        categories = self.cursor.fetchall()

        category_list_window = tk.Toplevel(self.root)
        category_list_window.title("Categories List")

        tk.Label(category_list_window, text="Categories", font=("Arial", 16, "bold"), fg="#FF6F61", bg="#2E3B4E").pack(pady=10)

    # Create treeview for displaying categories
        tree = ttk.Treeview(category_list_window, columns=("ID", "Name"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Name", text="Name")

        tree.column("ID", width=100, anchor="center")
        tree.column("Name", width=200, anchor="center")

    # Insert categories into the treeview
        for category in categories:
            tree.insert("", tk.END, values=(category[0], category[1]))

        tree.pack(pady=10)

    # Create frame to hold the update and delete buttons
        button_frame = tk.Frame(category_list_window)
        button_frame.pack(pady=10)

    # Function to update the selected category
        def update_selected_category():
            selected_item = tree.selection()
            if selected_item:
                category_id = tree.item(selected_item, "values")[0]
                self.update_category(category_id)  # Call the update_category function

    # Function to delete the selected category
        def delete_selected_category():
            selected_item = tree.selection()
            if selected_item:
                category_id = tree.item(selected_item, "values")[0]
                self.delete_category(category_id)  # Call the delete_category function

    # Create update and delete buttons for the selected category
        update_button = tk.Button(button_frame, text="Update Selected", command=update_selected_category)
        update_button.pack(side="left", padx=10, pady=5)

        delete_button = tk.Button(button_frame, text="Delete Selected", command=delete_selected_category)
        delete_button.pack(side="left", padx=10, pady=5)

    # Create close button at the bottom of the window
        close_button = tk.Button(category_list_window, text="Close", command=category_list_window.destroy, font=("Arial", 14))
        close_button.pack(pady=5)

    def update_category(self, category_id):
    # Open a new window to update category details
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Category")

    # Get category details
        self.cursor.execute("SELECT * FROM categories WHERE category_id = %s", (category_id,))
        category = self.cursor.fetchone()

    # Create fields to update category details
        name_label = tk.Label(update_window, text="Category Name:", font=("Arial", 12), bg="#FFFFFF")
        name_label.grid(row=0, column=0, padx=10, pady=10)
        name_entry = tk.Entry(update_window, font=("Arial", 12))
        name_entry.insert(0, category[1])  # Pre-fill with current category name
        name_entry.grid(row=0, column=1, padx=10, pady=10)

        def save_update():
            category_name = name_entry.get()

        # Call the method to update the category data in the database
            self.cursor.execute("""
                UPDATE categories
                SET category_name = %s
                WHERE category_id = %s
            """, (category_name, category_id))
            self.conn.commit()
            messagebox.showinfo("Success", "Category Updated Successfully")
            update_window.destroy()  # Close the update window

        save_button = tk.Button(update_window, text="Save", command=save_update, font=("Arial", 14), bg="#4F81BD", fg="white")
        save_button.grid(row=1, columnspan=2, pady=20)

    def delete_category(self, category_id):
        confirm = messagebox.askyesno("Delete Category", "Are you sure you want to delete this category?")
        if confirm:
            self.cursor.execute("DELETE FROM categories WHERE category_id = %s", (category_id,))
            self.conn.commit()
            messagebox.showinfo("Success", "Category Deleted Successfully")
            self.create_admin_panel()  # Refresh admin panel after deletion


    # Manage Songs in Albums
    def add_song_of_neha(self):
        self.open_song_to_album_input_window("Add Song", self.insert_song_of_neha)

    def open_song_to_album_input_window(self, title, insert_method):
        input_window = tk.Toplevel(self.root)
        input_window.title(title)

    # Album input (Textbox to enter album ID or name manually)
        category_label = tk.Label(input_window, text="Album Id:", font=("Arial", 12))
        category_label.grid(row=1, column=0, padx=10, pady=10)
        category_entry = tk.Entry(input_window, font=("Arial", 12))
    
    # Fetch albums from the database and display in the entry as a list
        self.cursor.execute("SELECT album_id, album_name FROM albums")
        albums = self.cursor.fetchall()
        album_list = [f"{album[0]} - {album[1]}" for album in albums]
        album_entry.insert(0, ", ".join(album_list))  # Insert the list of albums into the textbox
        album_entry.grid(row=1, column=1, padx=10, pady=10)

    
        song_path_label = tk.Label(input_window, text="Song Path:", font=("Arial", 12))
        song_path_label.grid(row=3, column=0, padx=10, pady=10)
        path_entry = tk.Entry(input_window, font=("Arial", 12))
        path_entry.grid(row=3, column=1, padx=10, pady=10)


     # Submit button
        submit_button = tk.Button(input_window, text="Submit", command=lambda: insert_method(album_entry.get(), path_entry.get()), font=("Arial", 14))
        submit_button.grid(row=4, columnspan=2, pady=20)

    def select_song_file(self, input_window):
        # Open a file dialog to choose the song file
        self.selected_song_path = filedialog.askopenfilename(title="Select Song File", filetypes=(("Audio files", "*.mp3;*.ogg;*.wav"), ("All files", "*.*")))
        if self.selected_song_path:
            messagebox.showinfo("Song Selected", "Song file selected successfully")



    def insert_song_of_neha(self,album_id,song_path):
        
        self.cursor.execute("INSERT INTO neha_songs(album_id,song_path) VALUES (%s, %s)", (album_id,song_path))
        self.conn.commit()
        messagebox.showinfo("Success", "Song Added Successfully")
        self.create_admin_panel()

    def list_songs_of_neha(self):
        # Execute SQL to fetch the songs
        self.cursor.execute("SELECT * FROM neha_songs")
        gujarati_songs = self.cursor.fetchall()

    # Create a new window for displaying the list
        song_list_window = tk.Toplevel(self.root)
        song_list_window.title("Songs in Category List")

    # Label for the window
        tk.Label(song_list_window, text="Gujarati Songs", font=("Arial", 16, "bold"), fg="#FF6F61", bg="#2E3B4E").pack(pady=10)

    # Create a Treeview widget for displaying songs
        tree = ttk.Treeview(song_list_window, columns=("Song ID", "Album ID", "Song Path"), show="headings")

    # Set headings
        tree.heading("Song ID", text="Song ID")
        tree.heading("Album ID", text="Album ID")
        tree.heading("Song Path", text="Song Path")

    # Set column widths
        tree.column("Song ID", width=100, anchor="center")
        tree.column("Album ID", width=100, anchor="center")
        tree.column("Song Path", width=800, anchor="w")

    # Insert data into the treeview
        for song in gujarati_songs:
            tree.insert("", tk.END, values=(song[0], song[1], song[2]))

        tree.pack(pady=10)

    # Create frame to hold the update and delete buttons
        button_frame = tk.Frame(song_list_window)
        button_frame.pack(pady=10)

    # Function to update the selected song
        def update_selected_song():
            selected_item = tree.selection()
            if selected_item:
                song_id = tree.item(selected_item, "values")[0]
                self.update_song_of_neha(song_id)  # Call the update_song_of_neha function

    # Function to delete the selected song
        def delete_selected_song():
            selected_item = tree.selection()
            if selected_item:
                song_id = tree.item(selected_item, "values")[0]
                self.delete_song_of_neha(song_id)  # Call the delete_song_of_neha function

    # Create update and delete buttons for the selected song
        update_button = tk.Button(button_frame, text="Update Selected", command=update_selected_song)
        update_button.pack(side="left", padx=10, pady=5)

        delete_button = tk.Button(button_frame, text="Delete Selected", command=delete_selected_song)
        delete_button.pack(side="left", padx=10, pady=5)

    # Create close button at the bottom of the window
        close_button = tk.Button(song_list_window, text="Close", command=song_list_window.destroy, font=("Arial", 14))
        close_button.pack(pady=5)

    def update_song_of_neha(self, song_id):
    # Open a new window to update song details
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Song")

    # Get song details
        self.cursor.execute("SELECT * FROM neha_songs WHERE song_id = %s", (song_id,))
        song = self.cursor.fetchone()

    # Create fields to update song details
        song_path_label = tk.Label(update_window, text="Song Path:", font=("Arial", 12), bg="#FFFFFF")
        song_path_label.grid(row=0, column=0, padx=10, pady=10)
        song_path_entry = tk.Entry(update_window, font=("Arial", 12))
        song_path_entry.insert(0, song[2])  # Pre-fill with current song path
        song_path_entry.grid(row=0, column=1, padx=10, pady=10)

        def save_update():
            song_path = song_path_entry.get()

        # Call the method to update the song data in the database
            self.cursor.execute("""
                UPDATE neha_songs
                SET song_path = %s
                WHERE song_id = %s
            """, (song_path, song_id))
            self.conn.commit()
            messagebox.showinfo("Success", "Song Updated Successfully")
            update_window.destroy()  # Close the update window

        save_button = tk.Button(update_window, text="Save", command=save_update, font=("Arial", 14), bg="#4F81BD", fg="white")
        save_button.grid(row=1, columnspan=2, pady=20)

    def delete_song_of_neha(self, song_id):
        confirm = messagebox.askyesno("Delete Song", "Are you sure you want to delete this song?")
        if confirm:
            self.cursor.execute("DELETE FROM neha_songs WHERE song_id = %s", (song_id,))
            self.conn.commit()
            messagebox.showinfo("Success", "Song Deleted Successfully")
            self.create_admin_panel()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #manage songs of shreya
    def add_song_of_shreya(self):
        self.open_song_to_album_input_window("Add Song to Album", self.insert_song_of_shreya)

    def open_song_to_album_input_window(self, title, insert_method):
        input_window = tk.Toplevel(self.root)
        input_window.title(title)

    # Album input (Textbox to enter album ID or name manually)
        album_label = tk.Label(input_window, text="Album Id:", font=("Arial", 12))
        album_label.grid(row=1, column=0, padx=10, pady=10)
        album_entry = tk.Entry(input_window, font=("Arial", 12))
    
    # Fetch albums from the database and display in the entry as a list
        self.cursor.execute("SELECT album_id, album_name FROM albums")
        albums = self.cursor.fetchall()
        album_list = [f"{album[0]} - {album[1]}" for album in albums]
        album_entry.insert(0, ", ".join(album_list))  # Insert the list of albums into the textbox
        album_entry.grid(row=1, column=1, padx=10, pady=10)

    
        song_path_label = tk.Label(input_window, text="Song Path:", font=("Arial", 12))
        song_path_label.grid(row=3, column=0, padx=10, pady=10)
        path_entry = tk.Entry(input_window, font=("Arial", 12))
        path_entry.grid(row=3, column=1, padx=10, pady=10)


     # Submit button
        submit_button = tk.Button(input_window, text="Submit", command=lambda: insert_method(album_entry.get(), path_entry.get()), font=("Arial", 14))
        submit_button.grid(row=4, columnspan=2, pady=20)

    def select_song_file(self, input_window):
        # Open a file dialog to choose the song file
        self.selected_song_path = filedialog.askopenfilename(title="Select Song File", filetypes=(("Audio files", "*.mp3;*.ogg;*.wav"), ("All files", "*.*")))
        if self.selected_song_path:
            messagebox.showinfo("Song Selected", "Song file selected successfully")



    def insert_song_of_shreya(self,album_id,song_path):
        
        self.cursor.execute("INSERT INTO shreya_songs(album_id,song_path) VALUES (%s, %s)", (album_id,song_path))
        self.conn.commit()
        messagebox.showinfo("Success", "Song Added to Album Successfully")
        self.create_admin_panel()

    def list_songs_of_shreya(self):
        # Execute SQL to fetch the songs in albums
        self.cursor.execute("SELECT * FROM shreya_songs")
        songs_of_shreya = self.cursor.fetchall()

    # Create a new window for displaying the list
        song_list_window = tk.Toplevel(self.root)
        song_list_window.title("Songs in Albums List")

    # Label for the window
        tk.Label(song_list_window, text="Songs of Shreya", font=("Arial", 16, "bold"), fg="#FF6F61", bg="#2E3B4E").pack(pady=10)

    # Create a Treeview widget
        tree = ttk.Treeview(song_list_window, columns=("Song ID", "Album ID", "Song Path"), show="headings")

    # Set headings
        tree.heading("Song ID", text="Song ID")
        tree.heading("Album ID", text="Album ID")
        tree.heading("Song Path", text="Song Path")

    # Set column widths if necessary
        tree.column("Song ID", width=100, anchor="center")
        tree.column("Album ID", width=100, anchor="center")
        tree.column("Song Path", width=800, anchor="w")

    # Insert data into the tree
        for song in songs_of_shreya:
            tree.insert("", tk.END, values=(song[0], song[1], song[2]))

        tree.pack(pady=10)

    # Create a frame for update and delete buttons
        button_frame = tk.Frame(song_list_window)
        button_frame.pack(pady=10)

    # Function to update the selected song
        def update_selected_song():
            selected_item = tree.selection()
            if selected_item:
                song_id = tree.item(selected_item, "values")[0]
                self.update_song_of_shreya(song_id)  # Call the update method for the selected song

    # Function to delete the selected song
        def delete_selected_song():
            selected_item = tree.selection()
            if selected_item:
                song_id = tree.item(selected_item, "values")[0]
                self.delete_song_of_shreya(song_id)  # Call the delete method for the selected song

    # Create Update and Delete buttons for the selected song
        update_button = tk.Button(button_frame, text="Update Selected", command=update_selected_song)
        update_button.pack(side="left", padx=10, pady=5)

        delete_button = tk.Button(button_frame, text="Delete Selected", command=delete_selected_song)
        delete_button.pack(side="left", padx=10, pady=5)

    # Create close button at the bottom of the window
        close_button = tk.Button(song_list_window, text="Close", command=song_list_window.destroy, font=("Arial", 14))
        close_button.pack(pady=10)

    def update_song_of_shreya(self, song_id):
        # Open a new window to update song details
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Song")

    # Get song details
        self.cursor.execute("SELECT * FROM shreya_songs WHERE song_id = %s", (song_id,))
        song = self.cursor.fetchone()

    # Create fields to update song details
        album_id_label = tk.Label(update_window, text="Album ID:", font=("Arial", 12), bg="#FFFFFF")
        album_id_label.grid(row=0, column=0, padx=10, pady=10)
        album_id_entry = tk.Entry(update_window, font=("Arial", 12))
        album_id_entry.insert(0, song[1])  # Pre-fill with current album ID
        album_id_entry.grid(row=0, column=1, padx=10, pady=10)

        song_path_label = tk.Label(update_window, text="Song Path:", font=("Arial", 12), bg="#FFFFFF")
        song_path_label.grid(row=1, column=0, padx=10, pady=10)
        song_path_entry = tk.Entry(update_window, font=("Arial", 12))
        song_path_entry.insert(0, song[2])  # Pre-fill with current song path
        song_path_entry.grid(row=1, column=1, padx=10, pady=10)

        def save_update():
            album_id = album_id_entry.get()
            song_path = song_path_entry.get()

        # Call the method to update the song data in the database
            self.cursor.execute("""
                UPDATE shreya_songs
                SET album_id = %s, song_path = %s
                WHERE song_id = %s
            """, (album_id, song_path, song_id))
            self.conn.commit()
            messagebox.showinfo("Success", "Song Updated Successfully")
            update_window.destroy()  # Close the update window

        save_button = tk.Button(update_window, text="Save", command=save_update, font=("Arial", 14), bg="#4F81BD", fg="white")
        save_button.grid(row=2, columnspan=2, pady=20)

    def delete_song_of_shreya(self, song_id):
        confirm = messagebox.askyesno("Delete Song from Album", "Are you sure you want to delete this song?")
        if confirm:
            self.cursor.execute("DELETE FROM shreya_songs WHERE song_id = %s", (song_id,))
            self.conn.commit()
            messagebox.showinfo("Success", "Song Deleted from Album Successfully")
            self.create_admin_panel()  # Refresh admin panel after deletion




    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Manage songs of arijit
    def add_song_of_arijit(self):
        self.open_song_to_album_input_window("Add Song to Album", self.insert_song_of_arijit)

    def open_song_to_album_input_window(self, title, insert_method):
        input_window = tk.Toplevel(self.root)
        input_window.title(title)

    # Album input (Textbox to enter album ID or name manually)
        album_label = tk.Label(input_window, text="Album Id:", font=("Arial", 12))
        album_label.grid(row=1, column=0, padx=10, pady=10)
        album_entry = tk.Entry(input_window, font=("Arial", 12))
    
    # Fetch albums from the database and display in the entry as a list
        self.cursor.execute("SELECT album_id, album_name FROM albums")
        albums = self.cursor.fetchall()
        album_list = [f"{album[0]} - {album[1]}" for album in albums]
        album_entry.insert(0, ", ".join(album_list))  # Insert the list of albums into the textbox
        album_entry.grid(row=1, column=1, padx=10, pady=10)

    
        song_path_label = tk.Label(input_window, text="Song Path:", font=("Arial", 12))
        song_path_label.grid(row=3, column=0, padx=10, pady=10)
        path_entry = tk.Entry(input_window, font=("Arial", 12))
        path_entry.grid(row=3, column=1, padx=10, pady=10)


     # Submit button
        submit_button = tk.Button(input_window, text="Submit", command=lambda: insert_method(album_entry.get(), path_entry.get()), font=("Arial", 14))
        submit_button.grid(row=4, columnspan=2, pady=20)

    def select_song_file(self, input_window):
        # Open a file dialog to choose the song file
        self.selected_song_path = filedialog.askopenfilename(title="Select Song File", filetypes=(("Audio files", "*.mp3;*.ogg;*.wav"), ("All files", "*.*")))
        if self.selected_song_path:
            messagebox.showinfo("Song Selected", "Song file selected successfully")



    def insert_song_of_arijit(self,album_id,song_path):
        
        self.cursor.execute("INSERT INTO arijit_songs(album_id,song_path) VALUES (%s, %s)", (album_id,song_path))
        self.conn.commit()
        messagebox.showinfo("Success", "Song Added to Album Successfully")
        self.create_admin_panel()

    def list_songs_of_arijit(self):
    # Execute SQL to fetch the songs in albums
        self.cursor.execute("SELECT * FROM arijit_songs")
        songs_of_arijit = self.cursor.fetchall()

    # Create a new window for displaying the list
        song_list_window = tk.Toplevel(self.root)
        song_list_window.title("Songs in Albums List")

    # Label for the window
        tk.Label(song_list_window, text="Songs of Arijit", font=("Arial", 16, "bold"), fg="#FF6F61", bg="#2E3B4E").pack(pady=10)

    # Create a Treeview widget
        tree = ttk.Treeview(song_list_window, columns=("Song ID", "Album ID", "Song Path"), show="headings")

    # Set headings
        tree.heading("Song ID", text="Song ID")
        tree.heading("Album ID", text="Album ID")
        tree.heading("Song Path", text="Song Path")

    # Set column widths if necessary
        tree.column("Song ID", width=100, anchor="center")
        tree.column("Album ID", width=100, anchor="center")
        tree.column("Song Path", width=800, anchor="w")

    # Insert data into the tree
        for song in songs_of_arijit:
            tree.insert("", tk.END, values=(song[0], song[1], song[2]))

        tree.pack(pady=10)

    # Create a frame for update and delete buttons
        button_frame = tk.Frame(song_list_window)
        button_frame.pack(pady=10)

    # Function to update the selected song
        def update_selected_song():
            selected_item = tree.selection()
            if selected_item:
                song_id = tree.item(selected_item, "values")[0]
                self.update_song_of_arijit(song_id)  # Call the update method for the selected song

    # Function to delete the selected song
        def delete_selected_song():
            selected_item = tree.selection()
            if selected_item:
                song_id = tree.item(selected_item, "values")[0]
                self.delete_song_of_arijit(song_id)  # Call the delete method for the selected song
    
    # Create Update and Delete buttons for the selected song
        update_button = tk.Button(button_frame, text="Update Selected", command=update_selected_song)
        update_button.pack(side="left", padx=10, pady=5)

        delete_button = tk.Button(button_frame, text="Delete Selected", command=delete_selected_song)
        delete_button.pack(side="left", padx=10, pady=5)

    # Create close button at the bottom of the window
        close_button = tk.Button(song_list_window, text="Close", command=song_list_window.destroy, font=("Arial", 14))
        close_button.pack(pady=10)

    def update_song_of_arijit(self, song_id):
    # Open a new window to update song details
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Song")

    # Get song details
        self.cursor.execute("SELECT * FROM arijit_songs WHERE song_id = %s", (song_id,))
        song = self.cursor.fetchone()

    # Create fields to update song details
        album_id_label = tk.Label(update_window, text="Album ID:", font=("Arial", 12), bg="#FFFFFF")
        album_id_label.grid(row=0, column=0, padx=10, pady=10)
        album_id_entry = tk.Entry(update_window, font=("Arial", 12))
        album_id_entry.insert(0, song[1])  # Pre-fill with current album ID
        album_id_entry.grid(row=0, column=1, padx=10, pady=10)

        song_path_label = tk.Label(update_window, text="Song Path:", font=("Arial", 12), bg="#FFFFFF")
        song_path_label.grid(row=1, column=0, padx=10, pady=10)
        song_path_entry = tk.Entry(update_window, font=("Arial", 12))
        song_path_entry.insert(0, song[2])  # Pre-fill with current song path
        song_path_entry.grid(row=1, column=1, padx=10, pady=10)

        def save_update():
            album_id = album_id_entry.get()
            song_path = song_path_entry.get()

        # Call the method to update the song data in the database
            self.cursor.execute("""
                UPDATE arijit_songs
                SET album_id = %s, song_path = %s
                WHERE song_id = %s
            """, (album_id, song_path, song_id))
            self.conn.commit()
            messagebox.showinfo("Success", "Song Updated Successfully")
            update_window.destroy()  # Close the update window

        save_button = tk.Button(update_window, text="Save", command=save_update, font=("Arial", 14), bg="#4F81BD", fg="white")
        save_button.grid(row=2, columnspan=2, pady=20)

    def delete_song_of_arijit(self, song_id):
        confirm = messagebox.askyesno("Delete Song from Album", "Are you sure you want to delete this song?")
        if confirm:
            self.cursor.execute("DELETE FROM arijit_songs WHERE song_id = %s", (song_id,))
            self.conn.commit()
            messagebox.showinfo("Success", "Song Deleted from Album Successfully")
            self.create_admin_panel()  # Refresh admin panel after deletion


    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #manage songs of Rehman
    def add_song_of_rehman(self):
        self.open_song_to_album_input_window("Add Song to Album", self.insert_song_of_rehman)

    def open_song_to_album_input_window(self, title, insert_method):
        input_window = tk.Toplevel(self.root)
        input_window.title(title)

    # Album input (Textbox to enter album ID or name manually)
        album_label = tk.Label(input_window, text="Album Id:", font=("Arial", 12))
        album_label.grid(row=1, column=0, padx=10, pady=10)
        album_entry = tk.Entry(input_window, font=("Arial", 12))
    
    # Fetch albums from the database and display in the entry as a list
        self.cursor.execute("SELECT album_id, album_name FROM albums")
        albums = self.cursor.fetchall()
        album_list = [f"{album[0]} - {album[1]}" for album in albums]
        album_entry.insert(0, ", ".join(album_list))  # Insert the list of albums into the textbox
        album_entry.grid(row=1, column=1, padx=10, pady=10)

    
        song_path_label = tk.Label(input_window, text="Song Path:", font=("Arial", 12))
        song_path_label.grid(row=3, column=0, padx=10, pady=10)
        path_entry = tk.Entry(input_window, font=("Arial", 12))
        path_entry.grid(row=3, column=1, padx=10, pady=10)


     # Submit button
        submit_button = tk.Button(input_window, text="Submit", command=lambda: insert_method(album_entry.get(), path_entry.get()), font=("Arial", 14))
        submit_button.grid(row=4, columnspan=2, pady=20)

    def select_song_file(self, input_window):
        # Open a file dialog to choose the song file
        self.selected_song_path = filedialog.askopenfilename(title="Select Song File", filetypes=(("Audio files", "*.mp3;*.ogg;*.wav"), ("All files", "*.*")))
        if self.selected_song_path:
            messagebox.showinfo("Song Selected", "Song file selected successfully")



    def insert_song_of_rehman(self,album_id,song_path):
        
        self.cursor.execute("INSERT INTO rehman_songs(album_id,song_path) VALUES (%s, %s)", (album_id,song_path))
        self.conn.commit()
        messagebox.showinfo("Success", "Song Added to Album Successfully")
        self.create_admin_panel()

    def list_songs_of_rehman(self):
    # Execute SQL to fetch the songs in albums
        self.cursor.execute("SELECT * FROM rehman_songs")
        songs_of_rehman = self.cursor.fetchall()

    # Create a new window for displaying the list
        song_list_window = tk.Toplevel(self.root)
        song_list_window.title("Songs in Albums List")

    # Label for the window
        tk.Label(song_list_window, text="Songs of rehman", font=("Arial", 16, "bold"), fg="#FF6F61", bg="#2E3B4E").pack(pady=10)

    # Create a Treeview widget
        tree = ttk.Treeview(song_list_window, columns=("Song ID", "Album ID", "Song Path"), show="headings")

    # Set headings
        tree.heading("Song ID", text="Song ID")
        tree.heading("Album ID", text="Album ID")
        tree.heading("Song Path", text="Song Path")

        # Set column widths if necessary
        tree.column("Song ID", width=100, anchor="center")
        tree.column("Album ID", width=100, anchor="center")
        tree.column("Song Path", width=800, anchor="w")

    # Insert data into the tree
        for song in songs_of_rehman:
            tree.insert("", tk.END, values=(song[0], song[1], song[2]))

        tree.pack(pady=10)

    # Create a frame for update and delete buttons
        button_frame = tk.Frame(song_list_window)
        button_frame.pack(pady=10)

    # Function to update the selected song
        def update_selected_song():
            selected_item = tree.selection()
            if selected_item:
                song_id = tree.item(selected_item, "values")[0]
                self.update_song_of_rehman(song_id)  # Call the update method for the selected song

    # Function to delete the selected song
        def delete_selected_song():
            selected_item = tree.selection()
            if selected_item:
                song_id = tree.item(selected_item, "values")[0]
                self.delete_song_of_rehman(song_id)  # Call the delete method for the selected song

    # Create Update and Delete buttons for the selected song
        update_button = tk.Button(button_frame, text="Update Selected", command=update_selected_song)
        update_button.pack(side="left", padx=10, pady=5)

        delete_button = tk.Button(button_frame, text="Delete Selected", command=delete_selected_song)
        delete_button.pack(side="left", padx=10, pady=5)

    # Create close button at the bottom of the window
        close_button = tk.Button(song_list_window, text="Close", command=song_list_window.destroy, font=("Arial", 14))
        close_button.pack(pady=10)

    def update_song_of_rehman(self, song_id):
        # Open a new window to update song details
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Song")

    # Get song details
        self.cursor.execute("SELECT * FROM rehman_songs WHERE song_id = %s", (song_id,))
        song = self.cursor.fetchone()

    # Create fields to update song details
        album_id_label = tk.Label(update_window, text="Album ID:", font=("Arial", 12), bg="#FFFFFF")
        album_id_label.grid(row=0, column=0, padx=10, pady=10)
        album_id_entry = tk.Entry(update_window, font=("Arial", 12))
        album_id_entry.insert(0, song[1])  # Pre-fill with current album ID
        album_id_entry.grid(row=0, column=1, padx=10, pady=10)

        song_path_label = tk.Label(update_window, text="Song Path:", font=("Arial", 12), bg="#FFFFFF")
        song_path_label.grid(row=1, column=0, padx=10, pady=10)
        song_path_entry = tk.Entry(update_window, font=("Arial", 12))
        song_path_entry.insert(0, song[2])  # Pre-fill with current song path
        song_path_entry.grid(row=1, column=1, padx=10, pady=10)

        def save_update():
            album_id = album_id_entry.get()
            song_path = song_path_entry.get()

        # Call the method to update the song data in the database
            self.cursor.execute("""
                UPDATE rehman_songs
                SET album_id = %s, song_path = %s
                WHERE song_id = %s
            """, (album_id, song_path, song_id))
            self.conn.commit()
            messagebox.showinfo("Success", "Song Updated Successfully")
            update_window.destroy()  # Close the update window

        save_button = tk.Button(update_window, text="Save", command=save_update, font=("Arial", 14), bg="#4F81BD", fg="white")
        save_button.grid(row=2, columnspan=2, pady=20)

    def delete_song_of_rehman(self, song_id):
        confirm = messagebox.askyesno("Delete Song from Album", "Are you sure you want to delete this song?")
        if confirm:
            self.cursor.execute("DELETE FROM rehman_songs WHERE song_id = %s", (song_id,))
            self.conn.commit()
            messagebox.showinfo("Success", "Song Deleted from Album Successfully")
            self.create_admin_panel()  # Refresh admin panel after deletion



    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #manage songs of sachin-Jigar
    
    def add_song_of_sachJig(self):
        self.open_song_to_album_input_window("Add Song", self.insert_sachin_jigar_songs)

    def open_song_to_album_input_window(self, title, insert_method):
        input_window = tk.Toplevel(self.root)
        input_window.title(title)

    # Album input (Textbox to enter album ID or name manually)
        category_label = tk.Label(input_window, text="Album Id:", font=("Arial", 12))
        category_label.grid(row=1, column=0, padx=10, pady=10)
        category_entry = tk.Entry(input_window, font=("Arial", 12))
    
    # Fetch albums from the database and display in the entry as a list
        self.cursor.execute("SELECT album_id, album_name FROM albums")
        categories = self.cursor.fetchall()
        category_list = [f"{album[0]} - {album[1]}" for category in categories]
        category_entry.insert(0, ", ".join(category_list))  # Insert the list of albums into the textbox
        category_entry.grid(row=1, column=1, padx=10, pady=10)

    
        song_path_label = tk.Label(input_window, text="Song Path:", font=("Arial", 12))
        song_path_label.grid(row=3, column=0, padx=10, pady=10)
        path_entry = tk.Entry(input_window, font=("Arial", 12))
        path_entry.grid(row=3, column=1, padx=10, pady=10)


     # Submit button
        submit_button = tk.Button(input_window, text="Submit", command=lambda: insert_method(category_entry.get(), path_entry.get()), font=("Arial", 14))
        submit_button.grid(row=4, columnspan=2, pady=20)

    def select_song_file(self, input_window):
        # Open a file dialog to choose the song file
        self.selected_song_path = filedialog.askopenfilename(title="Select Song File", filetypes=(("Audio files", "*.mp3;*.ogg;*.wav"), ("All files", "*.*")))
        if self.selected_song_path:
            messagebox.showinfo("Song Selected", "Song file selected successfully")



    def insert_song_of_sachJig_songs(self,category_id,song_path):
        
        self.cursor.execute("INSERT INTO sachin_jigar_songs(album_id,song_path) VALUES (%s, %s)", (album_id,song_path))
        self.conn.commit()
        messagebox.showinfo("Success", "Song Added Successfully")
        self.create_admin_panel()

    def list_songs_of_sachJig(self):
    # Execute SQL to fetch the songs in albums
        self.cursor.execute("SELECT * FROM sachin_jigar_songs")
        songs_of_sachJig = self.cursor.fetchall()

    # Create a new window for displaying the list
        song_list_window = tk.Toplevel(self.root)
        song_list_window.title("Songs in Sachin Jigar List")

    # Label for the window
        tk.Label(song_list_window, text="Sachin Jigar Songs", font=("Arial", 16, "bold"), fg="#FF6F61", bg="#2E3B4E").pack(pady=10)

    # Create a Treeview widget
        tree = ttk.Treeview(song_list_window, columns=("Song ID", "Category ID", "Song Path"), show="headings")

    # Set headings
        tree.heading("Song ID", text="Song ID")
        tree.heading("Album ID", text="Album ID")
        tree.heading("Song Path", text="Song Path")

    # Set column widths if necessary
        tree.column("Song ID", width=100, anchor="center")
        tree.column("Album ID", width=100, anchor="center")
        tree.column("Song Path", width=800, anchor="w")

    # Insert data into the tree
        for song in songs_of_sachJig:
            tree.insert("", tk.END, values=(song[0], song[1], song[2]))

        tree.pack(pady=10)

    # Create a frame for update and delete buttons
        button_frame = tk.Frame(song_list_window)
        button_frame.pack(pady=10)

    # Function to update the selected song
        def update_selected_song():
            selected_item = tree.selection()
            if selected_item:
                song_id = tree.item(selected_item, "values")[0]
                self.update_song_of_sachJig(song_id)  # Call the update method for the selected song

    # Function to delete the selected song
        def delete_selected_song():
            selected_item = tree.selection()
            if selected_item:
                song_id = tree.item(selected_item, "values")[0]
                self.delete_song_of_sachJig(song_id)  # Call the delete method for the selected song
    
    # Create Update and Delete buttons for the selected song
        update_button = tk.Button(button_frame, text="Update Selected", command=update_selected_song)
        update_button.pack(side="left", padx=10, pady=5)

        delete_button = tk.Button(button_frame, text="Delete Selected", command=delete_selected_song)
        delete_button.pack(side="left", padx=10, pady=5)
    
    # Create close button at the bottom of the window
        close_button = tk.Button(song_list_window, text="Close", command=song_list_window.destroy, font=("Arial", 14))
        close_button.pack(pady=10)
    
    def update_song_of_sachJig(self, song_id):
        # Open a new window to update song details
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Sachin Jigar Song")
    
        # Get song details
        self.cursor.execute("SELECT * FROM sachin_jigar_songs WHERE song_id = %s", (song_id,))
        song = self.cursor.fetchone()
    
        # Create fields to update song details
        category_id_label = tk.Label(update_window, text="Album ID:", font=("Arial", 12), bg="#FFFFFF")
        category_id_label.grid(row=0, column=0, padx=10, pady=10)
        category_id_entry = tk.Entry(update_window, font=("Arial", 12))
        category_id_entry.insert(0, song[1])  # Pre-fill with current category ID
        category_id_entry.grid(row=0, column=1, padx=10, pady=10)
    
        song_path_label = tk.Label(update_window, text="Song Path:", font=("Arial", 12), bg="#FFFFFF")
        song_path_label.grid(row=1, column=0, padx=10, pady=10)
        song_path_entry = tk.Entry(update_window, font=("Arial", 12))
        song_path_entry.insert(0, song[2])  # Pre-fill with current song path
        song_path_entry.grid(row=1, column=1, padx=10, pady=10)
    
        def save_update():
            category_id = category_id_entry.get()
            song_path = song_path_entry.get()
    
            # Call the method to update the song data in the database
            self.cursor.execute("""
                UPDATE sachin_jigar_songs
                SET album_id = %s, song_path = %s
                WHERE song_id = %s
            """, (category_id, song_path, song_id))
            self.conn.commit()
            messagebox.showinfo("Success", "Sachin Jigar Songs Updated Successfully")
            update_window.destroy()  # Close the update window
    
        save_button = tk.Button(update_window, text="Save", command=save_update, font=("Arial", 14), bg="#4F81BD", fg="white")
        save_button.grid(row=2, columnspan=2, pady=20)
    
    def delete_song_of_sachJig(self, song_id):
        confirm = messagebox.askyesno("Delete Song from Category", "Are you sure you want to delete this song?")
        if confirm:
            self.cursor.execute("DELETE FROM sachin_jigar_songs WHERE song_id = %s", (song_id,))
            self.conn.commit()
            messagebox.showinfo("Success", "Song Deleted Successfully")
            self.create_admin_panel()  # Refresh admin panel after deletion



    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #manage Songs of Diljit

    def add_song_of_diljit(self):
        self.open_song_to_album_input_window("Add Song to Album", self.insert_song_of_diljit)

    def open_song_to_album_input_window(self, title, insert_method):
        input_window = tk.Toplevel(self.root)
        input_window.title(title)

    # Album input (Textbox to enter album ID or name manually)
        album_label = tk.Label(input_window, text="Album Id:", font=("Arial", 12))
        album_label.grid(row=1, column=0, padx=10, pady=10)
        album_entry = tk.Entry(input_window, font=("Arial", 12))
    
    # Fetch albums from the database and display in the entry as a list
        self.cursor.execute("SELECT album_id, album_name FROM albums")
        albums = self.cursor.fetchall()
        album_list = [f"{album[0]} - {album[1]}" for album in albums]
        album_entry.insert(0, ", ".join(album_list))  # Insert the list of albums into the textbox
        album_entry.grid(row=1, column=1, padx=10, pady=10)

    
        song_path_label = tk.Label(input_window, text="Song Path:", font=("Arial", 12))
        song_path_label.grid(row=3, column=0, padx=10, pady=10)
        path_entry = tk.Entry(input_window, font=("Arial", 12))
        path_entry.grid(row=3, column=1, padx=10, pady=10)


     # Submit button
        submit_button = tk.Button(input_window, text="Submit", command=lambda: insert_method(album_entry.get(), path_entry.get()), font=("Arial", 14))
        submit_button.grid(row=4, columnspan=2, pady=20)

    def select_song_file(self, input_window):
        # Open a file dialog to choose the song file
        self.selected_song_path = filedialog.askopenfilename(title="Select Song File", filetypes=(("Audio files", "*.mp3;*.ogg;*.wav"), ("All files", "*.*")))
        if self.selected_song_path:
            messagebox.showinfo("Song Selected", "Song file selected successfully")



    def insert_song_of_diljit(self,album_id,song_path):
        
        self.cursor.execute("INSERT INTO diljit_songs(album_id,song_path) VALUES (%s, %s)", (album_id,song_path))
        self.conn.commit()
        messagebox.showinfo("Success", "Song Added to Album Successfully")
        self.create_admin_panel()

    def list_songs_of_diljit(self):
        # Execute SQL to fetch the songs in albums
        self.cursor.execute("SELECT * FROM diljit_songs")
        songs_of_diljit = self.cursor.fetchall()

    # Create a new window for displaying the list
        song_list_window = tk.Toplevel(self.root)
        song_list_window.title("Songs in Albums List")

    # Label for the window
        tk.Label(song_list_window, text="Songs of Diljit", font=("Arial", 16, "bold"), fg="#FF6F61", bg="#2E3B4E").pack(pady=10)

    # Create a Treeview widget
        tree = ttk.Treeview(song_list_window, columns=("Song ID", "Album ID", "Song Path"), show="headings")

    # Set headings
        tree.heading("Song ID", text="Song ID")
        tree.heading("Album ID", text="Album ID")
        tree.heading("Song Path", text="Song Path")

    # Set column widths if necessary
        tree.column("Song ID", width=100, anchor="center")
        tree.column("Album ID", width=100, anchor="center")
        tree.column("Song Path", width=800, anchor="w")

    # Insert data into the tree
        for song in songs_of_diljit:
            tree.insert("", tk.END, values=(song[0], song[1], song[2]))

        tree.pack(pady=10)

    # Create a frame for update and delete buttons
        button_frame = tk.Frame(song_list_window)
        button_frame.pack(pady=10)
    
    # Function to update the selected song
        def update_selected_song():
            selected_item = tree.selection()
            if selected_item:
                song_id = tree.item(selected_item, "values")[0]
                self.update_song_of_diljit(song_id)  # Call the update method for the selected song

    # Function to delete the selected song
        def delete_selected_song():
            selected_item = tree.selection()
            if selected_item:
                song_id = tree.item(selected_item, "values")[0]
                self.delete_song_of_diljit(song_id)  # Call the delete method for the selected song

    # Create Update and Delete buttons for the selected song
        update_button = tk.Button(button_frame, text="Update Selected", command=update_selected_song)
        update_button.pack(side="left", padx=10, pady=5)
    
        delete_button = tk.Button(button_frame, text="Delete Selected", command=delete_selected_song)
        delete_button.pack(side="left", padx=10, pady=5)

    # Create close button at the bottom of the window
        close_button = tk.Button(song_list_window, text="Close", command=song_list_window.destroy, font=("Arial", 14))
        close_button.pack(pady=10)

    def update_song_of_diljit(self, song_id):
    # Open a new window to update song details
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Song")

    # Get song details
        self.cursor.execute("SELECT * FROM diljit_songs WHERE song_id = %s", (song_id,))
        song = self.cursor.fetchone()

    # Create fields to update song details
        album_id_label = tk.Label(update_window, text="Album ID:", font=("Arial", 12), bg="#FFFFFF")
        album_id_label.grid(row=0, column=0, padx=10, pady=10)
        album_id_entry = tk.Entry(update_window, font=("Arial", 12))
        album_id_entry.insert(0, song[1])  # Pre-fill with current album ID
        album_id_entry.grid(row=0, column=1, padx=10, pady=10)

        song_path_label = tk.Label(update_window, text="Song Path:", font=("Arial", 12), bg="#FFFFFF")
        song_path_label.grid(row=1, column=0, padx=10, pady=10)
        song_path_entry = tk.Entry(update_window, font=("Arial", 12))
        song_path_entry.insert(0, song[2])  # Pre-fill with current song path
        song_path_entry.grid(row=1, column=1, padx=10, pady=10)

        def save_update():
            album_id = album_id_entry.get()
            song_path = song_path_entry.get()
    
        # Call the method to update the song data in the database
            self.cursor.execute("""
                UPDATE diljit_songs
                SET album_id = %s, song_path = %s
                WHERE song_id = %s
            """, (album_id, song_path, song_id))
            self.conn.commit()
            messagebox.showinfo("Success", "Song Updated Successfully")
            update_window.destroy()  # Close the update window

        save_button = tk.Button(update_window, text="Save", command=save_update, font=("Arial", 14), bg="#4F81BD", fg="white")
        save_button.grid(row=2, columnspan=2, pady=20)

    def delete_song_of_diljit(self, song_id):
        confirm = messagebox.askyesno("Delete Song from Album", "Are you sure you want to delete this song?")
        if confirm:
            self.cursor.execute("DELETE FROM diljit_songs WHERE song_id = %s", (song_id,))
            self.conn.commit()
            messagebox.showinfo("Success", "Song Deleted from Album Successfully")
            self.create_admin_panel()  # Refresh admin panel after deletion



    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #manage songs of badshah

    def add_song_of_badshah(self):
        self.open_song_to_album_input_window("Add Song to Album", self.insert_song_of_badshah)

    def open_song_to_album_input_window(self, title, insert_method):
        input_window = tk.Toplevel(self.root)
        input_window.title(title)

    # Album input (Textbox to enter album ID or name manually)
        album_label = tk.Label(input_window, text="Album Id:", font=("Arial", 12))
        album_label.grid(row=1, column=0, padx=10, pady=10)
        album_entry = tk.Entry(input_window, font=("Arial", 12))
    
    # Fetch albums from the database and display in the entry as a list
        self.cursor.execute("SELECT album_id, album_name FROM albums")
        albums = self.cursor.fetchall()
        album_list = [f"{album[0]} - {album[1]}" for album in albums]
        album_entry.insert(0, ", ".join(album_list))  # Insert the list of albums into the textbox
        album_entry.grid(row=1, column=1, padx=10, pady=10)

    
        song_path_label = tk.Label(input_window, text="Song Path:", font=("Arial", 12))
        song_path_label.grid(row=3, column=0, padx=10, pady=10)
        path_entry = tk.Entry(input_window, font=("Arial", 12))
        path_entry.grid(row=3, column=1, padx=10, pady=10)


     # Submit button
        submit_button = tk.Button(input_window, text="Submit", command=lambda: insert_method(album_entry.get(), path_entry.get()), font=("Arial", 14))
        submit_button.grid(row=4, columnspan=2, pady=20)

    def select_song_file(self, input_window):
        # Open a file dialog to choose the song file
        self.selected_song_path = filedialog.askopenfilename(title="Select Song File", filetypes=(("Audio files", "*.mp3;*.ogg;*.wav"), ("All files", "*.*")))
        if self.selected_song_path:
            messagebox.showinfo("Song Selected", "Song file selected successfully")



    def insert_song_of_badshah(self,album_id,song_path):
        
        self.cursor.execute("INSERT INTO badshah_songs(album_id,song_path) VALUES (%s, %s)", (album_id,song_path))
        self.conn.commit()
        messagebox.showinfo("Success", "Song Added to Album Successfully")
        self.create_admin_panel()

    def list_songs_of_badshah(self):
    # Execute SQL to fetch the songs in albums
        self.cursor.execute("SELECT * FROM badshah_songs")
        songs_of_badshah = self.cursor.fetchall()

    # Create a new window for displaying the list
        song_list_window = tk.Toplevel(self.root)
        song_list_window.title("Songs in Albums List")

    # Label for the window
        tk.Label(song_list_window, text="Songs of Badshah", font=("Arial", 16, "bold"), fg="#FF6F61", bg="#2E3B4E").pack(pady=10)

    # Create a Treeview widget
        tree = ttk.Treeview(song_list_window, columns=("Song ID", "Album ID", "Song Path"), show="headings")

    # Set headings
        tree.heading("Song ID", text="Song ID")
        tree.heading("Album ID", text="Album ID")
        tree.heading("Song Path", text="Song Path")

    # Set column widths if necessary
        tree.column("Song ID", width=100, anchor="center")
        tree.column("Album ID", width=100, anchor="center")
        tree.column("Song Path", width=800, anchor="w")

    # Insert data into the tree
        for song in songs_of_badshah:
            tree.insert("", tk.END, values=(song[0], song[1], song[2]))

        tree.pack(pady=10)

    # Create a frame for update and delete buttons
        button_frame = tk.Frame(song_list_window)
        button_frame.pack(pady=10)

    # Function to update the selected song
        def update_selected_song():
            selected_item = tree.selection()
            if selected_item:
                song_id = tree.item(selected_item, "values")[0]
                self.update_song_of_badshah(song_id)  # Call the update method for the selected song

    # Function to delete the selected song
        def delete_selected_song():
            selected_item = tree.selection()
            if selected_item:
                song_id = tree.item(selected_item, "values")[0]
                self.delete_song_of_badshah(song_id)  # Call the delete method for the selected song

    # Create Update and Delete buttons for the selected song
        update_button = tk.Button(button_frame, text="Update Selected", command=update_selected_song)
        update_button.pack(side="left", padx=10, pady=5)

        delete_button = tk.Button(button_frame, text="Delete Selected", command=delete_selected_song)
        delete_button.pack(side="left", padx=10, pady=5)

    # Create close button at the bottom of the window
        close_button = tk.Button(song_list_window, text="Close", command=song_list_window.destroy, font=("Arial", 14))
        close_button.pack(pady=10)

    def update_song_of_badshah(self, song_id):
    # Open a new window to update song details
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Song")

    # Get song details
        self.cursor.execute("SELECT * FROM badshah_songs WHERE song_id = %s", (song_id,))
        song = self.cursor.fetchone()

    # Create fields to update song details
        album_id_label = tk.Label(update_window, text="Album ID:", font=("Arial", 12), bg="#FFFFFF")
        album_id_label.grid(row=0, column=0, padx=10, pady=10)
        album_id_entry = tk.Entry(update_window, font=("Arial", 12))
        album_id_entry.insert(0, song[1])  # Pre-fill with current album ID
        album_id_entry.grid(row=0, column=1, padx=10, pady=10)

        song_path_label = tk.Label(update_window, text="Song Path:", font=("Arial", 12), bg="#FFFFFF")
        song_path_label.grid(row=1, column=0, padx=10, pady=10)
        song_path_entry = tk.Entry(update_window, font=("Arial", 12))
        song_path_entry.insert(0, song[2])  # Pre-fill with current song path
        song_path_entry.grid(row=1, column=1, padx=10, pady=10)

        def save_update():
            album_id = album_id_entry.get()
            song_path = song_path_entry.get()

        # Call the method to update the song data in the database
            self.cursor.execute("""
                UPDATE badshah_songs
                SET album_id = %s, song_path = %s
                WHERE song_id = %s
            """, (album_id, song_path, song_id))
            self.conn.commit()
            messagebox.showinfo("Success", "Song Updated Successfully")
            update_window.destroy()  # Close the update window

        save_button = tk.Button(update_window, text="Save", command=save_update, font=("Arial", 14), bg="#4F81BD", fg="white")
        save_button.grid(row=2, columnspan=2, pady=20)
    
    def delete_song_of_badshah(self, song_id):
        confirm = messagebox.askyesno("Delete Song from Album", "Are you sure you want to delete this song?")
        if confirm:
            self.cursor.execute("DELETE FROM badshah_songs WHERE song_id = %s", (song_id,))
            self.conn.commit()
            messagebox.showinfo("Success", "Song Deleted from Album Successfully")
            self.create_admin_panel()  # Refresh admin panel after deletion


    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #manage songs of honey singh
    def add_song_of_honey(self):
        self.open_song_to_album_input_window("Add Song to Album", self.insert_song_of_honey)

    def open_song_to_album_input_window(self, title, insert_method):
        input_window = tk.Toplevel(self.root)
        input_window.title(title)

    # Album input (Textbox to enter album ID or name manually)
        album_label = tk.Label(input_window, text="Album Id:", font=("Arial", 12))
        album_label.grid(row=1, column=0, padx=10, pady=10)
        album_entry = tk.Entry(input_window, font=("Arial", 12))
    
    # Fetch albums from the database and display in the entry as a list
        self.cursor.execute("SELECT album_id, album_name FROM albums")
        albums = self.cursor.fetchall()
        album_list = [f"{album[0]} - {album[1]}" for album in albums]
        album_entry.insert(0, ", ".join(album_list))  # Insert the list of albums into the textbox
        album_entry.grid(row=1, column=1, padx=10, pady=10)

    
        song_path_label = tk.Label(input_window, text="Song Path:", font=("Arial", 12))
        song_path_label.grid(row=3, column=0, padx=10, pady=10)
        path_entry = tk.Entry(input_window, font=("Arial", 12))
        path_entry.grid(row=3, column=1, padx=10, pady=10)


     # Submit button
        submit_button = tk.Button(input_window, text="Submit", command=lambda: insert_method(album_entry.get(), path_entry.get()), font=("Arial", 14))
        submit_button.grid(row=4, columnspan=2, pady=20)

    def select_song_file(self, input_window):
        # Open a file dialog to choose the song file
        self.selected_song_path = filedialog.askopenfilename(title="Select Song File", filetypes=(("Audio files", "*.mp3;*.ogg;*.wav"), ("All files", "*.*")))
        if self.selected_song_path:
            messagebox.showinfo("Song Selected", "Song file selected successfully")



    def insert_song_of_honey(self,album_id,song_path):
        
        self.cursor.execute("INSERT INTO honey_singh_songs(album_id,song_path) VALUES (%s, %s)", (album_id,song_path))
        self.conn.commit()
        messagebox.showinfo("Success", "Song Added to Album Successfully")
        self.create_admin_panel()

    def list_songs_of_honey(self):
    # Execute SQL to fetch the songs in albums
        self.cursor.execute("SELECT * FROM honey_singh_songs")
        songs_of_honey = self.cursor.fetchall()

    # Create a new window for displaying the list
        song_list_window = tk.Toplevel(self.root)
        song_list_window.title("Songs in Albums List")

    # Label for the window
        tk.Label(song_list_window, text="Songs of Honey Singh", font=("Arial", 16, "bold"), fg="#FF6F61", bg="#2E3B4E").pack(pady=10)

    # Create a Treeview widget
        tree = ttk.Treeview(song_list_window, columns=("Song ID", "Album ID", "Song Path"), show="headings")

    # Set headings
        tree.heading("Song ID", text="Song ID")
        tree.heading("Album ID", text="Album ID")
        tree.heading("Song Path", text="Song Path")

    # Set column widths if necessary
        tree.column("Song ID", width=100, anchor="center")
        tree.column("Album ID", width=100, anchor="center")
        tree.column("Song Path", width=800, anchor="w")

    # Insert data into the tree
        for song in songs_of_honey:
            tree.insert("", tk.END, values=(song[0], song[1], song[2]))

        tree.pack(pady=10)

    # Create a frame for update and delete buttons
        button_frame = tk.Frame(song_list_window)
        button_frame.pack(pady=10)

    # Function to update the selected song
        def update_selected_song():
            selected_item = tree.selection()
            if selected_item:
                song_id = tree.item(selected_item, "values")[0]
                self.update_song_of_honey(song_id)  # Call the update method for the selected song

    # Function to delete the selected song
        def delete_selected_song():
            selected_item = tree.selection()
            if selected_item:
                song_id = tree.item(selected_item, "values")[0]
                self.delete_song_of_honey(song_id)  # Call the delete method for the selected song
    
    # Create Update and Delete buttons for the selected song
        update_button = tk.Button(button_frame, text="Update Selected", command=update_selected_song)
        update_button.pack(side="left", padx=10, pady=5)
    
        delete_button = tk.Button(button_frame, text="Delete Selected", command=delete_selected_song)
        delete_button.pack(side="left", padx=10, pady=5)
    
        # Create close button at the bottom of the window
        close_button = tk.Button(song_list_window, text="Close", command=song_list_window.destroy, font=("Arial", 14))
        close_button.pack(pady=10)
    
    def update_song_of_honey(self, song_id):
    # Open a new window to update song details
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Song")
    
    # Get song details
        self.cursor.execute("SELECT * FROM honey_singh_songs WHERE song_id = %s", (song_id,))
        song = self.cursor.fetchone()

    # Create fields to update song details
        album_id_label = tk.Label(update_window, text="Album ID:", font=("Arial", 12), bg="#FFFFFF")
        album_id_label.grid(row=0, column=0, padx=10, pady=10)
        album_id_entry = tk.Entry(update_window, font=("Arial", 12))
        album_id_entry.insert(0, song[1])  # Pre-fill with current album ID
        album_id_entry.grid(row=0, column=1, padx=10, pady=10)

        song_path_label = tk.Label(update_window, text="Song Path:", font=("Arial", 12), bg="#FFFFFF")
        song_path_label.grid(row=1, column=0, padx=10, pady=10)
        song_path_entry = tk.Entry(update_window, font=("Arial", 12))
        song_path_entry.insert(0, song[2])  # Pre-fill with current song path
        song_path_entry.grid(row=1, column=1, padx=10, pady=10)

        def save_update():
            album_id = album_id_entry.get()
            song_path = song_path_entry.get()

        # Call the method to update the song data in the database
            self.cursor.execute("""
                UPDATE honey_singh_songs
                SET album_id = %s, song_path = %s
                WHERE song_id = %s
            """, (album_id, song_path, song_id))
            self.conn.commit()
            messagebox.showinfo("Success", "Song Updated Successfully")
            update_window.destroy()  # Close the update window
    
        save_button = tk.Button(update_window, text="Save", command=save_update, font=("Arial", 14), bg="#4F81BD", fg="white")
        save_button.grid(row=2, columnspan=2, pady=20)

    def delete_song_of_honey(self, song_id):
        confirm = messagebox.askyesno("Delete Song from Album", "Are you sure you want to delete this song?")
        if confirm:
            self.cursor.execute("DELETE FROM honey_singh_songs WHERE song_id = %s", (song_id,))
            self.conn.commit()
            messagebox.showinfo("Success", "Song Deleted from Album Successfully")
            self.create_admin_panel()  # Refresh admin panel after deletion


     #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #manage songs of K.K.
    def add_song_of_kk(self):
        self.open_song_to_album_input_window("Add Song to Album", self.insert_song_of_kk)

    def open_song_to_album_input_window(self, title, insert_method):
        input_window = tk.Toplevel(self.root)
        input_window.title(title)

    # Album input (Textbox to enter album ID or name manually)
        album_label = tk.Label(input_window, text="Album Id:", font=("Arial", 12))
        album_label.grid(row=1, column=0, padx=10, pady=10)
        album_entry = tk.Entry(input_window, font=("Arial", 12))
    
    # Fetch albums from the database and display in the entry as a list
        self.cursor.execute("SELECT album_id, album_name FROM albums")
        albums = self.cursor.fetchall()
        album_list = [f"{album[0]} - {album[1]}" for album in albums]
        album_entry.insert(0, ", ".join(album_list))  # Insert the list of albums into the textbox
        album_entry.grid(row=1, column=1, padx=10, pady=10)

    
        song_path_label = tk.Label(input_window, text="Song Path:", font=("Arial", 12))
        song_path_label.grid(row=3, column=0, padx=10, pady=10)
        path_entry = tk.Entry(input_window, font=("Arial", 12))
        path_entry.grid(row=3, column=1, padx=10, pady=10)


     # Submit button
        submit_button = tk.Button(input_window, text="Submit", command=lambda: insert_method(album_entry.get(), path_entry.get()), font=("Arial", 14))
        submit_button.grid(row=4, columnspan=2, pady=20)

    def select_song_file(self, input_window):
        # Open a file dialog to choose the song file
        self.selected_song_path = filedialog.askopenfilename(title="Select Song File", filetypes=(("Audio files", "*.mp3;*.ogg;*.wav"), ("All files", "*.*")))
        if self.selected_song_path:
            messagebox.showinfo("Song Selected", "Song file selected successfully")



    def insert_song_of_kk(self,album_id,song_path):
        
        self.cursor.execute("INSERT INTO kk_songs(album_id,song_path) VALUES (%s, %s)", (album_id,song_path))
        self.conn.commit()
        messagebox.showinfo("Success", "Song Added to Album Successfully")
        self.create_admin_panel()

    def list_songs_of_kk(self):
    # Execute SQL to fetch the songs in albums
        self.cursor.execute("SELECT * FROM kk_songs")
        songs_of_kk = self.cursor.fetchall()

    # Create a new window for displaying the list
        song_list_window = tk.Toplevel(self.root)
        song_list_window.title("Songs in Albums List")
    
    # Label for the window
        tk.Label(song_list_window, text="Songs of KK", font=("Arial", 16, "bold"), fg="#FF6F61", bg="#2E3B4E").pack(pady=10)

    # Create a Treeview widget
        tree = ttk.Treeview(song_list_window, columns=("Song ID", "Album ID", "Song Path"), show="headings")

    # Set headings
        tree.heading("Song ID", text="Song ID")
        tree.heading("Album ID", text="Album ID")
        tree.heading("Song Path", text="Song Path")

    # Set column widths if necessary
        tree.column("Song ID", width=100, anchor="center")
        tree.column("Album ID", width=100, anchor="center")
        tree.column("Song Path", width=800, anchor="w")

    # Insert data into the tree
        for song in songs_of_kk:
            tree.insert("", tk.END, values=(song[0], song[1], song[2]))
    
        tree.pack(pady=10)

    # Create a frame for update and delete buttons
        button_frame = tk.Frame(song_list_window)
        button_frame.pack(pady=10)

    # Function to update the selected song
        def update_selected_song():
            selected_item = tree.selection()
            if selected_item:
                song_id = tree.item(selected_item, "values")[0]
                self.update_song_of_kk(song_id)  # Call the update method for the selected song

    # Function to delete the selected song
        def delete_selected_song():
            selected_item = tree.selection()
            if selected_item:
                song_id = tree.item(selected_item, "values")[0]
                self.delete_song_of_kk(song_id)  # Call the delete method for the selected song

    # Create Update and Delete buttons for the selected song
        update_button = tk.Button(button_frame, text="Update Selected", command=update_selected_song)
        update_button.pack(side="left", padx=10, pady=5)
    
        delete_button = tk.Button(button_frame, text="Delete Selected", command=delete_selected_song)
        delete_button.pack(side="left", padx=10, pady=5)

    # Create close button at the bottom of the window
        close_button = tk.Button(song_list_window, text="Close", command=song_list_window.destroy, font=("Arial", 14))
        close_button.pack(pady=10)

    def update_song_of_kk(self, song_id):
    # Open a new window to update song details
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Song")

    # Get song details
        self.cursor.execute("SELECT * FROM kk_songs WHERE song_id = %s", (song_id,))
        song = self.cursor.fetchone()

    # Create fields to update song details
        album_id_label = tk.Label(update_window, text="Album ID:", font=("Arial", 12), bg="#FFFFFF")
        album_id_label.grid(row=0, column=0, padx=10, pady=10)
        album_id_entry = tk.Entry(update_window, font=("Arial", 12))
        album_id_entry.insert(0, song[1])  # Pre-fill with current album ID
        album_id_entry.grid(row=0, column=1, padx=10, pady=10)

        song_path_label = tk.Label(update_window, text="Song Path:", font=("Arial", 12), bg="#FFFFFF")
        song_path_label.grid(row=1, column=0, padx=10, pady=10)
        song_path_entry = tk.Entry(update_window, font=("Arial", 12))
        song_path_entry.insert(0, song[2])  # Pre-fill with current song path
        song_path_entry.grid(row=1, column=1, padx=10, pady=10)

        def save_update():
            album_id = album_id_entry.get()
            song_path = song_path_entry.get()

        # Call the method to update the song data in the database
            self.cursor.execute("""
                UPDATE kk_songs
                SET album_id = %s, song_path = %s
                WHERE song_id = %s
            """, (album_id, song_path, song_id))
            self.conn.commit()
            messagebox.showinfo("Success", "Song Updated Successfully")
            update_window.destroy()  # Close the update window

        save_button = tk.Button(update_window, text="Save", command=save_update, font=("Arial", 14), bg="#4F81BD", fg="white")
        save_button.grid(row=2, columnspan=2, pady=20)

    def delete_song_of_kk(self, song_id):
        confirm = messagebox.askyesno("Delete Song from Album", "Are you sure you want to delete this song?")
        if confirm:
            self.cursor.execute("DELETE FROM kk_songs WHERE song_id = %s", (song_id,))
            self.conn.commit()
            messagebox.showinfo("Success", "Song Deleted from Album Successfully")
            self.create_admin_panel()  # Refresh admin panel after deletion

            
     #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #manage songs of Darshan
    def add_song_of_darshan(self):
        self.open_song_to_album_input_window("Add Song to Album", self.insert_song_of_darshan)

    def open_song_to_album_input_window(self, title, insert_method):
        input_window = tk.Toplevel(self.root)
        input_window.title(title)

    # Album input (Textbox to enter album ID or name manually)
        album_label = tk.Label(input_window, text="Album Id:", font=("Arial", 12))
        album_label.grid(row=1, column=0, padx=10, pady=10)
        album_entry = tk.Entry(input_window, font=("Arial", 12))
    
    # Fetch albums from the database and display in the entry as a list
        self.cursor.execute("SELECT album_id, album_name FROM albums")
        albums = self.cursor.fetchall()
        album_list = [f"{album[0]} - {album[1]}" for album in albums]
        album_entry.insert(0, ", ".join(album_list))  # Insert the list of albums into the textbox
        album_entry.grid(row=1, column=1, padx=10, pady=10)

    
        song_path_label = tk.Label(input_window, text="Song Path:", font=("Arial", 12))
        song_path_label.grid(row=3, column=0, padx=10, pady=10)
        path_entry = tk.Entry(input_window, font=("Arial", 12))
        path_entry.grid(row=3, column=1, padx=10, pady=10)


     # Submit button
        submit_button = tk.Button(input_window, text="Submit", command=lambda: insert_method(album_entry.get(), path_entry.get()), font=("Arial", 14))
        submit_button.grid(row=4, columnspan=2, pady=20)

    def select_song_file(self, input_window):
        # Open a file dialog to choose the song file
        self.selected_song_path = filedialog.askopenfilename(title="Select Song File", filetypes=(("Audio files", "*.mp3;*.ogg;*.wav"), ("All files", "*.*")))
        if self.selected_song_path:
            messagebox.showinfo("Song Selected", "Song file selected successfully")



    def insert_song_of_darshan(self,album_id,song_path):
        
        self.cursor.execute("INSERT INTO darshan_songs(album_id,song_path) VALUES (%s, %s)", (album_id,song_path))
        self.conn.commit()
        messagebox.showinfo("Success", "Song Added to Album Successfully")
        self.create_admin_panel()

    def list_songs_of_darshan(self):
    # Execute SQL to fetch the songs in albums
        self.cursor.execute("SELECT * FROM darshan_songs")
        songs_of_darshan = self.cursor.fetchall()

    # Create a new window for displaying the list
        song_list_window = tk.Toplevel(self.root)
        song_list_window.title("Songs in Albums List")

    # Label for the window
        tk.Label(song_list_window, text="Songs of Darshan", font=("Arial", 16, "bold"), fg="#FF6F61", bg="#2E3B4E").pack(pady=10)

    # Create a Treeview widget
        tree = ttk.Treeview(song_list_window, columns=("Song ID", "Album ID", "Song Path"), show="headings")

    # Set headings
        tree.heading("Song ID", text="Song ID")
        tree.heading("Album ID", text="Album ID")
        tree.heading("Song Path", text="Song Path")

    # Set column widths if necessary
        tree.column("Song ID", width=100, anchor="center")
        tree.column("Album ID", width=100, anchor="center")
        tree.column("Song Path", width=800, anchor="w")

    # Insert data into the tree
        for song in songs_of_darshan:
            tree.insert("", tk.END, values=(song[0], song[1], song[2]))

        tree.pack(pady=10)

    # Create a frame for update and delete buttons
        button_frame = tk.Frame(song_list_window)
        button_frame.pack(pady=10)
    
    # Function to update the selected song
        def update_selected_song():
            selected_item = tree.selection()
            if selected_item:
                song_id = tree.item(selected_item, "values")[0]
                self.update_song_of_darshan(song_id)  # Call the update method for the selected song

    # Function to delete the selected song
        def delete_selected_song():
            selected_item = tree.selection()
            if selected_item:
                song_id = tree.item(selected_item, "values")[0]
                self.delete_song_of_darshan(song_id)  # Call the delete method for the selected song

    # Create Update and Delete buttons for the selected song
        update_button = tk.Button(button_frame, text="Update Selected", command=update_selected_song)
        update_button.pack(side="left", padx=10, pady=5)

        delete_button = tk.Button(button_frame, text="Delete Selected", command=delete_selected_song)
        delete_button.pack(side="left", padx=10, pady=5)

    # Create close button at the bottom of the window
        close_button = tk.Button(song_list_window, text="Close", command=song_list_window.destroy, font=("Arial", 14))
        close_button.pack(pady=10)

    def update_song_of_darshan(self, song_id):
    # Open a new window to update song details
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Song")

    # Get song details
        self.cursor.execute("SELECT * FROM darshan_songs WHERE song_id = %s", (song_id,))
        song = self.cursor.fetchone()
    
    # Create fields to update song details
        album_id_label = tk.Label(update_window, text="Album ID:", font=("Arial", 12), bg="#FFFFFF")
        album_id_label.grid(row=0, column=0, padx=10, pady=10)
        album_id_entry = tk.Entry(update_window, font=("Arial", 12))
        album_id_entry.insert(0, song[1])  # Pre-fill with current album ID
        album_id_entry.grid(row=0, column=1, padx=10, pady=10)
    
        song_path_label = tk.Label(update_window, text="Song Path:", font=("Arial", 12), bg="#FFFFFF")
        song_path_label.grid(row=1, column=0, padx=10, pady=10)
        song_path_entry = tk.Entry(update_window, font=("Arial", 12))
        song_path_entry.insert(0, song[2])  # Pre-fill with current song path
        song_path_entry.grid(row=1, column=1, padx=10, pady=10)

        def save_update():
            album_id = album_id_entry.get()
            song_path = song_path_entry.get()
    
            # Call the method to update the song data in the database
            self.cursor.execute("""
                UPDATE darshan_songs
                SET album_id = %s, song_path = %s
                WHERE song_id = %s
            """, (album_id, song_path, song_id))
            self.conn.commit()
            messagebox.showinfo("Success", "Song Updated Successfully")
            update_window.destroy()  # Close the update window
    
        save_button = tk.Button(update_window, text="Save", command=save_update, font=("Arial", 14), bg="#4F81BD", fg="white")
        save_button.grid(row=2, columnspan=2, pady=20)
    
    def delete_song_of_darshan(self, song_id):
        confirm = messagebox.askyesno("Delete Song from Album", "Are you sure you want to delete this song?")
        if confirm:
            self.cursor.execute("DELETE FROM darshan_songs WHERE song_id = %s", (song_id,))
            self.conn.commit()
            messagebox.showinfo("Success", "Song Deleted from Album Successfully")
            self.create_admin_panel()  # Refresh admin panel after deletion
    

#============================================================================================================================================================================================================================================================================

    # Manage Gujarati Songs
    def add_gujarati_songs(self):
        self.open_song_to_album_input_window("Add Song", self.insert_gujarati_songs)

    def open_song_to_album_input_window(self, title, insert_method):
        input_window = tk.Toplevel(self.root)
        input_window.title(title)

    # Album input (Textbox to enter album ID or name manually)
        category_label = tk.Label(input_window, text="Category Id:", font=("Arial", 12))
        category_label.grid(row=1, column=0, padx=10, pady=10)
        category_entry = tk.Entry(input_window, font=("Arial", 12))
    
    # Fetch albums from the database and display in the entry as a list
        self.cursor.execute("SELECT category_id, category_name FROM categories")
        categories = self.cursor.fetchall()
        category_list = [f"{category[0]} - {category[1]}" for category in categories]
        category_entry.insert(0, ", ".join(category_list))  # Insert the list of albums into the textbox
        category_entry.grid(row=1, column=1, padx=10, pady=10)

    
        song_path_label = tk.Label(input_window, text="Song Path:", font=("Arial", 12))
        song_path_label.grid(row=3, column=0, padx=10, pady=10)
        path_entry = tk.Entry(input_window, font=("Arial", 12))
        path_entry.grid(row=3, column=1, padx=10, pady=10)


     # Submit button
        submit_button = tk.Button(input_window, text="Submit", command=lambda: insert_method(category_entry.get(), path_entry.get()), font=("Arial", 14))
        submit_button.grid(row=4, columnspan=2, pady=20)

    def select_song_file(self, input_window):
        # Open a file dialog to choose the song file
        self.selected_song_path = filedialog.askopenfilename(title="Select Song File", filetypes=(("Audio files", "*.mp3;*.ogg;*.wav"), ("All files", "*.*")))
        if self.selected_song_path:
            messagebox.showinfo("Song Selected", "Song file selected successfully")



    def insert_gujarati_songs(self,category_id,song_path):
        
        self.cursor.execute("INSERT INTO gujarati_songs(category_id,song_path) VALUES (%s, %s)", (category_id,song_path))
        self.conn.commit()
        messagebox.showinfo("Success", "Song Added Successfully")
        self.create_admin_panel()

    def list_gujarati_songs(self):
    # Execute SQL to fetch the songs in albums
        self.cursor.execute("SELECT * FROM gujarati_songs")
        gujarati_songs = self.cursor.fetchall()

    # Create a new window for displaying the list
        song_list_window = tk.Toplevel(self.root)
        song_list_window.title("Songs in Gujarati Category List")

    # Label for the window
        tk.Label(song_list_window, text="Gujarati Songs", font=("Arial", 16, "bold"), fg="#FF6F61", bg="#2E3B4E").pack(pady=10)

    # Create a Treeview widget
        tree = ttk.Treeview(song_list_window, columns=("Song ID", "Category ID", "Song Path"), show="headings")

    # Set headings
        tree.heading("Song ID", text="Song ID")
        tree.heading("Category ID", text="Category ID")
        tree.heading("Song Path", text="Song Path")

    # Set column widths if necessary
        tree.column("Song ID", width=100, anchor="center")
        tree.column("Category ID", width=100, anchor="center")
        tree.column("Song Path", width=800, anchor="w")

    # Insert data into the tree
        for song in gujarati_songs:
            tree.insert("", tk.END, values=(song[0], song[1], song[2]))

        tree.pack(pady=10)

    # Create a frame for update and delete buttons
        button_frame = tk.Frame(song_list_window)
        button_frame.pack(pady=10)

    # Function to update the selected song
        def update_selected_song():
            selected_item = tree.selection()
            if selected_item:
                song_id = tree.item(selected_item, "values")[0]
                self.update_gujarati_songs(song_id)  # Call the update method for the selected song

    # Function to delete the selected song
        def delete_selected_song():
            selected_item = tree.selection()
            if selected_item:
                song_id = tree.item(selected_item, "values")[0]
                self.delete_gujarati_songs(song_id)  # Call the delete method for the selected song

    # Create Update and Delete buttons for the selected song
        update_button = tk.Button(button_frame, text="Update Selected", command=update_selected_song)
        update_button.pack(side="left", padx=10, pady=5)

        delete_button = tk.Button(button_frame, text="Delete Selected", command=delete_selected_song)
        delete_button.pack(side="left", padx=10, pady=5)

    # Create close button at the bottom of the window
        close_button = tk.Button(song_list_window, text="Close", command=song_list_window.destroy, font=("Arial", 14))
        close_button.pack(pady=10)

    def update_gujarati_songs(self, song_id):
    # Open a new window to update song details
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Gujarati Song")
    
    # Get song details
        self.cursor.execute("SELECT * FROM gujarati_songs WHERE song_id = %s", (song_id,))
        song = self.cursor.fetchone()

    # Create fields to update song details
        category_id_label = tk.Label(update_window, text="Category ID:", font=("Arial", 12), bg="#FFFFFF")
        category_id_label.grid(row=0, column=0, padx=10, pady=10)
        category_id_entry = tk.Entry(update_window, font=("Arial", 12))
        category_id_entry.insert(0, song[1])  # Pre-fill with current category ID
        category_id_entry.grid(row=0, column=1, padx=10, pady=10)

        song_path_label = tk.Label(update_window, text="Song Path:", font=("Arial", 12), bg="#FFFFFF")
        song_path_label.grid(row=1, column=0, padx=10, pady=10)
        song_path_entry = tk.Entry(update_window, font=("Arial", 12))
        song_path_entry.insert(0, song[2])  # Pre-fill with current song path
        song_path_entry.grid(row=1, column=1, padx=10, pady=10)

        def save_update():
            category_id = category_id_entry.get()
            song_path = song_path_entry.get()

        # Call the method to update the song data in the database
            self.cursor.execute("""
                UPDATE gujarati_songs
                SET category_id = %s, song_path = %s
                WHERE song_id = %s
            """, (category_id, song_path, song_id))
            self.conn.commit()
            messagebox.showinfo("Success", "Gujarati Song Updated Successfully")
            update_window.destroy()  # Close the update window

        save_button = tk.Button(update_window, text="Save", command=save_update, font=("Arial", 14), bg="#4F81BD", fg="white")
        save_button.grid(row=2, columnspan=2, pady=20)

    def delete_gujarati_songs(self, song_id):
        confirm = messagebox.askyesno("Delete Song from Category", "Are you sure you want to delete this song?")
        if confirm:
            self.cursor.execute("DELETE FROM gujarati_songs WHERE song_id = %s", (song_id,))
            self.conn.commit()
            messagebox.showinfo("Success", "Song Deleted Successfully")
            self.create_admin_panel()  # Refresh admin panel after deletion

 #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    

# Manage Romantic Songs
    def add_romantic_songs(self):
        self.open_song_to_album_input_window("Add Song", self.insert_romantic_songs)

    def open_song_to_album_input_window(self, title, insert_method):
        input_window = tk.Toplevel(self.root)
        input_window.title(title)

    # Album input (Textbox to enter album ID or name manually)
        category_label = tk.Label(input_window, text="Category Id:", font=("Arial", 12))
        category_label.grid(row=1, column=0, padx=10, pady=10)
        category_entry = tk.Entry(input_window, font=("Arial", 12))
    
    # Fetch albums from the database and display in the entry as a list
        self.cursor.execute("SELECT category_id, category_name FROM categories")
        categories = self.cursor.fetchall()
        category_list = [f"{category[0]} - {category[1]}" for category in categories]
        category_entry.insert(0, ", ".join(category_list))  # Insert the list of albums into the textbox
        category_entry.grid(row=1, column=1, padx=10, pady=10)

    
        song_path_label = tk.Label(input_window, text="Song Path:", font=("Arial", 12))
        song_path_label.grid(row=3, column=0, padx=10, pady=10)
        path_entry = tk.Entry(input_window, font=("Arial", 12))
        path_entry.grid(row=3, column=1, padx=10, pady=10)


     # Submit button
        submit_button = tk.Button(input_window, text="Submit", command=lambda: insert_method(category_entry.get(), path_entry.get()), font=("Arial", 14))
        submit_button.grid(row=4, columnspan=2, pady=20)

    def select_song_file(self, input_window):
        # Open a file dialog to choose the song file
        self.selected_song_path = filedialog.askopenfilename(title="Select Song File", filetypes=(("Audio files", "*.mp3;*.ogg;*.wav"), ("All files", "*.*")))
        if self.selected_song_path:
            messagebox.showinfo("Song Selected", "Song file selected successfully")



    def insert_romantic_songs(self,category_id,song_path):
        
        self.cursor.execute("INSERT INTO romantic_songs(category_id,song_path) VALUES (%s, %s)", (category_id,song_path))
        self.conn.commit()
        messagebox.showinfo("Success", "Song Added Successfully")
        self.create_admin_panel()

    def list_romantic_songs(self):
    # Execute SQL to fetch the songs in albums
        self.cursor.execute("SELECT * FROM romantic_songs")
        romantic_songs = self.cursor.fetchall()

    # Create a new window for displaying the list
        song_list_window = tk.Toplevel(self.root)
        song_list_window.title("Songs in Romantic Category List")

    # Label for the window
        tk.Label(song_list_window, text="Romantic Songs", font=("Arial", 16, "bold"), fg="#FF6F61", bg="#2E3B4E").pack(pady=10)

    # Create a Treeview widget
        tree = ttk.Treeview(song_list_window, columns=("Song ID", "Category ID", "Song Path"), show="headings")

    # Set headings
        tree.heading("Song ID", text="Song ID")
        tree.heading("Category ID", text="Category ID")
        tree.heading("Song Path", text="Song Path")

    # Set column widths if necessary
        tree.column("Song ID", width=100, anchor="center")
        tree.column("Category ID", width=100, anchor="center")
        tree.column("Song Path", width=800, anchor="w")

    # Insert data into the tree
        for song in romantic_songs:
            tree.insert("", tk.END, values=(song[0], song[1], song[2]))

        tree.pack(pady=10)

    # Create a frame for update and delete buttons
        button_frame = tk.Frame(song_list_window)
        button_frame.pack(pady=10)

    # Function to update the selected song
        def update_selected_song():
            selected_item = tree.selection()
            if selected_item:
                song_id = tree.item(selected_item, "values")[0]
                self.update_romantic_songs(song_id)  # Call the update method for the selected song

    # Function to delete the selected song
        def delete_selected_song():
            selected_item = tree.selection()
            if selected_item:
                song_id = tree.item(selected_item, "values")[0]
                self.delete_romantic_songs(song_id)  # Call the delete method for the selected song

    # Create Update and Delete buttons for the selected song
        update_button = tk.Button(button_frame, text="Update Selected", command=update_selected_song)
        update_button.pack(side="left", padx=10, pady=5)

        delete_button = tk.Button(button_frame, text="Delete Selected", command=delete_selected_song)
        delete_button.pack(side="left", padx=10, pady=5)

    # Create close button at the bottom of the window
        close_button = tk.Button(song_list_window, text="Close", command=song_list_window.destroy, font=("Arial", 14))
        close_button.pack(pady=10)

    def update_romantic_songs(self, song_id):
        # Open a new window to update song details
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Romantic Song")
    
    # Get song details
        self.cursor.execute("SELECT * FROM romantic_songs WHERE song_id = %s", (song_id,))
        song = self.cursor.fetchone()
    
    # Create fields to update song details
        category_id_label = tk.Label(update_window, text="Category ID:", font=("Arial", 12), bg="#FFFFFF")
        category_id_label.grid(row=0, column=0, padx=10, pady=10)
        category_id_entry = tk.Entry(update_window, font=("Arial", 12))
        category_id_entry.insert(0, song[1])  # Pre-fill with current category ID
        category_id_entry.grid(row=0, column=1, padx=10, pady=10)

        song_path_label = tk.Label(update_window, text="Song Path:", font=("Arial", 12), bg="#FFFFFF")
        song_path_label.grid(row=1, column=0, padx=10, pady=10)
        song_path_entry = tk.Entry(update_window, font=("Arial", 12))
        song_path_entry.insert(0, song[2])  # Pre-fill with current song path
        song_path_entry.grid(row=1, column=1, padx=10, pady=10)

        def save_update():
            category_id = category_id_entry.get()
            song_path = song_path_entry.get()
    
        # Call the method to update the song data in the database
            self.cursor.execute("""
                UPDATE romantic_songs
                SET category_id = %s, song_path = %s
                WHERE song_id = %s
            """, (category_id, song_path, song_id))
            self.conn.commit()
            messagebox.showinfo("Success", "Romantic Song Updated Successfully")
            update_window.destroy()  # Close the update window

        save_button = tk.Button(update_window, text="Save", command=save_update, font=("Arial", 14), bg="#4F81BD", fg="white")
        save_button.grid(row=2, columnspan=2, pady=20)
    
    def delete_romantic_songs(self, song_id):
        confirm = messagebox.askyesno("Delete Song from Category", "Are you sure you want to delete this song?")
        if confirm:
            self.cursor.execute("DELETE FROM romantic_songs WHERE song_id = %s", (song_id,))
            self.conn.commit()
            messagebox.showinfo("Success", "Song Deleted Successfully")
            self.create_admin_panel()  # Refresh admin panel after deletion


 #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    

# Manage Trending Songs
    def add_trending_songs(self):
        self.open_song_to_album_input_window("Add Song", self.insert_trending_songs)

    def open_song_to_album_input_window(self, title, insert_method):
        input_window = tk.Toplevel(self.root)
        input_window.title(title)

    # Album input (Textbox to enter album ID or name manually)
        category_label = tk.Label(input_window, text="Category Id:", font=("Arial", 12))
        category_label.grid(row=1, column=0, padx=10, pady=10)
        category_entry = tk.Entry(input_window, font=("Arial", 12))
    
    # Fetch albums from the database and display in the entry as a list
        self.cursor.execute("SELECT category_id, category_name FROM categories")
        categories = self.cursor.fetchall()
        category_list = [f"{category[0]} - {category[1]}" for category in categories]
        category_entry.insert(0, ", ".join(category_list))  # Insert the list of albums into the textbox
        category_entry.grid(row=1, column=1, padx=10, pady=10)

    
        song_path_label = tk.Label(input_window, text="Song Path:", font=("Arial", 12))
        song_path_label.grid(row=3, column=0, padx=10, pady=10)
        path_entry = tk.Entry(input_window, font=("Arial", 12))
        path_entry.grid(row=3, column=1, padx=10, pady=10)


     # Submit button
        submit_button = tk.Button(input_window, text="Submit", command=lambda: insert_method(category_entry.get(), path_entry.get()), font=("Arial", 14))
        submit_button.grid(row=4, columnspan=2, pady=20)

    def select_song_file(self, input_window):
        # Open a file dialog to choose the song file
        self.selected_song_path = filedialog.askopenfilename(title="Select Song File", filetypes=(("Audio files", "*.mp3;*.ogg;*.wav"), ("All files", "*.*")))
        if self.selected_song_path:
            messagebox.showinfo("Song Selected", "Song file selected successfully")



    def insert_trending_songs(self,category_id,song_path):
        
        self.cursor.execute("INSERT INTO trending_songs(category_id,song_path) VALUES (%s, %s)", (category_id,song_path))
        self.conn.commit()
        messagebox.showinfo("Success", "Song Added Successfully")
        self.create_admin_panel()

    def list_trending_songs(self):
    # Execute SQL to fetch the songs in albums
        self.cursor.execute("SELECT * FROM trending_songs")
        trending_songs = self.cursor.fetchall()

    # Create a new window for displaying the list
        song_list_window = tk.Toplevel(self.root)
        song_list_window.title("Songs in Trending Category List")

    # Label for the window
        tk.Label(song_list_window, text="Trending Songs", font=("Arial", 16, "bold"), fg="#FF6F61", bg="#2E3B4E").pack(pady=10)

    # Create a Treeview widget
        tree = ttk.Treeview(song_list_window, columns=("Song ID", "Category ID", "Song Path"), show="headings")

    # Set headings
        tree.heading("Song ID", text="Song ID")
        tree.heading("Category ID", text="Category ID")
        tree.heading("Song Path", text="Song Path")
    
    # Set column widths if necessary
        tree.column("Song ID", width=100, anchor="center")
        tree.column("Category ID", width=100, anchor="center")
        tree.column("Song Path", width=800, anchor="w")
    
    # Insert data into the tree
        for song in trending_songs:
            tree.insert("", tk.END, values=(song[0], song[1], song[2]))

        tree.pack(pady=10)

    # Create a frame for update and delete buttons
        button_frame = tk.Frame(song_list_window)
        button_frame.pack(pady=10)

    # Function to update the selected song
        def update_selected_song():
            selected_item = tree.selection()
            if selected_item:
                song_id = tree.item(selected_item, "values")[0]
                self.update_trending_songs(song_id)  # Call the update method for the selected song

    # Function to delete the selected song
        def delete_selected_song():
            selected_item = tree.selection()
            if selected_item:
                song_id = tree.item(selected_item, "values")[0]
                self.delete_trending_songs(song_id)  # Call the delete method for the selected song

    # Create Update and Delete buttons for the selected song
        update_button = tk.Button(button_frame, text="Update Selected", command=update_selected_song)
        update_button.pack(side="left", padx=10, pady=5)
    
        delete_button = tk.Button(button_frame, text="Delete Selected", command=delete_selected_song)
        delete_button.pack(side="left", padx=10, pady=5)

    # Create close button at the bottom of the window
        close_button = tk.Button(song_list_window, text="Close", command=song_list_window.destroy, font=("Arial", 14))
        close_button.pack(pady=10)

    def update_trending_songs(self, song_id):
    # Open a new window to update song details
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Trending Song")
    
    # Get song details
        self.cursor.execute("SELECT * FROM trending_songs WHERE song_id = %s", (song_id,))
        song = self.cursor.fetchone()

    # Create fields to update song details
        category_id_label = tk.Label(update_window, text="Category ID:", font=("Arial", 12), bg="#FFFFFF")
        category_id_label.grid(row=0, column=0, padx=10, pady=10)
        category_id_entry = tk.Entry(update_window, font=("Arial", 12))
        category_id_entry.insert(0, song[1])  # Pre-fill with current category ID
        category_id_entry.grid(row=0, column=1, padx=10, pady=10)
    
        song_path_label = tk.Label(update_window, text="Song Path:", font=("Arial", 12), bg="#FFFFFF")
        song_path_label.grid(row=1, column=0, padx=10, pady=10)
        song_path_entry = tk.Entry(update_window, font=("Arial", 12))
        song_path_entry.insert(0, song[2])  # Pre-fill with current song path
        song_path_entry.grid(row=1, column=1, padx=10, pady=10)

        def save_update():
            category_id = category_id_entry.get()
            song_path = song_path_entry.get()
    
        # Call the method to update the song data in the database
            self.cursor.execute("""
                UPDATE trending_songs
                SET category_id = %s, song_path = %s
                WHERE song_id = %s
            """, (category_id, song_path, song_id))
            self.conn.commit()
            messagebox.showinfo("Success", "Trending Song Updated Successfully")
            update_window.destroy()  # Close the update window
    
        save_button = tk.Button(update_window, text="Save", command=save_update, font=("Arial", 14), bg="#4F81BD", fg="white")
        save_button.grid(row=2, columnspan=2, pady=20)
    
    def delete_trending_songs(self, song_id):
        confirm = messagebox.askyesno("Delete Song from Category", "Are you sure you want to delete this song?")
        if confirm:
            self.cursor.execute("DELETE FROM trending_songs WHERE song_id = %s", (song_id,))
            self.conn.commit()
            messagebox.showinfo("Success", "Song Deleted Successfully")
            self.create_admin_panel()  # Refresh admin panel after deletion
    

 #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    

# Manage Clasical Songs
    def add_classical_songs(self):
        self.open_song_to_album_input_window("Add Song", self.insert_classical_songs)

    def open_song_to_album_input_window(self, title, insert_method):
        input_window = tk.Toplevel(self.root)
        input_window.title(title)

    # Album input (Textbox to enter album ID or name manually)
        category_label = tk.Label(input_window, text="Category Id:", font=("Arial", 12))
        category_label.grid(row=1, column=0, padx=10, pady=10)
        category_entry = tk.Entry(input_window, font=("Arial", 12))
    
    # Fetch albums from the database and display in the entry as a list
        self.cursor.execute("SELECT category_id, category_name FROM categories")
        categories = self.cursor.fetchall()
        category_list = [f"{category[0]} - {category[1]}" for category in categories]
        category_entry.insert(0, ", ".join(category_list))  # Insert the list of albums into the textbox
        category_entry.grid(row=1, column=1, padx=10, pady=10)

    
        song_path_label = tk.Label(input_window, text="Song Path:", font=("Arial", 12))
        song_path_label.grid(row=3, column=0, padx=10, pady=10)
        path_entry = tk.Entry(input_window, font=("Arial", 12))
        path_entry.grid(row=3, column=1, padx=10, pady=10)


     # Submit button
        submit_button = tk.Button(input_window, text="Submit", command=lambda: insert_method(category_entry.get(), path_entry.get()), font=("Arial", 14))
        submit_button.grid(row=4, columnspan=2, pady=20)

    def select_song_file(self, input_window):
        # Open a file dialog to choose the song file
        self.selected_song_path = filedialog.askopenfilename(title="Select Song File", filetypes=(("Audio files", "*.mp3;*.ogg;*.wav"), ("All files", "*.*")))
        if self.selected_song_path:
            messagebox.showinfo("Song Selected", "Song file selected successfully")



    def insert_classical_songs(self,category_id,song_path):
        
        self.cursor.execute("INSERT INTO classical_songs(category_id,song_path) VALUES (%s, %s)", (category_id,song_path))
        self.conn.commit()
        messagebox.showinfo("Success", "Song Added Successfully")
        self.create_admin_panel()

    def list_classical_songs(self):
    # Execute SQL to fetch the songs in albums
        self.cursor.execute("SELECT * FROM classical_songs")
        classical_songs = self.cursor.fetchall()

    # Create a new window for displaying the list
        song_list_window = tk.Toplevel(self.root)
        song_list_window.title("Songs in Classical Category List")

    # Label for the window
        tk.Label(song_list_window, text="Classical Songs", font=("Arial", 16, "bold"), fg="#FF6F61", bg="#2E3B4E").pack(pady=10)

    # Create a Treeview widget
        tree = ttk.Treeview(song_list_window, columns=("Song ID", "Category ID", "Song Path"), show="headings")

    # Set headings
        tree.heading("Song ID", text="Song ID")
        tree.heading("Category ID", text="Category ID")
        tree.heading("Song Path", text="Song Path")
    
    # Set column widths if necessary
        tree.column("Song ID", width=100, anchor="center")
        tree.column("Category ID", width=100, anchor="center")
        tree.column("Song Path", width=800, anchor="w")

    # Insert data into the tree
        for song in classical_songs:
            tree.insert("", tk.END, values=(song[0], song[1], song[2]))

        tree.pack(pady=10)

    # Create a frame for update and delete buttons
        button_frame = tk.Frame(song_list_window)
        button_frame.pack(pady=10)

    # Function to update the selected song
        def update_selected_song():
            selected_item = tree.selection()
            if selected_item:
                song_id = tree.item(selected_item, "values")[0]
                self.update_classical_songs(song_id)  # Call the update method for the selected song

    # Function to delete the selected song
        def delete_selected_song():
            selected_item = tree.selection()
            if selected_item:
                song_id = tree.item(selected_item, "values")[0]
                self.delete_classical_songs(song_id)  # Call the delete method for the selected song

    # Create Update and Delete buttons for the selected song
        update_button = tk.Button(button_frame, text="Update Selected", command=update_selected_song)
        update_button.pack(side="left", padx=10, pady=5)

        delete_button = tk.Button(button_frame, text="Delete Selected", command=delete_selected_song)
        delete_button.pack(side="left", padx=10, pady=5)

    # Create close button at the bottom of the window
        close_button = tk.Button(song_list_window, text="Close", command=song_list_window.destroy, font=("Arial", 14))
        close_button.pack(pady=10)

    def update_classical_songs(self, song_id):
    # Open a new window to update song details
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Classical Song")
    
        # Get song details
        self.cursor.execute("SELECT * FROM classical_songs WHERE song_id = %s", (song_id,))
        song = self.cursor.fetchone()
    
    # Create fields to update song details
        category_id_label = tk.Label(update_window, text="Category ID:", font=("Arial", 12), bg="#FFFFFF")
        category_id_label.grid(row=0, column=0, padx=10, pady=10)
        category_id_entry = tk.Entry(update_window, font=("Arial", 12))
        category_id_entry.insert(0, song[1])  # Pre-fill with current category ID
        category_id_entry.grid(row=0, column=1, padx=10, pady=10)
    
        song_path_label = tk.Label(update_window, text="Song Path:", font=("Arial", 12), bg="#FFFFFF")
        song_path_label.grid(row=1, column=0, padx=10, pady=10)
        song_path_entry = tk.Entry(update_window, font=("Arial", 12))
        song_path_entry.insert(0, song[2])  # Pre-fill with current song path
        song_path_entry.grid(row=1, column=1, padx=10, pady=10)

        def save_update():
            category_id = category_id_entry.get()
            song_path = song_path_entry.get()
    
            # Call the method to update the song data in the database
            self.cursor.execute("""
                UPDATE classical_songs
                SET category_id = %s, song_path = %s
                WHERE song_id = %s
            """, (category_id, song_path, song_id))
            self.conn.commit()
            messagebox.showinfo("Success", "Classical Song Updated Successfully")
            update_window.destroy()  # Close the update window
    
        save_button = tk.Button(update_window, text="Save", command=save_update, font=("Arial", 14), bg="#4F81BD", fg="white")
        save_button.grid(row=2, columnspan=2, pady=20)
    
    def delete_classical_songs(self, song_id):
        confirm = messagebox.askyesno("Delete Song from Category", "Are you sure you want to delete this song?")
        if confirm:
            self.cursor.execute("DELETE FROM classical_songs WHERE song_id = %s", (song_id,))
            self.conn.commit()
            messagebox.showinfo("Success", "Song Deleted Successfully")
            self.create_admin_panel()  # Refresh admin panel after deletion
    

 #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    

# Manage english Songs
    def add_english_songs(self):
        self.open_song_to_album_input_window("Add Song", self.insert_english_songs)

    def open_song_to_album_input_window(self, title, insert_method):
        input_window = tk.Toplevel(self.root)
        input_window.title(title)

    # Album input (Textbox to enter album ID or name manually)
        category_label = tk.Label(input_window, text="Category Id:", font=("Arial", 12))
        category_label.grid(row=1, column=0, padx=10, pady=10)
        category_entry = tk.Entry(input_window, font=("Arial", 12))
    
    # Fetch albums from the database and display in the entry as a list
        self.cursor.execute("SELECT category_id, category_name FROM categories")
        categories = self.cursor.fetchall()
        category_list = [f"{category[0]} - {category[1]}" for category in categories]
        category_entry.insert(0, ", ".join(category_list))  # Insert the list of albums into the textbox
        category_entry.grid(row=1, column=1, padx=10, pady=10)

    
        song_path_label = tk.Label(input_window, text="Song Path:", font=("Arial", 12))
        song_path_label.grid(row=3, column=0, padx=10, pady=10)
        path_entry = tk.Entry(input_window, font=("Arial", 12))
        path_entry.grid(row=3, column=1, padx=10, pady=10)


     # Submit button
        submit_button = tk.Button(input_window, text="Submit", command=lambda: insert_method(category_entry.get(), path_entry.get()), font=("Arial", 14))
        submit_button.grid(row=4, columnspan=2, pady=20)

    def select_song_file(self, input_window):
        # Open a file dialog to choose the song file
        self.selected_song_path = filedialog.askopenfilename(title="Select Song File", filetypes=(("Audio files", "*.mp3;*.ogg;*.wav"), ("All files", "*.*")))
        if self.selected_song_path:
            messagebox.showinfo("Song Selected", "Song file selected successfully")



    def insert_english_songs(self,category_id,song_path):
        
        self.cursor.execute("INSERT INTO english_songs(category_id,song_path) VALUES (%s, %s)", (category_id,song_path))
        self.conn.commit()
        messagebox.showinfo("Success", "Song Added Successfully")
        self.create_admin_panel()

    def list_english_songs(self):
    # Execute SQL to fetch the songs in albums
        self.cursor.execute("SELECT * FROM english_songs")
        english_songs = self.cursor.fetchall()

    # Create a new window for displaying the list
        song_list_window = tk.Toplevel(self.root)
        song_list_window.title("Songs in English Category List")

    # Label for the window
        tk.Label(song_list_window, text="English Songs", font=("Arial", 16, "bold"), fg="#FF6F61", bg="#2E3B4E").pack(pady=10)

    # Create a Treeview widget
        tree = ttk.Treeview(song_list_window, columns=("Song ID", "Category ID", "Song Path"), show="headings")

    # Set headings
        tree.heading("Song ID", text="Song ID")
        tree.heading("Category ID", text="Category ID")
        tree.heading("Song Path", text="Song Path")

    # Set column widths if necessary
        tree.column("Song ID", width=100, anchor="center")
        tree.column("Category ID", width=100, anchor="center")
        tree.column("Song Path", width=800, anchor="w")

    # Insert data into the tree
        for song in english_songs:
            tree.insert("", tk.END, values=(song[0], song[1], song[2]))
    
        tree.pack(pady=10)

    # Create a frame for update and delete buttons
        button_frame = tk.Frame(song_list_window)
        button_frame.pack(pady=10)

    # Function to update the selected song
        def update_selected_song():
            selected_item = tree.selection()
            if selected_item:
                song_id = tree.item(selected_item, "values")[0]
                self.update_english_songs(song_id)  # Call the update method for the selected song
    
    # Function to delete the selected song
        def delete_selected_song():
            selected_item = tree.selection()
            if selected_item:
                song_id = tree.item(selected_item, "values")[0]
                self.delete_english_songs(song_id)  # Call the delete method for the selected song

    # Create Update and Delete buttons for the selected song
        update_button = tk.Button(button_frame, text="Update Selected", command=update_selected_song)
        update_button.pack(side="left", padx=10, pady=5)
    
        delete_button = tk.Button(button_frame, text="Delete Selected", command=delete_selected_song)
        delete_button.pack(side="left", padx=10, pady=5)

    # Create close button at the bottom of the window
        close_button = tk.Button(song_list_window, text="Close", command=song_list_window.destroy, font=("Arial", 14))
        close_button.pack(pady=10)
    
    def update_english_songs(self, song_id):
        # Open a new window to update song details
        update_window = tk.Toplevel(self.root)
        update_window.title("Update English Song")
    
            # Get song details
        self.cursor.execute("SELECT * FROM english_songs WHERE song_id = %s", (song_id,))
        song = self.cursor.fetchone()
    
        # Create fields to update song details
        category_id_label = tk.Label(update_window, text="Category ID:", font=("Arial", 12), bg="#FFFFFF")
        category_id_label.grid(row=0, column=0, padx=10, pady=10)
        category_id_entry = tk.Entry(update_window, font=("Arial", 12))
        category_id_entry.insert(0, song[1])  # Pre-fill with current category ID
        category_id_entry.grid(row=0, column=1, padx=10, pady=10)
    
        song_path_label = tk.Label(update_window, text="Song Path:", font=("Arial", 12), bg="#FFFFFF")
        song_path_label.grid(row=1, column=0, padx=10, pady=10)
        song_path_entry = tk.Entry(update_window, font=("Arial", 12))
        song_path_entry.insert(0, song[2])  # Pre-fill with current song path
        song_path_entry.grid(row=1, column=1, padx=10, pady=10)
    
        def save_update():
            category_id = category_id_entry.get()
            song_path = song_path_entry.get()
    
        # Call the method to update the song data in the database
            self.cursor.execute("""
                UPDATE english_songs
                SET category_id = %s, song_path = %s
                WHERE song_id = %s
            """, (category_id, song_path, song_id))
            self.conn.commit()
            messagebox.showinfo("Success", "English Song Updated Successfully")
            update_window.destroy()  # Close the update window
    
        save_button = tk.Button(update_window, text="Save", command=save_update, font=("Arial", 14), bg="#4F81BD", fg="white")
        save_button.grid(row=2, columnspan=2, pady=20)
    
    def delete_english_songs(self, song_id):
        confirm = messagebox.askyesno("Delete Song from Category", "Are you sure you want to delete this song?")
        if confirm:
            self.cursor.execute("DELETE FROM english_songs WHERE song_id = %s", (song_id,))
            self.conn.commit()
            messagebox.showinfo("Success", "Song Deleted Successfully")
            self.create_admin_panel()  # Refresh admin panel after deletion



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    

# Manage Punjabi Songs
    def add_punjabi_songs(self):
        self.open_song_to_album_input_window("Add Song", self.insert_punjabi_songs)

    def open_song_to_album_input_window(self, title, insert_method):
        input_window = tk.Toplevel(self.root)
        input_window.title(title)

    # Album input (Textbox to enter album ID or name manually)
        category_label = tk.Label(input_window, text="Category Id:", font=("Arial", 12))
        category_label.grid(row=1, column=0, padx=10, pady=10)
        category_entry = tk.Entry(input_window, font=("Arial", 12))
    
    # Fetch albums from the database and display in the entry as a list
        self.cursor.execute("SELECT category_id, category_name FROM categories")
        categories = self.cursor.fetchall()
        category_list = [f"{category[0]} - {category[1]}" for category in categories]
        category_entry.insert(0, ", ".join(category_list))  # Insert the list of albums into the textbox
        category_entry.grid(row=1, column=1, padx=10, pady=10)

    
        song_path_label = tk.Label(input_window, text="Song Path:", font=("Arial", 12))
        song_path_label.grid(row=3, column=0, padx=10, pady=10)
        path_entry = tk.Entry(input_window, font=("Arial", 12))
        path_entry.grid(row=3, column=1, padx=10, pady=10)


     # Submit button
        submit_button = tk.Button(input_window, text="Submit", command=lambda: insert_method(category_entry.get(), path_entry.get()), font=("Arial", 14))
        submit_button.grid(row=4, columnspan=2, pady=20)

    def select_song_file(self, input_window):
        # Open a file dialog to choose the song file
        self.selected_song_path = filedialog.askopenfilename(title="Select Song File", filetypes=(("Audio files", "*.mp3;*.ogg;*.wav"), ("All files", "*.*")))
        if self.selected_song_path:
            messagebox.showinfo("Song Selected", "Song file selected successfully")



    def insert_punjabi_songs(self,category_id,song_path):
        
        self.cursor.execute("INSERT INTO punjabi_songs(category_id,song_path) VALUES (%s, %s)", (category_id,song_path))
        self.conn.commit()
        messagebox.showinfo("Success", "Song Added Successfully")
        self.create_admin_panel()

    def list_punjabi_songs(self):
        # Execute SQL to fetch the songs in albums
        self.cursor.execute("SELECT * FROM punjabi_songs")
        punjabi_songs = self.cursor.fetchall()

    # Create a new window for displaying the list
        song_list_window = tk.Toplevel(self.root)
        song_list_window.title("Songs in Punjabi Category List")
    
    # Label for the window
        tk.Label(song_list_window, text="Punjabi Songs", font=("Arial", 16, "bold"), fg="#FF6F61", bg="#2E3B4E").pack(pady=10)
    
    # Create a Treeview widget
        tree = ttk.Treeview(song_list_window, columns=("Song ID", "Category ID", "Song Path"), show="headings")

    # Set headings
        tree.heading("Song ID", text="Song ID")
        tree.heading("Category ID", text="Category ID")
        tree.heading("Song Path", text="Song Path")

    # Set column widths if necessary
        tree.column("Song ID", width=100, anchor="center")
        tree.column("Category ID", width=100, anchor="center")
        tree.column("Song Path", width=800, anchor="w")

    # Insert data into the tree
        for song in punjabi_songs:
            tree.insert("", tk.END, values=(song[0], song[1], song[2]))
    
        tree.pack(pady=10)
    
    # Create a frame for update and delete buttons
        button_frame = tk.Frame(song_list_window)
        button_frame.pack(pady=10)

    # Function to update the selected song
        def update_selected_song():
            selected_item = tree.selection()
            if selected_item:
                song_id = tree.item(selected_item, "values")[0]
                self.update_punjabi_songs(song_id)  # Call the update method for the selected song
    
    # Function to delete the selected song
        def delete_selected_song():
            selected_item = tree.selection()
            if selected_item:
                song_id = tree.item(selected_item, "values")[0]
                self.delete_punjabi_songs(song_id)  # Call the delete method for the selected song
    
    # Create Update and Delete buttons for the selected song
        update_button = tk.Button(button_frame, text="Update Selected", command=update_selected_song)
        update_button.pack(side="left", padx=10, pady=5)
    
        delete_button = tk.Button(button_frame, text="Delete Selected", command=delete_selected_song)
        delete_button.pack(side="left", padx=10, pady=5)
    
    # Create close button at the bottom of the window
        close_button = tk.Button(song_list_window, text="Close", command=song_list_window.destroy, font=("Arial", 14))
        close_button.pack(pady=10)
    
    def update_punjabi_songs(self, song_id):
    # Open a new window to update song details
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Punjabi Song")
    
    # Get song details
        self.cursor.execute("SELECT * FROM punjabi_songs WHERE song_id = %s", (song_id,))
        song = self.cursor.fetchone()
    
    # Create fields to update song details
        category_id_label = tk.Label(update_window, text="Category ID:", font=("Arial", 12), bg="#FFFFFF")
        category_id_label.grid(row=0, column=0, padx=10, pady=10)
        category_id_entry = tk.Entry(update_window, font=("Arial", 12))
        category_id_entry.insert(0, song[1])  # Pre-fill with current category ID
        category_id_entry.grid(row=0, column=1, padx=10, pady=10)
    
        song_path_label = tk.Label(update_window, text="Song Path:", font=("Arial", 12), bg="#FFFFFF")
        song_path_label.grid(row=1, column=0, padx=10, pady=10)
        song_path_entry = tk.Entry(update_window, font=("Arial", 12))
        song_path_entry.insert(0, song[2])  # Pre-fill with current song path
        song_path_entry.grid(row=1, column=1, padx=10, pady=10)
    
        def save_update():
            category_id = category_id_entry.get()
            song_path = song_path_entry.get()
    
        # Call the method to update the song data in the database
            self.cursor.execute("""
                UPDATE punjabi_songs
                SET category_id = %s, song_path = %s
                WHERE song_id = %s
            """, (category_id, song_path, song_id))
            self.conn.commit()
            messagebox.showinfo("Success", "Punjabi Song Updated Successfully")
            update_window.destroy()  # Close the update window
    
        save_button = tk.Button(update_window, text="Save", command=save_update, font=("Arial", 14), bg="#4F81BD", fg="white")
        save_button.grid(row=2, columnspan=2, pady=20)

    def delete_punjabi_songs(self, song_id):
        confirm = messagebox.askyesno("Delete Song from Category", "Are you sure you want to delete this song?")
        if confirm:
            self.cursor.execute("DELETE FROM punjabi_songs WHERE song_id = %s", (song_id,))
            self.conn.commit()
            messagebox.showinfo("Success", "Song Deleted Successfully")
            self.create_admin_panel()  # Refresh admin panel after deletion
    


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    

# Manage Hip Hop Songs
    def add_hiphop_songs(self):
        self.open_song_to_album_input_window("Add Song", self.insert_hiphop_songs)

    def open_song_to_album_input_window(self, title, insert_method):
        input_window = tk.Toplevel(self.root)
        input_window.title(title)

    # Album input (Textbox to enter album ID or name manually)
        category_label = tk.Label(input_window, text="Category Id:", font=("Arial", 12))
        category_label.grid(row=1, column=0, padx=10, pady=10)
        category_entry = tk.Entry(input_window, font=("Arial", 12))
    
    # Fetch albums from the database and display in the entry as a list
        self.cursor.execute("SELECT category_id, category_name FROM categories")
        categories = self.cursor.fetchall()
        category_list = [f"{category[0]} - {category[1]}" for category in categories]
        category_entry.insert(0, ", ".join(category_list))  # Insert the list of albums into the textbox
        category_entry.grid(row=1, column=1, padx=10, pady=10)

    
        song_path_label = tk.Label(input_window, text="Song Path:", font=("Arial", 12))
        song_path_label.grid(row=3, column=0, padx=10, pady=10)
        path_entry = tk.Entry(input_window, font=("Arial", 12))
        path_entry.grid(row=3, column=1, padx=10, pady=10)


     # Submit button
        submit_button = tk.Button(input_window, text="Submit", command=lambda: insert_method(category_entry.get(), path_entry.get()), font=("Arial", 14))
        submit_button.grid(row=4, columnspan=2, pady=20)

    def select_song_file(self, input_window):
        # Open a file dialog to choose the song file
        self.selected_song_path = filedialog.askopenfilename(title="Select Song File", filetypes=(("Audio files", "*.mp3;*.ogg;*.wav"), ("All files", "*.*")))
        if self.selected_song_path:
            messagebox.showinfo("Song Selected", "Song file selected successfully")



    def insert_hiphop_songs(self,category_id,song_path):
        
        self.cursor.execute("INSERT INTO hiphop_songs(category_id,song_path) VALUES (%s, %s)", (category_id,song_path))
        self.conn.commit()
        messagebox.showinfo("Success", "Song Added Successfully")
        self.create_admin_panel()

    def list_hiphop_songs(self):
    # Execute SQL to fetch the songs in albums
        self.cursor.execute("SELECT * FROM hiphop_songs")
        hiphop_songs = self.cursor.fetchall()

    # Create a new window for displaying the list
        song_list_window = tk.Toplevel(self.root)
        song_list_window.title("Songs in Hip-Hop Category List")

    # Label for the window
        tk.Label(song_list_window, text="Hip-Hop Songs", font=("Arial", 16, "bold"), fg="#FF6F61", bg="#2E3B4E").pack(pady=10)

    # Create a Treeview widget
        tree = ttk.Treeview(song_list_window, columns=("Song ID", "Category ID", "Song Path"), show="headings")

    # Set headings
        tree.heading("Song ID", text="Song ID")
        tree.heading("Category ID", text="Category ID")
        tree.heading("Song Path", text="Song Path")

    # Set column widths if necessary
        tree.column("Song ID", width=100, anchor="center")
        tree.column("Category ID", width=100, anchor="center")
        tree.column("Song Path", width=800, anchor="w")
    
    # Insert data into the tree
        for song in hiphop_songs:
            tree.insert("", tk.END, values=(song[0], song[1], song[2]))

        tree.pack(pady=10)

    # Create a frame for update and delete buttons
        button_frame = tk.Frame(song_list_window)
        button_frame.pack(pady=10)

    # Function to update the selected song
        def update_selected_song():
            selected_item = tree.selection()
            if selected_item:
                song_id = tree.item(selected_item, "values")[0]
                self.update_hiphop_songs(song_id)  # Call the update method for the selected song
    
        # Function to delete the selected song
        def delete_selected_song():
            selected_item = tree.selection()
            if selected_item:
                song_id = tree.item(selected_item, "values")[0]
                self.delete_hiphop_songs(song_id)  # Call the delete method for the selected song
    
    # Create Update and Delete buttons for the selected song
        update_button = tk.Button(button_frame, text="Update Selected", command=update_selected_song)
        update_button.pack(side="left", padx=10, pady=5)
    
        delete_button = tk.Button(button_frame, text="Delete Selected", command=delete_selected_song)
        delete_button.pack(side="left", padx=10, pady=5)

    # Create close button at the bottom of the window
        close_button = tk.Button(song_list_window, text="Close", command=song_list_window.destroy, font=("Arial", 14))
        close_button.pack(pady=10)

    def update_hiphop_songs(self, song_id):
        # Open a new window to update song details
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Hip-Hop Song")
    
        # Get song details
        self.cursor.execute("SELECT * FROM hiphop_songs WHERE song_id = %s", (song_id,))
        song = self.cursor.fetchone()
    
        # Create fields to update song details
        category_id_label = tk.Label(update_window, text="Category ID:", font=("Arial", 12), bg="#FFFFFF")
        category_id_label.grid(row=0, column=0, padx=10, pady=10)
        category_id_entry = tk.Entry(update_window, font=("Arial", 12))
        category_id_entry.insert(0, song[1])  # Pre-fill with current category ID
        category_id_entry.grid(row=0, column=1, padx=10, pady=10)
    
        song_path_label = tk.Label(update_window, text="Song Path:", font=("Arial", 12), bg="#FFFFFF")
        song_path_label.grid(row=1, column=0, padx=10, pady=10)
        song_path_entry = tk.Entry(update_window, font=("Arial", 12))
        song_path_entry.insert(0, song[2])  # Pre-fill with current song path
        song_path_entry.grid(row=1, column=1, padx=10, pady=10)
    
        def save_update():
            category_id = category_id_entry.get()
            song_path = song_path_entry.get()
    
            # Call the method to update the song data in the database
            self.cursor.execute("""
                UPDATE hiphop_songs
                SET category_id = %s, song_path = %s
                WHERE song_id = %s
            """, (category_id, song_path, song_id))
            self.conn.commit()
            messagebox.showinfo("Success", "Hip-Hop Song Updated Successfully")
            update_window.destroy()  # Close the update window
    
        save_button = tk.Button(update_window, text="Save", command=save_update, font=("Arial", 14), bg="#4F81BD", fg="white")
        save_button.grid(row=2, columnspan=2, pady=20)
    
    def delete_hiphop_songs(self, song_id):
        confirm = messagebox.askyesno("Delete Song from Category", "Are you sure you want to delete this song?")
        if confirm:
            self.cursor.execute("DELETE FROM hiphop_songs WHERE song_id = %s", (song_id,))
            self.conn.commit()
            messagebox.showinfo("Success", "Song Deleted Successfully")
            self.create_admin_panel()  # Refresh admin panel after deletion


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    

# Manage Wedding Songs
    def add_wedding_songs(self):
        self.open_song_to_album_input_window("Add Song", self.insert_wedding_songs)

    def open_song_to_album_input_window(self, title, insert_method):
        input_window = tk.Toplevel(self.root)
        input_window.title(title)

    # Album input (Textbox to enter album ID or name manually)
        category_label = tk.Label(input_window, text="Category Id:", font=("Arial", 12))
        category_label.grid(row=1, column=0, padx=10, pady=10)
        category_entry = tk.Entry(input_window, font=("Arial", 12))
    
    # Fetch albums from the database and display in the entry as a list
        self.cursor.execute("SELECT category_id, category_name FROM categories")
        categories = self.cursor.fetchall()
        category_list = [f"{category[0]} - {category[1]}" for category in categories]
        category_entry.insert(0, ", ".join(category_list))  # Insert the list of albums into the textbox
        category_entry.grid(row=1, column=1, padx=10, pady=10)

    
        song_path_label = tk.Label(input_window, text="Song Path:", font=("Arial", 12))
        song_path_label.grid(row=3, column=0, padx=10, pady=10)
        path_entry = tk.Entry(input_window, font=("Arial", 12))
        path_entry.grid(row=3, column=1, padx=10, pady=10)


     # Submit button
        submit_button = tk.Button(input_window, text="Submit", command=lambda: insert_method(category_entry.get(), path_entry.get()), font=("Arial", 14))
        submit_button.grid(row=4, columnspan=2, pady=20)

    def select_song_file(self, input_window):
        # Open a file dialog to choose the song file
        self.selected_song_path = filedialog.askopenfilename(title="Select Song File", filetypes=(("Audio files", "*.mp3;*.ogg;*.wav"), ("All files", "*.*")))
        if self.selected_song_path:
            messagebox.showinfo("Song Selected", "Song file selected successfully")



    def insert_wedding_songs(self,category_id,song_path):
        
        self.cursor.execute("INSERT INTO wedding_songs(category_id,song_path) VALUES (%s, %s)", (category_id,song_path))
        self.conn.commit()
        messagebox.showinfo("Success", "Song Added Successfully")
        self.create_admin_panel()

    def list_wedding_songs(self):
    # Execute SQL to fetch the songs in albums
        self.cursor.execute("SELECT * FROM wedding_songs")
        wedding_songs = self.cursor.fetchall()

    # Create a new window for displaying the list
        song_list_window = tk.Toplevel(self.root)
        song_list_window.title("Songs in Wedding Category List")

    # Label for the window
        tk.Label(song_list_window, text="Wedding Songs", font=("Arial", 16, "bold"), fg="#FF6F61", bg="#2E3B4E").pack(pady=10)

    # Create a Treeview widget
        tree = ttk.Treeview(song_list_window, columns=("Song ID", "Category ID", "Song Path"), show="headings")

    # Set headings
        tree.heading("Song ID", text="Song ID")
        tree.heading("Category ID", text="Category ID")
        tree.heading("Song Path", text="Song Path")

    # Set column widths if necessary
        tree.column("Song ID", width=100, anchor="center")
        tree.column("Category ID", width=100, anchor="center")
        tree.column("Song Path", width=800, anchor="w")

    # Insert data into the tree
        for song in wedding_songs:
            tree.insert("", tk.END, values=(song[0], song[1], song[2]))

        tree.pack(pady=10)

    # Create a frame for update and delete buttons
        button_frame = tk.Frame(song_list_window)
        button_frame.pack(pady=10)

    # Function to update the selected song
        def update_selected_song():
            selected_item = tree.selection()
            if selected_item:
                song_id = tree.item(selected_item, "values")[0]
                self.update_wedding_songs(song_id)  # Call the update method for the selected song

    # Function to delete the selected song
        def delete_selected_song():
            selected_item = tree.selection()
            if selected_item:
                song_id = tree.item(selected_item, "values")[0]
                self.delete_wedding_songs(song_id)  # Call the delete method for the selected song
    
    # Create Update and Delete buttons for the selected song
        update_button = tk.Button(button_frame, text="Update Selected", command=update_selected_song)
        update_button.pack(side="left", padx=10, pady=5)

        delete_button = tk.Button(button_frame, text="Delete Selected", command=delete_selected_song)
        delete_button.pack(side="left", padx=10, pady=5)
    
    # Create close button at the bottom of the window
        close_button = tk.Button(song_list_window, text="Close", command=song_list_window.destroy, font=("Arial", 14))
        close_button.pack(pady=10)
    
    def update_wedding_songs(self, song_id):
        # Open a new window to update song details
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Wedding Song")
    
        # Get song details
        self.cursor.execute("SELECT * FROM wedding_songs WHERE song_id = %s", (song_id,))
        song = self.cursor.fetchone()
    
        # Create fields to update song details
        category_id_label = tk.Label(update_window, text="Category ID:", font=("Arial", 12), bg="#FFFFFF")
        category_id_label.grid(row=0, column=0, padx=10, pady=10)
        category_id_entry = tk.Entry(update_window, font=("Arial", 12))
        category_id_entry.insert(0, song[1])  # Pre-fill with current category ID
        category_id_entry.grid(row=0, column=1, padx=10, pady=10)
    
        song_path_label = tk.Label(update_window, text="Song Path:", font=("Arial", 12), bg="#FFFFFF")
        song_path_label.grid(row=1, column=0, padx=10, pady=10)
        song_path_entry = tk.Entry(update_window, font=("Arial", 12))
        song_path_entry.insert(0, song[2])  # Pre-fill with current song path
        song_path_entry.grid(row=1, column=1, padx=10, pady=10)
    
        def save_update():
            category_id = category_id_entry.get()
            song_path = song_path_entry.get()
    
            # Call the method to update the song data in the database
            self.cursor.execute("""
                UPDATE wedding_songs
                SET category_id = %s, song_path = %s
                WHERE song_id = %s
            """, (category_id, song_path, song_id))
            self.conn.commit()
            messagebox.showinfo("Success", "Wedding Song Updated Successfully")
            update_window.destroy()  # Close the update window
    
        save_button = tk.Button(update_window, text="Save", command=save_update, font=("Arial", 14), bg="#4F81BD", fg="white")
        save_button.grid(row=2, columnspan=2, pady=20)
    
    def delete_wedding_songs(self, song_id):
        confirm = messagebox.askyesno("Delete Song from Category", "Are you sure you want to delete this song?")
        if confirm:
            self.cursor.execute("DELETE FROM wedding_songs WHERE song_id = %s", (song_id,))
            self.conn.commit()
            messagebox.showinfo("Success", "Song Deleted Successfully")
            self.create_admin_panel()  # Refresh admin panel after deletion
    


# Create the Tkinter window
root = tk.Tk()
app = MusicPlayerApp(root)

# Start the Tkinter event loop
root.mainloop()
