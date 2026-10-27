from tkinter import *
from tkinter import messagebox, filedialog

PRODUCTOS = {
    "Chocolates": 20,
    "Gomitas": 15,
    "Paletas": 10,
    "Caramelos": 5,
    "Chicles": 8,
    "Malvaviscos": 25,
    "Galletas": 18,
    "Mazapanes": 7,
    "Pulparindos": 9,
    "Regaliz": 12,
    "Gomitas ácidas": 16,
    "Brownies": 22,
    "Donas": 14,
    "Bombones": 11,
}

INVENTARIO = {
    "Chocolates": 15,
    "Gomitas": 20,
    "Paletas": 25,
    "Caramelos": 30,
    "Chicles": 30,
    "Malvaviscos": 10,
    "Galletas": 12,
    "Mazapanes": 20,
    "Pulparindos": 18,
    "Regaliz": 15,
    "Gomitas ácidas": 14,
    "Brownies": 8,
    "Donas": 10,
    "Bombones": 16,
}

USUARIOS = {
    "admin": "1234",
    "cajero1": "0000",
    "cajero2": "1111",
}


COLOR_FONDO = "#ffebee"    
COLOR_PRINCIPAL = "#c62828" 
COLOR_SUAVE = "#ef9a9a"     
COLOR_SECCION = "#ffcdd2"   

IVA = 0.16                
STOCK_BAJO = 3             
REABASTECER_CANTIDAD = 10  
PRODUCTOS_POR_COLUMNA = 7  


root = Tk()
root.title("Punto de Venta - Sweet Shop")
root.geometry("420x380")
root.config(bg=COLOR_FONDO)


login_usuario = StringVar()
login_pin = StringVar()
usuario_activo = StringVar()

nombre_cliente = StringVar()
tipo_cliente = IntVar(value=1)  
numero_ticket = IntVar(value=1)
pago_cliente = IntVar(value=0) 

vars_productos = {}
vars_stock = {}
for nombre in PRODUCTOS:
    vars_productos[nombre] = IntVar(value=0)
    vars_stock[nombre] = StringVar()

botones_mas = {}
labels_stock = {}

subtotal_venta = StringVar()
descuento_venta = StringVar()
iva_venta = StringVar()
total_venta = StringVar()
cambio_venta = StringVar()
ticket_texto = StringVar()

subtotal_venta.set("Subtotal: $0.00")
descuento_venta.set("Descuento VIP: -$0.00")
iva_venta.set("IVA (16%): $0.00")
total_venta.set("Total: $0.00")
cambio_venta.set("Cambio: $0.00")
ticket_texto.set("\n\n   Aún no hay tickets.\n\n   Confirma una venta y\n   el ticket aparecerá aquí.\n\n")

def actualizar_inventario():
    """Refresca las etiquetas de stock y bloquea los dulces agotados."""
    for nombre in PRODUCTOS:
        existencias = INVENTARIO[nombre]
        vars_stock[nombre].set(f"Stock: {existencias}")

        if existencias == 0:
            vars_productos[nombre].set(0)
            botones_mas[nombre].config(state="disabled")
            labels_stock[nombre].config(fg="red")
            vars_stock[nombre].set("AGOTADO")
        elif existencias <= STOCK_BAJO:
            botones_mas[nombre].config(state="normal")
            labels_stock[nombre].config(fg="#e65100")
        else:
            botones_mas[nombre].config(state="normal")
            labels_stock[nombre].config(fg="gray")

def calcular_subtotal():
    """Suma precio x cantidad de cada producto (sin descuento ni IVA)."""
    subtotal = 0
    for nombre, precio in PRODUCTOS.items():
        subtotal += precio * vars_productos[nombre].get()
    return subtotal

def calcular_descuento():
    """10% de descuento si el cliente es VIP."""
    descuento = 0
    if tipo_cliente.get() == 2:
        descuento = calcular_subtotal() * 0.10
    return descuento

def calcular_iva():
    """IVA sobre el subtotal ya con descuento."""
    return (calcular_subtotal() - calcular_descuento()) * IVA

def calcular_total():
    """Actualiza subtotal, descuento, IVA y total en pantalla; regresa el total con IVA."""
    subtotal = calcular_subtotal()
    descuento = calcular_descuento()
    iva = calcular_iva()
    total = subtotal - descuento + iva

    subtotal_venta.set(f"Subtotal: ${subtotal:.2f}")
    descuento_venta.set(f"Descuento VIP: -${descuento:.2f}")
    iva_venta.set(f"IVA (16%): ${iva:.2f}")
    total_venta.set(f"Total: ${total:.2f}")
    cambio_venta.set("Cambio: $0.00")
    return total

