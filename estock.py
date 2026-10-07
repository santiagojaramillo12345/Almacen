def registrar_prenda(nombre, categoria, talla, color, cantidad, costo, venta):
    sku = f"{categoria[:3].upper()}-{nombre[:3].upper()}-{talla}-{color[:2].upper()}"
    valor_total = cantidad * costo

    return {
        "SKU": sku,
        "PRENDA": nombre,
        "CATEGORIA": categoria.lower(),  # Normalizamos a minúsculas para agrupar mejor
        "TALLA": talla,
        "COLOR": color,
        "CANTIDAD": cantidad,
        "COSTO": costo,
        "VENTA": venta,
        "VALOR_TOTAL": valor_total
    }

# --- Interacción con el usuario en ciclo ---
if __name__ == "__main__":
    print("=== SISTEMA DE REGISTRO Y AGRUPACIÓN POR CATEGORÍA ===")
    
    n_registros = int(input("¿Cuántos registros deseas realizar?: "))
    lista_prendas = []

    for i in range(n_registros):
        print(f"\n--- Registro {i + 1} de {n_registros} ---")
        nombre = input("Ingrese el nombre de la prenda: ")
        categoria = input("Ingrese la categoría: ")
        talla = input("Ingrese la talla: ")
        color = input("Ingrese el color: ")
        cantidad = int(input("Ingrese la cantidad: "))
        costo = float(input("Ingrese el costo unitario: "))
        venta = float(input("Ingrese el precio de venta: "))

        # Llamada a la función y almacenamiento en la lista
        prenda = registrar_prenda(nombre, categoria, talla, color, cantidad, costo, venta)
        lista_prendas.append(prenda)

    # --- Agrupar por Categoría ---
    categorias_dict = {}
    for prenda in lista_prendas:
        cat = prenda["CATEGORIA"]
        if cat not in categorias_dict:
            categorias_dict[cat] = []
        categorias_dict[cat].append(prenda)

    # --- Impresión organizada por Categoría ---
    print("\n" + "="*50)
    print("=== INVENTARIO ORGANIZADO POR CATEGORÍA ===")
    
    stock_total_general = 0
    valor_total_general = 0

    for categoria, prendas in categorias_dict.items():
        print(f"\n[CATEGORÍA: {categoria.upper()}]")
        print("-" * 40)
        
        stock_cat = 0
        valor_cat = 0
        
        for p in prendas:
            print(f"  • Prenda: {p['PRENDA']} | SKU: {p['SKU']} | Talla: {p['TALLA']} | Color: {p['COLOR']}")
            print(f"    Cantidad: {p['CANTIDAD']} | Costo: ${p['COSTO']:.2f} | Venta: ${p['VENTA']:.2f} | Total: ${p['VALOR_TOTAL']:.2f}")
            
            stock_cat += p['CANTIDAD']
            valor_cat += p['VALOR_TOTAL']
        
        print(f"  > Subtotal Categoría '{categoria}': {stock_cat} unidades | Valor: ${valor_cat:,.2f}")
        
        stock_total_general += stock_cat
        valor_total_general += valor_cat

    # --- Resumen Final ---
    print("\n" + "="*50)
    print("=== RESUMEN GENERAL GLOBAL ===")
    print(f"Stock total en inventario: {stock_total_general} unidades")
    print(f"Valor total general del inventario: ${valor_total_general:,.2f}")
    print("="*50)