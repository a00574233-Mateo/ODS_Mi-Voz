import tkinter as tk
from tkinter import ttk, messagebox
import requests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def fetch_data():
    """Obtiene temperaturas horarias de León, Gto (últimos 3 días) desde Open-Meteo."""
    try:
        url = (
            "https://api.open-meteo.com/v1/forecast"
            "?latitude=21.12&longitude=-101.68"
            "&hourly=temperature_2m&past_days=3&forecast_days=1"
            "&timezone=auto"
        )
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        data = response.json()
        return data["hourly"]["time"], data["hourly"]["temperature_2m"]
    except Exception as e:
        messagebox.showerror("Error", f"No se pudieron obtener los datos:\n{e}")
        return [], []


def formatear_eje_x(ax, horas):
    """Muestra una sola etiqueta por día en el eje X."""
    posiciones = list(range(0, len(horas), 24))
    etiquetas = [horas[i][:10] for i in posiciones]
    ax.set_xticks(posiciones)
    ax.set_xticklabels(etiquetas, rotation=45)
    ax.set_xlabel("Día")
    ax.set_ylabel("Temperatura (°C)")
    ax.grid(True, linestyle="--", alpha=0.5)


def create_line_chart(horas, temps):
    """Gráfica de línea verde."""
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot(range(len(temps)), temps, color="green", linewidth=1.5)
    ax.set_title("Temperatura en León (línea)")
    formatear_eje_x(ax, horas)
    fig.tight_layout()
    return fig


def create_bar_chart(horas, temps):
    """Gráfica de barras naranja."""
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.bar(range(len(temps)), temps, color="orange")
    ax.set_title("Temperatura en León (barras)")
    formatear_eje_x(ax, horas)
    fig.tight_layout()
    return fig


def create_scatter_chart(horas, temps):
    """Gráfica de dispersión morada."""
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.scatter(range(len(temps)), temps, color="purple", alpha=0.7, s=10)
    ax.set_title("Temperatura en León (dispersión)")
    formatear_eje_x(ax, horas)
    fig.tight_layout()
    return fig


def mostrar_graficas(frm, horas, temps):
    """Inserta las tres gráficas en el frame."""
    for crear in (create_line_chart, create_bar_chart, create_scatter_chart):
        fig = crear(horas, temps)
        canvas = FigureCanvasTkAgg(fig, master=frm)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=5, fill="x")


def open_win_canvas(parent: tk.Tk):
    """Crea la ventana secundaria con las gráficas de la API."""
    win = tk.Toplevel(parent)
    win.title("Canvas con API (Open-Meteo) y gráficas")
    win.geometry("960x1000")

    frm = ttk.Frame(win, padding=12)
    frm.pack(fill="both", expand=True)

    def cargar():
        horas, temps = fetch_data()
        if horas and temps:
            mostrar_graficas(frm, horas, temps)

    ttk.Button(frm, text="Cargar y mostrar gráficas", command=cargar).pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Prueba win_canvas")
    ttk.Button(root, text="Abrir ventana Canvas", command=lambda: open_win_canvas(root)).pack(pady=20)
    root.mainloop()