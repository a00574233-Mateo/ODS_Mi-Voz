# Cambios en win_canvas.py - Mateo Cosulich

## Entorno virtual y dependencias
- Creé el entorno virtual `.venv` y lo seleccioné como intérprete en VS Code.
- Instalé `matplotlib` y `requests` con `pip install -r requirements.txt`.
- Verifiqué la instalación con `pip list`.
- Agregué `requirements.txt` y `.gitignore` (para no subir `.venv` ni `__pycache__`).

## Cambios realizados
- Cambié la ciudad a Guanajuato capital (latitud 21.02, longitud -101.26).
- Cambié el rango de consulta a los últimos 2 días más el día actual (`past_days=2`, `forecast_days=1`).
- Agregué un segundo dato de la API: humedad relativa (`relativehumidity_2m`), además de la temperatura.
- Gráfica de línea: temperatura en color morado, con marcadores cuadrados y el área debajo sombreada.
- Gráfica de barras: ahora muestra la humedad en azul, con el eje Y de 0 a 100 %.
- Gráfica de dispersión: relación entre temperatura y humedad, en color rosa.
- Agregué rejilla a las tres gráficas.
- En el eje X dejé solo una etiqueta cada 12 horas para que se lea mejor.
- Si se presiona el botón otra vez, las gráficas se reemplazan en lugar de repetirse.

## Lo que se observa
En la gráfica de dispersión se ve que cuando sube la temperatura baja la humedad: en las tardes hace más calor y el aire está más seco, y en las madrugadas pasa lo contrario.

## Captura
![Gráficas](img/graficas_mateo_cosulich.png)
