import numpy as np


def ejercicio_3():
    """Analiza las calificaciones académicas de un grupo de estudiantes.

    Genera una matriz de 40 filas (estudiantes) por 5 columnas (asignaturas)
    con notas aleatorias entre 30 y 100 para calcular:
      - Promedio individual de cada estudiante (filas).
      - Promedio general por materia (columnas).
      - Estudiantes con mejor y peor rendimiento académico.
      - Conteo y porcentaje de alumnos aprobados (>= 60) y reprobados (< 60).
    """

    # Imprime un encabezado decorativo de 70 caracteres de ancho
    print("\n" + "=" * 70)
    print("EJERCICIO 3: ANÁLISIS ACADÉMICO (40 estudiantes × 5 asignaturas)")
    print("=" * 70)

    try:
        # -------------------------------------------------------------
        # CONFIGURACIÓN Y GENERACIÓN DE LA MATRIZ DE NOTAS
        # -------------------------------------------------------------

        estudiantes = 40  # Número de filas
        asignaturas = 5  # Número de columnas

        # Genera una matriz de dimensión (40, 5) con notas aleatorias
        # flotantes distribuidas uniformemente en el rango [30.0, 100.0].
        matriz_calificaciones = np.random.uniform(30, 100, (estudiantes, asignaturas))

        # -------------------------------------------------------------
        # OPERACIONES ESTADÍSTICAS POR EJE (AXIS)
        # -------------------------------------------------------------

        # axis=1: Calcula la media a lo largo de las columnas (horizontal).
        # Devuelve un arreglo de 40 elementos con el promedio de cada estudiante.
        promedio_estudiante = np.mean(matriz_calificaciones, axis=1)

        # axis=0: Calcula la media a lo largo de las filas (vertical).
        # Devuelve un arreglo de 5 elementos con el promedio general de cada asignatura.
        promedio_asignatura = np.mean(matriz_calificaciones, axis=0)

        # -------------------------------------------------------------
        # BÚSQUEDA DE EXTREMOS ACADÉMICOS
        # -------------------------------------------------------------

        # np.argmax() ubica el índice del promedio más alto.
        # Se le suma 1 para representar el número de estudiante en base 1.
        mejor_estudiante = np.argmax(promedio_estudiante) + 1

        # np.argmin() ubica el índice del promedio más bajo.
        peor_estudiante = np.argmin(promedio_estudiante) + 1

        # -------------------------------------------------------------
        # INDEXACIÓN BOOLEANA (CONTEO DE APROBADOS/REPROBADOS)
        # -------------------------------------------------------------

        # 'promedio_estudiante >= 60' genera un arreglo de True/False.
        # np.sum() cuenta cuántos valores son True (es decir, aprobados).
        aprobados = np.sum(promedio_estudiante >= 60)

        # Cuenta cuántos valores cumplen con la condición de reprobado (< 60).
        reprobados = np.sum(promedio_estudiante < 60)

        # -------------------------------------------------------------
        # IMPRESIÓN Y FORMATO DE RESULTADOS
        # -------------------------------------------------------------

        print(f"\n📚 PROMEDIO POR ESTUDIANTE (primeros 10):")
        # Recorre solo los primeros 10 estudiantes para mantener limpia la consola
        for i in range(min(10, estudiantes)):
            # Determina el estado evaluando la nota promedio del estudiante actual
            estado = (
                "✅ APROBADO" if promedio_estudiante[i] >= 60 else "❌ REPROBADO"
            )
            # Imprime la nota con 2 decimales y su estado correspondiente
            print(f"   Estudiante {i+1}: {promedio_estudiante[i]:.2f} - {estado}")

        print(f"\n📚 PROMEDIO POR ASIGNATURA:")
        # Lista con los nombres de las asignaturas ordenadas según las columnas (0 a 4)
        asignaturas_nombres = [
            "Matemáticas",
            "Español",
            "Inglés",
            "Ciencias",
            "Historia",
        ]
        for i in range(asignaturas):
            print(f"   {asignaturas_nombres[i]}: {promedio_asignatura[i]:.2f}")

        # Muestra el mejor y peor estudiante accediendo a su valor con el índice base 0 (-1)
        print(
            f"\n🏆 MEJOR ESTUDIANTE: Estudiante {mejor_estudiante} "
            f"con {promedio_estudiante[mejor_estudiante-1]:.2f}"
        )
        print(
            f"📉 PEOR ESTUDIANTE:  Estudiante {peor_estudiante} "
            f"con {promedio_estudiante[peor_estudiante-1]:.2f}"
        )

        # Muestra las estadísticas globales calculando el porcentaje del total
        print(f"\n📊 RESULTADOS GENERALES:")
        print(
            f"   • Aprobados:  {aprobados} estudiantes "
            f"({aprobados/estudiantes*100:.1f}%)"
        )
        print(
            f"   • Reprobados: {reprobados} estudiantes "
            f"({reprobados/estudiantes*100:.1f}%)"
        )

    except Exception as e:
        # Manejo y despliegue seguro de excepciones
        print(f"❌ Error en ejercicio 3: {e}")


# Bloque de ejecución principal
if __name__ == "__main__":
    ejercicio_3()