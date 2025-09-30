import tkinter as tk
from tkinter import ttk
from app.win_form import open_win_form
from pathlib import Path
from PIL import Image, ImageTk

def open_win_canvas(parent: tk.Tk):
    win = tk.Toplevel(parent)
    win.title("Reciclable")
    win.geometry("480x340")

    frm = ttk.Frame(win, padding=12)
    frm.pack(fill="both", expand=True)

    canvas = tk.Canvas(frm, width=440, height=240, bg="green")
    canvas.pack()

    ruta = Path(__file__).resolve().parents[1] / "data" / "caja.jpg"
    print("Ruta de imagen:", ruta)  # Debug
    imagen = Image.open(ruta)  
    imagen = imagen.resize((200, 150))
    img_tk = ImageTk.PhotoImage(imagen)

    canvas.create_image(220, 120, image=img_tk, anchor="center")

# Guardar referencia
    canvas.img_ref = img_tk

    # Texto arriba
    canvas.create_text(220, 20, text="El desecho es reciclable",font=("Segoe UI", 12, "bold"), fill="white")

    ttk.Button(frm, text="Información",command=lambda: open_win_form(win)).pack(pady=8, anchor="w")
    ttk.Button(frm, text="Cerrar", command=win.destroy).pack(pady=6, anchor="e")
