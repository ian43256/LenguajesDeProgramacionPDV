from tkinter import *                              # Importa todas las herramientas de la librería gráfica tkinter

raiz = Tk()                                        # Crea la ventana principal de la calculadora

miFrame = Frame(raiz)                              # Crea el marco interno que contendrá los elementos
miFrame.pack()                                     # Empaqueta y muestra el marco en la ventana principal

# --- PANTALLA ---
pantalla = Entry(miFrame)                          # Crea el cuadro de texto para la pantalla
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4) # Fila 1, ocupa 4 columnas con márgenes
pantalla.config(background="black", fg="#03f943", justify="right") # Fondo negro, texto verde y alineado a la derecha

# --- FILA 1 ---
boton7 = Button(miFrame, text="7", width=3)        # Crea el botón '7' con un ancho de 3
boton7.grid(row=2, column=1)                       # Lo ubica en la fila 2, columna 1
boton8 = Button(miFrame, text="8", width=3)        # Crea el botón '8' con un ancho de 3
boton8.grid(row=2, column=2)                       # Lo ubica en la fila 2, columna 2
boton9 = Button(miFrame, text="9", width=3)        # Crea el botón '9' con un ancho de 3
boton9.grid(row=2, column=3)                       # Lo ubica en la fila 2, columna 3
botonDiv = Button(miFrame, text="/", width=3)      # Crea el botón de división '/' con un ancho de 3
botonDiv.grid(row=2, column=4)                     # Lo ubica en la fila 2, columna 4

# --- FILA 2 ---
boton4 = Button(miFrame, text="4", width=3)        # Crea el botón '4'
boton4.grid(row=3, column=1)                       # Lo ubica en la fila 3, columna 1
boton5 = Button(miFrame, text="5", width=3)        # Crea el botón '5'
boton5.grid(row=3, column=2)                       # Lo ubica en la fila 3, columna 2
boton6 = Button(miFrame, text="6", width=3)        # Crea el botón '6'
boton6.grid(row=3, column=3)                       # Lo ubica en la fila 3, columna 3
botonMult = Button(miFrame, text="x", width=3)     # Crea el botón de multiplicación 'x'
botonMult.grid(row=3, column=4)                    # Lo ubica en la fila 3, columna 4

# --- FILA 3 ---
boton1 = Button(miFrame, text="1", width=3)        # Crea el botón '1'
boton1.grid(row=4, column=1)                       # Lo ubica en la fila 4, columna 1
boton2 = Button(miFrame, text="2", width=3)        # Crea el botón '2'
boton2.grid(row=4, column=2)                       # Lo ubica en la fila 4, columna 2
boton3 = Button(miFrame, text="3", width=3)        # Crea el botón '3'
boton3.grid(row=4, column=3)                       # Lo ubica en la fila 4, columna 3
botonRest = Button(miFrame, text="-", width=3)     # Crea el botón de resta '-'
botonRest.grid(row=4, column=4)                    # Lo ubica en la fila 4, columna 4

# --- FILA 4 ---
boton0 = Button(miFrame, text="0", width=3)        # Crea el botón '0'
boton0.grid(row=5, column=1)                       # Lo ubica en la fila 5, columna 1
botonComa = Button(miFrame, text=",", width=3)     # Crea el botón para la coma decimal ','
botonComa.grid(row=5, column=2)                    # Lo ubica en la fila 5, columna 2
botonIgual = Button(miFrame, text="=", width=3)    # Crea el botón de resultado '='
botonIgual.grid(row=5, column=3)                   # Lo ubica en la fila 5, columna 3
botonSum = Button(miFrame, text="+", width=3)      # Crea el botón de suma '+'
botonSum.grid(row=5, column=4)                     # Lo ubica en la fila 5, columna 4


raiz.mainloop()                                    # Bucle que mantiene la calculadora abierta