import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Learning GUI")
app.geometry("800x400")
app.wm_attributes("-topmost", 1)  # Keep window on top
app.grid_columnconfigure(0, weight=1)

button = ctk.CTkButton(
    app, 
    text="Click Me!",
    fg_color="#FF5733",          # Button color (light/dark theme)
    hover_color="#CC4628",       # Color on hover
    text_color="#FFFFFF",         # Text color
    corner_radius=10,             # Rounded corners
    font=("Helvetica", 16),
    command=lambda: print("Button clicked!")
)
button.grid(row = 0, column = 0, padx = 100, pady = 100, sticky = "ew")

checkbox1 = ctk.CTkCheckBox(
    app,
    text="Checkbox 1",
    command=lambda: print("Checked!")
)
checkbox1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")

#checkbox_2 = ctk.CTkCheckBox(app, text="checkbox 2")


app.mainloop()