def agregar_producto(nombre):
    """Suma una pieza del dulce a la compra (sin pasar de las existencias)."""
    if vars_productos[nombre].get() >= INVENTARIO[nombre]:
        messagebox.showwarning("Sin existencias", f"Solo hay {INVENTARIO[nombre]} piezas de {nombre}.")
        return
    vars_productos[nombre].set(vars_productos[nombre].get() + 1)
    calcular_total()

def quitar_producto(nombre):
    """Resta una pieza del dulce de la compra."""
    if vars_productos[nombre].get() > 0:
        vars_productos[nombre].set(vars_productos[nombre].get() - 1)
        calcular_total()

def calcular_cambio():
    """Calcula el cambio con lo que paga el cliente y lo muestra en pantalla."""
    total = calcular_total()
    try:
        pagado = pago_cliente.get()
    except Exception:
        cambio_venta.set("Pago no válido (solo números)")
        return

    if pagado + 0.001 < total:
        cambio_venta.set(f"Faltan: ${total - pagado:.2f}")
    else:
        cambio = pagado - total
        if cambio < 0:
            cambio = 0
        cambio_venta.set(f"Cambio: ${cambio:.2f}")

def limpiar_venta():
    """Deja el formulario listo para una nueva venta."""
    nombre_cliente.set("")
    tipo_cliente.set(1)
    pago_cliente.set(0)
    for nombre in PRODUCTOS:
        vars_productos[nombre].set(0)
    texto_notas.delete("1.0", END)
    calcular_total()
    actualizar_inventario()

def confirmar_venta():
    """Valida, cobra, descuenta inventario, guarda venta/cliente/ticket en txt y muestra el ticket."""
    cajero = usuario_activo.get()
    cliente = nombre_cliente.get()
    total = calcular_total()
    subtotal = calcular_subtotal()
    descuento = calcular_descuento()
    iva = calcular_iva()
    notas = texto_notas.get("1.0", END).strip().replace("\n", " ")

    if cliente == "" or cajero == "":
        messagebox.showwarning("Faltan datos", "Por favor ingresa el nombre del cliente.")
        return
    if total == 0:
        messagebox.showwarning("Venta vacía", "Agrega al menos un dulce.")
        return

    dulces = []
    for nombre in PRODUCTOS:
        if vars_productos[nombre].get() > 0:
            dulces.append(nombre)

    for nombre in dulces:
        if vars_productos[nombre].get() > INVENTARIO[nombre]:
            messagebox.showwarning("Sin existencias", f"Solo hay {INVENTARIO[nombre]} piezas de {nombre}.")
            return

    try:
        pagado = pago_cliente.get()
    except Exception:
        messagebox.showwarning("Pago no válido", "Escribe con cuánto paga el cliente (solo números enteros).")
        return
    if pagado + 0.001 < total:
        messagebox.showwarning("Pago insuficiente", f"El cliente paga ${pagado:.2f} y el total es ${total:.2f}.\nFaltan ${total - pagado:.2f}.")
        return

    cambio = pagado - total
    if cambio < 0:
        cambio = 0

    if tipo_cliente.get() == 2:
        membresia = "VIP"
    else:
        membresia = "Regular"

    numero = numero_ticket.get()

    detalle = []
    ticket = "==============================\n"
    ticket = ticket + "         SWEET SHOP\n"
    ticket = ticket + "==============================\n"
    ticket = ticket + f"Ticket: #{numero:04d}\n"
    ticket = ticket + f"Cajero: {cajero}\n"
    ticket = ticket + f"Cliente: {cliente} ({membresia})\n"
    ticket = ticket + "------------------------------\n"
    for nombre in dulces:
        cantidad = vars_productos[nombre].get()
        importe = PRODUCTOS[nombre] * cantidad
        linea = f"{cantidad} x {nombre}"
        ticket = ticket + f"{linea:<20}${importe:>8.2f}\n"
        detalle.append(f"{cantidad}x {nombre}")
    ticket = ticket + "------------------------------\n"
    ticket = ticket + f"{'Subtotal:':<20}${subtotal:>8.2f}\n"
    if tipo_cliente.get() == 2:
        ticket = ticket + f"{'Descuento VIP 10%:':<20}-${descuento:>7.2f}\n"
    ticket = ticket + f"{'IVA 16%:':<20}${iva:>8.2f}\n"
    ticket = ticket + "==============================\n"
    ticket = ticket + f"{'TOTAL:':<20}${total:>8.2f}\n"
    ticket = ticket + f"{'Paga con:':<20}${pagado:>8.2f}\n"
    ticket = ticket + f"{'Cambio:':<20}${cambio:>8.2f}\n"
    ticket = ticket + "==============================\n"
    if notas != "":
        ticket = ticket + f"Notas: {notas}\n"
    ticket = ticket + "   ¡Gracias por su compra!\n"

    try:

        with open("ventas.txt", "a", encoding="utf-8") as file:
            file.write(
                f"Ticket: #{numero:04d} | Cajero: {cajero} | Cliente: {cliente} | Membresía: {membresia} | "
                f"Dulces: {', '.join(detalle)} | Subtotal: ${subtotal:.2f} | IVA: ${iva:.2f} | "
                f"Total: ${total:.2f} | Pagó: ${pagado:.2f} | Cambio: ${cambio:.2f} | Notas: {notas}\n"
            )

        with open("clientes.txt", "a", encoding="utf-8") as file:
            file.write(
                f"Cliente: {cliente} | Membresía: {membresia} | Ticket: #{numero:04d} | "
                f"Compra: ${total:.2f} | Pagó: ${pagado:.2f} | Cambio: ${cambio:.2f} | Atendió: {cajero}\n"
            )

        with open("tickets.txt", "a", encoding="utf-8") as file:
            file.write(ticket + "\n\n")

        for nombre in dulces:
            INVENTARIO[nombre] = INVENTARIO[nombre] - vars_productos[nombre].get()

        aviso = ""
        for nombre in dulces:
            if INVENTARIO[nombre] <= STOCK_BAJO:
                aviso = aviso + f"\n- {nombre}: quedan {INVENTARIO[nombre]}"

        mensaje = f"¡Venta registrada! Ticket #{numero:04d}\nCambio a entregar: ${cambio:.2f}\nSe guardó en ventas.txt, clientes.txt y tickets.txt."
        if aviso != "":
            mensaje = mensaje + "\n\nStock bajo:" + aviso

        ticket_texto.set(ticket)
        numero_ticket.set(numero + 1)
        limpiar_venta()
        messagebox.showinfo("Éxito", mensaje)

    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")

