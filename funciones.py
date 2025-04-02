import re
from sympy import sympify, symbols, diff
from sympy.functions import sin, cos, tan

x = symbols('x')

def funcion_a_lambda(func_str):
    try:
        func_str = func_str.lower().replace("sen", "sin").replace("coseno", "cos").replace("tangente", "tan")
        func_str = func_str.replace("^", "").replace(" ", "")
        func_str = re.sub(r"(\d)([a-zA-Z])", r"\1*\2", func_str)
        expr = sympify(func_str)
        return lambda x_val: float(expr.subs(x, x_val))
    except Exception as e:
        raise ValueError(f"La función no es válida. Error: {e}")

def derivada_exacta(func_str):
    try:
        expr = sympify(func_str, evaluate=False)
        return diff(expr, x)
    except Exception as e:
        raise ValueError(f"Error al calcular la derivada exacta: {e}")

def evaluar_derivada_exacta(func_str, x_val):
    try:
        derivada = derivada_exacta(func_str)
        return float(derivada.subs(x, x_val)) if derivada else None
    except Exception as e:
        raise ValueError(f"Error al evaluar la derivada exacta: {e}")