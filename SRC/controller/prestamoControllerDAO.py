import sys
import os
# Añadir SRC al path para poder importar desde cualquier subcarpeta
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from data.conexionBD import conexion
from classes.prestamo import prestamo
from datetime import date

class prestamoControllerDAO:
    @classmethod
    def ingresarPrestamo(cls,idUser):
        conn = conexion.getConexion()
        if conn is None:
            print("No se pudo conectar a la base de datos.")
            return
        try:
            cursor = conn.cursor()
            nuevoPrestamo = prestamo(idUser,date.today(),False)
            sql = "INSERT INTO prestamos (id_user,date,devuelto) VALUES (%s,%s,%s)"
            cursor.execute(sql,(nuevoPrestamo.idUser, nuevoPrestamo.fechaPrestamo,nuevoPrestamo.estadoPrestamo))
            conn.commit()
            print("Prestamo registrado.")
        except Exception as e:
            print(f"Error al crear prestamo: {e}")
            conn.rollback()
        finally:
            conn.close()
    
    @classmethod
    def buscarPrestamos(cls,idUser=None,fechaPrestamoInicio = None,fechaPrestamoFinal = None, idPrestamo = None ):
        conn = conexion.getConexion()
        if conn is None:
            print("No se pudo conectar a la base de datos.")
            return
        try:
            cursor = conn.cursor()
            if idUser != None and fechaPrestamoInicio == None and fechaPrestamoFinal == None:
                sql = "SELECT * FROM prestamos WHERE id_user = %s"
                cursor.execute(sql,(idUser,))
            elif idUser == None and fechaPrestamoInicio != None and fechaPrestamoFinal != None:
                sql = "SELECT * FROM prestamos WHERE date BETWEEN %s AND %s"
                cursor.execute(sql,(fechaPrestamoInicio, fechaPrestamoFinal))
            elif idUser != None and fechaPrestamoInicio != None and fechaPrestamoFinal != None:
                sql = "SELECT * FROM prestamos WHERE id_user = %s AND date BETWEEN %s AND %s"
                cursor.execute(sql,(idUser,fechaPrestamoInicio, fechaPrestamoFinal))
            elif idPrestamo != None:
                sql = "SELECT * FROM prestamos WHERE id_prestamo = %s"
                cursor.execute(sql,(idPrestamo,))
            prestamos = cursor.fetchall()
            return prestamos
        except Exception as e:
            print(f"Error al crear prestamo: {e}")
            conn.rollback()
        finally:
            conn.close()
    
    @classmethod
    def changeStatus(cls,idprestamo):
        conn = conexion.getConexion()
        if conn is None:
            print("No se pudo conectar a la base de datos.")
            return
        try:
            cursor = conn.cursor()
            sql = "UPDATE prestamos SET devuelto = %s WHERE id_prestamo = %s"
            cursor.execute(sql,(True,idprestamo))
            conn.commit()
            print("Cambio realizado")
        except Exception as e:
            print(f"Error al crear prestamo: {e}")
            conn.rollback()
        finally:
            conn.close()