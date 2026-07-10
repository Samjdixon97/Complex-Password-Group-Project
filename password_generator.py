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
            break

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