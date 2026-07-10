import tkinter as tk
from tkinter import ttk
import random
import string

# Global variables and data 

# Define character pools
LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
NUMBERS = string.digits
SYMBOLS = "!@#$%^&*()_+-=[]{}|;:,.<>?"
ALL_CHARACTERS = LOWERCASE + UPPERCASE + NUMBERS + SYMBOLS

# History set to track generated passwords and prevent repeats
password_history = set()

# Functions

def generate_password():
    """Generates a secure, unique password based on the hardcoded rules."""
    # To select the length of the password from the dropdown
    try:
        chosen_length = int(length_dropdown.get())
    except ValueError:
        chosen_length = 12  # Fallback safety default

    # Infinite loop that only breaks when a completely unique password is made
    while True:
        password_list = []

        # Guarantee at least 1 of each required type
        password_list.append(random.choice(LOWERCASE))
        password_list.append(random.choice(UPPERCASE))
        password_list.append(random.choice(NUMBERS))
        password_list.append(random.choice(SYMBOLS))