def vocales(palabra):
  return palabra in "a"
def vocale(palabra):
  return palabra in "e"
def vocali(palabra):
  return palabra in "i"
def vocalo(palabra):
  return palabra in "o"
def vocalu(palabra):
  return palabra in "u"

palabra = input("Ingresa una frase: ");
palabra_modificada = palabra.lower()
cant_vocales = 0
cant_vocalese = 0
cant_vocalesi = 0
cant_vocaleso = 0
cant_vocalesu = 0
for indice in palabra_modificada:
  if indice.isalpha() and   vocales(indice):
    cant_vocales +=1
print(f"En la frase {palabra} existe { cant_vocales} vocales a")

for indice in palabra_modificada:
  if indice.isalpha() and   vocale(indice):
    cant_vocalese +=1
print(f"En la frase {palabra} existe { cant_vocalese} vocales e")

for indice in palabra_modificada:
  if indice.isalpha() and   vocali(indice):
    cant_vocalesi +=1
print(f"En la frase {palabra} existe { cant_vocalesi} vocales i")

for indice in palabra_modificada:
  if indice.isalpha() and   vocalo(indice):
    cant_vocaleso +=1
print(f"En la frase {palabra} existe { cant_vocaleso} vocales o")

for indice in palabra_modificada:
  if indice.isalpha() and   vocalu(indice):
    cant_vocalesu +=1
print(f"En la frase {palabra} existe { cant_vocalesu} vocales u")

