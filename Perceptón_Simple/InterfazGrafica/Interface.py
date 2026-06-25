import tkinter as tk
import random
from tkinter import messagebox
from Logica import Perceptón as p

class Perceptron:
    def __init__(self, interfaz):
        self.interface = interfaz

    def update_entry(self, entry_widget, value, x):
        entry_widget.config(state='normal')
        entry_widget.delete(x, tk.END)
        entry_widget.insert(tk.END, value)
        entry_widget.config(state='disabled')

    def data_pigeon(self, pattern):
        inputs = [
        [1,   1,  1],
        [1,   1, -1],
        [1,  -1,  1],
        [1,  -1, -1],
        [-1,  1,  1],
        [-1,  1, -1],
        [-1, -1,  1],
        [-1, -1, -1]
        ]

        outputs = [1, 1, 1, 1, 1, 1, -1, 1]

        w_c1 = [random.random() for _ in range(len(inputs[0]))]
        bia_c1 = random.random()
        inter_max = 100 #Este depende del problema y es aleatorio

        waux_c1 = list(w_c1)
        bias_aux = bia_c1

        w_c1, bia_c1, error_c1 = p.Perceptron.training(inputs, outputs, w_c1, bia_c1, p.Perceptron.hardlims, inter_max, 0.1)
        # Entradas del sistema
        self.update_entry(self.interface.info_input, pattern, 0)
        # Epocas del sistema 
        self.update_entry(self.interface.info_ep, len(error_c1), 0)

        try:
            print(pattern)
            prediccion = p.Perceptron.prediction(w_c1, bia_c1, p.Perceptron.hardlims, pattern)
            print(f"resultado:{prediccion}")
            
            resultado = "La paloma come." if prediccion > 0 else "La paloma no come."
            self.update_entry(self.interface.info_result, resultado, 0) # Resultado de la prediccion del sistema
            self.update_entry(self.interface.info_output, prediccion, 0) #Prediccion del sistema

        except Exception as e:
            messagebox.showerror("Ocurrió un error", str(e))
        
        # Valores iniciales area de texto
        info_Vi = f"Pesos:\n{waux_c1}\nBias:\n{bias_aux}"
        info_Vf = f"Pesos:\n{w_c1}\nBias:\n{bia_c1}\nErrores:\n{error_c1}\n"
        self.update_entry(self.interface.text_area1, info_Vi, 1.0)
        self.update_entry(self.interface.text_area2, info_Vf, 1.0)

        p.Perceptron.graphError(error_c1)
        print({'w_inicial': waux_c1, 'bias_inicial': bias_aux})
        print({'w_final': w_c1, 'bias_final': bia_c1, 'epocas': len(error_c1), '\nerrors_c1': error_c1})
    
    def data_disease(self, pattern):
        inputs = [
        [1, 1, 1],
        [1, 1, -1],
        [1, -1, 1],
        [1, -1, -1],
        [-1, 1, 1],
        [-1, 1, -1],
        [-1, -1, 1],
        [-1, -1, -1],
        ]

        outputs = [1, 1, 1, -1, 1, -1, -1, -1]

        w_c2 = [random.random() for _ in range(len(inputs[0]))]
        bia_c2 = random.random()
        inter_max = 100 #Este depende del problema y es aleatorio

        # Guardar datos originales
        waux_c2 = list(w_c2)
        biac2_aux = bia_c2

        w_c2, bia_c2, error_c2 = p.Perceptron.training(inputs, outputs, w_c2, bia_c2, p.Perceptron.hardlims, inter_max, 1)
        # Entradas del sistema
        self.update_entry(self.interface.info_input, pattern, 0)
        # Epocas del sistema 
        self.update_entry(self.interface.info_ep, len(error_c2), 0)

        try:
            print(pattern)
            prediccion = p.Perceptron.prediction(w_c2, bia_c2, p.Perceptron.hardlims, pattern)
            print(f"resultado:{prediccion}")
            
            resultado = "El paciente tiene la enfermedad." if prediccion > 0 else "El paciente no tiene la enfermedad."
            self.update_entry(self.interface.info_result, resultado, 0) # Resultado de la prediccion del sistema
            self.update_entry(self.interface.info_output, prediccion, 0) #Prediccion del sistema

        except Exception as e:
           messagebox.showerror("Ocurrió un error", str(e))
        
        # Valores iniciales area de texto
        info_Vi = f"Pesos:\n{waux_c2}\nBias:\n{biac2_aux}"
        info_Vf = f"Pesos:\n{w_c2}\nBias:\n{bia_c2}\nErrores:\n{error_c2}\n"
        self.update_entry(self.interface.text_area1, info_Vi, 1.0)
        self.update_entry(self.interface.text_area2, info_Vf, 1.0)

        p.Perceptron.graphError(error_c2)

