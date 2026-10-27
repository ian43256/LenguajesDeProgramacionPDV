from tkinter import *

# Ventana principal
raiz = Tk()
raiz.title("Ventana de pruebas")          # Título
# raiz.resizable(True, False)             # Permitir/bloquear redimensionar
# raiz.iconbitmap("gato.ico")             # Icono de la ventana
raiz.geometry("650x350")                  # Tamaño (Ancho x Alto)
raiz.config(bg="lightblue")                    # Fondo azul
raiz.config(bd=45)                        # Borde de 45px
raiz.config(relief="groove")              # Estilo de borde acanalado
raiz.config(cursor="hand2")               # Cursor de mano

# Marco interior
miFrame = Frame()
miFrame.pack(fill="both", expand=True)    # Expande el marco con la ventana
miFrame.config(bg="red")                  # Fondo rojo
miFrame.config(width="650", height="350") # Tamaño del marco
miFrame.config(bd=35)                     # Borde de 35px
miFrame.config(relief="sunken")           # Estilo de borde hundido
miFrame.config(cursor="pirate")           # Cursor de calavera

# Mantiene la ventana abierta
raiz.mainloop()