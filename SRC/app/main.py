import sys
import os
# Añadir SRC al path para poder importar desde cualquier subcarpeta
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from controller.userControllerDAO import userControllerDAO
from controller.prestamoControllerDAO import prestamoControllerDAO
if __name__ == "__main__":
    userControllerDAO.createUsers()
    username = input("Ingrese su usuario: ")
    password = input("Ingrese su contraseña: ")
    userLogin = userControllerDAO.loginUser(username,password)
    opcion = None
    if userLogin:
        id, user_name, user_password, user_role, user_document = userLogin
        if user_role == 'admin':
            while opcion != 6:
                print("""**** Sistema Prestamos Admin \n
                    1. Ver prestamos usuarios
                    2. Ver prestamos por fechas
                    3. Ver Prestamos por usuario y fecha
                    4. Cambiar el estado de un prestamo
                    5. Buscar por id de prestamo
                    6. Cerrar cession""")
                opcion = int(input("Seleccione una opcion: "))
                if opcion == 1:
                    documentUser = input("Ingrese el documento del usuario: ")
                    searchUser = userControllerDAO.searchUserByDocument(documentUser)
                    id = searchUser[0]
                    prestamoController = prestamoControllerDAO.buscarPrestamos(id)
                    print(prestamoController)
                elif opcion == 2:
                    fecha_inicio = input("Ingrese fecha inicio en formato yyyy-mm-dd ")
                    fecha_final = input("Ingrese fecha inicio en formato yyyy-mm-dd ")
                    prestamoController = prestamoControllerDAO.buscarPrestamos(fechaPrestamoInicio=fecha_inicio,fechaPrestamoFinal=fecha_final)
                    print(prestamoController)
                elif opcion == 3:
                    documentUser = input("Ingrese el documento del usuario: ")
                    searchUser = userControllerDAO.searchUserByDocument(documentUser)
                    id = searchUser[0]
                    fecha_inicio = input("Ingrese fecha inicio en formato yyyy-mm-dd ")
                    fecha_final = input("Ingrese fecha inicio en formato yyyy-mm-dd ")
                    prestamoController = prestamoControllerDAO.buscarPrestamos(idUser=id,fechaPrestamoInicio=fecha_inicio,fechaPrestamoFinal=fecha_final)
                    print(prestamoController)
                elif opcion == 4:
                    idPrestamo = int(input("Ingrese el id del prestamo a cambiar su estado: "))
                    prestamoController = prestamoControllerDAO.changeStatus(idPrestamo)
                elif opcion == 5:
                    id_prestamo = int(input("Ingrese el id del prestamo: "))
                    prestamoController = prestamoControllerDAO.buscarPrestamos(idPrestamo=id_prestamo)
                    print(prestamoController)
                elif opcion == 6:
                    print("Gracias por utilizar nuestros servicios: ")
                    break
            
        if user_role == 'user':
            while opcion != 3:
                print("""*** Sistema de prestamos *** 
                        Seleccione una opcion 
                        1. Registrar prestamo
                        2. ver mis prestamos
                        3. cerrar session
                    """)
                opcion = int(input("Que opcion desea: "))
                if opcion == 1:
                    prestamoController = prestamoControllerDAO.ingresarPrestamo(id)
                elif opcion == 2:
                    prestamoController = prestamoControllerDAO.buscarPrestamos(id)
                    print(prestamoController)
                elif opcion == 3:
                    print("Gracias por utilizar nuestros servicios: ")
                    break