import tkinter as tk
from tkinter import messagebox
import mysql.connector
import smtplib
import random
import string
import re  # For email regex validation
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import subprocess
from PIL import Image, ImageTk  # Importing PIL (Pillow)

# Connect to MySQL Database
def connect_db():
    return mysql.connector.connect(
        host="localhost",  # Your database host
        user="root",       # Your database user
        password="",  # Your database password
        database="music_player"  # Your database name
    )

# Function to generate a random code
def generate_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

# Function to send email
def send_email(to_email, code):
    from_email = "hastipipliya3245@gmail.com"  # Replace with your Gmail address
    app_password = "dsok bqoi mvpw pase"  # Replace with your generated app-specific password

    subject = "Password Reset Verification Code"
    body = f"Your verification code is: {code}"

    msg = MIMEMultipart()   
    msg['From'] = from_email
    msg['To'] = to_email  # Use the actual email from the user
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(from_email, app_password)
            text = msg.as_string()
            server.sendmail(from_email, to_email, text)
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")
        messagebox.showerror("Email Error", f"Failed to send email: {e}")

def is_valid_email(email):
    # Simple regex pattern for email validation
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def is_valid_password(password):
    # Password should have at least 6 characters
    if len(password) < 6:
        return False
    return True

# Function to handle the "Verify" button
def verify_email():
    username = entry_username.get()
    email = entry_email.get()

    # Validate fields
    if not username or not email:
        messagebox.showerror("Error", "Both fields are required!")
        return

    # Connect to DB and check if the user exists
    try:
        conn = connect_db()
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE username = %s AND email = %s"
        cursor.execute(query, (username, email))
        user = cursor.fetchone()
        if user:
            # User found, generate and send verification code
            verification_code = generate_code()
            send_email(email, verification_code)
            messagebox.showinfo("Success", f"Verification code sent to {email}.")
            entry_code.place(x=220, y=230)  # Show code input field
            entry_code.focus()
            # Store the code in a global variable for later verification
            global stored_code
            stored_code = verification_code
        else:
            messagebox.showerror("Error", "Username or email is incorrect!")
    except Exception as e:
        messagebox.showerror("Database Error", f"Failed to connect to database: {e}")
    finally:
        conn.close()

# Function to verify the code entered by the user
def verify_code():
    entered_code = entry_code.get()
    if entered_code == stored_code:
        messagebox.showinfo("Success", "Code verified. You can now reset your password.")
        show_reset_password_form()
    else:
        messagebox.showerror("Error", "Invalid code. Please try again.")

# Function to show reset password form
def show_reset_password_form():
    # Hide the verification form
    label_code.place_forget()
    entry_code.place_forget()
    verify_code_button.place_forget()

    # Show the reset password form
    label_reset_email.place(x=50, y=350)
    entry_reset_email.place(x=210, y=350)
    label_new_password.place(x=50, y=390)
    entry_new_password.place(x=210, y=390)
    label_confirm_password.place(x=50, y=430)
    entry_confirm_password.place(x=210, y=430)
    reset_password_button.place(x=150, y=480)
    toggle_password_icon.place(x=500, y=390)  # Show the toggle icon for New Password
    toggle_confirm_password_icon.place(x=500, y=430)  # Show the toggle icon for Confirm Password

# Function to handle reset password logic
def reset_password():
    reset_email = entry_reset_email.get()
    new_password = entry_new_password.get()
    confirm_password = entry_confirm_password.get()

    # Validate fields
    if not reset_email or not new_password or not confirm_password:
        messagebox.showerror("Error", "All fields are required!")
        return

    # Validate email format
    if not is_valid_email(reset_email):
        messagebox.showerror("Error", "Invalid email format!")
        return

    # Check if reset email matches the original email
    if reset_email != entry_email.get():
        messagebox.showerror("Error", "Email addresses do not match!")
        return

    # Validate password length (minimum 6 characters)
    if not is_valid_password(new_password):
        messagebox.showerror("Error", "Password must be at least 6 characters long.")
        return

    # Check if passwords match
    if new_password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    # Update password in database
    try:
        conn = connect_db()
        cursor = conn.cursor()
        update_query = "UPDATE users SET password = %s WHERE email = %s"
        cursor.execute(update_query, (new_password, reset_email))
        conn.commit()
        messagebox.showinfo("Success", "Password has been successfully reset.")
        subprocess.run(["python", "Register.py"])  # Redirect to Register.py (replace with the script you want)
        root.quit()  # Close the current Tkinter window
    except Exception as e:
        messagebox.showerror("Database Error", f"Failed to reset password: {e}")
    finally:
        conn.close()

