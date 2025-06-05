print("******* EL SIGUIENTE PROGRAMA CALCULA EL PROMEDIO DE X CANTIDAD DE ALUMNOS *******")
print("*******  DESAPROBO: 1 - 5    /   APROBADOS: 6 - 10   *******")

# Programa para cargar alumnos y calcular su promedio

#Se declara la lista
alumnos = []

while True:
    nombre = input("Nombre del alumno (0 para salir): ")
 # Si se ingresa un 0 por teclado se termina el bucle 
    if nombre == "0":
        break

    apellido = input("Apellido del alumno: ")

    notas = []
    # Se evaluan las 3 notas
    for i in range(1, 4):
         while True:
            try:
                nota = float(input(f"Ingrese la nota {i} (1-10): "))
                # Se verifica que la nota este entre 1 y 10
                if 1 <= nota <= 10:
                    # Si es correcto se guarda
                    notas.append(nota)
                    break
                else:
                    print("La nota debe estar entre 1 y 10.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
    # Se evalua el promedio de las notas. Suma las notas y divide por 3
    promedio = sum(notas) / len(notas)

    # Muestra si aprobo con el promedio y lo guarda
    if promedio >= 6:
        estado = "Aprobado"
    else:
        estado = "Desaprobado"

    # Guarda los alumnos
    alumno = {
        "nombre": nombre,
        "apellido": apellido,
        "promedio": promedio,
        "estado": estado
    }
    # Los lista
    alumnos.append(alumno)

print("\n--- Listado de Alumnos ---")
# Se imprime la lista de alumnos
for a in alumnos:
    print(f"{a['nombre']} {a['apellido']} - Promedio: {a['promedio']:.2f} - {a['estado']}")
