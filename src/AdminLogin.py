import os
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import re
import subprocess
from PIL import Image, ImageTk


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # MusixBeat/
ASSETS_DIR = os.path.join(PROJECT_ROOT, "assets")  # folder for icons/images


def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="music_player"
    )


def login():
    username = entry_username.get()
    password = entry_password.get()
    
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM AdminLogin WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()
    
    if user:
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
        # Launch AdminPanel.py
        panel_path = os.path.join(os.path.dirname(__file__), "AdminPanel.py")
        subprocess.run(["python", panel_path])
        root.quit()
    else:
        messagebox.showerror("Error", "Invalid username or password.")
    
    cursor.close()
    db.close()

 
def signup():
    username = entry_signup_username.get()
    password = entry_signup_password.get()
    email = entry_signup_email.get()

    # Validation
    if not re.match(r'^(?=.*\d)(?=.*[!@#$%^&*])', username):
        messagebox.showerror("Error", "Username must contain at least a number and a special symbol.")
        return

    if len(password) < 6:
        messagebox.showerror("Error", "Password must be at least 6 characters long.")
        return

    if not re.match(r'\S+@\S+\.\S+', email):
        messagebox.showerror("Error", "Invalid email address.")
        return

    db = connect_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO AdminLogin (username, password, email) VALUES (%s,%s,%s)",
        (username, password, email)
    )
    db.commit()
    cursor.close()
    db.close()

    messagebox.showinfo("Success", "Account created successfully.")
    show_login_form()


def show_signup_form():
    login_frame.pack_forget()
    signup_frame.pack(padx=60, pady=60)

def show_login_form():
    signup_frame.pack_forget()
    login_frame.pack(padx=60, pady=60)


def forgot_password():
    forgot_path = os.path.join(os.path.dirname(__file__), "forgetPassword.py")
    subprocess.run(["python", forgot_path])
    root.quit()

# =======================
# Toggle Password Visibility
# =======================
def toggle_password_visibility(event, entry_field, icon_label):
    if entry_field.cget('show') == '':
        entry_field.config(show='*')
        icon_label.config(image=eye_open)
    else:
        entry_field.config(show='')
        icon_label.config(image=eye_closed)


root = tk.Tk()
root.title("Admin Login Form")
root.geometry("900x900")
root.configure(bg="#2E3B4E")
font = ("Arial", 14)
entry_font = ("Arial", 12)

eye_open_image = Image.open(os.path.join(ASSETS_DIR, "eye_opened.jpg"))
eye_closed_image = Image.open(os.path.join(ASSETS_DIR, "eye_closed.jpg"))
eye_open = ImageTk.PhotoImage(eye_open_image.resize((20, 20)))
eye_closed = ImageTk.PhotoImage(eye_closed_image.resize((20, 20)))


login_frame = tk.Frame(root, bg="#f0f0f0", relief="solid", bd=7, padx=80, pady=60, highlightbackground="#4F81BD", highlightthickness=3)
tk.Label(login_frame, text="Admin Login", font=("Arial", 30, "bold"), bg="#f0f0f0", fg="#2E3B4E").grid(row=0, column=0, columnspan=2, pady=20)

tk.Label(login_frame, text="Username:", font=("Arial", 12, "bold"), bg="#f0f0f0", fg="#2E3B4E").grid(row=1, column=0, pady=15, padx=25, sticky="e")
entry_username = tk.Entry(login_frame, font=entry_font, width=25)
entry_username.grid(row=1, column=1, pady=15, padx=25)

tk.Label(login_frame, text="Password:", font=("Arial", 12, "bold"), bg="#f0f0f0", fg="#2E3B4E").grid(row=2, column=0, pady=15, padx=25, sticky="e")
entry_password = tk.Entry(login_frame, show="*", font=entry_font, width=25)
entry_password.grid(row=2, column=1, pady=15, padx=25)

toggle_password_icon = tk.Label(login_frame, image=eye_open)
toggle_password_icon.grid(row=2, column=2, padx=10)
toggle_password_icon.bind("<Button-1>", lambda e: toggle_password_visibility(e, entry_password, toggle_password_icon))

login_button = tk.Button(login_frame, text="Login", font=font, command=login, bg="#4CAF50", fg="#000000", width=15)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

forgot_password_link = tk.Label(login_frame, text="Forgot Password?", font=("Arial", 12, "italic"), bg="#f0f0f0", fg="#4F81BD")
forgot_password_link.grid(row=4, column=0, columnspan=2, pady=15)
forgot_password_link.bind("<Button-1>", lambda e: forgot_password())

sign_up_link = tk.Label(login_frame, text="Don't have an account? Sign Up", font=("Arial", 12, "italic"), bg="#f0f0f0", fg="#4F81BD")
sign_up_link.grid(row=5, column=0, columnspan=2, pady=15)
sign_up_link.bind("<Button-1>", lambda e: show_signup_form())


# Signup Frame
 
signup_frame = tk.Frame(root, bg="#f0f0f0", relief="solid", bd=7, padx=80, pady=60, highlightbackground="#4F81BD", highlightthickness=3)
tk.Label(signup_frame, text="Sign Up", font=("Arial", 30, "bold"), bg="#f0f0f0", fg="#2E3B4E").grid(row=0, column=0, columnspan=2, pady=20)

tk.Label(signup_frame, text="Username:", font=("Arial", 12, "bold"), bg="#f0f0f0", fg="#2E3B4E").grid(row=1, column=0, pady=15, padx=25, sticky="e")
entry_signup_username = tk.Entry(signup_frame, font=entry_font, width=25)
entry_signup_username.grid(row=1, column=1, pady=15, padx=25)

tk.Label(signup_frame, text="Password:", font=("Arial", 12, "bold"), bg="#f0f0f0", fg="#2E3B4E").grid(row=2, column=0, pady=15, padx=25, sticky="e")
entry_signup_password = tk.Entry(signup_frame, show="*", font=entry_font, width=25)
entry_signup_password.grid(row=2, column=1, pady=15, padx=25)

toggle_signup_password_icon = tk.Label(signup_frame, image=eye_open)
toggle_signup_password_icon.grid(row=2, column=2, padx=10)
toggle_signup_password_icon.bind("<Button-1>", lambda e: toggle_password_visibility(e, entry_signup_password, toggle_signup_password_icon))

tk.Label(signup_frame, text="Email:", font=("Arial", 12, "bold"), bg="#f0f0f0", fg="#2E3B4E").grid(row=3, column=0, pady=15, padx=25, sticky="e")
entry_signup_email = tk.Entry(signup_frame, font=entry_font, width=25)
entry_signup_email.grid(row=3, column=1, pady=15, padx=25)

signup_button = tk.Button(signup_frame, text="Sign Up", font=font, command=signup, bg="#4CAF50", fg="#000000", width=15)
signup_button.grid(row=5, column=0, columnspan=2, pady=30)

back_to_login_link = tk.Label(signup_frame, text="Already have an account? Login", font=("Arial", 12, "italic"), bg="#f0f0f0", fg="#4F81BD")
back_to_login_link.grid(row=6, column=0, columnspan=2, pady=15)
back_to_login_link.bind("<Button-1>", lambda e: show_login_form())


show_login_form()

root.mainloop()
