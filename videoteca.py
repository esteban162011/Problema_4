# Matriz: [Título, Año de Lanzamiento, Calificación (1-10), Género]
videoteca = [
    ["Inception",             2010, 9, "Ciencia Ficción"],
    ["The Dark Knight",       2008, 9, "Acción"],
    ["Interstellar",          2014, 8, "Ciencia Ficción"],
    ["Parasite",              2019, 9, "Drama"],
    ["Dune",                  2021, 8, "Ciencia Ficción"],
    ["Everything Everywhere", 2022, 9, "Comedia"],
    ["Oppenheimer",           2023, 8, "Drama"],
    ["Avatar",                2009, 7, "Ciencia Ficción"],
    ["Tenet",                 2020, 6, "Acción"],
]


def contar_titulos(matriz, calificacion_minima, anio_minimo):
    conteo = 0
    for pelicula in matriz:
        calificacion = pelicula[2]
        anio = pelicula[1]
        if calificacion >= calificacion_minima and anio >= anio_minimo:
            conteo = conteo + 1
    return conteo


# El usuario ingresa los criterios
umbral_calificacion = int(input())
anio_limite = int(input())

total = contar_titulos(videoteca, umbral_calificacion, anio_limite)

print("=== VIDEOTECA DIGITAL ===")
print("Criterios aplicados:")
print("  Calificacion minima :", umbral_calificacion)
print("  Año minimo          :", anio_limite)
print("Total de titulos que cumplen ambos criterios:", total)
