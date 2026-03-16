# Modulo para manejo de datos de ideas
# Importamos librerias
import json
import os
from datetime import datetime
# Funciones


def escribir(name, text):
    with open(name, "w") as file:
        json.dump(text, file, indent=4)


def crear(name):
    escribir(name, [])
# Crea un archivo json vacio


def abrir(name):
    try:
        with open(name, "r") as file:
            ideas = json.load(file)
            return ideas
    except (FileNotFoundError, json.JSONDecodeError):
        return []
# Abrir un archivo (traer datos de json)


def anexar(name, elemento):
    data = abrir(name)
    data.append(elemento)
    escribir(name, data)
# Guardar archivo (enviar datos a json)


def editar(name, indice, clave, valor):
    data = abrir(name)
    if indice < len(data):
        data[indice][clave] = valor
    escribir(name, data)
# Edita una idea


def editar_dicci(name, indice, nuevo):
    data = abrir(name)
    if indice < len(data):
        data[indice].update(nuevo)
    escribir(name, data)


def borrar(name, indice):
    data = abrir(name)
    # if indice < len(data):
    del data[indice]
    escribir(name, data)
# Elimina la idea por el indice de la lista


def validar(name):
    # 1. Obtiene la carpeta exacta donde está este script (.py)
    ruta_script = os.path.dirname(os.path.abspath(__file__))
    # 2. Une esa ruta con el nombre que le diste (ej: "files/ideas.json")
    # Esto asegura que "files" sea una subcarpeta de "Code"
    ruta_completa = os.path.join(ruta_script, name)
    # 3. Extraemos el directorio de la ruta completa para crearlo
    directorio = os.path.dirname(ruta_completa)
    if not os.path.exists(directorio):
        os.makedirs(directorio)
    if not os.path.exists(ruta_completa):
        crear(ruta_completa)
    return ruta_completa
# Valida que el archivo exista y añade en el archivo


def fecha_act():
    return datetime.now().strftime("%d/%m/%Y")
# Obtiene la fecha de hoy


def fecha_per(fec=None):
    if not fec:
        dia = fecha_act()
    else:
        dia = fec
    return dia
# Validacion si hay fecha


def indice_agre(name=validar("files/ideas.json")):
    data = abrir(name)
    return len(data)
# Definicion de indice de elemento


def actualizar_indice_idea(name=validar("files/ideas.json")):
    data = abrir(name)
    for j, i in enumerate(data):
        i["indice"] = j
        editar_dicci(name, j, i)


"""def idea(title, description, tags, date, state):
    return {"titulo": title, "descripcion": description,
            "tags": tags, "fecha": date, "estado": state}"""


def idea(title, description, tags, date, state, index=None):
    if not index:
        index = indice_agre()
    return {"titulo": title, "descripcion": description,
            "tags": tags, "fecha": date, "estado": state, "indice": index}
# Crea la idea como diccionario


# Variables
opciones = {"estado": ["Activo", "Archivado", "Terminado"],
            "tags": ["ingenieria", "software", "arte", "investigacion", "personal", "educacion"]}


# print(indice_agre(validar("files/ideas.json")))
# actualizar solo se emplea una ves ya que coloca el indice a todo
# actualizar_indice_idea()
