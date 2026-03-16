import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QDialog, QLineEdit,
    QComboBox, QListWidget, QAbstractItemView,
    QListWidgetItem, QTextEdit, QFormLayout)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

# Funcion que crea fuente


def fuente_l(tipo, tama, bolt=False):
    f = QFont(tipo)
    f.setPointSize(tama)
    f.setBold(bolt)
    return f


def crear_lista_checkbox(lista_elementos):
    lista = QListWidget()
    for elemento in lista_elementos:
        item = QListWidgetItem(elemento)
        item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
        item.setCheckState(Qt.Unchecked)
        lista.addItem(item)
    return lista


class PrimeraPantalla(QWidget):

    def __init__(self, cambiar_pantalla):
        super().__init__()

        layout = QVBoxLayout()
        # Fuente
        fuente = fuente_l("Agency FB", 60)

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

# Clase para cada boton


class Agrega_idea(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AGREGANDO IDEA")
        layout = QVBoxLayout()

        form = QFormLayout()

        bot_hor = QHBoxLayout()

        self.line_tit = QLineEdit()
        self.text_des = QTextEdit()
        self.text_des.setMinimumHeight(100)
        self.text_des.setMinimumWidth(500)

        self.list_tag = crear_lista_checkbox(["ingenieria", "software", "arte",
                                              "investigacion", "personal", "educacion"])
        self.box_est = QComboBox()

        self.box_est.addItems(["Activo", "Archivado", "Terminado"])

        form.addRow("Título:", self.line_tit)
        form.addRow("Descripción:", self.text_des)
        form.addRow("Tags:", self.list_tag)
        form.addRow("Estado:", self.box_est)

        layout.addLayout(form)

        self.Guardar = QPushButton("GUARDAR")
        self.Cancelar = QPushButton("CANCELAR")

        self.Guardar.clicked.connect(self.obtener_info)
        self.Cancelar.clicked.connect(self.cerrar)

        bot_hor.addWidget(self.Guardar)
        bot_hor.addWidget(self.Cancelar)
        layout.addLayout(bot_hor)

        self.setLayout(layout)

    def obtener_info(self):
        tags = []
        for i in range(self.list_tag.count()):
            item = self.list_tag.item(i)
            if item.checkState() == Qt.Checked:
                tags.append(item.text())

        self.datos = {
            "titulo": self.line_tit.text(),
            "descripcion": self.text_des.toPlainText(),
            "tags": tags,
            "estado": self.box_est.currentText()
        }
        print(self.datos)

        self.accept()

    def cerrar(self):
        self.close()


class Editar_idea(QDialog):
    def __init__(self, la_idea):
        super().__init__()
        self.setWindowTitle("EDITANDO IDEA")
        layout = QVBoxLayout()

        form = QFormLayout()

        bot_hor = QHBoxLayout()

        self.line_tit = QLineEdit(la_idea["titulo"])
        self.text_des = QTextEdit(la_idea["descripcion"])
        self.text_des.setMinimumHeight(100)
        self.text_des.setMinimumWidth(500)

        self.list_tag = crear_lista_checkbox(["ingenieria", "software", "arte",
                                              "investigacion", "personal", "educacion"])
        self.box_est = QComboBox()

        self.box_est.addItems(["Activo", "Archivado", "Terminado"])

        form.addRow("Título:", self.line_tit)
        form.addRow("Descripción:", self.text_des)
        form.addRow("Tags:", self.list_tag)
        form.addRow("Estado:", self.box_est)

        layout.addLayout(form)

        self.Guardar = QPushButton("GUARDAR")
        self.Cancelar = QPushButton("CANCELAR")

        self.Guardar.clicked.connect(self.obtener_info)
        self.Cancelar.clicked.connect(self.cerrar)

        bot_hor.addWidget(self.Guardar)
        bot_hor.addWidget(self.Cancelar)
        layout.addLayout(bot_hor)

        self.setLayout(layout)

    def obtener_info(self):
        tags = []
        for i in range(self.list_tag.count()):
            item = self.list_tag.item(i)
            if item.checkState() == Qt.Checked:
                tags.append(item.text())

        self.datos = {
            "titulo": self.line_tit.text(),
            "descripcion": self.text_des.toPlainText(),
            "tags": tags,
            "estado": self.box_est.currentText()
        }
        print(self.datos)

        self.accept()

    def cerrar(self):
        self.close()


class PantallaIdeas(QWidget):

    # , agrega_idea, editar_idea, borrar_idea, filtar_idea, atras):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout_botones = QHBoxLayout()

        texto = QLabel("IDEAS Y PROYECTOS")
        texto.setAlignment(Qt.AlignCenter)

        # Botones
        self.Agregar = QPushButton("AGREGAR")
        self.Editar = QPushButton("EDITAR")
        self.Borrar = QPushButton("BORRAR")
        self.Filtar = QPushButton("FILTRAR")
        self.Atras = QPushButton("ATRAS")

        self.Agregar.clicked.connect(self.abrir_agregar)
        self.Editar.clicked.connect(self.abrir_editar)

        layout.addWidget(texto)
        layout_botones.addWidget(self.Agregar)
        layout_botones.addWidget(self.Editar)
        layout_botones.addWidget(self.Borrar)
        layout_botones.addWidget(self.Filtar)
        layout_botones.addWidget(self.Atras)
        layout.addLayout(layout_botones)

        self.setLayout(layout)

    def abrir_agregar(self):
        self.ventana = Agrega_idea()
        self.ventana.show()

    def abrir_editar(self):
        self.ven = Editar_idea({'titulo': 'llorar', 'descripcion': 'correr', 'tags': [
                               'arte', 'personal'], 'estado': 'Activo'})
        self.ven.show()


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("ADA 0.0v")

        self.base_width = 800

        # Primera pantalla
        self.pantalla1 = PrimeraPantalla(self.cambiar_pantalla)
        self.setCentralWidget(self.pantalla1)

        self.resize(800, 600)

    def cambiar_pantalla(self):

        self.pantalla2 = PantallaIdeas()
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
