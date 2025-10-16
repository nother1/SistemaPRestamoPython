import sys
import os
# Añadir SRC al path para poder importar desde cualquier subcarpeta
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from data.conexionBD import conexion
from classes.user import user

class userControllerDAO:
    @classmethod
    def createUsers(cls):
        conn = conexion.getConexion()
        if conn is None:
            print("No se pudo conectar a la base de datos.")
            return

        try:
            cursor = conn.cursor()
            persona = user('Jhonatan','123','admin','1036659275')
            persona1 = user('Nother','123','user','95050815928')
            sentencia = "INSERT INTO usuarios (user_name, user_password, user_rol, user_document) VALUES (%s,%s,%s,%s)"

            cursor.execute(sentencia, (persona.userName, persona.userPassword, persona.userRole, persona.userDocument))
            cursor.execute(sentencia, (persona1.userName, persona1.userPassword, persona1.userRole, persona1.userDocument))

            conn.commit()
            print("Usuarios creados correctamente.")
        except Exception as e:
            print(f"Error al crear usuarios: {e}")
            conn.rollback()
        finally:
            conn.close()

    @classmethod
    def loginUser(cls,username, userpassword):
        conn = conexion.getConexion()
        if conn is None:
            print("No se pudo conectar a la base de datos.")
            return
        try:
            cursor = conn.cursor()
            sentencia = "SELECT * FROM usuarios WHERE user_document = %s AND user_password = %s"
            cursor.execute(sentencia, (username,userpassword))
            userLogin = cursor.fetchone()
            return userLogin
        except Exception as e:
            print(f"Error al crear usuarios: {e}")
            conn.rollback()
        finally:
            conn.close()
            
    @classmethod
    def searchUserByDocument(cls,documentUser):
        conn = conexion.getConexion()
        if conn is None:
            print("No se pudo conectar a la base de datos.")
            return
        try:
            cursor = conn.cursor()
            sentencia = "SELECT * FROM usuarios WHERE user_document = %s"
            cursor.execute(sentencia, (documentUser,))
            userLogin = cursor.fetchone()
            return userLogin
        except Exception as e:
            print(f"Error al buscar usuario: {e}")
            conn.rollback()
        finally:
            conn.close()