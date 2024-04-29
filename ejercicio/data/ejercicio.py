import os

# Definir el nombre del directorio donde se guardarán los archivos HTML
directorio_salida = "ejercicio/data/reportes"

# Crear el directorio si no existe
if not os.path.exists(directorio_salida):
    os.makedirs(directorio_salida)

# proceso 
#
# acceder al archivo
archivo = open('ejercicio/data/Listado-Instituciones-Educativas-distribuidas-por-zona-distrito-y-circuito.csv', "r")

# obtener las líneas del archivo
lineas = archivo.readlines()

# lineas es ina lista de cadenas
# se imprime las siguientes posiciones
encabezados = lineas[0]
encabezados = encabezados.split("|")
# en línea tomo el valor de lineas[1]
linea = lineas[1]
# a línea que es una cadena, la separo mediante la función
# de Python split
# Recuerdo que el separador de la cadena es un "|"

linea = linea.split("|")
# imprimo la nueva línea; que ahora es una lista

archivo.close()


# Recorrer todas las líneas del archivo excepto la primera (que son los encabezados)
for linea in lineas[1:]:
    # Separar los valores de la línea
    valores = linea.split("|")
    # Inicializar la variable para el HTML de esta página
    pagina = """
        <!DOCTYPE html>
        <html lang="en" dir="ltr">
        <head>
            <meta charset="utf-8">
            <title>Trabajo Grupal</title>
        </head>
        <body> 
        
        """

    # Iterar sobre los encabezados y los valores
    for encabezado, valor in zip(encabezados, valores):
        # Agregar cada par encabezado-valor al HTML
         pagina += "<b>{}</b>: {}<br>".format(encabezado, valor)

        # Cerrar la etiqueta body y html
    pagina += """
        </body>
        </html>
        """

        # Escribir el HTML en un archivo correspondiente al código AMIE de la institución
    with open(directorio_salida+"/{}.html".format(valores[0]), "w") as archivo_generado:
            archivo_generado.write(pagina)