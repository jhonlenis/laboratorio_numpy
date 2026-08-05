import numpy as np

def ejercicio_9():
    """
    Registra el precio de una acción durante 100 días.
    Calcula: precio promedio, máximo, mínimo, variación porcentual,
    días donde precio fue superior al promedio.
    """
    print("\n" + "="*70)
    print("EJERCICIO 9: SIMULACIÓN FINANCIERA (100 días)")
    print("="*70)
    
    try:
        # Generar 100 precios aleatorios (100-200)
        num_dias = 100
        precios = np.random.uniform(100, 200, num_dias)
        
        # Calcular estadísticas
        precio_promedio = np.mean(precios)
        precio_maximo = np.max(precios)
        precio_minimo = np.min(precios)
        
        # Variación porcentual (del primer al último día)
        variacion_porcentual = ((precios[-1] - precios[0]) / precios[0]) * 100
        
        # Días donde el precio fue superior al promedio (usando where())
        dias_superior = np.where(precios > precio_promedio)[0] + 1
        
        # Ganancia potencial si se hubiera comprado al mínimo y vendido al máximo
        ganancia_potencial = precio_maximo - precio_minimo
        ganancia_porcentual = (ganancia_potencial / precio_minimo) * 100
        
        # Volatilidad (desviación estándar)
        volatilidad = np.std(precios)
        
        # Mostrar resultados
        print(f"\n💹 PRIMEROS 20 DÍAS:")
        for dia in range(min(20, num_dias)):
            print(f"   Día {dia+1:3d}: ${precios[dia]:.2f}")
        
        print(f"\n📊 ESTADÍSTICAS DE PRECIO:")
        print(f"   • Precio promedio: ${precio_promedio:.2f}")
        print(f"   • Precio máximo: ${precio_maximo:.2f} (Día {np.argmax(precios)+1})")
        print(f"   • Precio mínimo: ${precio_minimo:.2f} (Día {np.argmin(precios)+1})")
        print(f"   • Volatilidad (desv. est.): ${volatilidad:.2f}")
        
        print(f"\n📈 ANÁLISIS DE TENDENCIA:")
        print(f"   • Precio inicial (Día 1): ${precios[0]:.2f}")
        print(f"   • Precio final (Día 100): ${precios[-1]:.2f}")
        print(f"   • Variación: {variacion_porcentual:+.2f}%")
        
        print(f"\n💰 OPORTUNIDADES DE INVERSIÓN:")
        print(f"   • Ganancia potencial (min→max): ${ganancia_potencial:.2f}")
        print(f"   • Retorno potencial: {ganancia_porcentual:.2f}%")
        print(f"   • Días con precio superior al promedio: {len(dias_superior)} de {num_dias}")
        print(f"   • Porcentaje: {len(dias_superior)/num_dias*100:.1f}%")
        
        if len(dias_superior) <= 20:
            print(f"   • Días: {dias_superior.tolist()}")
        else:
            print(f"   • Primeros 10 días: {dias_superior[:10].tolist()}")
            print(f"   • Últimos 10 días: {dias_superior[-10:].tolist()}")
        
    except Exception as e:
        print(f"❌ Error en ejercicio 9: {e}")

if __name__ == "__main__":
    ejercicio_9()