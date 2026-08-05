"""
Script principal del sistema:
- Solicita autenticación (login desde CSV).
- Presenta menú CRUD para gestionar usuarios.
- Maneja flujos principales y mensajes de salida.
"""

import csv
from funciones import *

repeat = True
while repeat:
    print("\033[95m\nLOGIN\033[0m")
    email = input("Correo: ").lower()
    password = input("Contraseña: ").lower()

    validate = validate_login(email, password)

    if validate == True: 
        print("\033[92m\nBienvenido, inició sesión correctamente.\033[0m")
        # Menú principal: permite CRUD de usuarios repitiendo hasta que el usuario decida salir
        while True:
            choice = menu_crud()
            if choice == 1:
                create_user()  # Opción para crear usuario
            elif choice == 2:
                show_users()   # Opción para mostrar usuarios
            elif choice == 3:
                update_user()  # Opción para actualizar usuario
            elif choice == 4:
                delete_user()  # Opción para eliminar usuario
            elif choice == 5:
                search_user()  # Opción para buscar usuario
            else:
                print("\033[93m\n¡Bye!\033[0m")
                repeat = False
                break
    elif validate == False:
        print("\033[91m\n¡ERROR! Correo o contraseña son incorrectos, intente nuevamente.\033[0m")
    else:
        repeat = False
