import tkinter as tk
from tkinter import scrolledtext

class CategoryGUI:
    def __init__(self, master, categories):
        self.master = master
        self.categories = categories

        self.create_widgets()

    def create_widgets(self):
        # Create a scrolled text widget
        self.scroll_text = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, width=40, height=10)
        self.scroll_text.pack(expand=True, fill='both')

        # Insert categories into the scrolled text widget
        for category in self.categories:
            self.scroll_text.insert(tk.END, category + '\n')

# Example categories list
categories = ["Category 1", "Category 2", "Category 3", "Category 4","Category 1", "Category 2", "Category 3", "Category 4","Category 1", "Category 2", "Category 3", "Category 4","Category 1", "Category 2", "Category 3", "Category 4","Category 1", "Category 2", "Category 3", "Category 4","Category 1", "Category 2", "Category 3", "Category 4","Category 1", "Category 2", "Category 3", "Category 4","Category 1", "Category 2", "Category 3", "Category 4","Category 1", "Category 2", "Category 3", "Category 4","Category 1", "Category 2", "Category 3", "Category 4","Category 1", "Category 2", "Category 3", "Category 4","Category 1", "Category 2", "Category 3", "Category 4","Category 1", "Category 2", "Category 3", "Category 4"]

# Create the Tkinter root window
root = tk.Tk()
root.title("Clickable Categories")

# Create an instance of CategoryGUI
app = CategoryGUI(root, categories)

# Start the Tkinter event loop
root.mainloop()