# Function to toggle password visibility
def toggle_password_visibility(event):
    # Check if the password is currently hidden or shown
    if entry_new_password.cget('show') == '':
        entry_new_password.config(show='*')  # Show the password
        toggle_password_icon.config(image=eye_open)  # Change icon to eye open
    else:
        entry_new_password.config(show='')  # Hide the password
        toggle_password_icon.config(image=eye_closed)  # Change icon to eye closed

def toggle_confirm_password_visibility(event):
    # Check if the confirm password is currently hidden or shown
    if entry_confirm_password.cget('show') == '':
        entry_confirm_password.config(show='*')  # Show the confirm password
        toggle_confirm_password_icon.config(image=eye_open)  # Change icon to eye open
    else:
        entry_confirm_password.config(show='')  # Hide the confirm password
        toggle_confirm_password_icon.config(image=eye_closed)  # Change icon to eye closed

# Create the Tkinter window
root = tk.Tk()
root.title("Forgot Password")
root.geometry("400x400")

# Set background color and styling
root.configure(bg="#2E3B4E")  # Background color for the window
font = ("Arial", 14)
entry_font = ("Arial", 12)

# Load eye icons using Pillow (PIL)
eye_open_image = Image.open("eye_closed.jpg")  # Path to the "eye open" icon image
eye_closed_image = Image.open("eye_opened.jpg")  # Path to the "eye closed" icon image

# Resize the images to fit the button size
eye_open = ImageTk.PhotoImage(eye_open_image.resize((20, 20)))  # Resize to appropriate size
eye_closed = ImageTk.PhotoImage(eye_closed_image.resize((20, 20)))  # Resize to appropriate size

# Username and email input fields
label_username = tk.Label(root, text="Username:", font=("Arial", 12, "bold"), bg="#2E3B4E", fg="white")
label_username.place(x=50, y=50)
entry_username = tk.Entry(root, font=entry_font, width=25)
entry_username.place(x=150, y=50)

label_email = tk.Label(root, text="Email:", font=("Arial", 12, "bold"), bg="#2E3B4E", fg="white")
label_email.place(x=50, y=100)
entry_email = tk.Entry(root, font=entry_font, width=25)
entry_email.place(x=150, y=100)

# Buttons for verification
verify_button = tk.Button(root, text="Verify", font=font, command=verify_email, bg="#4CAF50", fg="black", width=15)
verify_button.place(x=150, y=140)

# Code input field (hidden initially)
label_code = tk.Label(root, text="Verification Code:", font=("Arial", 12, "bold"), bg="#2E3B4E", fg="white")
label_code.place(x=60, y=230)
entry_code = tk.Entry(root, font=entry_font, width=20)


# Button to verify the code
verify_code_button = tk.Button(root, text="Verify Code", font=font, command=verify_code, bg="#4CAF50", fg="black", width=15)
verify_code_button.place(x=150, y=280)

# Reset Password Fields (hidden initially)
label_reset_email = tk.Label(root, text="Email:", font=("Arial", 12, "bold"), bg="#2E3B4E", fg="white")
entry_reset_email = tk.Entry(root, font=entry_font, width=30)

label_new_password = tk.Label(root, text="New Password:", font=("Arial", 12, "bold"), bg="#2E3B4E", fg="white")
entry_new_password = tk.Entry(root, show="*", font=entry_font, width=30)

label_confirm_password = tk.Label(root, text="Confirm Password:", font=("Arial", 12, "bold"), bg="#2E3B4E", fg="white")
entry_confirm_password = tk.Entry(root, show="*", font=entry_font, width=30)

# Button to reset password
reset_password_button = tk.Button(root, text="Reset Password",font=font, command=reset_password, bg="#4CAF50", fg="black", width=15)

# Icon to toggle password visibility (shown without a button)
toggle_password_icon = tk.Label(root, image=eye_open)
toggle_password_icon.bind("<Button-1>", toggle_password_visibility)  # Toggle on click

toggle_confirm_password_icon = tk.Label(root, image=eye_open)
toggle_confirm_password_icon.bind("<Button-1>", toggle_confirm_password_visibility)  # Toggle on click

# Run the Tkinter event loop
root.mainloop()
