# Lista de estudiantes (con diccionarios)
estudiantes = [
    {
        "usuario": "Miluska123",
        "contrasena": "1234",
        "nombre": "Miluska Gutierrez",
        "grado": "Primaria - 2° A",
        "horario": ["Lunes: Matemáticas", "Martes: Comunicación"],
        "notas": ["Matemáticas:18", "Comunicación:17"],
        "anuncios": ["Traer material de arte el martes.", "Ensayo del día de la madre."]
    },
    { #hola mundo
        "usuario": "Berenisse456",
        "contrasena": "abcd1",
        "nombre": "Berenisse Garcia",
        "grado": "Inicial - 4 años",
        "horario": ["Lunes: Psicomotricidad", "Miércoles: Música"],
        "notas": ["Psicomotricidad:19", "Música:20"],
        "anuncios": ["Día del color rojo el viernes.", "Llevar juguete favorito el lunes."]
    }
]
#hola mundo 2
# Función para buscar estudiante
def login(usuario, contrasena):
    for est in estudiantes:
        if est["usuario"] == usuario and est["contrasena"] == contrasena:
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
        elif any(est["usuario"] == usuario for est in estudiantes):
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

    nuevo_estudiante = {
        "usuario": usuario,
        "contrasena": contrasena,
        "nombre": nombre,
        "grado": grado,
        "horario": [],
        "notas": [],
        "anuncios": []
    }

    estudiantes.append(nuevo_estudiante)
    print("Registro exitoso.")
    mostrar_info(nuevo_estudiante)

# Función para mostrar la información
def mostrar_info(est):
    print("\n=== Información del Estudiante ===")
    print("Nombre:", est["nombre"])
    print("Grado:", est["grado"])
    print("Horario:")
    for clase in est["horario"]:
        print("-", clase)
    print("Notas:")
    for nota in est["notas"]:
        print("-", nota)
    print("Anuncios:")
    for anuncio in est["anuncios"]:
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
