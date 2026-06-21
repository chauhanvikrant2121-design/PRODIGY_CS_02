# PRODIGY_CS_02: Pixel Manipulation for Image Encryption

A simple and lightweight Python tool that utilizes pixel manipulation techniques to perform image encryption and decryption. Developed as part of the Cyber Security Internship at **Prodigy Infotech**.

---

## 🛠️ Features
- **Symmetric Encryption:** Uses a bitwise XOR mathematical operation on individual pixel RGB channels.
- **Reversible:** The same secret integer key (1–255) is used for both encryption and decryption.
- **Transparency Protection:** Automatically detects and leaves the Alpha channel (transparency) intact to keep PNG structures fully valid.

---

## 🚀 How It Works
The script loads the image array into memory via the **Pillow (PIL)** library. It sequentially loops through every single coordinate $(x, y)$, extracts its RGB color tuple, and applies the secret key transformation:

$$\text{New Color} = \text{Original Color} \oplus \text{Key}$$

Applying the operation a second time with the exact same key reverses the transformation completely.

---

## 💻 Prerequisites & Setup

1. **Install Dependencies:**
   Ensure you have the Python Image Library (Pillow) installed:
```bash
   pip install Pillow