import Interfaz as intfz
import Mod_Idea as mod
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QTableWidgetItem, QDialog, QLineEdit,
    QComboBox, QListWidget, QAbstractItemView,
    QListWidgetItem, QTextEdit, QFormLayout)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
import datos as d

# Funcion que crea fuente


class PrimeraPantalla(QWidget):

    def __init__(self, cambiar_pantalla):
        super().__init__()

        layout = QVBoxLayout()
        # Fuente
        fuente = intfz.fuente_l("Agency FB", 60)

        # Texto superior
        self.titulo = QLabel("PROYECTO ADA 0.0")
        # self.titulo.fond
        self.titulo.setAlignment(Qt.AlignCenter)
        self.titulo.setFont(fuente)

        # Botón
        self.boton = QPushButton("IDEAS Y PROYECTOS")
        self.boton.clicked.connect(cambiar_pantalla)

        layout.addWidget(self.titulo)
        layout.addWidget(self.boton)

        self.setLayout(layout)


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("ADA 0.0v")

        self.base_width = 800

        # Primera pantalla
        self.pantalla1 = PrimeraPantalla(self.cambiar_pantalla)
        self.setCentralWidget(self.pantalla1)

        self.resize(800, 600)

    def volver_inicio(self):
        self.pantalla1 = PrimeraPantalla(self.cambiar_pantalla)
        self.setCentralWidget(self.pantalla1)

    def cambiar_pantalla(self):

        self.pantalla2 = mod.PantallaIdeas(self.volver_inicio)
        self.setCentralWidget(self.pantalla2)

    # Mantener proporción 4:3
    def resizeEvent(self, event):

        width = self.width()
        height = int(width * 9 / 16)

        if height != self.height():
            self.resize(width, height)

        super().resizeEvent(event)


app = QApplication(sys.argv)

ventana = VentanaPrincipal()
ventana.show()

sys.exit(app.exec())
