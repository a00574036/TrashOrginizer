import tkinter as tk
from tkinter import ttk
from app.win_home import open_win_home
from app.win_form import open_win_form
from app.win_list import open_win_list
from app.win_table import open_win_table
from app.win_canvas import open_win_canvas

def main():
    root = tk.Tk()
    root.title("Trash Organizer")
    root.geometry("500x600")




    lblA=ttk.Label(root, text="Escanea tu basura", font=("Segoe UI", 12, "bold")).pack(pady=(0, 12))
    lblFoto=tk.Label(root, text="FOTO",bg="light blue",width=60,height=30).place(x=40,y=40)
    btnA=ttk.Button(root, text="Analizar", command=lambda: open_win_home(root))
    btnA.place(x=225,y=500)


    root.mainloop()

if __name__ == "__main__":
    main()
