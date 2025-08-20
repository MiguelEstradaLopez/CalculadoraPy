import tkinter as tk
from tkinter import messagebox, simpledialog
from Operaciones import suma, resta, multiplicacion, division, potencia, comparar, mcd, mcm
from Colaboradores import Creador, Colaborador

class CalculadoraApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Dark")
        master.geometry("500x650") 
        master.resizable(False, False)
        master.configure(bg="#1a1a1a") 
        self.expression = ""
        self.input_text = tk.StringVar()

        self.gothic_font_display = ('Consolas', 28, 'bold')
        self.gothic_font_buttons = ('Consolas', 18)
        self.gothic_font_info = ('Consolas', 12)

        # Display para la entrada y resultados
        self.input_field = tk.Entry(master, textvariable=self.input_text, font=self.gothic_font_display,
                                    bd=10, insertwidth=4, width=16, borderwidth=4, relief="sunken",
                                    justify='right', bg="#0f0f0f", fg="#00ff00") # Verde neón para el texto
        self.input_field.grid(row=0, column=0, columnspan=4, padx=15, pady=15)
        self.input_field.focus_set()

        # Definir el layout de los botones
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        # Botones de operaciones especiales
        special_buttons = [
            ('Potencia', self.power_operation),
            ('Comparar', self.compare_operation),
            ('MCD', self.mcd_operation),
            ('MCM', self.mcm_operation),
            ('C', self.clear_input),
            ('AC', self.clear_all)
        ]

        row_val = 1
        col_val = 0

        # Crear botones numéricos y de operaciones básicas
        for button in buttons:
            if button == '=':
                tk.Button(master, text=button, font=self.gothic_font_buttons, bg="#6a0505", fg="#ffffff", # Rojo oscuro para igual
                          command=self.evaluate_expression, height=2, width=6, bd=3, relief="raised") \
                          .grid(row=row_val, column=col_val, pady=7, padx=7, sticky="nsew")
            else:
                tk.Button(master, text=button, font=self.gothic_font_buttons, bg="#333333", fg="#00ff00", # Gris oscuro y verde neón
                          command=lambda b=button: self.button_click(b), height=2, width=6, bd=3, relief="raised") \
                          .grid(row=row_val, column=col_val, pady=7, padx=7, sticky="nsew")
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
        
        # Crear botones de operaciones especiales
        special_row_val = row_val
        special_col_val = 0
        for text, command in special_buttons:
            bg_color = "#8b0000" if text == 'C' or text == 'AC' else "#4d4d4d" # Rojo oscuro para borrar, gris medio para otros
            fg_color = "#ffffff" # Blanco para el texto
            tk.Button(master, text=text, font=self.gothic_font_buttons, bg=bg_color, fg=fg_color,
                      command=command, height=2, width=6, bd=3, relief="raised") \
                      .grid(row=special_row_val, column=special_col_val, pady=7, padx=7, sticky="nsew")
            special_col_val += 1
            if special_col_val > 3:
                special_col_val = 0
                special_row_val += 1

        # Ajustar pesos de columna y fila para responsividad
        for i in range(4):
            master.grid_columnconfigure(i, weight=1)
        for i in range(special_row_val + 1):
            master.grid_rowconfigure(i, weight=1)

        # Mostrar creadores y colaboradores
        self.info_label = tk.Label(master, text=f"Creadores: {Creador}\nColaboradores: {Colaborador}",
                                   font=self.gothic_font_info, bg="#1a1a1a", fg="#aaaaaa", # Gris claro para el texto de info
                                   justify='left', wraplength=400)
        self.info_label.grid(row=special_row_val + 1, column=0, columnspan=4, pady=10)

    def button_click(self, char):
        self.expression += str(char)
        self.input_text.set(self.expression)

    def clear_input(self):
        self.expression = self.expression[:-1]
        self.input_text.set(self.expression)

    def clear_all(self):
        self.expression = ""
        self.input_text.set("")

    def evaluate_expression(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except ZeroDivisionError:
            messagebox.showerror("Error", "¡No puedes dividir por la oscuridad (cero)!")
            self.expression = ""
            self.input_text.set("")
        except SyntaxError:
            messagebox.showerror("Error", "¡Expresión rúnica inválida!")
            self.expression = ""
            self.input_text.set("")
        except Exception as e:
            messagebox.showerror("Error", f"¡Un misterio ha ocurrido: {e}!")
            self.expression = ""
            self.input_text.set("")

    def power_operation(self):
        try:
            base_str = tk.simpledialog.askstring("Poder Gótico", "Ingrese la base mística:")
            if base_str is None: return
            base = float(base_str)

            exponent_str = tk.simpledialog.askstring("Poder Gótico", "Ingrese el exponente arcaico:")
            if exponent_str is None: return
            exponent = float(exponent_str)

            result = potencia(base, exponent)
            self.input_text.set(f"Poder({base}, {exponent}) = {result}")
            self.expression = str(result)
        except ValueError:
            messagebox.showerror("Error de entrada", "¡Entrada sombría inválida! Asegúrate de usar números.")
            self.expression = ""
            self.input_text.set("")

    def compare_operation(self):
        try:
            val1_str = tk.simpledialog.askstring("Duelo de Valores", "Ingrese el primer número espectral:")
            if val1_str is None: return
            val1 = float(val1_str)

            val2_str = tk.simpledialog.askstring("Duelo de Valores", "Ingrese el segundo número místico:")
            if val2_str is None: return
            val2 = float(val2_str)

            result = comparar(val1, val2)
            self.input_text.set(result)
            self.expression = ""
        except ValueError:
            messagebox.showerror("Error de entrada", "¡Entrada sombría inválida! Asegúrate de usar números.")
            self.expression = ""
            self.input_text.set("")

    def mcd_operation(self):
        try:
            val1_str = tk.simpledialog.askstring("Ritual del MCD", "Ingrese el primer número ancestral:")
            if val1_str is None: return
            val1 = float(val1_str)

            val2_str = tk.simpledialog.askstring("Ritual del MCD", "Ingrese el segundo número antiguo:")
            if val2_str is None: return
            val2 = float(val2_str)

            result = mcd(val1, val2)
            self.input_text.set(f"MCD({int(val1)}, {int(val2)}) = {result}")
            self.expression = ""
        except ValueError:
            messagebox.showerror("Error de entrada", "¡Entrada sombría inválida! Asegúrate de usar números enteros.")
            self.expression = ""
            self.input_text.set("")
        except Exception as e:
            messagebox.showerror("Error", f"¡Un misterio ha ocurrido: {e}!")
            self.expression = ""
            self.input_text.set("")

    def mcm_operation(self):
        try:
            val1_str = tk.simpledialog.askstring("Conjuro del MCM", "Ingrese el primer número arcano:")
            if val1_str is None: return
            val1 = float(val1_str)

            val2_str = tk.simpledialog.askstring("Conjuro del MCM", "Ingrese el segundo número secreto:")
            if val2_str is None: return
            val2 = float(val2_str)

            result = mcm(val1, val2)
            self.input_text.set(f"MCM({int(val1)}, {int(val2)}) = {result}")
            self.expression = ""
        except ValueError:
            messagebox.showerror("Error de entrada", "¡Entrada sombría inválida! Asegúrate de usar números enteros.")
            self.expression = ""
            self.input_text.set("")
        except Exception as e:
            messagebox.showerror("Error", f"¡Un misterio ha ocurrido: {e}!")
            self.expression = ""
            self.input_text.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.mainloop()