import numpy as np
import matplotlib.pyplot as plt
from derivacion import derivada_progresiva, derivada_regresiva, derivada_central, evaluar_derivada_exacta

def graficar_derivadas(func_str, f, x_val, h_val):
    x_vals = np.linspace(x_val - 2 * h_val, x_val + 2 * h_val, 100)
    y_vals = [f(x) for x in x_vals]
    
    dp = derivada_progresiva(f, x_val, h_val)
    dr = derivada_regresiva(f, x_val, h_val)
    dc = derivada_central(f, x_val, h_val)
    exacta = evaluar_derivada_exacta(func_str, x_val)

    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, label="f(x)", color="blue", linewidth=2)
    plt.scatter([x_val], [f(x_val)], color="red", label="Punto evaluado", zorder=5)

    plt.scatter(x_val + h_val, dp, color="green", s=100, label="Progresiva", zorder=7, marker="x", edgecolors="black")
    plt.scatter(x_val - h_val, dr, color="orange", s=100, label="Regresiva", zorder=7, marker="x", edgecolors="black")
    plt.scatter(x_val, dc, color="purple", s=100, label="Centrada", zorder=7, marker="x", edgecolors="black")
    
    plt.text(x_val + h_val, dp, f"({x_val + h_val:.2f}, {dp:.2f})", color="green", fontsize=12, ha='left', va='bottom')
    plt.text(x_val - h_val, dr, f"({x_val - h_val:.2f}, {dr:.2f})", color="orange", fontsize=12, ha='right', va='bottom')
    plt.text(x_val, dc, f"({x_val:.2f}, {dc:.2f})", color="purple", fontsize=12, ha='center', va='bottom')

    plt.scatter([x_val], [exacta], color="black", label="Exacta", zorder=6, marker="o")

    plt.legend()
    plt.xlabel("x")
    plt.ylabel("f(x) / Derivadas")
    plt.title("Comparación de Derivadas Numéricas")
    plt.grid(True)
    plt.show()