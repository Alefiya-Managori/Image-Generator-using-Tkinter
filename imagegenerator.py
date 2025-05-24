import requests
import io
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageEnhance
from ttkbootstrap import Style
from ttkbootstrap.widgets import Entry, Button, Label, Frame, Radiobutton, Checkbutton

# Initialize main window
root = tk.Tk()
root.title("Image Generator")
root.geometry("850x650")
root.resizable(False, False)

# Set initial theme
current_theme = "sandstone"
style = Style(theme=current_theme)

# Theme toggle function
def switch_theme():
    global current_theme
    current_theme = "darkly" if theme_var.get() == "Dark" else "sandstone"
    style.theme_use(current_theme)

# Apply night mode filter
def apply_night_filter(pil_image):
    if night_mode_var.get():
        enhancer = ImageEnhance.Brightness(pil_image.convert("RGB"))
        pil_image = enhancer.enhance(0.5)
    return pil_image

# Function to retrieve and display image
def display_image():
    category = category_entry.get()
    if not category:
        image_label.config(text="Please enter a category.", image="")
        return
    try:
        resolution = resolution_var.get()
        api_key = ""  # <--- Replace this with your Unsplash API key
        url = f"https://api.unsplash.com/photos/random?query={category}&orientation=landscape&client_id={api_key}"
        response = requests.get(url)

        if response.status_code != 200:
            image_label.config(text=f"API error: {response.status_code}", image="")
            return

        try:
            data = response.json()
        except Exception:
            image_label.config(text="Failed to parse JSON. Check API key or rate limit.", image="")
            return

        if "urls" not in data or resolution not in data["urls"]:
            image_label.config(text="No image found. Try another category.", image="")
            return

        img_url = data["urls"][resolution]
        img_data = requests.get(img_url).content
        pil_image = Image.open(io.BytesIO(img_data))
        pil_image = pil_image.resize((750, 450), Image.LANCZOS)
        pil_image = apply_night_filter(pil_image)

        photo = ImageTk.PhotoImage(pil_image)
        image_label.config(image=photo, text="")
        image_label.image = photo

    except Exception as e:
        image_label.config(text="Image could not be loaded.", image="")
        print(f"Error: {e}")

# GUI Layout
main_frame = Frame(root, padding=20)
main_frame.pack(fill="both", expand=True)

# Theme selector
theme_var = tk.StringVar(value="Light")
ttk.Label(main_frame, text="Choose Theme:", font=("Segoe UI", 10)).grid(row=0, column=0, sticky="w", padx=5)
Radiobutton(main_frame, text="Light", variable=theme_var, value="Light", command=switch_theme).grid(row=0, column=1, padx=5)
Radiobutton(main_frame, text="Dark", variable=theme_var, value="Dark", command=switch_theme).grid(row=0, column=2, padx=5)

# Search bar
ttk.Label(main_frame, text="Enter Category:", font=("Segoe UI", 10)).grid(row=1, column=0, pady=10, sticky="w", padx=5)
category_entry = Entry(main_frame, width=30)
category_entry.grid(row=1, column=1, columnspan=2, padx=5, sticky="ew")

# Resolution selector
ttk.Label(main_frame, text="Select Resolution:", font=("Segoe UI", 10)).grid(row=2, column=0, pady=10, sticky="w", padx=5)
resolution_var = tk.StringVar(value="regular")
resolution_dropdown = ttk.OptionMenu(main_frame, resolution_var, "regular", "small", "regular", "full", "raw")
resolution_dropdown.grid(row=2, column=1, columnspan=2, sticky="ew", padx=5)

# Night mode toggle
night_mode_var = tk.BooleanVar()
Checkbutton(main_frame, text="Night Mode Image Filter", variable=night_mode_var).grid(row=3, column=0, columnspan=2, pady=10, padx=5, sticky="w")

# Generate button
generate_button = Button(main_frame, text="Generate Image", bootstyle="primary", command=display_image)
generate_button.grid(row=3, column=2, padx=5, sticky="ew")

# Image display area
image_label = Label(main_frame, anchor="center", background="white", borderwidth=2, relief="solid", text="Your image will appear here.")
image_label.grid(row=4, column=0, columnspan=4, pady=20)

# Column layout
main_frame.columnconfigure(1, weight=1)
main_frame.columnconfigure(2, weight=1)

# Start app
root.mainloop()

