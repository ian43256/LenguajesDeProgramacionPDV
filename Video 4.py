from tkinter import *                              # Importa todas las funciones y clases de Tkinter

raiz = Tk()                                         # Crea la ventana principal de la aplicación
miFrame = Frame(raiz, width=1200, height=600)       # Crea el contenedor interno (marco) de 1200x600 px
miFrame.pack()                                      # Empaqueta y muestra el marco en la ventana principal

#Cuadros de entrada de texto
cuadroNombre = Entry(miFrame)                       # Crea el cuadro de texto para el nombre
cuadroNombre.grid(row=0, column=1, padx=10, pady=10) # Lo coloca en fila 0, columna 1 con margen de 10px
cuadroNombre.config(fg="red", justify="center")     # Hace que el texto escrito sea rojo y centrado

cuadroPass = Entry(miFrame)                         # Crea el cuadro de texto para la contraseña
cuadroPass.grid(row=1, column=1, padx=10, pady=10)  # Lo coloca en fila 1, columna 1 con margen de 10px
cuadroPass.config(show="*")                         # Enmascara los caracteres escritos reemplazándolos por '*'

cuadroApellido = Entry(miFrame)                     # Crea el cuadro de texto para el apellido
cuadroApellido.grid(row=2, column=1, padx=10, pady=10) # Lo coloca en fila 2, columna 1 con margen de 10px

cuadroDireccion = Entry(miFrame)                    # Crea el cuadro de texto para la dirección
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10) # Lo coloca en fila 3, columna 1 con margen de 10px

#Etiquetas de texto 
nombreLabel = Label(miFrame, text="Nombre:")        # Crea la etiqueta con el texto "Nombre:"
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10) # Fila 0, col 0, alineada a la derecha ('e' = Este)

passLabel = Label(miFrame, text="Password:")        # Crea la etiqueta con el texto "Password:"
passLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10) # Fila 1, col 0, alineada a la derecha

apellidoLabel = Label(miFrame, text="Apellido:")    # Crea la etiqueta con el texto "Apellido:"
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10) # Fila 2, col 0, alineada a la derecha

direccionLabel = Label(miFrame, text="Dirección de casa:") # Crea la etiqueta "Dirección de casa:"
direccionLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10) # Fila 3, col 0, alineada a la derecha

raiz.mainloop()                                     # Mantiene la ventana abierta a la escucha de eventos