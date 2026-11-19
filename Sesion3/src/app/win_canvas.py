import tkinter as tk
from tkinter import ttk, messagebox
import requests
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

FIG_SIZE = (6, 1.8)


def fetch_data():
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
        horas = [datetime.fromisoformat(t) for t in data["hourly"]["time"]]
        temperaturas = data["hourly"]["temperature_2m"]
        return horas, temperaturas
    except Exception as e:
        messagebox.showerror("Error", f"No se pudieron obtener los datos:\n{e}")
        return [], []


def formatear_eje(ax):
    ax.xaxis.set_major_locator(mdates.DayLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%m-%d"))
    ax.set_xlabel("Día")
    ax.set_ylabel("Temp. (°C)")
    ax.grid(True, linestyle="--", alpha=0.5)


def create_line_chart(horas, temps):
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    ax.plot(horas, temps, color="green", linestyle="-")
    ax.set_title("Temperatura en León (línea)")
    formatear_eje(ax)
    fig.tight_layout()
    return fig


def create_bar_chart(horas, temps):
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    ax.bar(horas, temps, width=1 / 24, color="orange")
    ax.set_title("Temperatura en León (barras)")
    formatear_eje(ax)
    fig.tight_layout()
    return fig


def create_scatter_chart(horas, temps):
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    ax.scatter(horas, temps, s=10, color="purple", alpha=0.7)
    ax.set_title("Temperatura en León (dispersión)")
    formatear_eje(ax)
    fig.tight_layout()
    return fig


def mostrar_graficas(frm, horas, temps):
    for crear in (create_line_chart, create_bar_chart, create_scatter_chart):
        fig = crear(horas, temps)
        canvas = FigureCanvasTkAgg(fig, master=frm)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=2, fill="x")
        plt.close(fig)


def open_win_canvas(parent: tk.Tk):
    win = tk.Toplevel(parent)
    win.title("Canvas con API (Open-Meteo) y gráficas")
    win.geometry("960x720")

    frm = ttk.Frame(win, padding=6)
    frm.pack(fill="both", expand=True)

    def cargar():
        horas, temps = fetch_data()
        if horas and temps:
            mostrar_graficas(frm, horas, temps)

    ttk.Button(frm, text="Cargar y mostrar gráficas", command=cargar).pack(pady=4)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Prueba win_canvas")
    ttk.Button(root, text="Abrir ventana Canvas", command=lambda: open_win_canvas(root)).pack(pady=20)
    root.mainloop()