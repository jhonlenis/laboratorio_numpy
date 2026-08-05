import numpy as np

def generar_reporte_estadistico(matriz):
    """
    Genera un reporte completo de estadísticas para cualquier matriz.
    
    Args:
        matriz: arreglo NumPy de cualquier dimensión
    
    Returns:
        diccionario con todas las estadísticas
    """
    # Validar entrada
    if not isinstance(matriz, np.ndarray):
        raise TypeError("La entrada debe ser un arreglo NumPy")
    
    if matriz.size == 0:
        raise ValueError("La matriz no puede estar vacía")
    
    # Calcular todas las estadísticas
    estadisticas = {
        'dimensión': matriz.ndim,
        'forma': matriz.shape,
        'filas': matriz.shape[0] if matriz.ndim >= 1 else 1,
        'columnas': matriz.shape[1] if matriz.ndim >= 2 else 1,
        'total_datos': matriz.size,
        'máximo': np.max(matriz),
        'mínimo': np.min(matriz),
        'promedio': np.mean(matriz),
        'mediana': np.median(matriz),
        'varianza': np.var(matriz),
        'desv_estandar': np.std(matriz),
    }
    
    return estadisticas
 
 
def ejercicio_10():
    """
    Construye un programa que reciba una matriz cualquiera
    y genere automáticamente un reporte completo.
    """
    print("\n" + "="*70)
    print("EJERCICIO 10: DASHBOARD ESTADÍSTICO")
    print("="*70)
    
    try:
        # Crear varias matrices de prueba
        print("\n📊 PRUEBA 1: Matriz pequeña 3×4")
        matriz1 = np.array([
            [10, 20, 30, 40],
            [50, 60, 70, 80],
            [90, 100, 110, 120]
        ])
        
        reporte1 = generar_reporte_estadistico(matriz1)
        
        print(f"\n   Matriz original:")
        print(f"   {matriz1}")
        
        print(f"\n   📈 REPORTE:")
        print(f"   • Dimensión: {reporte1['dimensión']}D")
        print(f"   • Forma: {reporte1['forma']}")
        print(f"   • Filas: {reporte1['filas']}")
        print(f"   • Columnas: {reporte1['columnas']}")
        print(f"   • Total de datos: {reporte1['total_datos']}")
        print(f"   • Máximo: {reporte1['máximo']}")
        print(f"   • Mínimo: {reporte1['mínimo']}")
        print(f"   • Promedio: {reporte1['promedio']:.2f}")
        print(f"   • Mediana: {reporte1['mediana']:.2f}")
        print(f"   • Varianza: {reporte1['varianza']:.2f}")
        print(f"   • Desviación estándar: {reporte1['desv_estandar']:.2f}")
        
        # Prueba 2: Matriz aleatoria grande
        print(f"\n📊 PRUEBA 2: Matriz aleatoria 10×8")
        matriz2 = np.random.randint(0, 100, (10, 8))
        reporte2 = generar_reporte_estadistico(matriz2)
        
        print(f"\n   📈 REPORTE:")
        print(f"   • Dimensión: {reporte2['dimensión']}D")
        print(f"   • Forma: {reporte2['forma']}")
        print(f"   • Filas: {reporte2['filas']}")
        print(f"   • Columnas: {reporte2['columnas']}")
        print(f"   • Total de datos: {reporte2['total_datos']}")
        print(f"   • Máximo: {reporte2['máximo']}")
        print(f"   • Mínimo: {reporte2['mínimo']}")
        print(f"   • Promedio: {reporte2['promedio']:.2f}")
        print(f"   • Mediana: {reporte2['mediana']:.2f}")
        print(f"   • Varianza: {reporte2['varianza']:.2f}")
        print(f"   • Desviación estándar: {reporte2['desv_estandar']:.2f}")
        
        # Prueba 3: Matriz 1D (vector)
        print(f"\n📊 PRUEBA 3: Vector 1D (20 elementos)")
        matriz3 = np.random.uniform(10, 50, 20)
        reporte3 = generar_reporte_estadistico(matriz3)
        
        print(f"\n   📈 REPORTE:")
        print(f"   • Dimensión: {reporte3['dimensión']}D")
        print(f"   • Forma: {reporte3['forma']}")
        print(f"   • Total de datos: {reporte3['total_datos']}")
        print(f"   • Máximo: {reporte3['máximo']:.2f}")
        print(f"   • Mínimo: {reporte3['mínimo']:.2f}")
        print(f"   • Promedio: {reporte3['promedio']:.2f}")
        print(f"   • Mediana: {reporte3['mediana']:.2f}")
        print(f"   • Varianza: {reporte3['varianza']:.2f}")
        print(f"   • Desviación estándar: {reporte3['desv_estandar']:.2f}")
        
    except Exception as e:
        print(f"❌ Error en ejercicio 10: {e}")
 
 
# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================
 
def main():
    """Ejecuta los ejercicios 6-10"""
    print("\n" + "🎓 "*20)
    print("LABORATORIO DE ANÁLISIS DE DATOS CON NumPy")
    print("Ejercicios 6-10")
    print("🎓 "*20)
    
    ejercicio_6()
    ejercicio_7()
    ejercicio_8()
    ejercicio_9()
    ejercicio_10()
    
    print("\n" + "="*70)
    print("✅ EJERCICIOS 6-10 COMPLETADOS")
    print("="*70 + "\n")
 
 
if __name__ == "__main__":
    ejercicio_10()