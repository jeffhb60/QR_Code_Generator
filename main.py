import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode
from PIL import Image, ImageTk


def generate_qr():
    data = entry.get()
    if not data.strip():
        messagebox.showerror("Error", "Input cannot be empty!")
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Resize the QR Code to 150x150
    img = img.resize((150, 150), Image.LANCZOS)
    qr_img = ImageTk.PhotoImage(img)

    # Display the QR Code
    qr_label.config(image=qr_img)
    qr_label.image = qr_img
    qr_label.pack(pady=10)

    # Enable and display the Save button
    save_button.config(state="normal")
    save_button.pack(pady=10)

    # Save QR Code functionality
    def save_qr():
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
        )
        if file_path:
            img.save(file_path)
            messagebox.showinfo("Saved", "QR Code saved successfully!")

    save_button.config(command=save_qr)


# Function to bind Enter key
def on_enter_key(event):
    generate_qr()


# GUI Setup
app = tk.Tk()
app.title("QR Code Generator")
app.geometry("400x400")

# Input Frame (Centered)
input_frame = tk.Frame(app)
input_frame.pack(pady=10)
tk.Label(input_frame, text="Enter Text or URL:", font=("Arial", 12)).pack()
entry = tk.Entry(input_frame, width=30, font=("Arial", 14))
entry.pack(pady=5)
entry.bind("<Return>", on_enter_key)  # Bind Enter key to the input field

# Generate Button (Centered)
generate_button = tk.Button(app, text="Generate QR Code", font=("Arial", 12), command=generate_qr)
generate_button.pack(pady=10)

# QR Code Display (Initially Hidden)
qr_label = tk.Label(app, bg="white")
qr_label.pack_forget()

# Save Button (Initially Hidden and Disabled)
save_button = tk.Button(app, text="Save Image", font=("Arial", 12), state="disabled")
save_button.pack_forget()

# Run the app
app.mainloop()
