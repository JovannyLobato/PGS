import tkinter as tk
from tkinter import messagebox
from database import Database

def verificar_usuario():
    id_huella = entry_id.get()
    if not id_huella:
        messagebox.showwarning("Campo vacío", "Por favor, introduce un ID de huella.")
        return

    db = Database()
    query = "SELECT * FROM usuarios WHERE id_huella = %s"
    resultado = db.ejecutar_query(query, (id_huella,))
    db.cerrar_conexion()

    if resultado:
        usuario = resultado[0]
        nombre = f"{usuario['nombre']} {usuario['apellido']}"
        messagebox.showinfo("Acceso concedido", f"¡Bienvenido, {nombre}!")
    else:
        messagebox.showerror("Acceso denegado", "Huella no registrada.")

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Login - Registro Huella")
ventana.geometry("300x180")

tk.Label(ventana, text="ID de Huella:").pack(pady=10)
entry_id = tk.Entry(ventana)
entry_id.pack()

btn_verificar = tk.Button(ventana, text="Verificar", command=verificar_usuario)
btn_verificar.pack(pady=20)

ventana.mainloop()
