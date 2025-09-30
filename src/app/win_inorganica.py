import tkinter as tk
from tkinter import ttk
from pathlib import Path
from PIL import Image, ImageTk

def open_win_inorganica(parent: tk.Tk):
    win = tk.Toplevel(parent)
    win.title("Inorgánica")
    win.geometry("480x340")

    frm = ttk.Frame(win, padding=12)
    frm.pack(fill="both", expand=True)

    canvas = tk.Canvas(frm, width=440, height=240, bg="gray")
    canvas.pack()

    # Cargar imagen (puedes poner otra en tu carpeta /data)
    ruta = Path(__file__).resolve().parents[1] / "data" / "botella.jpg"
    print("Ruta de imagen inorgánica:", ruta)  # Debug
    imagen = Image.open(ruta)
    imagen = imagen.resize((200, 150))
    img_tk = ImageTk.PhotoImage(imagen)

    canvas.create_image(220, 120, image=img_tk, anchor="center")
    canvas.img_ref = img_tk  # evitar garbage collector

    # Texto arriba
    canvas.create_text(220, 20, text="El desecho es inorgánico",
                       font=("Segoe UI", 12, "bold"), fill="white")

    ttk.Button(frm, text="Más información",
               command=lambda: open_info_inorganica(win)).pack(pady=8, anchor="w")
    ttk.Button(frm, text="Cerrar", command=win.destroy).pack(pady=6, anchor="e")


def open_info_inorganica(parent: tk.Toplevel):
    win = tk.Toplevel(parent)
    win.title("Información Inorgánica")
    win.geometry("420x200")

    frm = ttk.Frame(win, padding=16)
    frm.pack(fill="both", expand=True)

    info = (
        "La basura inorgánica incluye materiales no biodegradables,\n"
        "como plásticos, vidrios, metales y telas.\n\n"
        "Debe separarse adecuadamente para facilitar el reciclaje."
    )

    ttk.Label(frm, text=info, justify="left").pack()
    ttk.Button(frm, text="Cerrar", command=win.destroy).pack(pady=8)
