import numpy as np

def ejercicio_5():
    """
    Registra producción de 3 líneas durante 30 días.
    Calcula: producción diaria, semanal y mensual, línea más productiva.
    """
    print("\n" + "="*70)
    print("EJERCICIO 5: SISTEMA DE PRODUCCIÓN (30 días × 3 líneas)")
    print("="*70)
    
    try:
        # Crear matriz 30×3 con producción diaria (unidades)
        dias = 30
        lineas = 3
        matriz_produccion = np.random.randint(100, 500, (dias, lineas))
        
        # Producción diaria total
        produccion_diaria = np.sum(matriz_produccion, axis=1)
        
        # Producción por línea
        produccion_por_linea = np.sum(matriz_produccion, axis=0)
        
        # Línea más productiva
        linea_productiva = np.argmax(produccion_por_linea) + 1
        
        # Producción mensual total
        produccion_mensual = np.sum(matriz_produccion)
        
        # Producción semanal (dividir mes en semanas)
        semanas = dias // 7  # 4 semanas completas
        produccion_semanal = []
        for semana in range(semanas):
            inicio = semana * 7
            fin = inicio + 7
            produccion_semana = np.sum(matriz_produccion[inicio:fin])
            produccion_semanal.append(produccion_semana)
        
        # Mostrar resultados
        print(f"\n📊 PRODUCCIÓN DIARIA (primeros 10 días):")
        for dia in range(min(10, dias)):
            print(f"   Día {dia+1}: {produccion_diaria[dia]} unidades")
        
        print(f"\n📊 PRODUCCIÓN SEMANAL:")
        for semana in range(len(produccion_semanal)):
            print(f"   Semana {semana+1}: {produccion_semanal[semana]} unidades | Promedio diario: {produccion_semanal[semana]/7:.2f}")
        
        print(f"\n🏭 PRODUCCIÓN POR LÍNEA:")
        lineas_nombres = ["Línea A", "Línea B", "Línea C"]
        for i in range(lineas):
            print(f"   {lineas_nombres[i]}: {produccion_por_linea[i]} unidades | Promedio: {produccion_por_linea[i]/dias:.2f} unidades/día")
        
        print(f"\n📈 RESUMEN MENSUAL:")
        print(f"   • Producción total: {produccion_mensual} unidades")
        print(f"   • Promedio diario: {np.mean(produccion_diaria):.2f} unidades")
        print(f"   • Día más productivo: Día {np.argmax(produccion_diaria)+1} ({np.max(produccion_diaria)} unidades)")
        print(f"   • Línea más productiva: {lineas_nombres[linea_productiva-1]} con {produccion_por_linea[linea_productiva-1]} unidades")
        
    except Exception as e:
        print(f"❌ Error en ejercicio 5: {e}")
 
 
# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================
 
def main():
    """Ejecuta todos los ejercicios"""
    print("\n" + "🎓 "*20)
    print("LABORATORIO DE ANÁLISIS DE DATOS CON NumPy")
    print("Ejercicios 1-5")
    print("🎓 "*20)
    
    ejercicio_1()
    ejercicio_2()
    ejercicio_3()
    ejercicio_4()
    ejercicio_5()
    
    print("\n" + "="*70)
    print("✅ EJERCICIOS 1-5 COMPLETADOS")
    print("="*70 + "\n")
 
 
if __name__ == "__main__":
    ejercicio_5()