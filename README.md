# 🖼️ Tkinter Image Generator using Unsplash API

This is a desktop application built with **Python**, **Tkinter**, and **ttkbootstrap** that fetches and displays random images based on user-defined categories from the **Unsplash API**.

---

## 🚀 Features

- 🌗 Light and Dark theme toggle
- 🗂️ Category-based image search
- 🖼️ Resolution selector (small, regular, full, raw)
- 🌃 Optional Night Mode image filter (reduces brightness)
- 📷 Displays image directly in the app

---

## 🧰 Technologies Used

- Python
- Tkinter
- ttkbootstrap (for modern UI)
- Unsplash API
- Pillow (PIL) for image processing
- Requests library for HTTP calls

---

## 🔑 Getting an Unsplash API Key

To use this app, you need an Unsplash API key. Follow these steps:

1. **Visit**: [https://unsplash.com/developers](https://unsplash.com/developers)
2. **Log in / Sign up** with your Unsplash account.
3. Go to your **[developer dashboard](https://unsplash.com/oauth/applications)**.
4. Click **"New Application"** and fill in:
   - **Name**: e.g., `Image Generator App`
   - **Description**: e.g., A desktop app to fetch category-based random images
   - **Platform**: `Other`
   - **Callback URL**: `http://localhost` (optional)
   - **Usage**: Describe your app honestly
5. Click **Create Application**
6. Copy your **Access Key**
7. In the code, paste it here:

   ```python
   api_key = "YOUR_ACCESS_KEY_HERE"
📦 Installation
Prerequisites:
Python 3.x

Install the required libraries:
pip install pillow requests ttkbootstrap


▶️ Running the App
Paste your Unsplash API key into the code (api_key = "...")

Run the script:
python your_script_name.py


📸 Screenshot
![image](https://github.com/user-attachments/assets/b8f110d4-7e18-4768-99e1-eb54e11c667d)

