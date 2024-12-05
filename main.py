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

    # Display QR code in the GUI
    img.thumbnail((200, 200))
    qr_img = ImageTk.PhotoImage(img)
    qr_label.config(image=qr_img)
    qr_label.image = qr_img

    # Enable the Save button
    def save_qr():
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
        )
        if file_path:
            img.save(file_path)
            messagebox.showinfo("Saved", "QR Code saved successfully!")

    save_button.config(command=save_qr, state="normal")


# GUI Setup
app = tk.Tk()
app.title("QR Code Generator")
app.geometry("400x400")

# Input Frame
input_frame = tk.Frame(app)
input_frame.grid(row=0, column=0, pady=10, padx=10, columnspan=2)

tk.Label(input_frame, text="Enter Text or URL:", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
entry = tk.Entry(input_frame, width=30, font=("Arial", 14))
entry.pack(side=tk.LEFT, padx=5)

# Generate Button
generate_button = tk.Button(app, text="Generate QR Code", font=("Arial", 12), command=generate_qr)
generate_button.grid(row=1, column=0, pady=10, padx=10, columnspan=2)

# QR Code Display
qr_label = tk.Label(app, bg="white", width=25, height=12, relief="solid")
qr_label.grid(row=2, column=0, pady=10, padx=10, columnspan=2)

# Save Button
save_button = tk.Button(app, text="Save Image", font=("Arial", 12), state="disabled")
save_button.grid(row=3, column=0, pady=10, padx=10, columnspan=2)

# Run the app
app.mainloop()
