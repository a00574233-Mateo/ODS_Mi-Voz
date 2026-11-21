import tkinter as tk
import os
from registro import registrar_uso

def hablar(texto):
    os.system('say -r 155 "' + texto + '" &')

def open_win_home(root):
    win = tk.Toplevel(root)
    win.title("Mi Voz - Comida")
    win.geometry("1280x800")
    win.configure(bg="#F7F6F2")

    win.columnconfigure(0, weight=1)
    win.columnconfigure(1, weight=1)
    win.columnconfigure(2, weight=1)
    win.rowconfigure(1, weight=1)
    win.rowconfigure(2, weight=1)

    
    def decir_agua():
        registrar_uso("Comida", "Agua / Sed")
        hablar("Quiero agua, tengo sed")

    def decir_hambre():
        registrar_uso("Comida", "Tengo hambre")
        hablar("Tengo hambre, quiero comer")

    def decir_fruta():
        registrar_uso("Comida", "Fruta")
        hablar("Quiero fruta")

    def decir_leche():
        registrar_uso("Comida", "Leche / Jugo")
        hablar("Quiero leche o jugo")

    def decir_galleta():
        registrar_uso("Comida", "Galleta / Pan")
        hablar("Quiero una galleta o pan")

    def decir_lleno():
        registrar_uso("Comida", "Ya terminé")
        hablar("Ya terminé, estoy lleno")

    def regresar():
        hablar("Regresar")
        win.destroy()
        root.deiconify()

    win.protocol("WM_DELETE_WINDOW", regresar)

    titulo = tk.Label(win, text="COMIDA Y BEBIDA • TOCA UNA OPCIÓN",
                      font=("Arial Rounded MT Bold", 24, "bold"),
                      bg="#ECEAE4", fg="#334E68", pady=15)
    titulo.grid(row=0, column=0, columnspan=3, sticky="ew", padx=30, pady=(20, 10))

    
    b1 = tk.Button(win, text="💧\n\nAGUA / SED", font=("Arial Rounded MT Bold", 28, "bold"),
                   bg="#DBEAFE", fg="#1E40AF", highlightbackground="#3B82F6", highlightthickness=4,
                   command=decir_agua)
    b1.grid(row=1, column=0, sticky="nsew", padx=(30, 12), pady=12)

    b2 = tk.Button(win, text="🍽️\n\nTENGO HAMBRE", font=("Arial Rounded MT Bold", 28, "bold"),
                   bg="#FFEDD5", fg="#9A3412", highlightbackground="#F97316", highlightthickness=4,
                   command=decir_hambre)
    b2.grid(row=1, column=1, sticky="nsew", padx=12, pady=12)

    b3 = tk.Button(win, text="🍎\n\nFRUTA", font=("Arial Rounded MT Bold", 28, "bold"),
                   bg="#D1FAE5", fg="#065F46", highlightbackground="#10B981", highlightthickness=4,
                   command=decir_fruta)
    b3.grid(row=1, column=2, sticky="nsew", padx=(12, 30), pady=12)


    b4 = tk.Button(win, text="🥛\n\nLECHE / JUGO", font=("Arial Rounded MT Bold", 28, "bold"),
                   bg="#FEF3C7", fg="#92400E", highlightbackground="#F59E0B", highlightthickness=4,
                   command=decir_leche)
    b4.grid(row=2, column=0, sticky="nsew", padx=(30, 12), pady=12)

    b5 = tk.Button(win, text="🍪\n\nGALLETA / PAN", font=("Arial Rounded MT Bold", 28, "bold"),
                   bg="#FCE7F3", fg="#9D174D", highlightbackground="#EC4899", highlightthickness=4,
                   command=decir_galleta)
    b5.grid(row=2, column=1, sticky="nsew", padx=12, pady=12)

    b6 = tk.Button(win, text="✅\n\nYA TERMINÉ", font=("Arial Rounded MT Bold", 28, "bold"),
                   bg="#EDE9FE", fg="#5B21B6", highlightbackground="#8B5CF6", highlightthickness=4,
                   command=decir_lleno)
    b6.grid(row=2, column=2, sticky="nsew", padx=(12, 30), pady=12)


    btn_regresar = tk.Button(win, text="⬅️  Regresar al menú", font=("Arial Rounded MT Bold", 20, "bold"),
                             bg="#E2E8F0", fg="#334155", height=2, command=regresar)
    btn_regresar.grid(row=3, column=0, columnspan=3, sticky="ew", padx=30, pady=(10, 24))