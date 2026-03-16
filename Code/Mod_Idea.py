import Interfaz as intfz
import sys
from PySide6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QWidget,
    QPushButton, QDialog, QLabel, QLineEdit,
    QComboBox, QTextEdit, QFormLayout)
from PySide6.QtCore import Qt
import datos as d

# Datos globales
tags_posibles_v0 = ["ingenieria", "software", "arte", "investigacion",
                    "personal", "educacion"]
estados_ideasas = ["Activo", "Archivado", "Terminado"]
archivo_json = "files/ideas.json"
descrip_x = 500
descrip_y = 100

# Clases


class modifica_idea(QDialog):
    def __init__(self, tituloventana, tags_posibles=tags_posibles_v0,
                 estados=estados_ideasas, name=archivo_json, idea={}, indice=None, modo="agregar", callback=None):
        super().__init__()
        self.titvent = tituloventana
        self.tag_pos = tags_posibles
        self.ests = estados
        self.name = name
        self.idea = idea
        self.indice = indice
        self.callback = callback

        self.setWindowTitle(self.titvent)
        layout = QVBoxLayout()
        form = QFormLayout()
        bot_hor = QHBoxLayout()

        self.line_tit = intfz.crear_LineEdit(self.idea.get("titulo", None))
        self.text_des = intfz.crear_TextEdit(
            self.idea.get("descripcion", None))
        self.text_des.setMinimumHeight(descrip_y)
        self.text_des.setMinimumWidth(descrip_x)

        self.list_tag = intfz.crear_checklist()
        intfz.llenar_checklist(
            self.list_tag, self.tag_pos, self.idea.get("tags", None))
        self.date = QLabel(d.fecha_per(self.idea.get("fecha", None)))
        self.box_est = intfz.crear_combobox(
            self.ests, self.idea.get("estado", None))

        form.addRow("Título:", self.line_tit)
        form.addRow("Descripción:", self.text_des)
        form.addRow("Tags:", self.list_tag)
        form.addRow("Fecha:", self.date)
        form.addRow("Estado:", self.box_est)

        layout.addLayout(form)

        self.Guardar = QPushButton("GUARDAR")
        self.Cancelar = QPushButton("CANCELAR")

        if modo == "editar":
            self.Guardar.clicked.connect(self.editar_info)
        else:
            self.Guardar.clicked.connect(self.guardar_info)
        self.Cancelar.clicked.connect(self.cerrar)

        bot_hor.addWidget(self.Guardar)
        bot_hor.addWidget(self.Cancelar)
        layout.addLayout(bot_hor)

        self.setLayout(layout)

    def obtener_info(self):
        tags = intfz.obtener_checklist(self.list_tag)
        datos = d.idea(self.line_tit.text(), self.text_des.toPlainText(),
                       tags, d.fecha_act(), self.box_est.currentText(), self.indice)
        return datos

    def guardar_info(self):
        ruta = d.validar(self.name)
        d.anexar(ruta, self.obtener_info())
        self.callback()  # Ejecuta actualizar_tabla de la pantalla principal
        self.accept()

    def editar_info(self):
        ruta = d.validar(self.name)
        d.editar_dicci(ruta, self.indice, self.obtener_info())
        self.callback()  # Ejecuta actualizar_tabla de la pantalla principal
        self.accept()

    def cerrar(self):
        self.close()


