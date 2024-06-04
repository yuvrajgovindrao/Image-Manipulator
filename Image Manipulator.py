import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def open_image():
    global img, img_tk
    filepath = filedialog.askopenfilename(
        initialdir="/",
        title="Select an image",
        filetypes=(("Image files", "*.jpg *.jpeg *.png *.gif"), ("all files", "*.*"))
    )
    if filepath:
        img = Image.open(filepath)
        update_preview()

def update_preview():
    global img_tk
    if img:
        img.thumbnail((400, 400))  # Resize for preview
        img_tk = ImageTk.PhotoImage(img)
        preview_label.configure(image=img_tk)

def compress_image():
    quality = ctk.CTkInputDialog(text="Enter quality (1-95):", title="Compress Image").get_input()
    if quality:
        try:
            quality = int(quality)
            if 1 <= quality <= 95:
                save_path = filedialog.asksaveasfilename(defaultextension=".jpg")
                if save_path:
                    img.save(save_path, quality=quality)
            else:
                messagebox.showerror("Error", "Invalid quality value. Please enter a number between 1 and 95.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a number.")

def change_resolution():
    new_width = ctk.CTkInputDialog(text="Enter new width:", title="Change Resolution").get_input()
    new_height = ctk.CTkInputDialog(text="Enter new height:", title="Change Resolution").get_input()
    if new_width and new_height:
        try:
            new_width, new_height = int(new_width), int(new_height)
            resized_img = img.resize((new_width, new_height))
            save_path = filedialog.asksaveasfilename(defaultextension=".jpg")
            if save_path:
                resized_img.save(save_path)
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter numbers for width and height.")

def change_format():
    new_format = ctk.CTkInputDialog(text="Enter new format (e.g., PNG, JPEG, GIF):", title="Change Format").get_input()
    if new_format:
        save_path = filedialog.asksaveasfilename(defaultextension="." + new_format.lower())
        if save_path:
            img.save(save_path)


# --- GUI ---
ctk.set_appearance_mode("dark")
window = ctk.CTk()
window.title("Image Manipulator")
window.geometry("520x520")

open_button = ctk.CTkButton(window, text="Open Image", command=open_image)
compress_button = ctk.CTkButton(window, text="Compress", command=compress_image)
resolution_button = ctk.CTkButton(window, text="Change Resolution", command=change_resolution)
format_button = ctk.CTkButton(window, text="Change Format", command=change_format)
preview_label = ctk.CTkLabel(window, text="") 

open_button.pack(pady=10, padx=20)
compress_button.pack(pady=5, padx=20)
resolution_button.pack(pady=5, padx=20)
format_button.pack(pady=5, padx=20)
preview_label.pack(pady=10, padx=20)

window.mainloop()
