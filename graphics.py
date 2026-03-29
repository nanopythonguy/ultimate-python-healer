import windows
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Ultimate Python Healer v0.2")
root.geometry("520x700")

temp_button = ttk.Button(
    root, text="Clear Appdata`s Temp folder", command=windows.clear_tmp
)

sfc_button = ttk.Button(root, text="sfc /scannow", command=windows.sfc_scannow)

recycle_button = ttk.Button(
    root, text="Clear Recycle Bin", command=windows.clear_recyclebin
)

recycle_button.pack(pady=80, padx=50)
sfc_button.pack(pady=80, padx=70)
temp_button.pack(pady=80, padx=10)
root.mainloop()
