# JUEGO DEL AHORCADO – Versión en Tkinter (Nivel Principiante)

# ¿Qué hace este programa?

Este programa es un juego básico del *Ahorcado*, creado con el lenguaje de programación **Python** y usando la librería gráfica *Tkinter*.  
El juego elige una palabra al azar y el jugador debe adivinarla letra por letra antes de que se dibuje por completo el muñeco del ahorcado, como el que ya todos conocemos.

Incluye:
- Ventana gráfica con Tkinter.
- Canvas para dibujar al muñeco por partes.
- Botones de colores para jugar y reiniciar.
- Entrada de texto para escribir una letra.
- Mensajes cuando ganas y cuando pierdes.
- Reinicio automático de la partida.

Es un juego pensado para principiantes que empiezan a aprender Python.

---

## 📌 ¿Qué partes del código implementé?

Durante el desarrollo del juego agregué e implementé:

### ✔ Funciones principales del juego
- `elegir_palabra()` para seleccionar una palabra al azar.
- `crear_tablero()` para mostrar los guiones.
- `revisar_letra()` para saber si la letra está en la palabra.
- `mostrar_parte()` para dibujar las partes del ahorcado.
- `nueva_partida()` para reiniciar todo el juego.
- `procesar_letra()` para verificar cada intento del jugador.

### ✔ Interfaz gráfica (Tkinter)
- Creación de la ventana principal (`Tk()`).
- Etiquetas para mostrar la palabra y los intentos.
- Canvas para dibujar la base y las partes del muñeco.
- Caja de texto donde el usuario escribe una letra.
- Botones con colores usando una función personalizada:
  - Botón “Probar letra”
  - Botón “Nueva partida”

### ✔ Manejo del estado del juego
Usé un diccionario `datos` para controlar:
- palabra elegida
- tablero
- número de fallos
- partes del muñeco
- acceso a los objetos de la interfaz

Esto permite organizar el código de manera sencilla sin usar clases.

---

## 📌 ¿Qué aprendí durante el desarrollo?

Durante este proyecto aprendí varias cosas importantes:

### ✔ Cómo usar Tkinter
- Crear ventanas, botones, etiquetas y canvas.
- Cambiar colores y estilos básicos.
- Actualizar el contenido de los widgets durante el juego.

### ✔ Programación estructurada
- Dividir el programa en funciones.
- Evitar código repetido.
- Mantener el programa más fácil de entender y modificar.

### ✔ Manejo de lógica del juego
- Cómo verificar letra por letra.
- Actualizar el tablero en pantalla.
- Llevar control de los fallos.
- Detectar cuándo ganas o pierdes.

### ✔ Trabajo con Canvas
- Dibujar líneas, círculos y figuras básicas.
- Ocultar y mostrar partes del muñeco.

### ✔ Depuración de errores
- Problemas con indentación.
- Variables fuera de alcance.
- Botones mal escritos.
- Funciones colocadas fuera de su lugar.

En general, este proyecto me ayudó a reforzar mis conocimientos de Python, lógica y Tkinter, además de aprender a organizar mejor el código.

---

**Fin del README.md**
