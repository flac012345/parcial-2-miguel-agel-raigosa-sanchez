import tkinter as tk
from tkinter import messagebox

def verificar_division(num):
    """Lanza una excepción si el número es cero."""
    if num == 0:
        raise ZeroDivisionError("El divisor no puede ser cero.")

def realizar_operacion(operacion):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = ""

        if operacion == "suma":
            resultado = num1 + num2
        elif operacion == "resta":
            resultado = num1 - num2
        elif operacion == "multiplicacion":
            resultado = num1 * num2
        elif operacion == "division":
            verificar_division(num2)  # Verifica división por cero
            resultado = num1 / num2
        elif operacion == "potencia":
            verificar_division(num2)  # Verifica antes de calcular potencia
            resultado = num1 ** num2

        label_resultado.config(text="Resultado: " + str(resultado))

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
    except ZeroDivisionError as e:
        messagebox.showerror("Error", str(e))

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Calculadora")

label_num1 = tk.Label(root, text="Número 1:")
label_num1.grid(row=0, column=0)

entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1)

label_num2 = tk.Label(root, text="Número 2:")
label_num2.grid(row=1, column=0)

entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1)

label_resultado = tk.Label(root, text="Resultado: ")
label_resultado.grid(row=2, column=0, columnspan=2)

button_suma = tk.Button(root, text="Suma", command=lambda: realizar_operacion("suma"))
button_suma.grid(row=3, column=0)

button_resta = tk.Button(root, text="Resta", command=lambda: realizar_operacion("resta"))
button_resta.grid(row=3, column=1)

button_mult = tk.Button(root, text="Multiplicación", command=lambda: realizar_operacion("multiplicacion"))
button_mult.grid(row=4, column=0)

button_div = tk.Button(root, text="División", command=lambda: realizar_operacion("division"))
button_div.grid(row=4, column=1)

button_pot = tk.Button(root, text="Potencia", command=lambda: realizar_operacion("potencia"))
button_pot.grid(row=5, column=0, columnspan=2)

root.mainloop()
