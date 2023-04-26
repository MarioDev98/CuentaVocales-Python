def contar_vocales(frase):
    conteo_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    frase = frase.lower()
    for char in frase:
        if char in conteo_vocales:
            conteo_vocales[char] += 1
    return conteo_vocales

frase = input("Introduce una frase: ")
conteo = contar_vocales(frase)

print("Conteo de vocales en la frase:")
for vocal, conteo_vocal in conteo.items():
    print(f"{vocal}: {conteo_vocal}")