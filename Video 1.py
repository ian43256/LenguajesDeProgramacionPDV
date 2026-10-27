from tkinter import *

# Creación de la ventana principal (raíz)
raiz = Tk()

# Asignar un título a la ventana
raiz.title("Ventana de pruebas")

# Bloquear o permitir redimensión (ancho, alto)
# Usar (0, 0) o (False, False) bloquea completamente la redimensión. 
raiz.resizable(True, False) 

# Cambiar el icono de la ventana (requiere tener un archivo .ico en la misma carpeta)
raiz.iconbitmap("gato.ico")

# Definir las dimensiones iniciales (ancho x alto)
raiz.geometry("650x350")

# Cambiar el color de fondo (bg = background)
raiz.config(bg="red")

# 7. Bucle infinito para mantener la ventana en ejecución (debe ir siempre al final)
raiz.mainloop()