class interface:
    def __init__(self, root):
            self.root = root
            self.root.geometry("500x450")
            root.resizable(False, False)
            self.root.title("Perceptón Simple")

            self.lbt1 = tk.Label(text="Ingrese el patron")
            # Esta encendido o no el pulsador de la izquierda
            self.lbx1 = tk.Label(text='X1')
            self.lbx1.place(x=30, y=40)
            self.entx1 = tk.Entry(root)
            self.entx1.place(x=65, y=40, width=30, height=20)

            # Esta encendido o no el pulsador de la derecha
            self.lbx2 = tk.Label( text='X2')
            self.lbx2.place(x=120, y=40)
            self.entx2 = tk.Entry(root)
            self.entx2.place(x=150, y=40, width=30, height=20)

            # En qué pulsador pico la paloma
            self.lbx3 = tk.Label(root, text='X3')
            self.lbx3.place(x=210, y=40)
            self.entx3 = tk.Entry(root)
            self.entx3.place(x=250, y=40, width=30, height=20)

            # PAsando el objeto de self
            self.Perceptron = Perceptron(self)

            #Button para aplicar el caso #1 de la paloma
            self.btn1 = tk.Button(root, text="Paloma", command=lambda: self.procesar("Paloma"))
            self.btn1.place(x=290, y=40, width=80, height=20)

            #Button para evaluar el caso #2 de la enfermedad
            self.btn2 = tk.Button(root, text="Enfermedad", command=lambda: self.procesar("Enfermedad"))
            self.btn2.place(x=380, y=40, width=80, height=20)

            # Label de entradas 
            self.lbinput = tk.Label(root, text='Entradas:')
            self.lbinput.place(x=30, y=80)

            self.info_input = tk.Entry(root)
            self.info_input.insert(0, " ")
            self.info_input.config(state='readonly')  # Deshabilitar para que sea de solo lectura
            self.info_input.place(x=85, y=80, width=150, height=25)

            # Label de salidas
            self.lboutput = tk.Label(root, text='Salida:')
            self.lboutput.place(x=250, y=80)

            self.info_output = tk.Entry(root)
            self.info_output.insert(0, " ")
            self.info_output.config(state='readonly')
            self.info_output.place(x=310, y=80, width=150, height=25)

            # Conclusion del resultado
            self.lbresult = tk.Label(root, text='Resultado:')
            self.lbresult.place(x=30, y=120)

            self.info_result = tk.Entry(root)
            self.info_result.insert(0, " ")
            self.info_result.config(state='readonly') 
            self.info_result.place(x=95, y=120, width=220, height=25)

            #Numero de iteraciones realizadas -> Epocas
            self.lbep = tk.Label(root, text='Epocas:')
            self.lbep.place(x=350, y=120)

            self.info_ep = tk.Entry(root)
            self.info_ep.insert(0, " ")
            self.info_ep.config(state='readonly') 
            self.info_ep.place(x=410, y=120, width=50, height=25)

            # Valores iniciales de los casos pesoss y bias
            self.lbvi = tk.Label(root, text='Valores iniciales:')
            self.lbvi.place(x=30, y=170)

            self.text_area1 = tk.Text(root, height=10, width=40)
            self.text_area1.place(x=30, y=190, width=430, height=100)

            # Valores ifinales de los casos pesoss y bias
            self.lbvf = tk.Label(root, text='Valores finales:')
            self.lbvf.place(x=30, y=295)

            self.text_area2 = tk.Text(root, height=10, width=40)
            self.text_area2.place(x=30, y=320, width=430, height=100)
    def procesar(self, action):
        pattern = []

        try:
            # Obtener los valores de entrada desde los Entry y convertirlos a enteros
            x1 = int(self.entx1.get())
            x2 = int(self.entx2.get())
            x3 = int(self.entx3.get())
            
            # Guardar los valores en una lista
            pattern = [x1, x2, x3]
            
            if not all(-1 <= x <= 1 for x in (x1, x2, x3)):
                raise ValueError("Alguna de las entradas está fuera del rango permitido (-1 a 1).")
            # Realizar la acción según el valor de "action"
            if action == "Paloma":
                self.Perceptron.data_pigeon(pattern)
            elif action == "Enfermedad":
                self.Perceptron.data_disease(pattern)

        except ValueError as e:
            # Mostrar un mensaje de error si las entradas no son válidas
            messagebox.showerror("Error de entrada", str(e))


    def limpiar(self):
         self.entx1.delete(0, tk.END)
         self.entx2.delete(0, tk.END)
         self.entx3.delete(0, tk.END)
         self.info_result.delete(0, tk.END) #lUEGO DE CONECTAR VERIFICAR QUE FUNCIONE

class Main:
    def __init__(self):
        self.root = tk.Tk()
        self.app = interface(self.root)

    def run(self):
        self.root.mainloop()