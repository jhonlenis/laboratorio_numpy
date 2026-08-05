import numpy as np
from collections import Counter

def incrementar_brillo(imagen, factor=1.2):
    """
    Incrementa el brillo de una imagen multiplicando los valores por un factor.
    Utiliza clip() para mantener valores entre 0 y 255.
    
    Args:
        imagen: matriz NumPy con valores 0-255
        factor: factor multiplicativo (>1 aumenta brillo)
    
    Returns:
        imagen procesada
    """
    imagen_brillo = imagen * factor
    # clip() limita los valores al rango permitido
    return np.clip(imagen_brillo, 0, 255)
 
 
def disminuir_brillo(imagen, factor=0.8):
    """
    Disminuye el brillo de una imagen multiplicando los valores por un factor.
    
    Args:
        imagen: matriz NumPy con valores 0-255
        factor: factor multiplicativo (<1 disminuye brillo)
    
    Returns:
        imagen procesada
    """
    imagen_oscura = imagen * factor
    return np.clip(imagen_oscura, 0, 255)
 
 
def invertir_colores(imagen):
    """
    Invierte los colores de la imagen (negativo fotográfico).
    Fórmula: 255 - valor_pixel
    
    Args:
        imagen: matriz NumPy con valores 0-255
    
    Returns:
        imagen con colores invertidos
    """
    return 255 - imagen
 
 
def transponer_imagen(imagen):
    """
    Obtiene la imagen transpuesta (rotación 90 grados).
    Utiliza transpose() de NumPy.
    
    Args:
        imagen: matriz NumPy
    
    Returns:
        imagen transpuesta
    """
    return np.transpose(imagen)
 
 
def ejercicio_6():
    """
    Procesa una imagen en escala de grises (matriz 15×15).
    Permite: incrementar brillo, disminuir brillo, invertir colores, transponer.
    """
    print("\n" + "="*70)
    print("EJERCICIO 6: PROCESAMIENTO DE IMÁGENES (15×15)")
    print("="*70)
    
    try:
        # Crear matriz 15×15 con valores entre 0-255
        imagen_original = np.random.randint(0, 256, (15, 15))
        
        # Aplicar transformaciones
        imagen_brillo_aumentado = incrementar_brillo(imagen_original, 1.3)
        imagen_brillo_disminuido = disminuir_brillo(imagen_original, 0.7)
        imagen_invertida = invertir_colores(imagen_original)
        imagen_transpuesta = transponer_imagen(imagen_original)
        
        # Mostrar resultados
        print(f"\n🖼️ IMAGEN ORIGINAL (primeras 5×5):")
        print(imagen_original[:5, :5])
        
        print(f"\n🖼️ BRILLO AUMENTADO 30% (primeras 5×5):")
        print(imagen_brillo_aumentado[:5, :5].astype(int))
        
        print(f"\n🖼️ BRILLO DISMINUIDO 30% (primeras 5×5):")
        print(imagen_brillo_disminuido[:5, :5].astype(int))
        
        print(f"\n🖼️ COLORES INVERTIDOS (primeras 5×5):")
        print(imagen_invertida[:5, :5])
        
        print(f"\n🖼️ IMAGEN TRANSPUESTA (primeras 5×5):")
        print(imagen_transpuesta[:5, :5])
        
        print(f"\n📊 ESTADÍSTICAS:")
        print(f"   • Valor promedio original: {np.mean(imagen_original):.2f}")
        print(f"   • Valor promedio (brillo +): {np.mean(imagen_brillo_aumentado):.2f}")
        print(f"   • Valor promedio (brillo -): {np.mean(imagen_brillo_disminuido):.2f}")
        print(f"   • Valor promedio (invertida): {np.mean(imagen_invertida):.2f}")
        
    except Exception as e:
        print(f"❌ Error en ejercicio 6: {e}")


if __name__ == "__main__":
    ejercicio_6()
