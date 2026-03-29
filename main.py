import windows
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Ultimate Python Healer v0.1")
root.geometry("320x500")

temp_button = ttk.Button(
    root, text="Clear Appdata`s Temp folder", command=windows.clear_tmp
)
temp_button.pack(pady=90)
root.mainloop()
