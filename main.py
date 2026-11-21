import tkinter as tk
import os
from win_home import open_win_home
from win_form import open_win_form
from win_list import open_win_list
from win_table import open_win_table
from win_canvas import open_win_canvas

def hablar(texto):
    os.system('say -r 155 "' + texto + '" &')

def main():
    root = tk.Tk()
    root.title("Mi Voz - Comunicador Visual")
    root.geometry("1280x800")
    root.configure(bg="#F7F6F2")

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)

    def ir_comida():
        hablar("Comida")
        root.withdraw()
        open_win_home(root)

    def ir_sociable():
        hablar("Saludar")
        root.withdraw()
        open_win_form(root)

    def ir_ayuda():
        hablar("Ayuda")
        root.withdraw()
        open_win_list(root)

    def ir_bano():
        hablar("Baño")
        root.withdraw()
        open_win_table(root)

    def ir_estadisticas():
        hablar("Estadísticas")
        root.withdraw()
        open_win_canvas(root)

    def salir():
        hablar("Salir")
        root.destroy()


    titulo = tk.Label(root, text="TOCA UN DIBUJO PARA HABLAR",
                      font=("Arial Rounded MT Bold", 26, "bold"),
                      bg="#ECEAE4", fg="#334E68", pady=15)
    titulo.grid(row=0, column=0, columnspan=2, sticky="ew", padx=30, pady=(20, 10))


    boton_comida = tk.Button(root, text="🍎\n\nCOMIDA",
                             font=("Arial Rounded MT Bold", 36, "bold"),
                             bg="#D1FAE5", fg="#065F46",
                             highlightbackground="#10B981", highlightthickness=5,
                             command=ir_comida)
    boton_comida.grid(row=1, column=0, sticky="nsew", padx=(30, 15), pady=15)

    boton_sociable = tk.Button(root, text="👋\n\nSALUDAR",
                               font=("Arial Rounded MT Bold", 36, "bold"),
                               bg="#DBEAFE", fg="#1E40AF",
                               highlightbackground="#3B82F6", highlightthickness=5,
                               command=ir_sociable)
    boton_sociable.grid(row=1, column=1, sticky="nsew", padx=(15, 30), pady=15)

    boton_ayuda = tk.Button(root, text="🆘\n\nAYUDA",
                            font=("Arial Rounded MT Bold", 36, "bold"),
                            bg="#FEF3C7", fg="#92400E",
                            highlightbackground="#F59E0B", highlightthickness=5,
                            command=ir_ayuda)
    boton_ayuda.grid(row=2, column=0, sticky="nsew", padx=(30, 15), pady=15)

    boton_bano = tk.Button(root, text="🚽\n\nBAÑO",
                           font=("Arial Rounded MT Bold", 36, "bold"),
                           bg="#EDE9FE", fg="#5B21B6",
                           highlightbackground="#8B5CF6", highlightthickness=5,
                           command=ir_bano)
    boton_bano.grid(row=2, column=1, sticky="nsew", padx=(15, 30), pady=15)


    boton_stats = tk.Button(root, text="📊 Estadísticas para Adultos",
                            font=("Arial Rounded MT Bold", 18, "bold"),
                            bg="#E2E8F0", fg="#334155", height=2,
                            command=ir_estadisticas)
    boton_stats.grid(row=3, column=0, sticky="ew", padx=(30, 15), pady=(10, 24))

    boton_salir = tk.Button(root, text="Cerrar programa",
                            font=("Arial Rounded MT Bold", 18, "bold"),
                            bg="#E2E8F0", fg="#334155", height=2,
                            command=salir)
    boton_salir.grid(row=3, column=1, sticky="ew", padx=(15, 30), pady=(10, 24))

    root.mainloop()

if __name__ == "__main__":
    main()