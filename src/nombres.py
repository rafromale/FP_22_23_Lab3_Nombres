def lee_nombres(nombre_fichero):
    """
    Lee el fichero de texto y devuekve una lista de tuplas 

    Args:
        nombre_fichero (str): ruta y nombre del fichero de datos

    Returns:
        list[(int,str,int,str)]: lista de tuplas con los datos convertidos
    """
    lista = []
    with open(nombre_fichero,encoding='utf-8') as f:
        next(f)
        for linea in f:
            trozos = linea.split(',')
            lista.append((int(trozos[0]),trozos[1],int(trozos[2]),trozos[3]))
    return lista

print(lee_nombres('./data/frecuencias_nombres.csv')[:3])