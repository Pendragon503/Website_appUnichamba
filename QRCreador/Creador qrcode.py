import qrcode

def generar_qr(texto):
    # Crear un objeto de código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Añadir los datos al código QR
    qr.add_data(texto)
    qr.make(fit=True)
    
    # Crear una imagen del código QR
    img = qr.make_image(fill='black', back_color='white')
    
    # Guardar la imagen del código QR
    img.save('codigo_qr.png')
    print("Código QR generado y guardado como 'codigo_qr.png'")

def main():
    # Preguntar al usuario por el texto a convertir en QR
    texto = input("Ingrese el texto a convertir en un código QR: ")
    generar_qr(texto)

if __name__ == "__main__":
    main()
