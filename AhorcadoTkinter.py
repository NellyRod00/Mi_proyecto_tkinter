import tkinter as tk
from tkinter import messagebox
import random

#MENÚ SOBRE EL JUEGO
# Elegir palabra al azar
# Crear tablero con guiones
# Revisar la letra en la palabra
# Dibujar partes del muñeco
# Iniciar nueva partida
# Elegir palabra y crear tablero
# Limpiar canvas y redibujar base
# Base del ahorcado
# Crear partes ocultas
# Mostrar tablero
# Jugar partida
# Validar repetidas
# Revisar letra en palabra
# Gano??
# Perdió???
# Repetir partida

# Función para usar nombres de colores
def color(nombre):
    colores = {
        "morado": "red",
        "verde": "green",
        "azul": "blue",
        "rojo": "red",
        "amarillo": "yellow"
    }
    return colores.get(nombre, "gray")

# Elegir palabra al azar
def elegir_palabra():
    palabras = ["flores", "arcoiris", "piano", "unicornio", "girasol"]
    return random.choice(palabras)

# Crear tablero con guiones
def crear_tablero(palabra):
    return ["_"] * len(palabra)

# Revisar la letra en la palabra
def revisar_letra(letra, palabra, tablero):
    acierto = False
    for i in range(len(palabra)):
        if palabra[i] == letra:
            tablero[i] = letra
            acierto = True
    return acierto

# Dibujar partes del muñeco
def mostrar_parte(canvas, partes, indice):
    if indice < len(partes):
        canvas.itemconfig(partes[indice], state="normal")
        canvas.update()

# Iniciar nueva partida
def nueva_partida(root, datos):
    palabra = elegir_palabra()
    tablero = crear_tablero(palabra)

    datos["palabra"] = palabra
    datos["tablero"] = tablero
    datos["fallos"] = 0

    canvas = datos["canvas"]
    canvas.delete("all")

    # Base del ahorcado
    canvas.create_line(20, 230, 180, 230, width=4)
    canvas.create_line(60, 230, 60, 40, width=4)
    canvas.create_line(60, 40, 140, 40, width=4)
    canvas.create_line(140, 40, 140, 80, width=4)

    # Crear partes ocultas
    cabeza = canvas.create_oval(100, 60, 160, 100, width=3, state="hidden")
    cuerpo = canvas.create_line(120, 100, 180, 150, width=3, state="hidden")
    brazo_izq = canvas.create_line(120, 120, 150, 160, width=3, state="hidden")
    brazo_der = canvas.create_line(120, 120, 150, 160, width=3, state="hidden")
    pierna_izq = canvas.create_line(170, 180, 170, 210, width=3, state="hidden")
    pierna_der = canvas.create_line(170, 180, 170, 210, width=3, state="hidden")

    datos["partes"] = [cabeza, cuerpo, brazo_izq, brazo_der, pierna_izq, pierna_der]

    datos["lbl_tablero"].config(text=" ".join(tablero))
    datos["lbl_info"].config(text="Intentos restantes: 6")
    
# Procesar la letra
def procesar_letra(letra, datos):
    letra = letra.lower()
    palabra = datos["palabra"]
    tablero = datos["tablero"]
    fallos = datos["fallos"]

    if letra == "" or len(letra) > 1:
        messagebox.showinfo("Error", "Ingresa solo una letra.")
        return

    if revisar_letra(letra, palabra, tablero):
        datos["lbl_tablero"].config(text=" ".join(tablero))
    else:
        fallos += 1
        datos["fallos"] = fallos
        datos["lbl_info"].config(text=f"Intentos restantes: {6 - fallos}")
        mostrar_parte(datos["canvas"], datos["partes"], fallos - 1)

    if "_" not in tablero:
        messagebox.showinfo("Ganaste", "¡Adivinaste la palabra oculta!")
        nueva_partida(datos["root"], datos)

    if fallos == 6:
        messagebox.showinfo("Perdedor!!", f"La palabra era: {palabra}")
        nueva_partida(datos["root"], datos)

# Crear ventana principal
def iniciar_juego():
    root = tk.Tk()
    root.title("Ahorcado")
    root.geometry("450x600")

    lbl_titulo = tk.Label(root, text="Ahorcado", font=("Arial", 20))
    lbl_titulo.pack(pady=5)

    lbl_tablero = tk.Label(root, text="", font=("Arial", 24))
    lbl_tablero.pack(pady=10)

    lbl_info = tk.Label(root, text="Intentos restantes: 6", font=("Arial", 14))
    lbl_info.pack(pady=5)

    canvas = tk.Canvas(root, width=250, height=260, bg="pink")
    canvas.pack(pady=16)

    entry = tk.Entry(root, font=("Arial", 20), width=8)
    entry.pack(pady=12)

    datos = {
        "root": root,
        "canvas": canvas,
        "lbl_tablero": lbl_tablero,
        "lbl_info": lbl_info,
        "palabra": "",
        "tablero": [],
        "fallos": 0,
        "partes": []
    }

    def click():
        letra = entry.get()
        entry.delete(0, tk.END)
        procesar_letra(letra, datos)

    btn = tk.Button(
        root,
        text="Probar letra",
        font=("Arial", 12, "bold"),
        bg=color("verde"),
        fg="white",
        width=12,
        command=click
    )
    btn.pack(pady=10)

    btn_reset = tk.Button(
        root,
        text="Nueva Partida",
        font=("Arial", 12, "bold"),
        bg=color("morado"),
        fg="white",
        width=12,
        command=lambda: nueva_partida(root, datos)
    )
    btn_reset.pack(pady=5)

    nueva_partida(root, datos)

    root.mainloop()

iniciar_juego()