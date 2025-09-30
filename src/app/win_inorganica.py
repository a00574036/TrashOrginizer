import tkinter as tk
from tkinter import ttk

def open_win_inorganica(parent: tk.Tk):
    win = tk.Toplevel(parent)
    win.title("Inorgánica")
    win.geometry("420x260")

    frm = ttk.Frame(win, padding=16)
    frm.pack(fill="both", expand=True)


    ttk.Label(
        frm,
        text="El desecho es inorgánico",
        font=("Segoe UI", 12, "bold"),
        foreground="red"
    ).pack(pady=(0, 12))


    texto = (
        "La basura inorgánica está compuesta por materiales que\n"
        "no son biodegradables, como plásticos, vidrios, metales\n"
        "y telas. Debe separarse de la orgánica para facilitar\n"
        "su reciclaje y disposición adecuada."
    )
    ttk.Label(frm, text=texto, justify="left").pack(pady=(0, 12))

   
    ttk.Button(frm, text="Más información",
               command=lambda: open_info_inorganica(win)).pack(pady=6, anchor="w")
    ttk.Button(frm, text="Cerrar", command=win.destroy).pack(pady=6, anchor="e")


def open_info_inorganica(parent: tk.Toplevel):
    win = tk.Toplevel(parent)
    w
