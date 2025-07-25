# 📲 WhatsApp GUI Message Scheduler

This is a simple desktop application built with **Python and Tkinter** that allows you to schedule and send WhatsApp messages using **pywhatkit**. The user-friendly interface makes it easy to input the phone number, message content, and desired date/time for sending the message.

## 🖥️ Features

- GUI built with Tkinter (no need to use the terminal)
- Schedule a WhatsApp message to be sent at a future date and time
- Input validation for proper time scheduling
- Simple and intuitive user interface

## 🛠️ Technologies Used

- Python 3.x
- [Tkinter](https://docs.python.org/3/library/tkinter.html) – for the GUI
- [pywhatkit](https://pypi.org/project/pywhatkit/) – for sending WhatsApp messages
- `datetime` – to check if the scheduled time is valid

## 📦 Installation

1. **Clone the repository** or download the script.
2. **Install the required package** via pip:
   ```bash
   pip install pywhatkit
   ```

> Tkinter comes pre-installed with most Python distributions. If not, install it manually based on your OS.

## 🧠 How to Use

1. Run the Python script:
   ```bash
   python whatsapp_gui_sender.py
   ```

2. Fill in the following fields in the app:
   * **Phone Number** (with country code, e.g., +90xxxxxxxxxx)
   * **Message** you want to send
   * **Date** in `YYYY-MM-DD` format
   * **Time** in `HH:MM` (24-hour format)

3. Click **"Send Message"**

4. WhatsApp Web will open in your browser and the message will be sent automatically at the scheduled time.

## ⚠️ Notes

* You **must be logged into WhatsApp Web** in your default browser.
* Make sure the system time is accurate and you have a stable internet connection.
* The message must be scheduled at least **1 minute ahead** of the current time.

## 💬 Example Use Case

Let’s say you want to send a reminder to a friend:

* Phone: `+905xxxxxxxxx`
* Message: `"Don't forget the meeting!"`
* Date: `2023-07-26`
* Time: `14:30`

The app will launch WhatsApp Web and send the message automatically at 14:30 on July 26, 2023.

## 🧑‍💻 Author

Developed with ❤️ by Işıl Ceren Satıcı 
Feel free to fork, modify, or contribute!
