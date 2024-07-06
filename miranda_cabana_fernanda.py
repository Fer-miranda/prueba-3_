import csv
lista_curso = []
def procesar_lista():
    archivo = input("Ingrese el nombre del archivo CSV: ")
    with open(archivo, newline='') as archivo_csv:
        lector = csv.DictReader(archivo_csv)
        for fila in lector:
            rut = fila.get('Rut')
            nombre = fila.get('Nombre')
            nota1 = fila.get('Nota 1')
            nota2 = fila.get('Nota 2')
            if not nombre or not rut or not nota1 or not nota2:
                print(f"Fila inválida: {fila}")
                continue
            estudiante = {
                "rut": rut,
                "nombre": nombre,
                'nota 1': nota1,
                'nota 2': nota2
            }
            lista_curso.append(estudiante)
        print("Carga masiva completada exitosamente.")

def registrar_estudiante():
    try: 
        rut = input("Ingresa el rut del estudiante: ")
        nombre = input("Ingresa el nombre del estudiante: ")
        nota1 = float(input("Ingresa la nota 1 del estudiante: "))
        nota2 = float(input("Ingresa la nota 2 del estudiante: "))
        estudiante = {
            'rut': rut,
            'nombre': nombre,
            'nota 1': nota1,
            'nota 2': nota2
        }
        
        lista_curso.append(estudiante)
        print("Estudiante ingresado exitosamente")
    except:
        print("Error, ingresa un valor válido")

def modificar_nota():
    if not lista_curso:
        print("No hay estudiantes regisrados")
    else:
        rut = input("Ingrese el rut del estudiante: ")
        for estudiante in lista_curso:
            if estudiante['rut'] == rut:
                    modificar = int(input("Modificar Nota 1 (1) o Nota 2 (2)"))
                    if modificar == 1:
                        estudiante['nota 1'] = float(input("Ingrese la nueva nota 1 del estudiante: "))
                    elif modificar == 2:
                        estudiante['nota 2'] = float(input("Ingrese la nueva nota 2 del estudiante: "))
            print("Nota modificada exitosamente.")
            return
        print("No se encontró un estudiante con ese rut.")

def eliminar_estudiante():
    if not lista_curso:
        print("No hay estudiantes registrados")
    else:
        rut = input("Ingrese el rut del estudiante a eliminar: ")
        for estudiante in lista_curso:
            if estudiante['rut'] == rut:
                confirmacion = input(f"Está seguro que quiere eliminar (Si/No) {estudiante['nombre']}").lower()
                if confirmacion == 'si':
                    lista_curso.remove(estudiante)
                    print("estudiante eliminado exitosamente.")
                    return
                else:
                    break

def generar_promedio():
    nuevo_campo = input("Ingrese el nombre del nuevo campo: ")
    for estudiante in lista_curso:
        estudiante[nuevo_campo] = (estudiante['nota 1'] + estudiante['nota 2'])/2
    print(f"Campo '{nuevo_campo}' agregado exitosamente")

def listar():
    if not lista_curso:
        print("No hay estudiantes registrados")
    else:
        for estudiante in lista_curso:
            print(f"Nombre: {estudiante['nombre']},\nNota 1: {estudiante['nota 1']},\nNota 2: {estudiante['nota 2']}")

def generar_acta():
    if not lista_curso:
        print("No hay estudiantes registrados")
    else:
        generar_archivo(lista_curso, 'estudiantes.csv')
        print("Archivo generado exitosamente")
        return

def generar_archivo(lista_curso, archivo):
    with open(archivo, 'w', newline='') as archivo_csv:
        writer = csv.DictWriter(archivo_csv, fieldnames=lista_curso[0].keys())
        writer.writeheader()
        for estudiante in lista_curso:
            writer.writerow(estudiante)
    print("Archivo generado exitosamente")   


def salir():
    print("Saliendo del programa")
    exit()

def menu():
    while True:
        try:
            option = int(input("Seleccione una opción: \n1. Procesar Lista\n2. Registrar estudiante\n3. Modificar nota\n4. Eliminar estudiante\n5. Generar promedio\n6. Generar Acta de curso\n7. Salir"))
            if option == 1:
                procesar_lista()
            elif option == 2:
                registrar_estudiante()
            elif option == 3:
                modificar_nota()
            elif option == 4:
                eliminar_estudiante()
            elif option == 5:
                generar_promedio()
            elif option == 6:
                generar_acta()
            elif option == 7:
                salir()
            elif option == 8:
                listar()
            else:
                print("Ingresa una opción válida")
        except ValueError:
            print("Ingresa una opción válida")
        
menu()