from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                              QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, 
                              QMessageBox)
from PySide6.QtGui import QColor
from derivacion import funcion_a_lambda, evaluar_derivada_exacta, derivada_progresiva, derivada_regresiva, derivada_central
from plotter import graficar_derivadas

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora de Derivación Numérica")
        self.setGeometry(100, 100, 500, 400)
        layout = QVBoxLayout()
        layout_entrada = QHBoxLayout()

        self.label_funcion = QLabel("Función f(x):")
        self.entry_funcion = QLineEdit()
        self.label_x = QLabel("x:")
        self.entry_x = QLineEdit()
        self.label_h = QLabel("h:")
        self.entry_h = QLineEdit()
        self.btn_calcular = QPushButton("Calcular")
        self.btn_calcular.clicked.connect(self.calcular_derivadas)

        layout_entrada.addWidget(self.label_funcion)
        layout_entrada.addWidget(self.entry_funcion)
        layout_entrada.addWidget(self.label_x)
        layout_entrada.addWidget(self.entry_x)
        layout_entrada.addWidget(self.label_h)
        layout_entrada.addWidget(self.entry_h)
        layout_entrada.addWidget(self.btn_calcular)
        layout.addLayout(layout_entrada)

        self.tabla_resultados = QTableWidget(4, 6)
        self.tabla_resultados.setHorizontalHeaderLabels(["Método", "f(x+h)", "f(x)", "f(x-h)", "Resultado", "Error"])
        layout.addWidget(self.tabla_resultados)

        self.setLayout(layout)

    def colorear_celda(self, fila, columna, valor):
        item = QTableWidgetItem(f"{valor:.2f}" if valor is not None else "")
        if valor is not None:
            colores = [QColor(255, 102, 102), QColor(102, 178, 255), QColor(102, 255, 102), QColor(255, 255, 102)]
            item.setBackground(colores[fila])
        self.tabla_resultados.setItem(fila, columna, item)

    def calcular_derivadas(self):
        try:
            func_str = self.entry_funcion.text()
            f = funcion_a_lambda(func_str)
            if f is None:
                return

            x_val = float(self.entry_x.text())
            h_val = float(self.entry_h.text())

            f_x_menos_h = f(x_val - h_val)
            f_x = f(x_val)
            f_x_h = f(x_val + h_val)

            dp = derivada_progresiva(f, x_val, h_val)
            dr = derivada_regresiva(f, x_val, h_val)
            dc = derivada_central(f, x_val, h_val)
            exacta = evaluar_derivada_exacta(func_str, x_val)

            error_progresiva = abs(dp - exacta) if exacta is not None else None
            error_regresiva = abs(dr - exacta) if exacta is not None else None
            error_centrada = abs(dc - exacta) if exacta is not None else None

            datos = [
                ("Progresiva", f_x_h, f_x, "N/A", dp, error_progresiva),
                ("Regresiva", "N/A", f_x, f_x_menos_h, dr, error_regresiva),
                ("Centrada", f_x_h, f_x, f_x_menos_h, dc, error_centrada),
                ("Exacta", "-", "-", "-", exacta, "")
            ]

            for fila, (metodo, fx_h, fx, fx_mh, resultado, error) in enumerate(datos):
                self.tabla_resultados.setItem(fila, 0, QTableWidgetItem(metodo))
                self.tabla_resultados.setItem(fila, 1, QTableWidgetItem(f"{fx_h:.3f}" if isinstance(fx_h, float) else fx_h))
                self.tabla_resultados.setItem(fila, 2, QTableWidgetItem(f"{fx:.3f}" if isinstance(fx, float) else fx))
                self.tabla_resultados.setItem(fila, 3, QTableWidgetItem(f"{fx_mh:.3f}" if isinstance(fx_mh, float) else fx_mh))
                self.colorear_celda(fila, 4, resultado)
                self.tabla_resultados.setItem(fila, 5, QTableWidgetItem(f"{error:.2f}" if isinstance(error, float) else ""))

            graficar_derivadas(func_str, f, x_val, h_val)

        except ValueError:
            QMessageBox.critical(None, "Error", "Ingresa valores numéricos válidos para x y h.")
        except Exception:
            QMessageBox.critical(None, "Error", "Ingresa una función válida.")