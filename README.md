# QR Code Generator

A simple Python application to generate and save QR codes using a graphical user interface (GUI). This project utilizes the `tkinter` library for the GUI and the `qrcode` library for QR code generation.

---

## Features

- **Input Text/URL**: Enter any text or URL to generate a QR code.
- **Generate QR Code**: A dynamically displayed QR code within the app.
- **Save QR Code**: Save the generated QR code as a PNG image file.
- **Keyboard Shortcut**: Press Enter to quickly generate a QR code.
- **Resizable QR Code**: The QR code is displayed with a resolution of 150x150.

---

## Requirements

### Python Libraries
- `tkinter`: Built-in library for creating GUI applications in Python.
- `qrcode`: For generating QR codes.
- `Pillow`: For handling and resizing images.

To install the required libraries, run:
  ```bash
  
  pip install qrcode[pil] pillow
  
  ```
## How to Use
1. Clone this repository or copy the code into a Python File
2. Run the Python Script: `main.py`
3. Enter the text or URL you want to convert to a QR code in the input field.
4. Click the **Generate QR Code** button or press **Enter** to generate the QR code.
5. Once the QR code is displayed, click the **Save Image** button to save it as a PNG file.

