import sys
from PySide6.QtWidgets import QListWidget, QAbstractItemView, QListWidgetItem, QTableWidget, QTableWidgetItem, QHeaderView, QComboBox, QLineEdit, QTextEdit
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
# Modulo propio de informacion
import info_ada


# Conocer informacion


def consultar_fuentes_disponibles():
    f_info = info_ada.fonts_info
    c = 1
    for i in f_info:
        print(str(c) + ". " + i + " : " + f_info[i])
        c += 1


# Funciones generales
# Fuente

def fuente_l(tipo, tamano, negrina=False, cursiva=False):
    f = QFont(tipo)  # Que fuente
    f.setPointSize(tamano)
    f.setBold(negrina)
    f.setItalic(cursiva)
    return f

# Checklist


def crear_checklist():
    lista = QListWidget()
    lista.setSelectionMode(QAbstractItemView.NoSelection)
    return lista


def llenar_checklist(lista_widget, elementos, seleccionados=None):
    lista_widget.clear()
    if seleccionados is None:
        seleccionados = []
    for elemento in elementos:
        item = QListWidgetItem(elemento)
        item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
        if elemento in seleccionados:
            item.setCheckState(Qt.Checked)
        else:
            item.setCheckState(Qt.Unchecked)
        lista_widget.addItem(item)


def obtener_checklist(lista_widget):
    seleccionados = []
    for i in range(lista_widget.count()):
        item = lista_widget.item(i)
        if item.checkState() == Qt.Checked:
            seleccionados.append(item.text())
    return seleccionados

# LineEdit


def crear_LineEdit(text=None):
    if not text:
        linea = QLineEdit()
    else:
        linea = QLineEdit(text)
    return linea

# TextEdit


def crear_TextEdit(text=None):
    if not text:
        cuadro = QTextEdit()
    else:
        cuadro = QTextEdit(text)
    return cuadro


# Combobox


def crear_combobox(opciones, actual=None):
    combo = QComboBox()
    combo.addItems(opciones)
    if actual in opciones:
        combo.setCurrentText(actual)
    return combo


# Tablas


def lista_diccio(lista, claves):
    res = {}
    for i in range(len(lista)):
        res[claves[i]] = lista[i]
    return res


def crear_tabla(columnas):
    tabla = QTableWidget()
    tabla.setColumnCount(len(columnas))
    tabla.setHorizontalHeaderLabels(columnas)
    tabla.setSelectionBehavior(QAbstractItemView.SelectRows)
    tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
    tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    tabla.setColumnHidden(5, True)
    return tabla


def llenar_tabla(tabla, datos):
    tabla.setRowCount(len(datos))
    for fila, registro in enumerate(datos):
        for columna, valor in enumerate(registro):
            tabla.setItem(fila, columna, QTableWidgetItem(str(valor)))


def obtener_elemento_tabla(tabla):
    seleccionados = tabla.selectedItems()
    if not seleccionados:
        return None
    datos_fila = [item.text() for item in seleccionados]
    return datos_fila


def obtener_indice_tabla(tabla):
    """indices = tabla.selectionModel().selectedRows()
    if indices:
        return indices[0].row()
    return -1"""
    filas = tabla.selectionModel().selectedRows()
    if not filas:
        return -1
    fila_visual = filas[0].row()
    item_id = tabla.item(fila_visual, 5)

    if item_id:
        return int(item_id.text())
    print(item_id)
    return "es aqui"
