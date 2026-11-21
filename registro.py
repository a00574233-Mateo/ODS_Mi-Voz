from datetime import datetime
import os

ARCHIVO = "historial_uso.txt"

def registrar_uso(categoria, palabra):
    ahora = datetime.now()
    fecha = ahora.strftime("%d/%m/%Y")
    hora = ahora.strftime("%H:%M:%S")
    
    linea = fecha + " | " + hora + " | " + categoria + " | " + palabra + "\n"
    
    archivo = open(ARCHIVO, "a", encoding="utf-8")
    archivo.write(linea)
    archivo.close()

def obtener_estadisticas():
    total = 0
    comida = 0
    sociable = 0
    ayuda = 0
    bano = 0
    
    alertas_sensoriales = 0
    manana = 0
    tarde = 0
    noche = 0
    
    primera_hora = "Sin registros"
    ultima_hora = "Sin registros"
    
    conteo_palabras = {}
    historial_texto = ""

    if not os.path.exists(ARCHIVO):
        return (total, comida, sociable, ayuda, bano,
                "Ninguna aún", alertas_sensoriales, "Sin datos",
                primera_hora, ultima_hora, "Aún no se ha tocado ningún botón hoy.")

    archivo = open(ARCHIVO, "r", encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()

    for linea in lineas:
        partes = linea.strip().split(" | ")
        
        fecha = ""
        hora = ""
        categoria = ""
        palabra = ""

        if len(partes) == 4:
            fecha = partes[0]
            hora = partes[1]
            categoria = partes[2]
            palabra = partes[3]
        elif len(partes) == 3:
            fecha = "Hoy"
            hora = partes[0]
            categoria = partes[1]
            palabra = partes[2]

        if categoria != "":
            total = total + 1
            
            if total == 1:
                primera_hora = hora
            ultima_hora = hora
            
            if categoria == "Comida":
                comida = comida + 1
            if categoria == "Sociable":
                sociable = sociable + 1
            if categoria == "Ayuda":
                ayuda = ayuda + 1
            if categoria == "Baño":
                bano = bano + 1
                
            if palabra == "Mucho ruido" or palabra == "Tengo dolor" or palabra == "Ayuda urgente":
                alertas_sensoriales = alertas_sensoriales + 1
                
            hora_numero = int(hora.split(":")[0])
            if hora_numero < 12:
                manana = manana + 1
            elif hora_numero < 19:
                tarde = tarde + 1
            else:
                noche = noche + 1
                
            if palabra in conteo_palabras:
                conteo_palabras[palabra] = conteo_palabras[palabra] + 1
            else:
                conteo_palabras[palabra] = 1
                
            historial_texto = fecha + " (" + hora + ")  -  " + categoria + ": " + palabra + "\n" + historial_texto

    palabra_mas_usada = "Ninguna aún"
    mayor_cantidad = 0
    for p in conteo_palabras:
        if conteo_palabras[p] > mayor_cantidad:
            mayor_cantidad = conteo_palabras[p]
            palabra_mas_usada = p + " (" + str(mayor_cantidad) + " veces)"

    franja_activa = "Mañana (" + str(manana) + ")"
    if tarde > manana and tarde >= noche:
        franja_activa = "Tarde (" + str(tarde) + ")"
    if noche > manana and noche > tarde:
        franja_activa = "Noche (" + str(noche) + ")"

    if total == 0:
        franja_activa = "Sin datos"
        historial_texto = "Aún no se ha tocado ningún botón hoy."

    return (total, comida, sociable, ayuda, bano,
            palabra_mas_usada, alertas_sensoriales, franja_activa,
            primera_hora, ultima_hora, historial_texto)

def reiniciar_estadisticas():
    if os.path.exists(ARCHIVO):
        os.remove(ARCHIVO)