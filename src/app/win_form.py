import tkinter as tk
from tkinter import ttk, filedialog, messagebox

def open_win_form(parent: tk.Tk):
    win = tk.Toplevel(parent)
    win.title("Información")
    win.geometry("420x260")
    frm = ttk.Frame(win, padding=16)
    frm.pack(fill="both", expand=True)

    ttk.Label(frm, text="El desecho es reciclable, blaa bla bla..").grid(row=0, column=0, sticky="w")
