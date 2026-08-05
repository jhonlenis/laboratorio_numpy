import numpy as np


def ejercicio_7():
    """
    Una fábrica posee 100 sensores.
    Genera mediciones aleatorias y determina sensores fuera de rango.
    """
    print("\n" + "="*70)
    print("EJERCICIO 7: SIMULACIÓN DE SENSORES IoT (100 sensores)")
    print("="*70)
    
    try:
        # Número de sensores
        num_sensores = 100
        
        # Rango permitido de temperaturas (80-120°C)
        temperatura_minima = 80
        temperatura_maxima = 120
        temperatura_critica = 130  # Temperatura crítica
        
        # Generar mediciones aleatorias (usando random.uniform())
        # Mayoría en rango normal, algunas fuera
        mediciones = np.random.uniform(75, 135, num_sensores)
        
        # Calcular estadísticas
        promedio = np.mean(mediciones)
        desv_estandar = np.std(mediciones)
        minima = np.min(mediciones)
        maxima = np.max(mediciones)
        
        # Sensores fuera de rango (usando where())
        sensores_bajo_rango = np.where(mediciones < temperatura_minima)[0] + 1
        sensores_sobre_rango = np.where(mediciones > temperatura_maxima)[0] + 1
        sensores_criticos = np.where(mediciones >= temperatura_critica)[0] + 1
        
        # Sensores en rango normal
        sensores_normales = np.where((mediciones >= temperatura_minima) & 
                                     (mediciones <= temperatura_maxima))[0] + 1
        
        # Mostrar resultados
        print(f"\n🌡️ PRIMERAS 20 MEDICIONES:")
        for i in range(min(20, num_sensores)):
            estado = "✅" if temperatura_minima <= mediciones[i] <= temperatura_maxima else "⚠️"
            print(f"   Sensor {i+1:3d}: {mediciones[i]:6.2f}°C {estado}")
        
        print(f"\n📊 ESTADÍSTICAS GENERALES:")
        print(f"   • Promedio: {promedio:.2f}°C")
        print(f"   • Desviación estándar: {desv_estandar:.2f}°C")
        print(f"   • Temperatura mínima: {minima:.2f}°C")
        print(f"   • Temperatura máxima: {maxima:.2f}°C")
        
        print(f"\n⚠️ ESTADO DE SENSORES:")
        print(f"   • Sensores en rango normal (80-120°C): {len(sensores_normales)} ✅")
        print(f"   • Sensores bajo rango (<80°C): {len(sensores_bajo_rango)}")
        if len(sensores_bajo_rango) > 0:
            print(f"     Sensores: {sensores_bajo_rango[:10].tolist()}{'...' if len(sensores_bajo_rango) > 10 else ''}")
        
        print(f"   • Sensores sobre rango (>120°C): {len(sensores_sobre_rango)}")
        if len(sensores_sobre_rango) > 0:
            print(f"     Sensores: {sensores_sobre_rango[:10].tolist()}{'...' if len(sensores_sobre_rango) > 10 else ''}")
        
        print(f"   • Sensores críticos (≥130°C): {len(sensores_criticos)} 🔴")
        if len(sensores_criticos) > 0:
            print(f"     Sensores: {sensores_criticos[:10].tolist()}{'...' if len(sensores_criticos) > 10 else ''}")
        
    except Exception as e:
        print(f"❌ Error en ejercicio 7: {e}")


if __name__ == "__main__":
    ejercicio_7()
