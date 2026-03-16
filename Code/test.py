# from datos import *
import datos as d
# print(dir(d))


# text = abrir("files/ideas.json")
"""titulo = input("Titulo: ")
descripcion = input("Descripcion: ")
tags = input(
    "Tags (ingenieria,software,arte,investigacion,personal,educacion): ")
fecha = d.fecha_act()
estado = input("Estado (Activo, Archivado, Terminado): ")"""
# editar(ruta, 0, "titulo", "Idea inicial")

ruta = d.validar("files/ideas.json")
# ruta = d.validar("files/silaves.json")
print(d.abrir(ruta))
"""d.crear(ruta)
d.anexar(ruta, {"putos": "no tienes enemigos"})
d.editar(ruta, 0, "Fecha", d.fecha_act())
d.borrar(ruta, 0)"""

# d.borrar(ruta, 4)
# nuevo = d.idea(titulo, descripcion, tags, fecha, estado)
# d.anexar(ruta, nuevo)

# d.editar(ruta, 0, "fecha", d.fecha_act())
