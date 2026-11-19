import tkinter as tk
from tkinter import ttk
from win_home import open_win_home
from win_form import open_win_form
from win_list import open_win_list
from win_table import open_win_table
from win_canvas import open_win_canvas

def main():
    root = tk.Tk()
    root.title("Cuatro Voces")

    frame = ttk.Frame(root, padding=20)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="Cuatro Voces - Toca un botón para hablar", font=("Segoe UI", 15, "bold"))\
        .grid(row=0, column=0, columnspan=2, pady=(0, 15))

    # Tamaño, letra y color definidos directamente en cada botón
    tk.Button(frame, text="🍽️\nComida", width=14, height=6, font=("Segoe UI", 20, "bold"),
              bg="#A8E6CF", command=lambda: open_win_home(root))\
        .grid(row=1, column=0, padx=10, pady=10)

    tk.Button(frame, text="🤝\nSociable", width=14, height=6, font=("Segoe UI", 20, "bold"),
              bg="#81D4FA", command=lambda: open_win_form(root))\
        .grid(row=1, column=1, padx=10, pady=10)

    tk.Button(frame, text="🆘\nAyuda", width=14, height=6, font=("Segoe UI", 20, "bold"),
              bg="#FFD54F", command=lambda: open_win_list(root))\
        .grid(row=2, column=0, padx=10, pady=10)

    tk.Button(frame, text="🚻\nBaño", width=14, height=6, font=("Segoe UI", 20, "bold"),
              bg="#FF8A80", command=lambda: open_win_table(root))\
        .grid(row=2, column=1, padx=10, pady=10)

    # Botones de abajo
    ttk.Button(frame, text="5) Premium", command=lambda: open_win_canvas(root))\
        .grid(row=3, column=0, sticky="ew", padx=10, pady=(15, 0))
    ttk.Button(frame, text="Salir", command=root.destroy)\
        .grid(row=3, column=1, sticky="ew", padx=10, pady=(15, 0))

    root.mainloop()

if __name__ == "__main__":
    main()