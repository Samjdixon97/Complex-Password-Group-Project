# UI SETUP 

# Creating main window
window = tk.Tk()
window.title("Secure Password Generator")
window.geometry("400x250")
window.resizable(False, False)

# Dropdown Selection (Label + Dropdown menu from 8 to 36)
dropdown_label = tk.Label(window, text="Select Password Length:", font=("Arial", 10))
dropdown_label.pack(pady=(20, 2))

# Generate a list of strings from 8 to 36 for the dropdown options
length_options = [str(num) for num in range(8, 37)]
length_dropdown = ttk.Combobox(window, values=length_options, state="readonly", width=5)
length_dropdown.set("12")  # Default value
length_dropdown.pack(pady=5)

# Text Entry Box to display the output
password_display = tk.Entry(window, font=("Arial", 14), width=24, justify="center")
password_display.pack(pady=15)

# Action Buttons Container (Frame to hold buttons side by side)
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

generate_button = tk.Button(button_frame, text="Generate Password", command=generate_password, font=("Arial", 10), bg="#4CAF50", fg="white", padx=10, pady=5)
generate_button.pack(side=tk.LEFT, padx=10)

copy_button = tk.Button(button_frame, text="Copy", command=copy_to_clipboard, font=("Arial", 10), bg="#008CBA", fg="white", padx=15, pady=5)
copy_button.pack(side=tk.LEFT, padx=10)

# Start the application loop
window.mainloop()
