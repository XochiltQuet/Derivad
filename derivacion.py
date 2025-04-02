import re
from sympy import sympify, symbols, diff, sin, cos, tan
from PySide6.QtWidgets import QMessageBox 

x = symbols('x')

def funcion_a_lambda(func_str):
    try:
        func_str = func_str.lower().replace("sen", "sin").replace("coseno", "cos").replace("tangente", "tan")
        func_str = func_str.replace("^", "**").replace(" ", "")
        func_str = re.sub(r"(\d)([a-zA-Z])", r"\1*\2", func_str)
        expr = sympify(func_str)
        func = lambda x_val: float(expr.subs(x, x_val))
        return func
    except Exception as e:
        QMessageBox.critical(None, "Error de Sintaxis", f"La función no es válida. Error: {e}")
        return None

def derivada_exacta(func_str):
    try:
        expr = sympify(func_str, evaluate=False)
        return diff(expr, x)
    except Exception as e:
        print(f"Error al calcular la derivada exacta: {e}")
        return None

def evaluar_derivada_exacta(func_str, x_val):
    try:
        derivada = derivada_exacta(func_str)
        return float(derivada.subs(x, x_val)) if derivada else None
    except Exception as e:
        print(f"Error al evaluar la derivada exacta: {e}")
        return None

def derivada_progresiva(f, x_val, h):
    return (f(x_val + h) - f(x_val)) / h

def derivada_regresiva(f, x_val, h):
    return (f(x_val) - f(x_val - h)) / h

def derivada_central(f, x_val, h):
    return (f(x_val + h) - f(x_val - h)) / (2 * h)