# Perceptón Simple

> Proyecto educativo que implementa un perceptrón simple con una interfaz gráfica en Tkinter.

## Descripción

Este proyecto muestra un perceptrón entrenado en dos conjuntos de ejemplo (paloma y enfermedad).
La aplicación permite ingresar un patrón de 3 entradas (-1 o 1) y evaluar la predicción.

## Estructura

- `main.py` — Punto de entrada que inicia la interfaz gráfica.
- `InterfazGrafica/Interface.py` — Implementación de la GUI con Tkinter y lógica de interacción.
- `Logica/Perceptón.py` — Clase `Perceptron` que contiene funciones de activación, entrenamiento y predicción.
- `Librerias-Intalar.txt` — Instrucciones rápidas de instalación de dependencias.

## Requisitos

- Python 3.8+
- `matplotlib` (para graficar la evolución del error durante el entrenamiento)

Instalar la dependencia:

```bash
pip install matplotlib
```

## Uso

Ejecutar la aplicación desde la carpeta del proyecto:

```bash
cd Perceptón_Simple
python main.py
```

Ingrese cada valor de entrada (`-1` o `1`) en los campos X1, X2 y X3 y pulse **Paloma** o **Enfermedad** para entrenar y predecir con el perceptrón.

## Notas

- Los pesos y bias se inicializan de forma aleatoria cada vez que se ejecuta la predicción.
- El entrenamiento usa una regla de actualización simple con learning rate configurable en el código.