def ver_inventario():
    """Muestra en una ventana de mensaje las existencias de todos los dulces."""
    texto = ""
    for nombre in PRODUCTOS:
        texto = texto + f"{nombre}: {INVENTARIO[nombre]} pzas\n"
    messagebox.showinfo("Inventario actual", texto)

def reabastecer_inventario():
    """Suma REABASTECER_CANTIDAD piezas a cada producto."""
    if messagebox.askokcancel("Reabastecer", f"¿Agregar {REABASTECER_CANTIDAD} piezas a cada dulce?"):
        for nombre in PRODUCTOS:
            INVENTARIO[nombre] = INVENTARIO[nombre] + REABASTECER_CANTIDAD
        actualizar_inventario()
        messagebox.showinfo("Inventario", "Inventario reabastecido correctamente.")

def abrir_registro():
    """Utiliza FileDialog para buscar y obtener la ruta del archivo de ventas, clientes o tickets."""
    ruta_archivo = filedialog.askopenfilename(
        title="Abrir registro",
        initialdir="./",
        filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"))
    )
    if ruta_archivo:
        messagebox.showinfo("Ruta encontrada", f"El archivo se encuentra en:\n{ruta_archivo}")

def salir_app():
    """Pregunta antes de cerrar la ventana principal."""
    if messagebox.askokcancel("Salir", "¿Deseas cerrar el Punto de Venta?"):
        root.destroy()

def iniciar_sesion():
    """Valida usuario y PIN; si son correctos, quita el login y muestra el punto de venta."""
    usuario = login_usuario.get()
    pin = login_pin.get()

    if usuario == "" or pin == "":
        messagebox.showwarning("Faltan datos", "Ingresa tu usuario y tu PIN.")
        return

    if usuario in USUARIOS and USUARIOS[usuario] == pin:
        usuario_activo.set(usuario)
        login_pin.set("")
        frameLogin.destroy()

        root.geometry("1180x780")
        root.config(menu=barraMenu)
        miFrame.grid(row=0, column=0, padx=15, pady=15, sticky="n")
        panelTicket.grid(row=0, column=1, padx=5, pady=15, sticky="n")
    else:
        login_pin.set("")
        messagebox.showerror("Acceso denegado", "Usuario o PIN incorrectos.")

