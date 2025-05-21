# Lista de estudiantes (solo listas anidadas y strings)
estudiantes = [
    ["Miluska123", "1234", "Miluska Gutierrez", "Primaria - 2° A",
     ["Lunes: Matemáticas", "Martes: Comunicación"],
     ["Matemáticas:18", "Comunicación:17"],
     ["Traer material de arte el martes.", "Ensayo del día de la madre."]],
    
    ["Berenisse456", "abcd1", "Berenisse Garcia", "Inicial - 4 años",
     ["Lunes: Psicomotricidad", "Miércoles: Música"],
     ["Psicomotricidad:19", "Música:20"],
     ["Día del color rojo el viernes.", "Llevar juguete favorito el lunes."]]
]
#est[4][0]
# Función para buscar estudiante
def login(usuario, contrasena):
    for est in estudiantes:
        if est[0] == usuario and est[1] == contrasena:
            return est
    return None

# Función para registrar nuevo estudiante con validaciones
def registrar():
    while True:
        usuario = input("Nuevo usuario: ").strip()
        if usuario == "":
            print("El usuario no puede estar vacío.")
        elif " " in usuario:
            print("El usuario no debe contener espacios.")
        elif len(usuario) < 5:
            print("El usuario debe tener al menos 5 caracteres.")
        elif any(est[0] == usuario for est in estudiantes):
            print("Ese usuario ya existe. Intenta con otro.")
        else:
            break

    while True:
        contrasena = input("Nueva contraseña: ").strip()
        if len(contrasena) < 4:
            print("La contraseña debe tener al menos 4 caracteres.")
        elif " " in contrasena:
            print("La contraseña no debe contener espacios.")
        elif not any(c.isdigit() for c in contrasena):
            print("La contraseña debe tener al menos un número.")
        elif not any(c.isalpha() for c in contrasena):
            print("La contraseña debe tener al menos una letra.")
        else:
            break

    nombre = input("Nombre completo: ")
    grado = input("Grado: ")

    nuevo = [usuario, contrasena, nombre, grado, [], [], []]
    estudiantes.append(nuevo)
    print(" Registro exitoso.")
    mostrar_info(nuevo)

# Función para mostrar la información
def mostrar_info(est):
    print("\n=== Información del Estudiante ===")
    print("Nombre:", est[2])
    print("Grado:", est[3])
    print("Horario:")
    for clase in est[4]:
        print("-", clase)
    print("Notas:")
    for nota in est[5]:
        print("-", nota)
    print("Anuncios:")
    for anuncio in est[6]:
        print("-", anuncio)

# Menú principal
print("1. Iniciar sesión")
print("2. Registrar nuevo estudiante")
opcion = input("Elige una opción (1 o 2): ")

if opcion == "1":
    intentos = 3
    while intentos > 0:
        usuario = input("Usuario: ")
        contrasena = input("Contraseña: ")
        estudiante = login(usuario, contrasena)
        if estudiante:
            mostrar_info(estudiante)
            break
        else:
            intentos -= 1
            print("Usuario o contraseña incorrectos. Te quedan", intentos, "intentos.")
    if intentos == 0:
        print("Demasiados intentos. Intenta más tarde.")

elif opcion == "2":
    registrar()

else:
    print("Opción no válida.")
