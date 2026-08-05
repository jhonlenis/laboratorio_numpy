import numpy as np

def ejercicio_8():
    """
    Registra las edades de 500 personas.
    Calcula: promedio, mediana, moda, máxima, mínima, mayores de edad.
    """
    print("\n" + "="*70)
    print("EJERCICIO 8: ENCUESTA NACIONAL (500 personas)")
    print("="*70)
    
    try:
        # Generar 500 edades (18-80 años)
        num_personas = 500
        edades = np.random.randint(18, 81, num_personas)
        
        # Calcular estadísticas
        promedio = np.mean(edades)
        mediana = np.median(edades)
        minima = np.min(edades)
        maxima = np.max(edades)
        
        # Calcular moda (edad que más se repite)
        # Con NumPy: usar unique con return_counts
        valores_unicos, conteos = np.unique(edades, return_counts=True)
        indice_moda = np.argmax(conteos)
        moda = valores_unicos[indice_moda]
        
        # Mayores de edad (>=18)
        mayores_edad = np.sum(edades >= 18)
        menores_edad = np.sum(edades < 18)
        
        # Rango de edad más frecuente
        rango_20_30 = np.sum((edades >= 20) & (edades < 30))
        rango_30_40 = np.sum((edades >= 30) & (edades < 40))
        rango_40_50 = np.sum((edades >= 40) & (edades < 50))
        rango_50_60 = np.sum((edades >= 50) & (edades < 60))
        rango_60_70 = np.sum((edades >= 60) & (edades < 70))
        
        # Mostrar resultados
        print(f"\n👥 PRIMERAS 30 EDADES:")
        print(edades[:30])
        
        print(f"\n📊 ESTADÍSTICAS DESCRIPTIVAS:")
        print(f"   • Promedio de edad: {promedio:.2f} años")
        print(f"   • Mediana: {mediana:.0f} años")
        print(f"   • Moda: {moda:.0f} años (aparece {conteos[indice_moda]} veces)")
        print(f"   • Edad mínima: {minima} años")
        print(f"   • Edad máxima: {maxima} años")
        print(f"   • Rango: {maxima - minima} años")
        
        print(f"\n👨‍👩‍👧‍👦 DISTRIBUCIÓN POR EDAD:")
        print(f"   • Mayores de 18 años: {mayores_edad} personas ({mayores_edad/num_personas*100:.1f}%)")
        print(f"   • Menores de 18 años: {menores_edad} personas ({menores_edad/num_personas*100:.1f}%)")
        
        print(f"\n📈 DISTRIBUCIÓN POR RANGOS:")
        print(f"   • 20-30 años: {rango_20_30} personas ({rango_20_30/num_personas*100:.1f}%)")
        print(f"   • 30-40 años: {rango_30_40} personas ({rango_30_40/num_personas*100:.1f}%)")
        print(f"   • 40-50 años: {rango_40_50} personas ({rango_40_50/num_personas*100:.1f}%)")
        print(f"   • 50-60 años: {rango_50_60} personas ({rango_50_60/num_personas*100:.1f}%)")
        print(f"   • 60-70 años: {rango_60_70} personas ({rango_60_70/num_personas*100:.1f}%)")
        
    except Exception as e:
        print(f"❌ Error en ejercicio 8: {e}")

if __name__ == "__main__":
    ejercicio_8()