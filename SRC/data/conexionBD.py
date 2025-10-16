import psycopg2
class conexion:
    _USER = "postgres"
    _PASSWORD = "admin"
    _HOST = "127.0.0.1"
    _PORT = "5432"
    _DATABASE = "sistemaPrestamo"

    @classmethod
    def getConexion(cls):
        try:
            return psycopg2.connect(
                user=cls._USER,
                password=cls._PASSWORD,
                host=cls._HOST,
                port=cls._PORT,
                database=cls._DATABASE
            )
        except Exception as e:
            print(f"Ocurrió un error al conectar: {e}")
            return None