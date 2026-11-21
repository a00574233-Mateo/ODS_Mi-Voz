import tkinter as tk
import os
from registro import registrar_uso

def hablar(texto):
    os.system('say -r 155 "' + texto + '" &')

def open_win_form(root):
    win = tk.Toplevel(root)
    win.title("Mi Voz - Sociable")
    win.geometry("1280x800")
    win.configure(bg="#F7F6F2")

    win.columnconfigure(0, weight=1)
    win.columnconfigure(1, weight=1)
    win.columnconfigure(2, weight=1)
    win.rowconfigure(1, weight=1)
    win.rowconfigure(2, weight=1)

    def decir_hola():
        registrar_uso("Sociable", "Hola")
        hablar("Hola, cómo estás")

    def decir_gracias():
        registrar_uso("Sociable", "Gracias")
        hablar("Muchas gracias")

    def decir_si():
        registrar_uso("Sociable", "Sí")
        hablar("Sí, quiero")

    def decir_no():
        registrar_uso("Sociable", "No")
        hablar("No, gracias")

    def decir_jugar():
        registrar_uso("Sociable", "Jugar")
        hablar("Quiero jugar")

    def decir_adios():
        registrar_uso("Sociable", "Adiós")
        hablar("Adiós, hasta luego")

    def regresar():
        hablar("Regresar")
        win.destroy()
        root.deiconify()

    win.protocol("WM_DELETE_WINDOW", regresar)

    titulo = tk.Label(win, text="SOCIABLE • TOCA UNA OPCIÓN",
                      font=("Arial Rounded MT Bold", 24, "bold"),
                      bg="#ECEAE4", fg="#334E68", pady=15)
    titulo.grid(row=0, column=0, columnspan=3, sticky="ew", padx=30, pady=(20, 10))


    b1 = tk.Button(win, text="👋\n\nHOLA", font=("Arial Rounded MT Bold", 30, "bold"),
                   bg="#DBEAFE", fg="#1E40AF", highlightbackground="#3B82F6", highlightthickness=4,
                   command=decir_hola)
    b1.grid(row=1, column=0, sticky="nsew", padx=(30, 12), pady=12)

    b2 = tk.Button(win, text="🙏\n\nGRACIAS", font=("Arial Rounded MT Bold", 30, "bold"),
                   bg="#D1FAE5", fg="#065F46", highlightbackground="#10B981", highlightthickness=4,
                   command=decir_gracias)
    b2.grid(row=1, column=1, sticky="nsew", padx=12, pady=12)

    b3 = tk.Button(win, text="👍\n\nSÍ", font=("Arial Rounded MT Bold", 30, "bold"),
                   bg="#DCFCE7", fg="#166534", highlightbackground="#22C55E", highlightthickness=4,
                   command=decir_si)
    b3.grid(row=1, column=2, sticky="nsew", padx=(12, 30), pady=12)


    b4 = tk.Button(win, text="👎\n\nNO", font=("Arial Rounded MT Bold", 30, "bold"),
                   bg="#FEE2E2", fg="#991B1B", highlightbackground="#EF4444", highlightthickness=4,
                   command=decir_no)
    b4.grid(row=2, column=0, sticky="nsew", padx=(30, 12), pady=12)

    b5 = tk.Button(win, text="🧸\n\nJUGAR", font=("Arial Rounded MT Bold", 30, "bold"),
                   bg="#FEF3C7", fg="#92400E", highlightbackground="#F59E0B", highlightthickness=4,
                   command=decir_jugar)
    b5.grid(row=2, column=1, sticky="nsew", padx=12, pady=12)

    b6 = tk.Button(win, text="🙋‍♂️\n\nADIÓS", font=("Arial Rounded MT Bold", 30, "bold"),
                   bg="#EDE9FE", fg="#5B21B6", highlightbackground="#8B5CF6", highlightthickness=4,
                   command=decir_adios)
    b6.grid(row=2, column=2, sticky="nsew", padx=(12, 30), pady=12)

    btn_regresar = tk.Button(win, text="⬅️  Regresar al menú", font=("Arial Rounded MT Bold", 20, "bold"),
                             bg="#E2E8F0", fg="#334155", height=2, command=regresar)
    btn_regresar.grid(row=3, column=0, columnspan=3, sticky="ew", padx=30, pady=(10, 24))