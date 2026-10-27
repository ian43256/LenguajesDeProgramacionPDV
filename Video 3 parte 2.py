from tkinter import *

root = Tk()
root.title("Práctica Salva a Bob Esponja")

mi_frame = Frame(root, width=500, height=700)
mi_frame.pack()

# Cargar la imagen (debe estar en el mismo directorio o especificar la ruta)
mi_imagen = PhotoImage(file="Bob.png")

# Asignar la imagen al Label
mi_label = Label(mi_frame, image=mi_imagen)
mi_label.place(x=100, y=100)

root.mainloop() 