barraMenu = Menu(root)

menuArchivo = Menu(barraMenu, tearoff=0)
menuArchivo.add_command(label="Ver registros (ventas, clientes, tickets)", command=abrir_registro)
menuArchivo.add_command(label="Limpiar venta", command=limpiar_venta)
menuArchivo.add_separator()
menuArchivo.add_command(label="Salir", command=salir_app)

menuInventario = Menu(barraMenu, tearoff=0)
menuInventario.add_command(label="Ver inventario", command=ver_inventario)
menuInventario.add_command(label="Reabastecer todo", command=reabastecer_inventario)

menuAyuda = Menu(barraMenu, tearoff=0)
menuAyuda.add_command(label="Acerca de", command=lambda: messagebox.showinfo("Acerca de", "Software de Dulcería v4.0\nCreado con Tkinter."))

barraMenu.add_cascade(label="Archivo", menu=menuArchivo)
barraMenu.add_cascade(label="Inventario", menu=menuInventario)
barraMenu.add_cascade(label="Ayuda", menu=menuAyuda)

frameLogin = Frame(root, bg="white", bd=5, relief="groove")
frameLogin.pack(fill="both", expand=True, padx=20, pady=20)

Label(frameLogin, text="SWEET SHOP", font=("Arial", 22, "bold"), bg="white", fg=COLOR_PRINCIPAL).grid(row=0, column=0, columnspan=2, pady=(25, 5), padx=40)
Label(frameLogin, text="Inicio de sesión", font=("Arial", 12), bg="white", fg="gray").grid(row=1, column=0, columnspan=2, pady=(0, 25))

Label(frameLogin, text="Usuario:", font=("Arial", 11), bg="white").grid(row=2, column=0, sticky="e", padx=10, pady=8)
Entry(frameLogin, textvariable=login_usuario, font=("Arial", 11)).grid(row=2, column=1, sticky="w")

Label(frameLogin, text="PIN:", font=("Arial", 11), bg="white").grid(row=3, column=0, sticky="e", padx=10, pady=8)
Entry(frameLogin, textvariable=login_pin, show="*", font=("Arial", 11)).grid(row=3, column=1, sticky="w")

Button(frameLogin, text="Entrar", command=iniciar_sesion, bg=COLOR_PRINCIPAL, fg="white",
       font=("Arial", 11, "bold"), cursor="hand2", width=18).grid(row=4, column=0, columnspan=2, pady=25)


miFrame = Frame(root, bg="white", bd=5, relief="groove")

Label(miFrame, text="NUEVA VENTA", font=("Arial", 16, "bold"), bg=COLOR_PRINCIPAL, fg="white").grid(row=0, column=0, columnspan=10, sticky="we", pady=(0, 10), ipady=6)

Label(miFrame, text="Cajero:", bg="white", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="e", padx=10, pady=5)
Label(miFrame, textvariable=usuario_activo, bg="white", fg=COLOR_PRINCIPAL, font=("Arial", 10, "bold")).grid(row=1, column=1, columnspan=4, sticky="w")

Label(miFrame, text="Cliente:", bg="white", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky="e", padx=10, pady=5)
Entry(miFrame, textvariable=nombre_cliente, width=25).grid(row=2, column=1, columnspan=4, sticky="w")

Label(miFrame, text="Membresía:", bg="white", font=("Arial", 10, "bold")).grid(row=3, column=0, sticky="e", padx=10, pady=10)
Radiobutton(miFrame, text="Regular", variable=tipo_cliente, value=1, bg="white", command=calcular_total).grid(row=3, column=1, columnspan=2, sticky="w")
Radiobutton(miFrame, text="VIP (-10%)", variable=tipo_cliente, value=2, bg="white", command=calcular_total).grid(row=3, column=3, columnspan=2, sticky="w")

Label(miFrame, text="DULCES  (usa + y - para elegir cuántas piezas)", font=("Arial", 11, "bold"), bg=COLOR_SECCION, fg=COLOR_PRINCIPAL).grid(row=4, column=0, columnspan=10, sticky="we", pady=(10, 5))

