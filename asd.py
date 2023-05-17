texto = input("Ingrese un texto: ")
letra1 = input("Ingrese la primer letra: ")
letra2 = input("Ingrese la segunda letra: ")
letra3 = input("Ingrese la tercer letra: ")

lista = texto.split()
minuscula = texto.lower()

print("\n")
print(f"La {letra1} aparece {minuscula.count(letra1)} veces en el texto.")
print(f"La {letra2} aparece {minuscula.count(letra2)} veces en el texto.")
print(f"La {letra3} aparece {minuscula.count(letra3)} veces en el texto.")
print("\n")


longitud = len(texto.split())

print("\n")
print(f"El texto contiene {longitud} palabras.")
print("\n")

print(f"la primera letra del texto es {texto[0]} y la última letra es {texto[-1]}")
print("\n")


print("El texto en reversa es:")
print(texto[::-1])
print("\n")

if "python" in minuscula:
    print("El texto si contiene la palabra python")
else:
    print("El texto NO contiene la palabra python")