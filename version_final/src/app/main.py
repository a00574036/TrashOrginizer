import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import PhotoImage
from pathlib import Path
from src.app.win_cv import open_win_cv

def main():
    app = ttk.Window(
        title="TrashOrganizer - MVP",
        themename="solar",  # Puedes probar: darkly, morph, solar
        size=None,
        resizable=(True, True)
    )

    # Pantalla completa
    app.state('zoomed')

    frame = ttk.Frame(app, padding=40)
    frame.pack(fill="both", expand=True)

    # --- LOGO ---
    logo_path = Path(__file__).resolve().parents[2] / "data" / "logo.png"
    if logo_path.exists():
        img = PhotoImage(file=str(logo_path))
        lbl_logo = ttk.Label(frame, image=img)
        lbl_logo.image = img
        lbl_logo.pack(pady=(0, 10))
    else:
        ttk.Label(frame, text="TrashOrganizer", font=("Segoe UI", 24, "bold")).pack(pady=(0, 10))

    # --- Título ---
    ttk.Label(
        frame,
        text="Clasificador inteligente de residuos",
        font=("Segoe UI", 14, "bold")
    ).pack(pady=(0, 20))

    # --- Botones principales ---
    ttk.Button(
        frame,
        text="Abrir Clasificador (Cámara)",
        bootstyle=SUCCESS,
        command=lambda: open_win_cv(app)
    ).pack(pady=10, fill="x")

    ttk.Button(
        frame,
        text="Salir",
        bootstyle=DANGER,
        command=app.destroy
    ).pack(pady=10, fill="x")

    # --- Créditos o pie ---
    ttk.Label(
        frame,
        text="Proyecto TrashOrganizer © 2025",
        font=("Segoe UI", 9),
        foreground="#888"
    ).pack(side="bottom", pady=10)

    app.mainloop()


if __name__ == "__main__":
    main()


# python -m src.tools.train_from_dir
#python -m src.app.main