contador = 0
for nombre, precio in PRODUCTOS.items():
    if contador < PRODUCTOS_POR_COLUMNA:
        fila = 5 + contador
        columna = 0
    else:
        fila = 5 + contador - PRODUCTOS_POR_COLUMNA
        columna = 5

    Label(miFrame, text=f"{nombre} (${precio})", bg="white", width=20, anchor="w").grid(row=fila, column=columna, sticky="w", padx=(10, 0), pady=2)

    Button(miFrame, text="-", width=2, command=lambda n=nombre: quitar_producto(n), bg=COLOR_SUAVE,
           font=("Arial", 9, "bold"), cursor="hand2").grid(row=fila, column=columna + 1)

    Label(miFrame, textvariable=vars_productos[nombre], width=3, bg="white", font=("Arial", 10, "bold")).grid(row=fila, column=columna + 2)

    botones_mas[nombre] = Button(miFrame, text="+", width=2, command=lambda n=nombre: agregar_producto(n), bg=COLOR_PRINCIPAL,
                                 fg="white", font=("Arial", 9, "bold"), cursor="hand2")
    botones_mas[nombre].grid(row=fila, column=columna + 3)

    labels_stock[nombre] = Label(miFrame, textvariable=vars_stock[nombre], bg="white", fg="gray", font=("Arial", 9), width=10, anchor="w")
    labels_stock[nombre].grid(row=fila, column=columna + 4, sticky="w", padx=(5, 10))
    contador += 1

fila = 5 + PRODUCTOS_POR_COLUMNA

Label(miFrame, text="Notas:", bg="white", font=("Arial", 10, "bold")).grid(row=fila, column=0, sticky="ne", padx=10, pady=10)
texto_notas = Text(miFrame, width=60, height=3)
texto_notas.grid(row=fila, column=1, columnspan=8, pady=10, sticky="w")

scroll = Scrollbar(miFrame, command=texto_notas.yview)
scroll.grid(row=fila, column=9, sticky="nsw", pady=10)
texto_notas.config(yscrollcommand=scroll.set)
fila += 1

Label(miFrame, textvariable=subtotal_venta, font=("Arial", 11), bg="white").grid(row=fila, column=1, columnspan=4, sticky="w")
Label(miFrame, text="Paga con: $", font=("Arial", 11, "bold"), bg="white").grid(row=fila, column=5, sticky="e")
Entry(miFrame, textvariable=pago_cliente, width=10, font=("Arial", 11)).grid(row=fila, column=6, columnspan=2, sticky="w")
fila += 1

Label(miFrame, textvariable=descuento_venta, font=("Arial", 11), fg="#2e7d32", bg="white").grid(row=fila, column=1, columnspan=4, sticky="w")
Button(miFrame, text="Calcular cambio", command=calcular_cambio, bg=COLOR_SUAVE, font=("Arial", 9, "bold"),
       cursor="hand2").grid(row=fila, column=5, columnspan=3, sticky="w", pady=3)
fila += 1

Label(miFrame, textvariable=iva_venta, font=("Arial", 11), bg="white").grid(row=fila, column=1, columnspan=4, sticky="w")
Label(miFrame, textvariable=cambio_venta, font=("Arial", 12, "bold"), fg=COLOR_PRINCIPAL, bg="white").grid(row=fila, column=5, columnspan=5, sticky="w")
fila += 1

Label(miFrame, textvariable=total_venta, font=("Arial", 15, "bold"), fg=COLOR_PRINCIPAL, bg="white").grid(row=fila, column=1, columnspan=4, pady=8, sticky="w")
fila += 1

Button(miFrame, text="Confirmar y Guardar Venta", command=confirmar_venta, bg=COLOR_PRINCIPAL, fg="white",
       font=("Arial", 10, "bold"), cursor="hand2").grid(row=fila, column=1, columnspan=4, sticky="w", pady=10)
Button(miFrame, text="Limpiar", command=limpiar_venta, bg=COLOR_SUAVE, fg="white",
       font=("Arial", 10, "bold"), cursor="hand2").grid(row=fila, column=5, columnspan=3, sticky="w", pady=10)

panelTicket = Frame(root, bg="white", bd=5, relief="groove")

Label(panelTicket, text="TICKET", font=("Arial", 16, "bold"), bg=COLOR_PRINCIPAL, fg="white").grid(row=0, column=0, sticky="we", ipady=6)
Label(panelTicket, textvariable=ticket_texto, font=("Courier", 10), bg="white", justify="left").grid(row=1, column=0, padx=10, pady=10, sticky="n")

actualizar_inventario()
root.mainloop()