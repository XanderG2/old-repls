import tkinter as tk
from tkinter import ttk

root = tk.Tk()
photoimages = tk.PhotoImage("Capture2.PNG")
label = ttk.Label(root, image=photoimages).pack()