import numpy as np
from datetime import datetime


def ejercicio_1():
    """Registra y analiza el comportamiento térmico diario.

    Genera una muestra de 30 temperaturas simuladas para calcular métricas
    estadísticas de tendencia central (promedio), valores extremos (máximo y
    mínimo) y medidas de dispersión (desviación estándar y varianza).
    """

    # Imprime un encabezado decorativo de 70 caracteres de ancho
    print("\n" + "=" * 70)
    print("Ejercicio 1: Registro de temperaturas")
    print("=" * 70)

    try:
        # Genera un arreglo NumPy de 30 valores aleatorios flotantes
        # distribuidos de forma uniforme entre 15.0°C y 35.0°C.
        temperaturas = np.random.uniform(15, 35, 30)

        # -------------------------------------------------------------
        # CÁLCULOS ESTADÍSTICOS CON NUMPY
        # -------------------------------------------------------------

        # Calcula la media aritmética (promedio) de las temperaturas
        temp_promedio = np.mean(temperaturas)

        # Obtiene el valor térmico más alto registrado en el periodo
        temp_maxima = np.max(temperaturas)

        # Obtiene el valor térmico más bajo registrado en el periodo
        temp_minima = np.min(temperaturas)

        # Calcula la desviación estándar (grado de dispersión respecto a la media)
        desv_estandar = np.std(temperaturas)

        # Calcula la varianza (cuadrado de la desviación estándar)
        varianza = np.var(temperaturas)

        # -------------------------------------------------------------
        # BÚSQUEDA DE POSICIONES (ÍNDICES)
        # -------------------------------------------------------------

        # np.argmax() devuelve la posición (índice 0, 1, 2...) del valor máximo.
        # Se le suma 1 para traducir el índice de programación a un número de día humano (1 a 30).
        dia_mas_calor = np.argmax(temperaturas) + 1

        # np.argmin() devuelve la posición del valor mínimo.
        # Se le suma 1 por la misma razón de indexación.
        dia_mas_frio = np.argmin(temperaturas) + 1

        # -------------------------------------------------------------
        # SALIDA Y FORMATO DE RESULTADOS
        # -------------------------------------------------------------

        # Muestra solo los primeros 10 días usando 'slicing' [:10] y los redondea a 2 decimales
        print(
            f"Temperaturas registradas (primeros 10): {temperaturas[:10].round(2)}"
        )

        print(f"\n📊 ESTADÍSTICAS:")
        # :.2f da formato flotante a exactamente 2 decimales
        print(f"   • Temperatura promedio: {temp_promedio:.2f}°C")
        print(
            f"   • Temperatura máxima: {temp_maxima:.2f}°C (Día {dia_mas_calor})"
        )
        print(
            f"   • Temperatura mínima: {temp_minima:.2f}°C (Día {dia_mas_frio})"
        )
        print(f"   • Desviación estándar: {desv_estandar:.2f}°C")
        print(f"   • Varianza: {varianza:.2f}")

    except Exception as e:
        # Bloque de contingencia: atrapa cualquier fallo en el código y muestra el mensaje
        print(f"❌ Error en ejercicio 1: {e}")


# Punto de entrada del script
if __name__ == "__main__":
    # Ejecuta la función principal únicamente si el archivo se corre de forma directa
    ejercicio_1()