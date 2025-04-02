import sys
from PySide6.QtWidgets import QApplication
from ventana import Ventana

app = QApplication(sys.argv)
ventana = Ventana()
ventana.show()
sys.exit(app.exec())