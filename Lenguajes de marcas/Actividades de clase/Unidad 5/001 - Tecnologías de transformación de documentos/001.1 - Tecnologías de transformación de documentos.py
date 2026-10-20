import pandas as pd

# 1. Cargamos el archivo de Excel
# Nos aseguramos de tener instalada la librería 'openpyxl'
try:
    archivo_excel = pd.read_excel('noticias.xlsx')
    
    # 2. Procesamos el contenido convirtiéndolo a una cadena de texto
    # Usamos to_string() para mantener la estructura visual de las columnas
    contenido_texto = archivo_excel.to_string()
    
    # 3. Guardamos el resultado en un nuevo archivo de texto
    with open('noticias_convertidas.txt', 'w', encoding='utf-8') as archivo_destino:
        archivo_destino.write(contenido_texto)
        
    print("La conversión de Excel a TXT se ha realizado con éxito.")

except Exception as e:
    print(f"Nosotros hemos detectado un error: {e}")
