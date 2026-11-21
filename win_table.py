import tkinter as tk
import os
from registro import registrar_uso

def hablar(texto):
    os.system('say -r 155 "' + texto + '" &')

def open_win_table(root):
    win = tk.Toplevel(root)
    win.title("Mi Voz - Baño")
    win.geometry("1280x800")
    win.configure(bg="#F7F6F2")

    win.columnconfigure(0, weight=1)
    win.columnconfigure(1, weight=1)
    win.columnconfigure(2, weight=1)
    win.rowconfigure(1, weight=1)
    win.rowconfigure(2, weight=1)

    def decir_bano():
        registrar_uso("Baño", "Ir al baño")
        hablar("Necesito ir al baño")

    def decir_manos():
        registrar_uso("Baño", "Lavar manos")
        hablar("Quiero lavarme las manos")

    def decir_banarme():
        registrar_uso("Baño", "Bañarme")
        hablar("Quiero bañarme")

    def decir_papel():
        registrar_uso("Baño", "Necesito papel")
        hablar("Necesito papel o ayuda en el baño")

    def decir_dientes():
        registrar_uso("Baño", "Lavar dientes")
        hablar("Quiero cepillarme los dientes")

    def decir_ropa():
        registrar_uso("Baño", "Cambiar ropa")
        hablar("Necesito cambiarme de ropa")

    def regresar():
        hablar("Regresar")
        win.destroy()
        root.deiconify()

    win.protocol("WM_DELETE_WINDOW", regresar)

    titulo = tk.Label(win, text="BAÑO E HIGIENE • TOCA UNA OPCIÓN",
                      font=("Arial Rounded MT Bold", 24, "bold"),
                      bg="#ECEAE4", fg="#334E68", pady=15)
    titulo.grid(row=0, column=0, columnspan=3, sticky="ew", padx=30, pady=(20, 10))


    b1 = tk.Button(win, text="🚽\n\nIR AL BAÑO", font=("Arial Rounded MT Bold", 28, "bold"),
                   bg="#EDE9FE", fg="#5B21B6", highlightbackground="#8B5CF6", highlightthickness=4,
                   command=decir_bano)
    b1.grid(row=1, column=0, sticky="nsew", padx=(30, 12), pady=12)

    b2 = tk.Button(win, text="🧼\n\nLAVAR MANOS", font=("Arial Rounded MT Bold", 28, "bold"),
                   bg="#DBEAFE", fg="#1E40AF", highlightbackground="#3B82F6", highlightthickness=4,
                   command=decir_manos)
    b2.grid(row=1, column=1, sticky="nsew", padx=12, pady=12)

    b3 = tk.Button(win, text="🚿\n\nBAÑARME", font=("Arial Rounded MT Bold", 28, "bold"),
                   bg="#CCFBF1", fg="#115E59", highlightbackground="#14B8A6", highlightthickness=4,
                   command=decir_banarme)
    b3.grid(row=1, column=2, sticky="nsew", padx=(12, 30), pady=12)


    b4 = tk.Button(win, text="🧻\n\nNECESITO PAPEL", font=("Arial Rounded MT Bold", 28, "bold"),
                   bg="#FEF3C7", fg="#92400E", highlightbackground="#F59E0B", highlightthickness=4,
                   command=decir_papel)
    b4.grid(row=2, column=0, sticky="nsew", padx=(30, 12), pady=12)

    b5 = tk.Button(win, text="🪥\n\nLAVAR DIENTES", font=("Arial Rounded MT Bold", 28, "bold"),
                   bg="#D1FAE5", fg="#065F46", highlightbackground="#10B981", highlightthickness=4,
                   command=decir_dientes)
    b5.grid(row=2, column=1, sticky="nsew", padx=12, pady=12)

    b6 = tk.Button(win, text="👕\n\nCAMBIAR ROPA", font=("Arial Rounded MT Bold", 28, "bold"),
                   bg="#FCE7F3", fg="#9D174D", highlightbackground="#EC4899", highlightthickness=4,
                   command=decir_ropa)
    b6.grid(row=2, column=2, sticky="nsew", padx=(12, 30), pady=12)

    btn_regresar = tk.Button(win, text="⬅️  Regresar al menú", font=("Arial Rounded MT Bold", 20, "bold"),
                             bg="#E2E8F0", fg="#334155", height=2, command=regresar)
    btn_regresar.grid(row=3, column=0, columnspan=3, sticky="ew", padx=30, pady=(10, 24))