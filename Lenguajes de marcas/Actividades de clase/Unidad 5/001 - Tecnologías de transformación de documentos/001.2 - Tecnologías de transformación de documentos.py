from fpdf import FPDF

# 1. Configuramos el documento PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# 2. Leemos el contenido del archivo de texto
try:
    with open('noticias_convertidas.txt', 'r', encoding='utf-8') as f:
        for linea in f:
            # Insertamos cada línea en el PDF
            pdf.cell(200, 10, txt=linea, ln=True, align='L')
    
    # 3. Exportamos el archivo final
    pdf.output("informe_final.pdf")
    print("Nosotros hemos generado el PDF correctamente.")

except FileNotFoundError:
    print("Error: Nosotros no hemos encontrado el archivo de origen.")
