import numpy as np


def ejercicio_2():
    """Registra y analiza la matriz de ventas de un equipo comercial.

    Genera una matriz de 12 filas (vendedores) por 6 columnas (meses)
    con valores aleatorios para calcular:
      - Totales acumulados por vendedor (suma horizontal / filas).
      - Totales y promedios por mes (suma vertical / columnas).
      - Identificación del vendedor con mayor y menor desempeño.
      - Gran total acumulado de la empresa.
    """

    # Imprime un encabezado decorativo de 70 caracteres de ancho
    print("\n" + "=" * 70)
    print("EJERCICIO 2: MATRIZ DE VENTAS (12 vendedores × 6 meses)")
    print("=" * 70)

    try:
        # -------------------------------------------------------------
        # CONFIGURACIÓN Y GENERACIÓN DE LA MATRIZ DE DATOS
        # -------------------------------------------------------------

        vendedores = 12  # Número de filas de la matriz
        meses = 6  # Número de columnas de la matriz

        # Genera una matriz de forma (12, 6) con montos aleatorios
        # de venta uniformemente distribuidos entre $1,000 y $10,000.
        matriz_ventas = np.random.uniform(1000, 10000, (vendedores, meses))

        # -------------------------------------------------------------
        # OPERACIONES CON EJES (AXIS) EN NUMPY
        # -------------------------------------------------------------

        # axis=1: Suma a lo largo de las COLUMNAS (de izquierda a derecha).
        # Agrupa los 6 meses de cada vendedor y retorna un arreglo de 12 elementos.
        venta_total_vendedor = np.sum(matriz_ventas, axis=1)

        # axis=0: Suma a lo largo de las FILAS (de arriba a abajo).
        # Agrupa los 12 vendedores para cada mes y retorna un arreglo de 6 elementos.
        venta_total_mes = np.sum(matriz_ventas, axis=0)

        # axis=0: Calcula la media vertical para obtener el promedio
        # de ventas por vendedor en cada uno de los 6 meses.
        promedio_mensual = np.mean(matriz_ventas, axis=0)

        # -------------------------------------------------------------
        # BÚSQUEDA DE MEJOR Y PEOR DESEMPEÑO
        # -------------------------------------------------------------

        # np.argmax() encuentra la posición del valor máximo dentro del arreglo de totales.
        # Se le suma 1 para adaptar la posición en Python (base 0) a una etiqueta humana (base 1).
        mejor_vendedor = np.argmax(venta_total_vendedor) + 1

        # np.argmin() encuentra la posición del valor mínimo dentro del arreglo de totales.
        peor_vendedor = np.argmin(venta_total_vendedor) + 1

        # -------------------------------------------------------------
        # IMPRESIÓN Y FORMATO DE RESULTADOS
        # -------------------------------------------------------------

        print(f"\n📊 VENTAS POR VENDEDOR (Total):")
        # Itera únicamente sobre los primeros 5 vendedores para no saturar la consola
        for i in range(min(5, vendedores)):
            # :,.2f da formato de moneda con comas para miles y 2 decimales (ej. $24,150.50)
            print(f"   Vendedor {i+1}: ${venta_total_vendedor[i]:,.2f}")
        print(f"   ... (mostrando 5 de {vendedores})")

        print(f"\n📊 VENTAS POR MES:")
        # Recorre cada uno de los 6 meses mostrando total acumulado y promedio por vendedor
        for mes in range(meses):
            print(
                f"   Mes {mes+1}: ${venta_total_mes[mes]:,.2f} | "
                f"Promedio: ${promedio_mensual[mes]:,.2f}"
            )

        # Muestra el mejor y peor vendedor accediendo a sus montos corregidos por índice (-1)
        print(
            f"\n🏆 MEJOR VENDEDOR: Vendedor {mejor_vendedor} "
            f"con ${venta_total_vendedor[mejor_vendedor-1]:,.2f}"
        )
        print(
            f"📉 PEOR VENDEDOR:  Vendedor {peor_vendedor} "
            f"con ${venta_total_vendedor[peor_vendedor-1]:,.2f}"
        )

        # np.sum(matriz_ventas) sin 'axis' suma absolutamente todos los elementos de la matriz
        print(f"💰 VENTA TOTAL GENERAL: ${np.sum(matriz_ventas):,.2f}")

    except Exception as e:
        # Bloque de captura de excepciones para manejo seguro de errores
        print(f"❌ Error en ejercicio 2: {e}")


# Punto de entrada principal para la ejecución directa del script
if __name__ == "__main__":
    ejercicio_2()