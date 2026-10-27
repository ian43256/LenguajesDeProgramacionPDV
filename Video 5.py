from tkinter import *                                   # Importa todas las herramientas de la librería gráfica

raiz = Tk()                                             # Crea la ventana principal

miFrame = Frame(raiz, width=1200, height=600)           # Crea el marco contenedor dentro de la ventana
miFrame.pack()                                          # Empaqueta e inserta el marco en la ventana

# --- VARIABLES ---
miNombre = StringVar()                                  # Crea una variable de texto dinámica de tkinter

# --- FUNCIONES ---
def codigoBoton():                                      # Función que se ejecutará al hacer clic
    miNombre.set("Juan")                                # Asigna el texto "Juan" a la variable dinámica

# --- CUADROS DE ENTRADA (Entry y Text) ---
cuadroNombre = Entry(miFrame, textvariable=miNombre)    # Crea campo asociado a la variable 'miNombre'
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)    # Lo ubica en fila 0, columna 1 con margen
cuadroNombre.config(fg="red", justify="right")          # Configura el texto escrito en rojo y a la derecha

cuadroPass = Entry(miFrame)                             # Crea campo para la contraseña
cuadroPass.grid(row=1, column=1, padx=10, pady=10)      # Lo ubica en la fila 1, columna 1
cuadroPass.config(show="*")                             # Oculta lo que se escriba mostrando asteriscos

cuadroApellido = Entry(miFrame)                         # Crea campo para el apellido
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)  # Lo ubica en la fila 2, columna 1

cuadroDireccion = Entry(miFrame)                        # Crea campo para la dirección
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10) # Lo ubica en la fila 3, columna 1

textoComentario = Text(miFrame, width=16, height=5)     # Crea área para texto largo (16 caracteres x 5 líneas)
textoComentario.grid(row=4, column=1, padx=10, pady=10) # Lo ubica en la fila 4, columna 1

# --- BARRA DE DESPLAZAMIENTO (Scrollbar) ---
scrollVert = Scrollbar(miFrame, command=textoComentario.yview) # Crea la barra y la asocia al eje vertical del texto
scrollVert.grid(row=4, column=2, sticky="nsew")         # La ubica junto al texto y la estira de arriba a abajo
textoComentario.config(yscrollcommand=scrollVert.set)   # Sincroniza la posición visual de la barra con el texto

# --- ETIQUETAS (Labels) ---
nombreLabel = Label(miFrame, text="Nombre:")            # Crea la etiqueta "Nombre:"
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10) # Fila 0, col 0, pegada a la derecha ('e' = Este)

passLabel = Label(miFrame, text="Password:")            # Crea la etiqueta "Password:"
passLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10) # Fila 1, col 0, pegada a la derecha

apellidoLabel = Label(miFrame, text="Apellido:")        # Crea la etiqueta "Apellido:"
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10) # Fila 2, col 0, pegada a la derecha

direccionLabel = Label(miFrame, text="Dirección:")      # Crea la etiqueta "Dirección:"
direccionLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10) # Fila 3, col 0, pegada a la derecha

comentariosLabel = Label(miFrame, text="Comentarios:")  # Crea la etiqueta "Comentarios:"
comentariosLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10) # Fila 4, col 0, pegada a la derecha

# --- BOTÓN ---
botonEnvio = Button(raiz, text="Enviar", command=codigoBoton) # Crea el botón "Enviar" que ejecuta la función
botonEnvio.pack()                                       # Inserta el botón directamente en la raíz (debajo del frame)

raiz.mainloop()                                         # Bucle que mantiene la ventana abierta y funcionando