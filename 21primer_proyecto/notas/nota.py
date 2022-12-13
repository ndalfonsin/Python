import notas.conexion as conexion


connect = conexion.conectar()
database = connect[0]
cursor = connect[1]


class nota:
    def __init__(self, usuario_id, titulo = "", descripcion = ""):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion
    
    

    
    def guardar(self):
        sql = "INSERT INTO note VALUES(null, %s, %s, %s, NOW())"
        nota = (self.usuario_id, self.titulo, self.descripcion)
        try:
            cursor.execute(sql, nota)
            database.commit()

            result =  [cursor.rowcount, self]
        except: 
            result = [0, self]
        return result

    def listar(self):
        sql = f"SELECT * from note WHERE usuario_id = {self.usuario_id}"

        cursor.execute(sql)
        result = cursor.fetchall()

        return result

    def eliminar(self):
        sql = f"DELETE FROM note WHERE usuario_id = {self.usuario_id} AND titulo LIKE '%{self.titulo}%' "

        cursor.execute(sql)
        database.commit()

        return [cursor.rowcount, self]

    
