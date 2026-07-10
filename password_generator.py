import random
import string
import tkinter as tk

# =====================================================================
# THIS CODE IS JUST TO PREVENT ERRORS IN THIS FILE ALONE 
# IGNORE
# |
# |
# V
# =====================================================================
class MockUI:
    def get(self): return "12"  # Simulates a default length of 12
    def delete(self, *args): pass
    def insert(self, *args): pass
    def config(self, *args): pass
    def clipboard_clear(self): pass
    def clipboard_append(self, text): pass
    def update(self): pass

# Empty layout placeholders to keep the code error-free
window = MockUI()
length_dropdown = MockUI()
password_display = MockUI()
copy_button = MockUI()
password_history = set()
ALL_CHARACTERS = string.ascii_letters + string.digits + string.punctuation
chosen_length = 12
password_list = []

# =====================================================================
# IGNORE CODE ABOVE
# =====================================================================


# Fill the length with completely random characters
remaining_length = chosen_length - 4
for _ in range(remaining_length):
    password_list.append(random.choice(ALL_CHARACTERS))

# Shuffle the list so the forced characters aren't always at the front
random.shuffle(password_list)

# Convert list back into a single string
final_password = "".join(password_list)

# Uniqueness Check: If it has never been generated before, keep it
if final_password not in password_history:
    password_history.add(final_password)

# Update the UI display box
password_display.delete(0, tk.END)
password_display.insert(0, final_password)

# Reset the copy button text back to normal
copy_button.config(text="Copy")

def copy_to_clipboard():
    """Copies the text inside the display box to the system clipboard."""
    password_text = password_display.get()
    if password_text:
        window.clipboard_clear()
        window.clipboard_append(password_text)
        window.update()  # Keeps the clipboard data alive after app closes
        copy_button.config(text="Copied! ✓")