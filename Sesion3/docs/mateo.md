# Cambios en win_canvas.py - Mateo Sanchez

## Cambios realizados
- Cambié el color de la gráfica de línea a verde (color="green").
- Cambié el color de las barras a naranja (color="orange").
- Amplié el rango de consulta de la API de past_days=1 a past_days=3 (se ven 4 días).
- Usé mdates (DayLocator y DateFormatter) para mostrar una etiqueta de fecha por día en el eje X.
- Agregué una tercera gráfica de dispersión en color morado (create_scatter_chart).
- Agregué rejilla punteada con ax.grid(True, linestyle="--", alpha=0.5).
- Agregué docstrings a las funciones para documentar el código.

## Captura
![Gráficas](mateo_imagen.png)
