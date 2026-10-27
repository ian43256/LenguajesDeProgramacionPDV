from tkinter import *
# Ventana principal
root = Tk()
root.title("Práctica Label")              # Título

# Marco interior (Frame)
mi_frame = Frame(root, width=500, height=400)
mi_frame.pack()                           # Empaquetado dentro de la raíz

# Etiqueta de texto (Label)
mi_label = Label(
    mi_frame, 
    text="CHICOOOOS COMO ESTAN", 
    fg="red",                             # Color de la fuente
    font=("Comic Sans MS", 18)            # Tipografía y tamaño
)
mi_label.place(x=100, y=200)              # Ubicación por coordenadas (x, y)

# Mantiene la ventana abierta
root.mainloop()