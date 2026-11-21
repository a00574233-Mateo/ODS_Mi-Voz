import tkinter as tk
from datetime import datetime
import time
import os
from registro import obtener_estadisticas, reiniciar_estadisticas

INICIO_SESION = time.time()

def hablar(texto):
    os.system('say -r 155 "' + texto + '" &')

def open_win_canvas(root):
    win = tk.Toplevel(root)
    win.title("Mi Voz - Estadísticas para Adultos")
    win.geometry("1280x800")
    win.configure(bg="#F7F6F2")

    win.columnconfigure(0, weight=1)
    win.columnconfigure(1, weight=1)
    win.rowconfigure(1, weight=1)

    def regresar():
        hablar("Regresar")
        win.destroy()
        root.deiconify()

    win.protocol("WM_DELETE_WINDOW", regresar)

    
    etiqueta_reloj = tk.Label(win, text="📊 PANEL DE ESTADÍSTICAS",
                              font=("Arial Rounded MT Bold", 19, "bold"),
                              bg="#ECEAE4", fg="#1E293B", pady=14)
    etiqueta_reloj.grid(row=0, column=0, columnspan=2, sticky="ew", padx=30, pady=(18, 10))

    def actualizar_reloj():
        if win.winfo_exists():
            ahora = datetime.now()
            hora_texto = ahora.strftime("%d/%m/%Y  •  %I:%M:%S %p")
            segundos_totales = int(time.time() - INICIO_SESION)
            minutos = segundos_totales // 60
            segundos = segundos_totales % 60
            
            texto = "📊 SEGUIMIENTO   |   🕒 " + hora_texto + "   |   ⏱️ Sesión: " + str(minutos) + "m " + str(segundos) + "s"
            etiqueta_reloj.config(text=texto)
            win.after(1000, actualizar_reloj)

    actualizar_reloj()


    (total, comida, sociable, ayuda, bano,
     mas_usada, alertas, franja,
     primera_h, ultima_h, texto_historial) = obtener_estadisticas()

    
    panel_izq = tk.Frame(win, bg="#FFFFFF", highlightbackground="#CBD5E1", highlightthickness=3)
    panel_izq.grid(row=1, column=0, sticky="nsew", padx=(30, 12), pady=8)

    lbl_grafica = tk.Label(panel_izq, text="Frecuencia por Categoría",
                           font=("Arial Rounded MT Bold", 21, "bold"),
                           bg="#FFFFFF", fg="#334E68")
    lbl_grafica.pack(pady=(15, 5))

    canvas = tk.Canvas(panel_izq, width=540, height=340, bg="#FFFFFF", highlightthickness=0)
    canvas.pack(pady=5, padx=20)

    def dibujar_barras(c_comida, c_sociable, c_ayuda, c_bano):
        canvas.delete("all")
        mayor = max(c_comida, c_sociable, c_ayuda, c_bano)
        if mayor == 0:
            mayor = 1

        y_piso = 285
        alto_maximo = 200
        canvas.create_line(40, y_piso, 510, y_piso, fill="#94A3B8", width=3)


        alto1 = (c_comida / mayor) * alto_maximo
        canvas.create_rectangle(65, y_piso - alto1, 145, y_piso, fill="#10B981", outline="")
        canvas.create_text(105, y_piso - alto1 - 16, text=str(c_comida), font=("Arial Rounded MT Bold", 19, "bold"), fill="#1E293B")
        canvas.create_text(105, y_piso + 22, text="Comida", font=("Arial Rounded MT Bold", 15, "bold"), fill="#475569")

    
        alto2 = (c_sociable / mayor) * alto_maximo
        canvas.create_rectangle(185, y_piso - alto2, 265, y_piso, fill="#3B82F6", outline="")
        canvas.create_text(225, y_piso - alto2 - 16, text=str(c_sociable), font=("Arial Rounded MT Bold", 19, "bold"), fill="#1E293B")
        canvas.create_text(225, y_piso + 22, text="Sociable", font=("Arial Rounded MT Bold", 15, "bold"), fill="#475569")

   
        alto3 = (c_ayuda / mayor) * alto_maximo
        canvas.create_rectangle(305, y_piso - alto3, 385, y_piso, fill="#F59E0B", outline="")
        canvas.create_text(345, y_piso - alto3 - 16, text=str(c_ayuda), font=("Arial Rounded MT Bold", 19, "bold"), fill="#1E293B")
        canvas.create_text(345, y_piso + 22, text="Ayuda", font=("Arial Rounded MT Bold", 15, "bold"), fill="#475569")

      
        alto4 = (c_bano / mayor) * alto_maximo
        canvas.create_rectangle(425, y_piso - alto4, 505, y_piso, fill="#8B5CF6", outline="")
        canvas.create_text(465, y_piso - alto4 - 16, text=str(c_bano), font=("Arial Rounded MT Bold", 19, "bold"), fill="#1E293B")
        canvas.create_text(465, y_piso + 22, text="Baño", font=("Arial Rounded MT Bold", 15, "bold"), fill="#475569")

    dibujar_barras(comida, sociable, ayuda, bano)

    lbl_horarios = tk.Label(panel_izq,
                            text="🌅 Primera vez hoy: " + primera_h + "    |    🌙 Última vez: " + ultima_h,
                            font=("Arial Rounded MT Bold", 15, "bold"),
                            bg="#F1F5F9", fg="#334155", pady=12)
    lbl_horarios.pack(fill="x", padx=25, pady=(10, 18))


    panel_der = tk.Frame(win, bg="#FFFFFF", highlightbackground="#CBD5E1", highlightthickness=3)
    panel_der.grid(row=1, column=1, sticky="nsew", padx=(12, 30), pady=8)

    lbl_total = tk.Label(panel_der, text="🗣️ Total de veces que se comunicó:  " + str(total),
                         font=("Arial Rounded MT Bold", 17, "bold"),
                         bg="#EFF6FF", fg="#1E40AF", pady=10, anchor="w", padx=15)
    lbl_total.pack(fill="x", padx=22, pady=(16, 6))

    lbl_top = tk.Label(panel_der, text="⭐ Necesidad más repetida:  " + mas_usada,
                       font=("Arial Rounded MT Bold", 17, "bold"),
                       bg="#FEF3C7", fg="#92400E", pady=10, anchor="w", padx=15)
    lbl_top.pack(fill="x", padx=22, pady=6)

    lbl_alertas = tk.Label(panel_der, text="🚨 Alertas (Ruido / Dolor / Urgencia):  " + str(alertas),
                           font=("Arial Rounded MT Bold", 17, "bold"),
                           bg="#FEE2E2", fg="#991B1B", pady=10, anchor="w", padx=15)
    lbl_alertas.pack(fill="x", padx=22, pady=6)

    lbl_franja = tk.Label(panel_der, text="⏰ Horario más activo:  " + franja,
                          font=("Arial Rounded MT Bold", 17, "bold"),
                          bg="#D1FAE5", fg="#065F46", pady=10, anchor="w", padx=15)
    lbl_franja.pack(fill="x", padx=22, pady=6)

    lbl_hist_titulo = tk.Label(panel_der, text="📋 Últimas solicitudes registradas:",
                               font=("Arial Rounded MT Bold", 16, "bold"),
                               bg="#FFFFFF", fg="#334E68")
    lbl_hist_titulo.pack(anchor="w", padx=24, pady=(10, 4))

    lbl_historial = tk.Label(panel_der, text=texto_historial,
                             font=("Arial Rounded MT Bold", 14),
                             bg="#F8FAFC", fg="#475569", justify="left", anchor="nw", padx=12, pady=10)
    lbl_historial.pack(fill="both", expand=True, padx=22, pady=(4, 16))


    def limpiar_datos():
        reiniciar_estadisticas()
        hablar("Estadísticas reiniciadas")
        lbl_total.config(text="🗣️ Total de veces que se comunicó:  0")
        lbl_top.config(text="⭐ Necesidad más repetida:  Ninguna aún")
        lbl_alertas.config(text="🚨 Alertas (Ruido / Dolor / Urgencia):  0")
        lbl_franja.config(text="⏰ Horario más activo:  Sin datos")
        lbl_horarios.config(text="🌅 Primera vez hoy: Sin registros    |    🌙 Última vez: Sin registros")
        lbl_historial.config(text="Aún no se ha tocado ningún botón hoy.")
        dibujar_barras(0, 0, 0, 0)

    btn_reiniciar = tk.Button(win, text="🗑️  Reiniciar estadísticas del día",
                              font=("Arial Rounded MT Bold", 18, "bold"),
                              bg="#FEE2E2", fg="#991B1B", height=2, command=limpiar_datos)
    btn_reiniciar.grid(row=2, column=0, sticky="ew", padx=(30, 12), pady=(8, 20))

    btn_regresar = tk.Button(win, text="⬅️  Regresar al menú",
                             font=("Arial Rounded MT Bold", 20, "bold"),
                             bg="#E2E8F0", fg="#334155", height=2, command=regresar)
    btn_regresar.grid(row=2, column=1, sticky="ew", padx=(12, 30), pady=(8, 20))