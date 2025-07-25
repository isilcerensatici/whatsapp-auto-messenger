import tkinter as tk
from tkinter import messagebox
import pywhatkit as kit
from datetime import datetime

def send_message():
    # Get user inputs
    phone_number = entry_phone.get()  # Retrieve phone number from input
    message = entry_message.get()      # Retrieve message from input
    date_input = entry_date.get()      # Retrieve date from input
    time_input = entry_time.get()      # Retrieve time from input

    # Split date and time inputs
    try:
        year, month, day = map(int, date_input.split('-'))  # Split date into year, month, day
        hour, minute = map(int, time_input.split(':'))      # Split time into hour and minute

        now = datetime.now()  # Get the current date and time
        # Check if the specified time is in the future
        if (year < now.year or (year == now.year and month < now.month) or 
            (year == now.year and month == now.month and day < now.day) or
            (year == now.year and month == now.month and day == now.day and hour < now.hour) or
            (year == now.year and month == now.month and day == now.day and hour == now.hour and minute <= now.minute)):
            messagebox.showerror("Error", "Please enter a future date and time.")  # Display error
        else:
            # Send the WhatsApp message
            kit.sendwhatmsg(phone_number, message, hour, minute)
            messagebox.showinfo("Success", "Message sent successfully!")  # Display success message
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")  # Display error if any

# Create the Tkinter window
root = tk.Tk()
root.title("WhatsApp Message Sender")  # Set the window title

# Phone number input
tk.Label(root, text="Phone Number (+CountryCodexxxxxxxxxx):").pack()  # Label for phone number
entry_phone = tk.Entry(root)  # Input field for phone number
entry_phone.pack()

# Message input
tk.Label(root, text="Message:").pack()  # Label for message
entry_message = tk.Entry(root)  # Input field for message
entry_message.pack()

# Date input
tk.Label(root, text="Date (YYYY-MM-DD):").pack()  # Label for date
entry_date = tk.Entry(root)  # Input field for date
entry_date.pack()

# Time input
tk.Label(root, text="Time (HH:MM):").pack()  # Label for time
entry_time = tk.Entry(root)  # Input field for time
entry_time.pack()

# Send button
send_button = tk.Button(root, text="Send Message", command=send_message)  # Button to send message
send_button.pack()

# Run the application
root.mainloop()  # Start the Tkinter event loop