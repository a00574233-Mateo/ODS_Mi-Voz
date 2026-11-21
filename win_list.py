import tkinter as tk
import os
from registro import registrar_uso

def hablar(texto):
    os.system('say -r 155 "' + texto + '" &')

def open_win_list(root):
    win = tk.Toplevel(root)
    win.title("Mi Voz - Ayuda")
    win.geometry("1280x800")
    win.configure(bg="#F7F6F2")

    win.columnconfigure(0, weight=1)
    win.columnconfigure(1, weight=1)
    win.columnconfigure(2, weight=1)
    win.rowconfigure(1, weight=1)
    win.rowconfigure(2, weight=1)

    def decir_urgente():
        registrar_uso("Ayuda", "Ayuda urgente")
        hablar("Por favor, necesito ayuda urgente")

    def decir_dolor():
        registrar_uso("Ayuda", "Tengo dolor")
        hablar("Me siento mal, tengo dolor")

    def decir_medicina():
        registrar_uso("Ayuda", "Medicina")
        hablar("Necesito mi medicina")

    def decir_familiar():
        registrar_uso("Ayuda", "Llamar a casa")
        hablar("Por favor, llama a mamá o papá")

    def decir_ruido():
        registrar_uso("Ayuda", "Mucho ruido")
        hablar("Hay mucho ruido, necesito calma")

    def decir_descansar():
        registrar_uso("Ayuda", "Descansar")
        hablar("Estoy cansado, quiero descansar")

    def regresar():
        hablar("Regresar")
        win.destroy()
        root.deiconify()

    win.protocol("WM_DELETE_WINDOW", regresar)

    titulo = tk.Label(win, text="AYUDA • TOCA UNA OPCIÓN",
                      font=("Arial Rounded MT Bold", 24, "bold"),
                      bg="#ECEAE4", fg="#334E68", pady=15)
    titulo.grid(row=0, column=0, columnspan=3, sticky="ew", padx=30, pady=(20, 10))

 
    b1 = tk.Button(win, text="🚨\n\nAYUDA URGENTE", font=("Arial Rounded MT Bold", 28, "bold"),
                   bg="#FEE2E2", fg="#991B1B", highlightbackground="#EF4444", highlightthickness=4,
                   command=decir_urgente)
    b1.grid(row=1, column=0, sticky="nsew", padx=(30, 12), pady=12)

    b2 = tk.Button(win, text="🤕\n\nTENGO DOLOR", font=("Arial Rounded MT Bold", 28, "bold"),
                   bg="#FEF3C7", fg="#92400E", highlightbackground="#F59E0B", highlightthickness=4,
                   command=decir_dolor)
    b2.grid(row=1, column=1, sticky="nsew", padx=12, pady=12)

    b3 = tk.Button(win, text="💊\n\nMEDICINA", font=("Arial Rounded MT Bold", 28, "bold"),
                   bg="#DBEAFE", fg="#1E40AF", highlightbackground="#3B82F6", highlightthickness=4,
                   command=decir_medicina)
    b3.grid(row=1, column=2, sticky="nsew", padx=(12, 30), pady=12)

    
    b4 = tk.Button(win, text="📞\n\nLLAMAR A CASA", font=("Arial Rounded MT Bold", 28, "bold"),
                   bg="#EDE9FE", fg="#5B21B6", highlightbackground="#8B5CF6", highlightthickness=4,
                   command=decir_familiar)
    b4.grid(row=2, column=0, sticky="nsew", padx=(30, 12), pady=12)

    b5 = tk.Button(win, text="🙉\n\nMUCHO RUIDO", font=("Arial Rounded MT Bold", 28, "bold"),
                   bg="#FFEDD5", fg="#9A3412", highlightbackground="#F97316", highlightthickness=4,
                   command=decir_ruido)
    b5.grid(row=2, column=1, sticky="nsew", padx=12, pady=12)

    b6 = tk.Button(win, text="😴\n\nDESCANSAR", font=("Arial Rounded MT Bold", 28, "bold"),
                   bg="#D1FAE5", fg="#065F46", highlightbackground="#10B981", highlightthickness=4,
                   command=decir_descansar)
    b6.grid(row=2, column=2, sticky="nsew", padx=(12, 30), pady=12)

    btn_regresar = tk.Button(win, text="⬅️  Regresar al menú", font=("Arial Rounded MT Bold", 20, "bold"),
                             bg="#E2E8F0", fg="#334155", height=2, command=regresar)
    btn_regresar.grid(row=3, column=0, columnspan=3, sticky="ew", padx=30, pady=(10, 24))