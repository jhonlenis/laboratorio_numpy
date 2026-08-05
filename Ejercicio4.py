import numpy as np

def ejercicio_4():
    """
    Registra existencias de 15 productos en 8 sucursales.
    Calcula: producto con mayor existencia, sucursal con menor inventario,
    inventario total y promedio, identifica productos agotados.
    """
    print("\n" + "="*70)
    print("EJERCICIO 4: INVENTARIO INTELIGENTE (15 productos × 8 sucursales)")
    print("="*70)
    
    try:
        # Crear matriz 15×8 con existencias aleatorias (0-1000)
        productos = 15
        sucursales = 8
        matriz_inventario = np.random.randint(0, 1000, (productos, sucursales))
        
        # Inventario total por producto
        inventario_por_producto = np.sum(matriz_inventario, axis=1)
        
        # Inventario total por sucursal
        inventario_por_sucursal = np.sum(matriz_inventario, axis=0)
        
        # Producto con mayor existencia
        producto_mayor = np.argmax(inventario_por_producto) + 1
        
        # Sucursal con menor inventario
        sucursal_menor = np.argmin(inventario_por_sucursal) + 1
        
        # Inventario total y promedio
        inventario_total = np.sum(matriz_inventario)
        inventario_promedio = np.mean(matriz_inventario)
        
        # Productos agotados (usando where())
        productos_agotados = np.where(inventario_por_producto == 0)[0] + 1
        
        # Mostrar resultados
        print(f"\n📦 INVENTARIO POR PRODUCTO (primeros 10):")
        for i in range(min(10, productos)):
            print(f"   Producto {i+1}: {inventario_por_producto[i]} unidades")
        
        print(f"\n🏪 INVENTARIO POR SUCURSAL:")
        for i in range(sucursales):
            print(f"   Sucursal {i+1}: {inventario_por_sucursal[i]} unidades")
        
        print(f"\n📊 ESTADÍSTICAS GENERALES:")
        print(f"   • Inventario total: {inventario_total} unidades")
        print(f"   • Inventario promedio: {inventario_promedio:.2f} unidades")
        print(f"   • Producto con mayor existencia: Producto {producto_mayor} ({inventario_por_producto[producto_mayor-1]} unidades)")
        print(f"   • Sucursal con menor inventario: Sucursal {sucursal_menor} ({inventario_por_sucursal[sucursal_menor-1]} unidades)")
        
        if len(productos_agotados) > 0:
            print(f"   ⚠️ Productos agotados: {productos_agotados.tolist()}")
        else:
            print(f"   ✅ No hay productos agotados")
        
    except Exception as e:
        print(f"❌ Error en ejercicio 4: {e}")

if __name__ == "__main__":
    ejercicio_4()