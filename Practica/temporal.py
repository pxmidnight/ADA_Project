dicti = ["titulo", "descripcion", "tags", "fecha", "estado"]
listos = ['Juego cryptid', "Juego 2d para pc", [
    'software', 'arte'], "20/05/2026", 'Archivado']


def lista_diccio(lista, claves):
    res = {}
    if len(lista) == len(claves):
        for i in range(len(lista)):
            res[claves[i]] = lista[i]
    return res


print(lista_diccio(listos, dicti))
