from mysql import connector

class Model:
    """
    ****************************************
    *Model de datos con MYSQL para un cine*
    ****************************************
    """
    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()

    def read_config_db(self):
        d = {}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val
        return d

    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()

    def close_db(self):
        self.cnx.close()

    """
    ***************************
    *Metodos para los clientes*
    ***************************
    """

    def crear_usuario(self, u_nombre, u_apellidos, u_correo, u_telefono):
        try:
            sql = 'INSERT into usuarios(`u_nombre`, `u_apellidos`, `u_correo`,`u_telefono`) values (%s, %s, %s, %s)'
            vals = (u_nombre, u_apellidos, u_correo, u_telefono)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def leer_un_usuario(self, id_usuario):
        try:
            sql = 'SELECT * FROM usuarios WHERE id_usuario = %s'
            vals = (id_usuario,)
            self.cursor.execute(sql, vals)
            registro = self.cursor.fetchone() 
            return registro
        except connector.Error as err:
            return err

    def leer_todo_usuarios(self):
        try:
            sql = 'SELECT * FROM usuarios'
            self.cursor.execute(sql)
            registros = self.cursor.fetchall() 
            return registros
        except connector.Error as err:
            return err

    def actualizar_usuarios(self, fields, vals):
        try:
            sql = 'UPDATE usuarios set '+','.join(fields)+'WHERE id_usuario = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def borrar_usuario(self, id_usuario):
        try:
            sql = 'DELETE from usuarios where id_usuario = %s' 
            vals = (id_usuario,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    """
    **********************************
    *Metodos para los administradores*
    **********************************
    """
    def crear_admin(self, a_nombre, a_apellidos, a_posicion, a_correo, a_telefono, a_pass):
        try:
            sql = 'INSERT into administrador(`a_nombre`, `a_apellidos`, `a_posicion`, `a_correo`, `a_telefono`, `a_pass`) values (%s,%s,%s,%s,%s,%s)'
            vals = (a_nombre, a_apellidos, a_posicion, a_correo, a_telefono, a_pass)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def leer_un_admin(self, id_admin):
        try:
            sql = 'SELECT * FROM administrador WHERE id_admin = %s'
            vals = (id_admin,)
            self.cursor.execute(sql, vals)
            registro = self.cursor.fetchone()
            return registro
        except connector.Error as err:
            return err

    def leer_todo_admin(self):
        try:
            sql = 'SELECT * FROM administrador'
            self.cursor.execute(sql)
            registros = self.cursor.fetchall()
            return registros
        except connector.Error as err:
            return err

    def actualizar_admin(self, fields, vals):
        try:
            sql = 'UPDATE administrador set '+','.join(fields)+'WHERE id_admin = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def borrar_admin(self, id_admin):
        try:
            sql = 'DELETE from administrador where id_admin = %s' 
            vals = (id_admin,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ****************************
    *Metodos para las peliculas*
    ****************************
    """
    def crear_pelicula(self, nombre, lenguaje, sinopsis):
        try:
            sql = 'INSERT into pelicula(`nombre`, `lenguaje`, `sinopsis`) values (%s,%s,%s)'
            vals = (nombre, lenguaje, sinopsis)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def leer_pelicula(self, id_pelicula):
        try:
            sql = 'SELECT * FROM pelicula WHERE id_pelicula = %s'
            vals = (id_pelicula,)
            self.cursor.execute(sql, vals)
            registro = self.cursor.fetchone()
            return registro
        except connector.Error as err:
            return err

    def leer_todas_peliculas(self):
        try:
            sql = 'SELECT * FROM pelicula'
            self.cursor.execute(sql)
            registros = self.cursor.fetchall()
            return registros
        except connector.Error as err:
            return err

    def lenguaje_pelicula(self, id_pelicula):
        try:
            sql = 'SELECT pelicula.nombre ,pelicula.lenguaje FROM pelicula where id_pelicula = %s'
            vals = (id_pelicula,)
            self.cursor.execute(sql, vals)
            registro = self.cursor.fetchone()
            return registro
        except connector.Error as err:
            return err

    def actualizar_pelicula(self, fields, vals):
        try:
            sql = 'UPDATE pelicula set '+','.join(fields)+'WHERE id_pelicula = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def borrar_pelicula(self, id_pelicula):
        try:
            sql = 'DELETE from pelicula where id_pelicula = %s' 
            vals = (id_pelicula,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ************************
    *Metodos para las salas*
    ************************
    """
    def crear_sala(self,no_sala, fila, pasillo, tipo):
        try:
            sql = 'INSERT into sala(`no_sala`, `pasillo`, `fila`, `tipo`) values(%s,%s,%s,%s)'
            vals = (no_sala, pasillo, fila, tipo)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def leer_sala(self, no_sala):
        try:
            sql = 'SELECT * FROM sala WHERE no_sala = %s'
            vals = (no_sala,)
            self.cursor.execute(sql, vals)
            registro = self.cursor.fetchone()
            return registro
        except connector.Error as err:
            return err

    def leer_salas(self):
        try:
            sql = 'SELECT * from sala'
            self.cursor.execute(sql)
            registros = self.cursor.fetchall()
            return registros
        except connector.Error as err:
            return err

    def actualizar_sala(self, fields, vals):
        try:
            sql = 'UPDATE sala set '+','.join(fields)+'WHERE no_sala = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def borrar_sala(self, id_horario):
        try:
            sql = 'DELETE from sala where no_sala = %s' 
            vals = (id_horario,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err


    """
    ***************************
    *Metodos para los horarios*
    ***************************
    """
    def crear_horario(self, id_horario, id_admin, id_pelicula, estrenos, prestrenos):
        try:
            sql = 'INSERT into horario(`id_horario`, `id_admin`, `id_pelicula` ,`estrenos`, `prestrenos`) values (%s,%s,%s,%s,%s)'
            vals = (id_horario, id_admin, id_pelicula, estrenos, prestrenos)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def leer_horario(self, id_horario):
        try:
            sql = 'SELECT * from horario where id_horario = %s'
            vals = (id_horario,)
            self.cursor.execute(sql, vals)
            registro = self.cursor.fetchone()
            return registro
        except connector.Error as err:
            return err

    def leer_estrenos(self):
        try:
            sql = 'SELECT estrenos, id_horario from horario where estrenos != "NULL"'
            self.cursor.execute(sql)
            registros = self.cursor.fetchall()
            return registros
        except connector.Error as err:
            return err

    def leer_prestrenos(self):
        try:
            sql = 'SELECT prestrenos, id_horario from horario where prestrenos != "NULL"'
            self.cursor.execute(sql)
            registros = self.cursor.fetchall()
            return registros
        except connector.Error as err:
            return err

    def actualizar_horario(self, fields, vals):
        try:
            sql = 'UPDATE horario set '+','.join(fields)+'WHERE id_horario = %s and id_pelicula = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def borrar_horario(self, id_horario, id_pelicula):
        try:
            sql = 'DELETE from horario where id_horario = %s and id_pelicula = %s' 
            vals = (id_horario, id_pelicula)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ***************************
    *Metodos para los asientos*
    ***************************
    """
    def crear_asiento(self, pasillo, fila, id_usuario, no_sala, asiento):
        try:
            sql = 'INSERT into asiento(`pasillo`, `fila`, `id_usuario`, `no_sala`, `asiento`) values(%s,%s,%s,%s,%s)'
            vals = (pasillo, fila, id_usuario, no_sala, asiento)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def leer_asientos_usuario(self, id_usuario, no_sala):
        try:
            sql = 'SELECT usuarios.u_nombre, sala.tipo, sala.no_sala, asiento.asiento, asiento.pasillo, asiento.fila from asiento join usuarios on usuarios.id_usuario = asiento.id_usuario join sala on sala.no_sala = asiento.no_sala where usuarios.id_usuario = %s and sala.no_sala = %s'
            vals = (id_usuario, no_sala)
            self.cursor.execute(sql,vals)
            registros = self.cursor.fetchall()
            return registros
        except connector.Error as err:
            return err
    
    def leer_asientos_sala(self, no_sala):
        try:
            sql = 'SELECT  asiento.pasillo, asiento.fila, asiento.asiento from asiento join usuarios on usuarios.id_usuario = asiento.id_usuario join sala on sala.no_sala = asiento.no_sala where sala.no_sala = %s'
            vals = (no_sala,)
            self.cursor.execute(sql,vals)
            registros = self.cursor.fetchall()
            return registros
        except connector.Error as err:
            return err
    
    def actualizar_asiento(self, fields, vals):
        try:
            sql = 'UPDATE asiento set '+','.join(fields)+'WHERE fila = %s and pasillo = %s and no_sala = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def borrar_asiento(self, pasillo, fila, no_sala):
        try:
            sql = 'DELETE from asiento where pasillo = %s and fila = %s and no_sala = %s' 
            vals = (pasillo, fila, no_sala)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err


    """
    *************************************
    *Metodos para los horarios_peliculas*
    *************************************
    """
    def crear_horario_pelicula(self, id_horario, id_pelicula, hora):
        try:
            sql = 'INSERT into horario_peliculas(`id_horario`, `id_pelicula`, `hora`) values(%s,%s,%s)'
            vals = (id_horario, id_pelicula, hora)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def leer_horario_peliculas(self):
        try: 
            sql = 'SELECT pelicula.nombre, horario.id_horario, horario_peliculas.hora from horario_peliculas join pelicula on pelicula.id_pelicula = horario_peliculas.id_pelicula join horario on horario.id_pelicula = horario_peliculas.id_pelicula'
            self.cursor.execute(sql)
            registros = self.cursor.fetchall()
            return registros
        except connector.Error as err:
            return err
            
    
    def leer_peliculas_fecha(self, id_horario):
        try:
            sql = 'SELECT pelicula.nombre, horario.id_horario, horario_peliculas.hora from horario_peliculas join pelicula on pelicula.id_pelicula = horario_peliculas.id_pelicula join horario on horario.id_pelicula = horario_peliculas.id_pelicula where horario_peliculas.id_horario = %s'
            vals = (id_horario,)
            self.cursor.execute(sql,vals)
            registros = self.cursor.fetchall()
            return registros
        except connector.Error as err:
            return err

    '''def actualizar_horario_peliculas(self, fields, vals):
        try:
            sql = 'UPDATE horario_peliculas set '+','.join(fields)+'WHERE id_hora_peli = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err'''

    def borrar_horario_pelicula(self, id_hora_peli):
        try:
            sql = 'DELETE from horario_peliculas where id_hora_peli = %s' 
            vals = (id_hora_peli,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    """
    **********************************
    *Metodos para los salas_peliculas*
    **********************************
    """
    def crear_sala_pelicula(self,no_sala, id_pelicula, costo):
        try:
            sql = 'INSERT into sala_pelicula(`no_sala`, `id_pelicula`, `costo`) values(%s,%s,%s)'
            vals = (no_sala, id_pelicula, costo)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def leer_precio_pelicula(self, id_pelicula):
        try:
            sql = 'SELECT pelicula.nombre, sala_pelicula.costo, sala.no_sala from sala_pelicula join pelicula on pelicula.id_pelicula = sala_pelicula.id_pelicula join sala on sala.no_sala = sala_pelicula.no_sala where pelicula.id_pelicula = %s'
            vals = (id_pelicula,)
            self.cursor.execute(sql, vals)
            registros = self.cursor.fetchall()
            return registros
        except connector.Error as err:
            return err

    def leer_precio_P_S(self, id_pelicula, no_sala):
        try:
            sql = 'SELECT pelicula.nombre, sala_pelicula.costo, sala.no_sala from sala_pelicula join pelicula on pelicula.id_pelicula = sala_pelicula.id_pelicula join sala on sala.no_sala = sala_pelicula.no_sala where pelicula.id_pelicula = %s and sala.no_sala = %s'
            vals = (id_pelicula, no_sala)
            self.cursor.execute(sql, vals)
            registro = self.cursor.fetchone()
            return registro
        except connector.Error as err:
            return err
        
    def borrar_sala_peli(self, no_sala, id_pelicula):
        try:
            sql = 'DELETE from sala_pelicula where no_sala = %s and id_pelicula = %s' 
            vals = (no_sala, id_pelicula)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    **************************
    *Metodos para los tickets*
    **************************
    """
    def crear_ticket(self,id_usuario, total_asientos, total_pago):
        try:
            sql = 'INSERT into ticket(`id_usuario`, `total_asientos`, `total_pago`) values(%s,%s,%s)'
            vals = (id_usuario, total_asientos, total_pago)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def leer_ticket_usuario(self, id_usuario):
        try:
            sql = 'SELECT u_nombre, ticket.total_asientos, total_pago from ticket join usuarios on usuarios.id_usuario = ticket.id_usuario where usuarios.id_usuario = %s'
            vals = (id_usuario,)
            self.cursor.execute(sql, vals)
            registros = self.cursor.fetchall()
            return registros
        except connector.Error as err:
            return err

    '''def actualizar_ticket(self, fields, vals):
        try:
            sql = 'UPDATE ticket set '+','.join(fields)+'WHERE id_ticket = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err'''

    def borrar_ticket(self, id_ticket):
        try:
            sql = 'DELETE from ticket where id_ticket = %s' 
            vals = (id_ticket,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
