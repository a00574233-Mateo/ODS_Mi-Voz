import tkinter as tk
from tkinter import ttk, messagebox
import requests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def fetch_data():
    """
    Modificación 1 (API y Rango):
    Consulta la humedad relativa horaria de Ciudad de México (últimos 2 días)
    en lugar de temperatura en León.
    """
    try:
        url = (
            "https://api.open-meteo.com/v1/forecast"
            "?latitude=19.43&longitude=-99.13"
            "&hourly=relativehumidity_2m&past_days=2"
            "&timezone=auto"
        )
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        data = response.json()

        # Filtramos las últimas 24 horas y dejamos solo la hora (HH:MM) para legibilidad
        horas = [h.split("T")[1] for h in data["hourly"]["time"][-24:]]
        humedad = data["hourly"]["relativehumidity_2m"][-24:]

        return horas, humedad
    except Exception as e:
        messagebox.showerror("Error de conexión", f"No se pudieron obtener los datos:\n{e}")
        return [], []


def create_line_chart(horas, humedad):
    """Gráfica 1: Línea con marcadores cuadrados, grosor personalizado y rejilla."""
    fig, ax = plt.subplots(figsize=(7.5, 3))
    ax.plot(horas, humedad, color="#1f77b4", linestyle="-", marker="s", markersize=4, linewidth=2)
    ax.set_title("Humedad Relativa en CDMX - Tendencia (Línea)", fontsize=11, fontweight="bold")
    ax.set_xlabel("Hora del día")
    ax.set_ylabel("Humedad (%)")
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.tick_params(axis="x", rotation=45)
    fig.tight_layout()
    return fig


def create_bar_chart(horas, humedad):
    """Gráfica 2: Barras con transparencia y borde definido."""
    fig, ax = plt.subplots(figsize=(7.5, 3))
    ax.bar(horas, humedad, color="#2ca02c", alpha=0.8, edgecolor="black")
    ax.set_title("Humedad Relativa en CDMX - Comparativa (Barras)", fontsize=11, fontweight="bold")
    ax.set_xlabel("Hora del día")
    ax.set_ylabel("Humedad (%)")
    ax.grid(axis="y", linestyle=":", alpha=0.6)
    ax.tick_params(axis="x", rotation=45)
    fig.tight_layout()
    return fig


def create_scatter_chart(horas, humedad):
    """Gráfica 3 (La que faltaba en el ejemplo): Dispersión (Scatter)."""
    fig, ax = plt.subplots(figsize=(7.5, 3))
    ax.scatter(horas, humedad, color="#d62728", s=45, alpha=0.85, marker="o")
    ax.set_title("Humedad Relativa en CDMX - Distribución (Dispersión)", fontsize=11, fontweight="bold")
    ax.set_xlabel("Hora del día")
    ax.set_ylabel("Humedad (%)")
    ax.grid(True, linestyle="-.", alpha=0.4)
    ax.tick_params(axis="x", rotation=45)
    fig.tight_layout()
    return fig


def mostrar_graficas(frm, horas, humedad):
    """Limpia gráficas previas e inserta las 3 gráficas en el frame."""
    for widget in frm.winfo_children():
        if isinstance(widget, tk.Canvas):
            widget.destroy()

    # 1. Línea
    fig1 = create_line_chart(horas, humedad)
    canvas1 = FigureCanvasTkAgg(fig1, master=frm)
    canvas1.draw()
    canvas1.get_tk_widget().pack(pady=10, fill="x")

    # 2. Barras
    fig2 = create_bar_chart(horas, humedad)
    canvas2 = FigureCanvasTkAgg(fig2, master=frm)
    canvas2.draw()
    canvas2.get_tk_widget().pack(pady=10, fill="x")

    # 3. Dispersión (Tercera gráfica)
    fig3 = create_scatter_chart(horas, humedad)
    canvas3 = FigureCanvasTkAgg(fig3, master=frm)
    canvas3.draw()
    canvas3.get_tk_widget().pack(pady=10, fill="x")


def open_win_canvas(parent: tk.Tk):
    """Crea la ventana secundaria con scroll (compatible con Mac) y las 3 gráficas."""
    win = tk.Toplevel(parent)
    win.title("Análisis Climático API (Open-Meteo) - Luis Angel")
    win.geometry("950x750")

    main_canvas = tk.Canvas(win)
    scrollbar = ttk.Scrollbar(win, orient="vertical", command=main_canvas.yview)
    scrollable_frame = ttk.Frame(main_canvas, padding=15)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all"))
    )

    main_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    main_canvas.configure(yscrollcommand=scrollbar.set)

    # Scroll con dos dedos para Trackpad de macOS
    def _on_mousewheel(event):
        main_canvas.yview_scroll(int(-1 * event.delta), "units")

    main_canvas.bind_all("<MouseWheel>", _on_mousewheel)

    main_canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    def cargar():
        horas, humedad = fetch_data()
        if horas and humedad:
            mostrar_graficas(scrollable_frame, horas, humedad)

    ttk.Button(
        scrollable_frame,
        text="Consultar API y Generar 3 Gráficas",
        command=cargar
    ).pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Prueba win_canvas")
    ttk.Button(root, text="Abrir ventana Canvas", command=lambda: open_win_canvas(root)).pack(pady=20)
    root.mainloop()