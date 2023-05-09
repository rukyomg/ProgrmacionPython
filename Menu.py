import Agenda


mi_agenda = Agenda.Agenda("agenda", "contactos")


while True:
    print("\t -----------------------------------")
    print("\t -       1. Añadir Contacto        -")
    print("\t -      2. Eliminar Contacto       -")
    print("\t -     3. Actualizar Contacto      -")
    print("\t -----------------------------------")

    opciones = input("Selecciona la acción que quieres realizar: ")

    if opciones == "1":
        nombre = input("Introduce el nombre: ")
        apellido = input("Introduce el apellido: ")
        telefono = input("Introduce el teléfono: ")
        email = input("Introduce el email: ")
        mi_agenda.insertar_contacto(nombre, apellido, telefono, email)
        break

    if opciones == "2":
        id = input("Introduce el id del usuario que quieres borrar: ")
        mi_agenda.borrar_contacto(id)
        break

    if opciones == "3":
        print("Has elegido actualizar contactos")
        id = input("Selecciona el ID del contacto que deseas actualizar: ")
        nombre = input("Introduce el nuevo nombre: ")
        apellido = input("Introduce el nuevo apellido: ")
        telefono = input("Introduce el nuevo número de teléfono: ")
        email = input("Introduce el nuevo correo electrónico: ")
        mi_agenda.actualizar_contacto(id, nombre, apellido, telefono, email)
        break

   