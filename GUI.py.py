import tkinter as tk
import smtplib

# Create main window
root = tk.Tk()
root.title("Email GUI")

# Create labels and entry widgets for email credentials
from_label = tk.Label(root, text="From:")
from_label.grid(row=0, column=0)
from_entry = tk.Entry(root)
from_entry.grid(row=0, column=1)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1)

to_label = tk.Label(root, text="To:")
to_label.grid(row=2, column=0)
to_entry = tk.Entry(root)
to_entry.grid(row=2, column=1)

subject_label = tk.Label(root, text="Subject:")
subject_label.grid(row=3, column=0)
subject_entry = tk.Entry(root)
subject_entry.grid(row=3, column=1)

body_label = tk.Label(root, text="Body:")
body_label.grid(row=4, column=0)
body_entry = tk.Text(root, height=10)
body_entry.grid(row=4, column=1)

    # Create button function to send email
def send_email():
    from_address = from_entry.get()
    password = password_entry.get()
    to_address = to_entry.get()
    subject = subject_entry.get()
    body = body_entry.get("1.0", tk.END)

    # Create SMTP session
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.starttls()
    smtp_server.login(from_address, password)
    # Create message
    message = f"Subject: {subject}\n\n{body}"

    # Send email
    smtp_server.sendmail(from_address, to_address, message)

    # Close SMTP session
    smtp_server.quit()

    # Clear fields
    from_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    to_entry.delete(0, tk.END)
    subject_entry.delete(0, tk.END)
    body_entry.delete("1.0", tk.END)

# Create button to send email
send_button = tk.Button(root, text="Send", command=send_email)
send_button.grid(row=5, column=1)

# Start GUI
root.mainloop()