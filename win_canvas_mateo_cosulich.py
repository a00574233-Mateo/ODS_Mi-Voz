import tkinter as tk
from tkinter import ttk, messagebox

import requests
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Version de Mateo Cosulich
# Ciudad: Guanajuato capital
# Datos: temperatura y humedad de los ultimos 2 dias

LATITUD = 21.02
LONGITUD = -101.26
DIAS_PASADOS = 2

COLOR_LINEA = "#6a1b9a"   # morado
COLOR_BARRAS = "#0288d1"  # azul
COLOR_PUNTOS = "#d81b60"  # rosa


def fetch_data():
    """
    Consulta la API de Open-Meteo y regresa tres listas:
    horas, temperaturas y humedad relativa.
    """
    try:
        url = (
            "https://api.open-meteo.com/v1/forecast"
            f"?latitude={LATITUD}&longitude={LONGITUD}"
            "&hourly=temperature_2m,relativehumidity_2m"
            f"&past_days={DIAS_PASADOS}&forecast_days=1"
            "&timezone=auto"
        )
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        data = response.json()

        horas = data["hourly"]["time"]
        temperaturas = data["hourly"]["temperature_2m"]
        humedad = data["hourly"]["relativehumidity_2m"]

        return horas, temperaturas, humedad
    except Exception as e:
        messagebox.showerror("Error", f"No se pudieron obtener los datos:\n{e}")
        return [], [], []


def etiquetas_eje_x(ax, horas):
    """Muestra una etiqueta cada 12 horas para que el eje X se lea mejor."""
    posiciones = list(range(0, len(horas), 12))
    textos = [horas[i][5:10] + " " + horas[i][11:16] for i in posiciones]
    ax.set_xticks(posiciones)
    ax.set_xticklabels(textos, rotation=30, fontsize=8)


def create_line_chart(horas, temps):
    """Grafica de linea: temperatura por hora."""
    fig = Figure(figsize=(8, 2.6), dpi=100)
    ax = fig.add_subplot(111)
    x = list(range(len(horas)))
    ax.plot(x, temps, color=COLOR_LINEA, linewidth=2, marker="s", markersize=3)
    ax.fill_between(x, temps, min(temps), color=COLOR_LINEA, alpha=0.15)
    ax.set_title("Temperatura en Guanajuato (linea)")
    ax.set_xlabel("Fecha y hora")
    ax.set_ylabel("°C")
    ax.grid(True, linestyle="--", alpha=0.5)
    etiquetas_eje_x(ax, horas)
    fig.tight_layout()
    return fig


def create_bar_chart(horas, humedad):
    """Grafica de barras: humedad relativa por hora."""
    fig = Figure(figsize=(8, 2.6), dpi=100)
    ax = fig.add_subplot(111)
    x = list(range(len(horas)))
    ax.bar(x, humedad, color=COLOR_BARRAS, alpha=0.8)
    ax.set_title("Humedad relativa en Guanajuato (barras)")
    ax.set_xlabel("Fecha y hora")
    ax.set_ylabel("%")
    ax.set_ylim(0, 100)
    ax.grid(True, axis="y", linestyle="--", alpha=0.5)
    etiquetas_eje_x(ax, horas)
    fig.tight_layout()
    return fig


def create_scatter_chart(temps, humedad):
    """Grafica de dispersion: relacion entre temperatura y humedad."""
    fig = Figure(figsize=(8, 2.6), dpi=100)
    ax = fig.add_subplot(111)
    ax.scatter(temps, humedad, color=COLOR_PUNTOS, alpha=0.7, edgecolors="black", linewidths=0.4)
    ax.set_title("Temperatura vs. humedad (dispersion)")
    ax.set_xlabel("Temperatura (°C)")
    ax.set_ylabel("Humedad (%)")
    ax.grid(True, linestyle="--", alpha=0.5)
    fig.tight_layout()
    return fig


def mostrar_graficas(frm, horas, temps, humedad):
    """Inserta las tres graficas en el frame de la ventana."""
    figuras = [
        create_line_chart(horas, temps),
        create_bar_chart(horas, humedad),
        create_scatter_chart(temps, humedad),
    ]
    for fig in figuras:
        canvas = FigureCanvasTkAgg(fig, master=frm)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=6, fill="x")


def open_win_canvas(parent: tk.Tk):
    """Crea la ventana secundaria con las graficas de la API."""
    win = tk.Toplevel(parent)
    win.title("Clima en Guanajuato - Open-Meteo")
    win.geometry("900x950")

    frm = ttk.Frame(win, padding=12)
    frm.pack(fill="both", expand=True)

    ttk.Label(
        frm,
        text="Temperatura y humedad de los ultimos 2 dias",
        font=("Segoe UI", 12, "bold"),
    ).pack(pady=(0, 6))

    # Frame donde van las graficas, para poder limpiarlas al recargar
    frm_graficas = ttk.Frame(frm)

    def cargar():
        # Borra las graficas anteriores para que no se repitan
        for widget in frm_graficas.winfo_children():
            widget.destroy()
        horas, temps, humedad = fetch_data()
        if horas and temps and humedad:
            mostrar_graficas(frm_graficas, horas, temps, humedad)

    ttk.Button(frm, text="Cargar y mostrar graficas", command=cargar).pack(pady=6)
    frm_graficas.pack(fill="both", expand=True)


# Para probar esta ventana sola (opcional)
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Prueba win_canvas")
    ttk.Button(root, text="Abrir ventana Canvas", command=lambda: open_win_canvas(root)).pack(pady=20)
    root.mainloop()
