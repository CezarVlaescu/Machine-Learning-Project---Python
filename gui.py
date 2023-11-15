from tkinter import Label, Button, Entry, messagebox
from availability_tracker import ProductAvailabilityTracker
from Styles.styles import Styles

class ProductAvailabilityTrakerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Media Galaxy Product Tracker")

        self.styles = Styles()
        master.configure(bg=self.styles.background_color)

        self.styles = Styles()
        master.configure(bg=self.styles.background_color)

        self.label_url = Label(master, text="Enter URL", bg=self.styles.background_color, font=self.styles.font)
        self.label_url.pack(pady=self.styles.label_padding)

        self.url_entry = Entry(master, font=self.styles.font)
        self.url_entry.pack(pady=self.styles.entry_padding)

        self.label_email = Label(master, text="Enter your email:", bg=self.styles.background_color,
                                 font=self.styles.font)
        self.label_email.pack(pady=self.styles.label_padding)

        self.email_entry = Entry(master, font=self.styles.font)
        self.email_entry.pack(pady=self.styles.entry_padding)

        self.track_button = Button(master, text="Track Availability", command=self.track_availability,
                                   font=self.styles.font)
        self.track_button.pack(pady=self.styles.button_padding)

    def track_availability(self):
        url = self.url_entry.get()
        email = self.email_entry.get()

        if not url or not email:
            messagebox.showerror("Error", "Please fill all the fields")
            return

        tracker = ProductAvailabilityTracker(url, email)
        tracker.check_availability()
