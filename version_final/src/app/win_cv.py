import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path
from PIL import Image, ImageTk
import cv2
from src.core.cv_core import classify_image_file
import tempfile

DEFAULT_MODEL_PATH = str(Path(__file__).resolve().parents[2] / "models" / "trashorg_garbage10.joblib")


def open_win_cv(parent: tk.Tk):
    win = tk.Toplevel(parent)
    win.title("Clasificador (Cámara en vivo)")
    win.geometry("800x640")

    frm = ttk.Frame(win, padding=12)
    frm.pack(fill="both", expand=True)

    # ---- Cámara ----
    lbl_video = tk.Label(frm)
    lbl_video.pack(pady=10)

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        messagebox.showerror("Error", "No se pudo abrir la cámara.")
        return

    # ---- Actualizar imagen en tiempo real ----
    def mostrar_frame():
        ret, frame = cap.read()
        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame_rgb)
            imgtk = ImageTk.PhotoImage(image=img)
            lbl_video.imgtk = imgtk
            lbl_video.configure(image=imgtk)
        lbl_video.after(10, mostrar_frame)

    mostrar_frame()

    # ---- Resultado ----
    lbl_result = ttk.Label(frm, text="Resultado: ---", font=("Segoe UI", 12, "bold"))
    lbl_result.pack(pady=10)

    # ---- Capturar y clasificar ----
    def capturar_y_clasificar():
        ret, frame = cap.read()
        if not ret:
            messagebox.showerror("Error", "No se pudo capturar la imagen.")
            return

        temp_path = Path(tempfile.gettempdir()) / "captura_trashorg.jpg"
        cv2.imwrite(str(temp_path), frame)

        try:
            label, score, _ = classify_image_file(str(temp_path), DEFAULT_MODEL_PATH)
            prob = f"{score*100:.1f}%" if score else "N/A"
            lbl_result.config(text=f"Resultado: {label.upper()} ({prob})")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo clasificar la imagen:\n{e}")

    ttk.Button(frm, text="📸 Capturar y clasificar", command=capturar_y_clasificar).pack(pady=8)
    ttk.Button(frm, text="Cerrar", command=lambda: (cap.release(), win.destroy())).pack(pady=8)

    win.protocol("WM_DELETE_WINDOW", lambda: (cap.release(), win.destroy()))