class filtrar(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("FILTRAR")
        self.setFixedSize(400, 250)
        layout = QVBoxLayout(self)

        # --- FILA 1: Texto y Ámbito ---
        fila1 = QHBoxLayout()
        self.txt_busqueda = QLineEdit()
        self.txt_busqueda.setPlaceholderText("Palabra clave...")

        self.combo_ambito = QComboBox()
        self.combo_ambito.addItems(["Título", "Descripción", "Ambos"])

        fila1.addWidget(self.txt_busqueda)
        fila1.addWidget(self.combo_ambito)
        layout.addLayout(fila1)

        # --- FILA 2: Tags ---
        layout.addWidget(QLabel("Filtrar por Tag:"))
        self.combo_tags = QComboBox()
        # "Seleccionar" es el índice 0, no filtra nada si está aquí
        self.combo_tags.addItems(
            ["Seleccionar", "ingenieria", "software", "arte", "investigacion", "personal", "educacion"])
        layout.addWidget(self.combo_tags)

        # --- FILA 3: Estados ---
        layout.addWidget(QLabel("Filtrar por Estado:"))
        self.combo_estado = QComboBox()
        self.combo_estado.addItems(
            ["Seleccionar", "Activo", "Archivado", "Terminado"])
        layout.addWidget(self.combo_estado)

        # --- BOTÓN FILTRAR ---
        self.btn_filtrar = QPushButton("APLICAR FILTRO")
        self.btn_filtrar.clicked.connect(
            self.accept)  # Cierra y retorna "Accepted"
        layout.addWidget(self.btn_filtrar)

    def obtener_filtros(self):
        """Devuelve un diccionario con los valores elegidos"""
        return {
            "texto": self.txt_busqueda.text().lower(),
            "ambito": self.combo_ambito.currentText(),
            "tag": self.combo_tags.currentText(),
            "estado": self.combo_estado.currentText()
        }


class PantallaIdeas(QWidget):

    # filtar_idea, atras):
    def __init__(self, volver_callback):
        super().__init__()

        self.volver_callback = volver_callback

        layout = QVBoxLayout()
        layout_botones = QHBoxLayout()
        f1 = intfz.fuente_l("Segoe UI", 24, cursiva=True)
        texto = QLabel("IDEAS Y PROYECTOS")
        texto.setAlignment(Qt.AlignCenter)
        texto.setFont(f1)

        self.tabla = intfz.crear_tabla(
            ["Titulo", "Descripción", "Tags", "Fecha", "Estado", "Indice"])
        self.actualizar_tabla()

        # Botones
        self.Agregar = QPushButton("AGREGAR")
        self.Editar = QPushButton("EDITAR/VER")
        self.Borrar = QPushButton("BORRAR")
        self.Filtrar = QPushButton("FILTRAR")
        self.LimpiaFil = QPushButton("LIMPIAR FILTRO")
        self.Atras = QPushButton("ATRAS")

        self.Agregar.clicked.connect(self.abrir_agregar)
        self.Editar.clicked.connect(self.abrir_editar)
        self.Borrar.clicked.connect(self.borrar)
        self.Filtrar.clicked.connect(self.abrir_filtrar)
        self.LimpiaFil.clicked.connect(self.limpieza_filtro)
        self.Atras.clicked.connect(self.volver_callback)

        layout.addWidget(texto)
        layout.addWidget(self.tabla)
        layout_botones.addWidget(self.Agregar)
        layout_botones.addWidget(self.Editar)
        layout_botones.addWidget(self.Borrar)
        layout_botones.addWidget(self.Filtrar)
        layout_botones.addWidget(self.LimpiaFil)
        layout_botones.addWidget(self.Atras)
        layout.addLayout(layout_botones)

        self.setLayout(layout)

    def actualizar_tabla(self):
        self.tabla.setRowCount(0)
        ruta = d.validar(archivo_json)
        datos = d.abrir(ruta)
        tabla_info = []
        for l in datos:
            tabla_info.append(list(l.values()))
        intfz.llenar_tabla(self.tabla, tabla_info)

    def aplicar_filtro_logica(self, f):
        # 1. Leer los datos originales (sin borrar el archivo)
        ruta = d.validar(archivo_json)
        todos_los_datos = d.abrir(ruta)

        resultados = []

        for idea in todos_los_datos:
            cumple = True

            # Filtro de Texto
            if f["texto"]:
                contiene_en_titulo = f["texto"] in idea["titulo"].lower()
                contiene_en_desc = f["texto"] in idea["descripcion"].lower()

                if f["ambito"] == "Título" and not contiene_en_titulo:
                    cumple = False
                elif f["ambito"] == "Descripción" and not contiene_en_desc:
                    cumple = False
                elif f["ambito"] == "Ambos" and not (contiene_en_titulo or contiene_en_desc):
                    cumple = False

            # Filtro de Tag (si no es "Seleccionar")
            if f["tag"] != "Seleccionar" and f["tag"] not in idea["tags"]:
                cumple = False

            # Filtro de Estado
            if f["estado"] != "Seleccionar" and f["estado"] != idea["estado"]:
                cumple = False

            if cumple:
                resultados.append(list(idea.values()))

        # 2. Limpiar y llenar la tabla SOLO con los resultados
        self.tabla.setRowCount(0)
        intfz.llenar_tabla(self.tabla, resultados)

    def limpieza_filtro(self):
        self.actualizar_tabla()

    def abrir_filtrar(self):
        dialogo = filtrar(self)
        if dialogo.exec():  # Si el usuario pulsó "Aplicar Filtro"
            filtros = dialogo.obtener_filtros()
            self.aplicar_filtro_logica(filtros)

    def abrir_agregar(self):
        self.ventana = modifica_idea(
            "AGREGANDO IDEA", callback=self.actualizar_tabla)
        self.ventana.show()

    def abrir_editar(self):
        ind = intfz.obtener_indice_tabla(self.tabla)
        selection = intfz.obtener_elemento_tabla(self.tabla)
        ideasel = intfz.lista_diccio(selection, intfz.info_ada.claves_ideas)
        self.ven = modifica_idea(
            "EDITANDO IDEA", modo="editar", idea=ideasel, indice=ind, callback=self.actualizar_tabla)
        self.ven.show()

    def borrar(self):
        ind = intfz.obtener_indice_tabla(self.tabla)
        if ind != -1:
            borrar_idea(ind=ind)
            d.actualizar_indice_idea()
            self.actualizar_tabla()


def borrar_idea(name=archivo_json, ind=None):
    ruta = d.validar(name)
    d.borrar(ruta, ind)
