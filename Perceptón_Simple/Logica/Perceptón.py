# Librerias
import matplotlib.pyplot as plt
import math

class Perceptron (object):
        
    # Funciones de activación
    # Funcion hardlims
    def hardlims(value):
        if value >= 0:
            return 1
        return -1
    # Funcion tanh
    def tanh(value):
        return (2/(1 + math.exp(-2*value))-1)
    # Función sigmoide
    def sigmoid(x):
        return 1 / (1 + math.exp(-x))
    
    '''
    Funcion de entrenamiento

    Datos que recibe
    inputs = lista de entrada de entrenamiento
    outputs = lista de salidas de entrenamiento
    weights = lista pesos aleatorios (se escogen de forma aleatoria)
    bia = Valor del umbral (se escogen de forma aleatoria)
    activation: representa la funcion de activación
    inter = interaciones permitidas de entrenamiento
    '''
    def training(inputs: list[list], outputs: list, weights: list, bias: float, activation, epochs: int, learning_rate: float):
        count: int = 0
        current_error: float = 999
        errors: list = [0]

        while count < epochs and current_error > 0.01:
            current_error = 0
            for i, e in enumerate(inputs):
                output = activation(sum(weights[j] * e[j] for j in range(len(weights))) + bias)
                error = outputs[i] - output
                current_error += error ** 2
                for j in range(len(weights)):
                    weights[j] += e[j] * error * learning_rate
                bias += error * learning_rate
            
            errors[count] = (current_error / len(inputs)) ** 0.5
            errors.append(0)
            count += 1
        
        return weights, bias, errors[:len(errors) - 1]
    # Funcion de predictions
    def prediction(weights: list, bias: float, activation, inputs: list):
        z: float = bias
        for i in range(len(inputs)):
            z += inputs[i] * weights[i]
        return activation(z)
    
    # Funcion para graficar el error durante el entrenamiento
    def graphError(errors_G):
        plt.figure(figsize=(10, 5))
        plt.plot(errors_G, label='Error')
        plt.title('Evolución del Error durante el Entrenamiento')
        plt.xlabel('Interaciones')
        plt.ylabel('Error')
        plt.legend()
        plt.grid(True)
        plt.show()