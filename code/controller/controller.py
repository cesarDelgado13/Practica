from model.model import Model
from view.view import View
from datetime import date
import time

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()
    
    def start(self):
        self.view.start()
        self.main_menu()

    def main_menu(self):
        o = '0'
        while o != '3':
            self.view.main_menu()
            self.view.option('3')
            o = input()
            if o == '1':
                self.user_menu()
            elif o == '2':
                self.admin_menu()
            elif o == '3':
                self.view.end()
            else:
                self.view.not_valid_option()
        return 

    def update_lists(self, fs, vs):
        fields = []
        vals = []
        for f,v in zip(fs,vs): #zip une de uno por uno
            if v != '':
                fields.append(f+' = %s')
                vals.append(v)
        return fields, vals

    def admin_menu(self):
        o = '0'
        while o != '10':
            self.view.admin_menu()
            self.view.option('10')
            o = input()
            if o == '1':
                self.usuario_menu()
            elif o == '2':
                self.admins_menu()
            elif o == '3':
                self.pelicula_menu()
            elif o == '4':
                self.sala_menu()
            elif o == '5':
                self.horario_menu()
            elif o == '6':
                self.asiento_menu()
            elif o == '7':
                self.hora_peli_menu()
            elif o == '8':
                self.sala_peli_menu()
            elif o == '9':
                self.ticket_menu()
            elif o == '10':
                self.view.end()
            else:
                self.view.not_valid_option()
        return 
    
    def user_menu(self):
        o = '0'
        while o != '10':
            self.view.user_menu()
            self.view.option('10')
            o = input()
            if o == '1':
                self.crear_usuario()
            elif o == '2':
                self.ver_sala()
            elif o == '3':
                self.leer_salas()
            elif o == '4':
                self.leer_estrenos()
            elif o == '5':
                self.leer_preestrenos()
            elif o == '6':
                self.crear_asiento()
            elif o == '7':
                self.leer_asientos_sala()
            elif o == '8':
                self.leer_horario_peliculas()
            elif o == '9':
                self.leer_costo_pelicula()
            elif o == '10':
                self.view.end()
            else:
                self.view.not_valid_option()
        return 

    """
    *******************************
    *Controlador para los clientes*
    *******************************
    """
    def usuario_menu(self):
        o = '0'
        while o != '6':
            self.view.clients_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.crear_usuario()
            elif o == '2':
                self.leer_usuario()
            elif o == '3':
                self.leer_todo_usuarios()
            elif o == '4':
                self.actualizar_usuarios()
            elif o == '5':
                self.borrar_usuario()
            elif o == '6':
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def pedir_usuario(self):
        self.view.ask('Nombre: ')
        u_nombre = input()
        self.view.ask('Apellido: ')
        u_apellidos = input()
        self.view.ask('Correo: ')
        u_correo = input()
        self.view.ask('Telefono: ')
        u_telefono = input()
        return [u_nombre, u_apellidos, u_correo, u_telefono]
    
    def crear_usuario(self):
        u_nombre, u_apellidos, u_correo, u_telefono = self.pedir_usuario()
        out = self.model.crear_usuario(u_nombre, u_apellidos, u_correo, u_telefono)
        if out == True:
            self.view.ok(u_nombre+' '+u_apellidos, 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR EL CCLIENTE. REVISA.')
        return

    def leer_usuario(self):
        self.view.ask('ID del usuario: ')
        id_usuario = input()
        cliente = self.model.leer_un_usuario(id_usuario)
        if type(cliente) == tuple:
            self.view.show_client_header(' Datos del cliente '+id_usuario+' ')
            self.view.show_a_client(cliente)
            self.view.show_client_midder()
            self.view.show_client_footer()
        else:
            if cliente == None:
                self.view.error('EL USUARIO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL USUARIO: REVISA.')
        return

    def leer_todo_usuarios(self):
        clientes = self.model.leer_todo_usuarios()    
        if type(clientes) == list:
            self.view.show_client_header(' Todos los clientes ')
            for cliente in clientes:
                self.view.show_a_client(cliente)
                self.view.show_client_midder()
            self.view.show_client_footer()
        else:
            self.view.error('PROBLEMA AL LEER EL USUARIO: REVISA.')
        return
    
    def actualizar_usuarios(self):
        self.view.ask(' ID de cliente a modificar: ')
        id_usuario = input()
        cliente = self.model.leer_un_usuario(id_usuario)
        if type(cliente) == tuple:
            self.view.show_client_header(' Datos del cliente '+id_usuario+' ')
            self.view.show_a_client(cliente)
            self.view.show_client_midder()
            self.view.show_client_footer()
        else:
            if cliente == None:
                self.view.error('EL CLIENTE NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL CLIENTE. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vaciar para dejar igual):')
        whole_vals = self.pedir_usuario()
        fields, vals = self.update_lists(['u_nombre', 'u_apellidos', 'u_correo','u_telefono'], whole_vals)
        vals.append(id_usuario)
        vals = tuple(vals)
        out = self.model.actualizar_usuarios(fields, vals)
        if out == True:
            self.view.ok(id_usuario, 'actualizo')
        else: 
            self.view.error('NO SE PUDO ACTUALIZAR EL CLIENTE. REVISA.')
        return

    def borrar_usuario(self):
        self.view.ask('Id  de cliente a borrar: ')
        id_usuario = input()
        count = self.model.borrar_usuario(id_usuario)
        if count != 0:
            self.view.ok(id_usuario, 'borro')
        else:
            if count == 0:
                self.view.error('EL CLIENTE NO EXISTE')
            else:
                self.view.error('PROBELEMA AL BORRAR EL CLIENTE. REVISA.')
        return

    """
    **************************************
    *Controlador para los administradores*
    **************************************
    """
    def admins_menu(self):
        o = '0'
        while o != '6':
            self.view.admins_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.crear_admin()
            elif o == '2':
                self.leer_admin()
            elif o == '3':
                self.leer_todo_admin()
            elif o == '4':
                self.actualizar_admin()
            elif o == '5':
                self.borrar_admin()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return

    def pedir_admin(self):
        self.view.ask('Nombre: ')
        a_nombre = input()
        self.view.ask('Apellido: ')
        a_apellidos = input()
        self.view.ask('Puesto: ')
        a_posicion = input()
        self.view.ask('Correo: ')
        a_correo = input()
        self.view.ask('Telefono: ')
        a_telefono = input()
        self.view.ask('Contraseña: ')
        a_pass = input()
        return [a_nombre, a_apellidos, a_posicion, a_correo, a_telefono, a_pass]
    
    def crear_admin(self):
        a_nombre, a_apellidos, a_posicion, a_correo, a_telefono, a_pass = self.pedir_admin()
        out = self.model.crear_admin(a_nombre, a_apellidos, a_posicion, a_correo, a_telefono, a_pass)
        if out == True:
            self.view.ok(a_nombre+' '+a_apellidos, 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR EL ADMINISTRADOR. REVISA.')
        return

    def leer_admin(self):
        self.view.ask('ID del administrador: ')
        id_admin = input()
        admin = self.model.leer_un_admin(id_admin)
        if type(admin) == tuple:
            self.view.show_admin_header(' Datos del administrador '+id_admin+' ')
            self.view.show_a_admin(admin)
            self.view.show_admin_midder()
            self.view.show_admin_footer()
        else:
            if admin == None:
                self.view.error('EL ADMINISTRADOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL ADMINISTRADOR: REVISA.')
        return

    def leer_todo_admin(self):
        admins = self.model.leer_todo_admin()    
        if type(admins) == list:
            self.view.show_admin_header(' Todos los administradores ')
            for admin in admins:
                self.view.show_a_admin(admin)
                self.view.show_admin_midder()
            self.view.show_admin_footer()
        else:
            self.view.error('PROBLEMA AL LEER EL ADMINISTRADOR: REVISA.')
        return
    
    def actualizar_admin(self):
        self.view.ask(' ID de administrador a modificar: ')
        id_admin = input()
        admin = self.model.leer_un_admin(id_admin)
        if type(admin) == tuple:
            self.view.show_admin_header(' Datos del administrador '+id_admin+' ')
            self.view.show_a_admin(admin)
            self.view.show_admin_midder()
            self.view.show_admin_footer()
        else:
            if admin == None:
                self.view.error('EL ADMINISTRADOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL ADMINISTRADOR. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vaciar para dejar igual):')
        whole_vals = self.pedir_admin()
        fields, vals = self.update_lists(['a_nombre', 'a_apellidos', 'a_posicion', 'a_correo', 'a_telefono', 'a_pass'], whole_vals)
        vals.append(id_admin)
        vals = tuple(vals)
        out = self.model.actualizar_admin(fields, vals)
        if out == True:
            self.view.ok(id_admin, 'actualizo')
        else: 
            self.view.error('NO SE PUDO ACTUALIZAR EL ADMINISTRADOR. REVISA.')
        return

    def borrar_admin(self):
        self.view.ask('Id del administrador a borrar: ')
        id_admin = input()
        count = self.model.borrar_admin(id_admin)
        if count != 0:
            self.view.ok(id_admin, 'borro')
        else:
            if count == 0:
                self.view.error('EL ADMINISTRADOR NO EXISTE')
            else:
                self.view.error('PROBELEMA AL BORRAR EL ADMINISTRADOR. REVISA.')
        return

    """
    *******************************
    *Controlador para los pelicula*
    *******************************
    """
    def pelicula_menu(self):
        o = '0'
        while o != '7':
            self.view.peliculas_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.crear_pelicula()
            elif o == '2':
                self.leer_pelicula()
            elif o == '3':
                self.leer_todo_peliculas()
            elif o == '4':
                self.leer_lenguaje_pelicula()
            elif o == '5':
                self.actualizar_pelicula()
            elif o == '6':
                self.borrar_pelicula()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return

    def pedir_pelicula(self):
        self.view.ask('Nombre: ')
        nombre = input()
        self.view.ask('Lenguaje: ')
        lenguaje = input()
        self.view.ask('Sinopsis: ')
        sinopsis = input()
        return [nombre, lenguaje, sinopsis]
    
    def crear_pelicula(self):
        nombre, lenguaje, sinopsis = self.pedir_pelicula()
        out = self.model.crear_pelicula(nombre, lenguaje, sinopsis)
        if out == True:
            self.view.ok(nombre+' ', 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR LA PELICULA. REVISA.')
        return

    def leer_pelicula(self):
        self.view.ask('ID del pelicula: ')
        id_pelicula = input()
        pelicula = self.model.leer_pelicula(id_pelicula)
        if type(pelicula) == tuple:
            self.view.show_movie_header(' Datos de la pelicula '+id_pelicula+' ')
            self.view.show_a_movie(pelicula)
            self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            if pelicula == None:
                self.view.error('LA PELICULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA PELICULA: REVISA.')
        return

    def leer_todo_peliculas(self):
        peliculas = self.model.leer_todas_peliculas()    
        if type(peliculas) == list:
            self.view.show_admin_header(' Todos las peliculas ')
            for pelicula in peliculas:
                self.view.show_a_movie(pelicula)
                self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            self.view.error('PROBLEMA AL LEER LA PELICULA: REVISA.')
        return

    def leer_lenguaje_pelicula(self):
        self.view.ask('ID del pelicula: ')
        id_pelicula = input()
        pelicula = self.model.lenguaje_pelicula(id_pelicula)
        if type(pelicula) == tuple:
            self.view.show_movie_header(' Lenguaje de la pelicula '+id_pelicula+' ')
            self.view.show_movie_languaje(pelicula)
            self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            if pelicula == None:
                self.view.error('LA PELICULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA PELICULA: REVISA.')
        return
    
    def actualizar_pelicula(self):
        self.view.ask(' ID de pelicula a modificar: ')
        id_pelicula = input()
        pelicula = self.model.leer_pelicula(id_pelicula)
        if type(pelicula) == tuple:
            self.view.show_movie_header(' Datos de la pelicula '+id_pelicula+' ')
            self.view.show_a_movie(pelicula)
            self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            if pelicula == None:
                self.view.error('LA PELICULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA PELICULA. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vaciar para dejar igual):')
        whole_vals = self.pedir_pelicula()
        fields, vals = self.update_lists(['nombre', 'lenguaje', 'sinopsis'], whole_vals)
        vals.append(id_pelicula)
        vals = tuple(vals)
        out = self.model.actualizar_pelicula(fields, vals)
        if out == True:
            self.view.ok(id_pelicula, 'actualizo')
        else: 
            self.view.error('NO SE PUDO ACTUALIZAR LA PELICULA. REVISA.')
        return

    def borrar_pelicula(self):
        self.view.ask('Id de la pelicula a borrar: ')
        id_pelicula = input()
        count = self.model.borrar_pelicula(id_pelicula)
        if count != 0:
            self.view.ok(id_pelicula, 'borro')
        else:
            if count == 0:
                self.view.error('LA PELICULA NO EXISTE')
            else:
                self.view.error('PROBELEMA AL BORRAR LA PELICULA. REVISA.')
        return

    """
    ****************************
    *Controlador para las Salas*
    ****************************
    """
    def sala_menu(self):
        o = '0'
        while o != '7':
            self.view.salas_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.crear_sala()
            elif o == '2':
                self.leer_sala()
            elif o == '3':
                self.leer_salas()
            elif o == '4':
                self.leer_lenguaje_pelicula()
            elif o == '5':
                self.actualizar_sala()
            elif o == '6':
                self.borrar_sala()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return
    def pedir_sala(self):
        self.view.ask('No. Sala: ')
        no_sala = input()
        self.view.ask('Filas (1-13): ')
        fila = input()
        self.view.ask('Pasillos (1-11): ')
        pasillo = input()
        self.view.ask('Tipo (3D, VIP, Normal): ')
        tipo = input()
        return [no_sala, fila, pasillo, tipo]
    
    def crear_sala(self):
        no_sala, fila, pasillo, tipo = self.pedir_sala()
        out = self.model.crear_sala(no_sala, fila, pasillo, tipo)
        if out == True:
            self.view.ok(no_sala+' ', 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR LA SALA. REVISA.')
        return

    def leer_sala(self):
        self.view.ask('No. de la sala: ')
        no_sala = input()
        sala = self.model.leer_sala(no_sala)
        if type(sala) == tuple:
            self.view.show_sala_header(' Datos de la sala '+no_sala+' ')
            self.view.show_sala(sala)
            self.view.show_sala_midder()
            self.view.show_sala_footer()
        else:
            if sala == None:
                self.view.error('LA SALA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA SALA: REVISA.')
        return
    
    def leer_salas(self):
        salas = self.model.leer_salas()    
        if type(salas) == list:
            self.view.show_sala_header(' Todos las salas ')
            for sala in salas:
                self.view.show_sala(sala)
                self.view.show_sala_midder()
            self.view.show_sala_footer()
        else:
            self.view.error('PROBLEMA AL LEER LA SALA: REVISA.')
        return

    def actualizar_sala(self):
        self.view.ask(' No. de sala a modificar: ')
        no_sala = input()
        sala = self.model.leer_sala(no_sala)
        if type(sala) == tuple:
            self.view.show_sala_header(' Datos de la sala '+no_sala+' ')
            self.view.show_sala(sala)
            self.view.show_sala_midder()
            self.view.show_sala_footer()
        else:
            if sala == None:
                self.view.error('LA SALA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA SALA. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vaciar para dejar igual):')
        whole_vals = self.pedir_sala()
        fields, vals = self.update_lists(['no_sala', 'pasillo', 'fila', 'tipo'], whole_vals)
        vals.append(no_sala)
        vals = tuple(vals)
        out = self.model.actualizar_sala(fields, vals)
        if out == True:
            self.view.ok(no_sala, 'actualizo')
        else: 
            self.view.error('NO SE PUDO ACTUALIZAR LA SALA. REVISA.')
        return

    def borrar_sala(self):
        self.view.ask('Id de la sala a borrar: ')
        no_sala = input()
        count = self.model.borrar_sala(no_sala)
        if count != 0:
            self.view.ok(no_sala, 'borro')
        else:
            if count == 0:
                self.view.error('LA SALA NO EXISTE')
            else:
                self.view.error('PROBELEMA AL BORRAR LA SALA. REVISA.')
        return

    """
    *******************************
    *Controlador para los horarios*
    *******************************
    """
    def horario_menu(self):
        o = '0'
        while o != '6':
            self.view.horario_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.crear_horario()
            elif o == '2':
                self.leer_horario()
            elif o == '3':
                self.leer_estrenos()
            elif o == '4':
                self.leer_preestrenos()
            elif o == '5':
                self.borrar_horario()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return
    def crear_horario(self):
        self.view.ask('Horario (yyy-mm-dd): ')
        id_horario = input()
        self.view.ask('ID Administrador: ')
        id_admin = input()
        self.view.ask('ID Pelicula: ')
        id_pelicula = input()
        self.view.ask('Estrenos: ')
        estrenos = input() 
        self.view.ask('Preestrenos: ')
        prestrenos = input()
        out = self.model.crear_horario(id_horario, id_admin, id_pelicula, estrenos, prestrenos)
        if out == True:
            self.view.ok(id_horario+' ', 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR EL HORARIO. REVISA.')
        return

    def leer_horario(self):
        self.view.ask('ID del Horario: ')
        id_horario = input()
        horario = self.model.leer_horario(id_horario)
        if type(horario) == tuple:
            self.view.show_date_header(' Datos de la fecha '+id_horario+' ')
            self.view.show_date(horario)
            self.view.show_date_midder()
            self.view.show_date_footer()
        else:
            if horario == None:
                self.view.error('LA FECHA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA FECHA: REVISA.')
        return

    def leer_estrenos(self):
        estrenos = self.model.leer_estrenos()    
        if type(estrenos) == list:
            self.view.show_date_header(' Todos los horarios ')
            for estreno in estrenos:
                self.view.show_estrenos(estreno)
                self.view.show_date_midder()
            self.view.show_date_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS PELICULAS: REVISA.')
        return

    def leer_preestrenos(self):
        estrenos = self.model.leer_prestrenos()    
        if type(estrenos) == list:
            self.view.show_date_header(' Todos los estrenos ')
            for estreno in estrenos:
                self.view.show_estrenos(estreno)
                self.view.show_date_midder()
            self.view.show_date_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS ESTRENOS: REVISA.')
        return

    def actualizar_horario(self):
        self.view.ask('ID de la fecha a modificar: ')
        id_horario = input()
        horario = self.model.leer_horario(id_horario)
        if type(horario) == tuple:
            self.view.show_date_header(' Datos del horario '+id_horario+' ')
            self.view.show_date(horario)
            self.view.show_date_footer()
        else:
            if horario == None:
                self.view.error('EL HORARIO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL HORARIO. REVISA.')
            return
        self.view.msg('Ingresa los valores a morificar (vacio para dejarlo igual): ')
        self.view.ask('Fecha (yy/mm/dd):')
        id_horario = input()
        self.view.ask('Administrador: ')
        id_admin = input()
        self.view.ask('ID Pelicula: ')
        id_pelicula = input()
        self.view.ask('Estrenos: ')
        estrenos = input()
        self.view.ask('Preestrenos: ')
        prestrenos = input()

        whole_vals = [id_horario, id_admin, id_pelicula, estrenos, prestrenos]
        fields, vals = self.update_lists(['id_horario', 'id_admin', 'id_pelicula', 'estrenos', 'prestrenos'], whole_vals)
        vals.append(id_horario)
        vals = tuple(vals)
        out = self.model.actualizar_horario(fields, vals)
        if out == True:
            self.view.ok(id_horario, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL HORARIO. REVISA.')
        return

    def borrar_horario(self):
        self.view.ask('Id del horario a borrar: ')
        id_horario = input()
        self.view.ask('Id de la pelicula a borrar: ')
        id_pelicula = input()
        count = self.model.borrar_horario(id_horario, id_pelicula)
        if count != 0:
            self.view.ok(id_horario, 'borro')
        else:
            if count == 0:
                self.view.error('EL HORARIO NO EXISTE')
            else:
                self.view.error('PROBELEMA AL BORRAR. REVISA.')
        return

    """
    *******************************
    *Controlador para los asientos*
    *******************************
    """
    def asiento_menu(self):
        o = '0'
        while o != '5':
            self.view.asiento_menu()
            self.view.option('5')
            o = input()
            if o == '1':
                self.crear_asiento()
            elif o == '2':
                self.leer_asientos_usuario()
            elif o == '3':
                self.leer_asientos_sala()
            #elif o == '5':
            #    self.actualizar_pelicula()
            elif o == '4':
                self.borrar_asiento()
            elif o == '5':
                return
            else:
                self.view.not_valid_option()
        return
    def pedir_asiento(self):
        self.view.ask('Pasillo: ')
        pasillo = input()
        self.view.ask('Filas: ')
        fila = input()
        self.view.ask('id_usuario: ')
        id_usuario = input()
        self.view.ask('No. Sala: ')
        no_sala = input()
        self.view.ask('Tipo (Ocupado, Apartado): ')
        asiento = input()
        return [pasillo, fila, id_usuario, no_sala, asiento]

    def pedir_asiento_sala(self):
        self.view.ask('Pasillo: ')
        pasillo = input()
        self.view.ask('Filas: ')
        fila = input()
        self.view.ask('Tipo (Ocupado, Apartado): ')
        asiento = input()
        return [pasillo, fila, asiento]
    
    def crear_asiento(self):
        pasillo, fila, id_usuario, no_sala, asiento = self.pedir_asiento()
        out = self.model.crear_asiento(pasillo, fila, id_usuario, no_sala, asiento)
        if out == True:
            self.view.ok(pasillo+'-'+fila, 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR EL ASIENTO. REVISA.')
        return
    
    def leer_asientos_usuario(self):
        self.view.ask('ID de Usuario: ')
        id_usuario = input()
        self.view.ask('No. Sala: ')
        no_sala = input()
        asientos = self.model.leer_asientos_usuario(id_usuario, no_sala)    
        if type(asientos) == list:
            self.view.show_date_header(' Asientos del usuario ')
            for asiento in asientos:
                self.view.show_asiento_user(asiento)
                self.view.show_asiento_midder()
            self.view.show_asiento_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS ASIENTOS: REVISA.')
        return
    
    def leer_asientos_sala(self):
        self.view.ask('No. Sala: ')
        no_sala = input()
        asientos = self.model.leer_asientos_sala(no_sala)    
        if type(asientos) == list:
            self.view.show_date_header(' Asientos de la sala ')
            for asiento in asientos:
                self.view.show_asiento_sala(asiento)
                self.view.show_asiento_midder()
            self.view.show_asiento_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS ASIENTOS: REVISA.')
        return

    def actualizar_asiento(self):
        self.view.ask('Pasillo a modificar: ')
        pasillo = input()
        self.view.ask('Fila a modificar: ')
        fila = input()
        self.view.ask('Sala a modificar: ')
        no_sala = input()
        sala = self.model.leer_asientos_sala(no_sala)
        if type(sala) == list:
            self.view.show_asiento_header(' Datos del asiento '+fila+ '- '+pasillo+' ')
            self.view.show_asiento(sala)
            self.view.show_asiento_midder()
            self.view.show_asiento_footer()
        else:
            if sala == None:
                self.view.error('EL ASIENTO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL ASIENTO. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vaciar para dejar igual):')
        whole_vals = self.pedir_asiento_sala()
        fields, vals = self.update_lists(['pasillo', 'fila', 'asiento'], whole_vals)
        vals.append(no_sala)
        vals = list(vals)
        out = self.model.actualizar_asiento(fields, vals)
        if out == True:
            self.view.ok(no_sala, 'actualizo')
        else: 
            self.view.error('NO SE PUDO ACTUALIZAR EL ASIENTO. REVISA.')
        return

    def borrar_asiento(self):
        self.view.ask('Pasillo de usuario a borrar (A-M): ')
        pasillo = input()
        self.view.ask('Fila de usuario a borrar (1-11): ')
        fila = input()
        self.view.ask('Sala de usuario a borrar: ')
        no_sala = input()
        count = self.model.borrar_asiento(pasillo, fila, no_sala)
        if count != 0:
            self.view.ok(pasillo+ ' - '+fila+' ', 'borro')
        else:
            if count == 0:
                self.view.error('EL ASIENTO NO EXISTE')
            else:
                self.view.error('PROBELEMA AL BORRAR EL ASIENTO. REVISA.')
        return

    """
    *****************************************
    *Controlador para los horarios_peliculas*
    *****************************************
    """
    def hora_peli_menu(self):
        o = '0'
        while o != '5':
            self.view.hora_peli_menu()
            self.view.option('5')
            o = input()
            if o == '1':
                self.crear_horario_pelicula()
            elif o == '2':
                self.leer_horario_peliculas()
            elif o == '3':
                self.leer_peliculas_fecha()
            #elif o == '5':
            #    self.actualizar_pelicula()
            elif o == '4':
                self.borrar_horario_pelicula()
            elif o == '5':
                return
            else:
                self.view.not_valid_option()
        return
    def pedir_horario_peli(self):
        self.view.ask('ID horario (yyyy-mmm-dd): ')
        id_horario = input()
        self.view.ask('ID pelicula: ')
        id_pelicula = input()
        self.view.ask('Hora: (hh:mm): ')
        hora = input()
        #hora = time.strftime("%I:%M")
        #print(hora)
        return [id_horario, id_pelicula, hora]

    def crear_horario_pelicula(self):
        id_horario, id_pelicula, hora = self.pedir_horario_peli()
        out = self.model.crear_horario_pelicula(id_horario, id_pelicula, hora)
        if out == True:
            self.view.ok(id_horario+'-'+hora, 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR EL HORARIO-PELICULA. REVISA.')
        return

    def leer_horario_peliculas(self):
        peliculas = self.model.leer_horario_peliculas()    
        if type(peliculas) == list:
            self.view.show_hora_peli_header(' Todos los horarios-peliculas ')
            for pelicula in peliculas:
                self.view.show_hora_peli(pelicula)
                self.view.show_hora_peli_midder()
            self.view.show_hora_peli_footer()
        else:
            self.view.error('PROBLEMA AL LEER HORARIO PELICULAS: REVISA.')
        return

    def leer_peliculas_fecha(self):
        self.view.ask('ID horario (yyyy-mmm-dd): ')
        id_horario = input()
        peliculas = self.model.leer_peliculas_fecha(id_horario)    
        if type(peliculas) == list:
            self.view.show_hora_peli_header(' Todos los horarios-peliculas ')
            for pelicula in peliculas:
                self.view.show_hora_peli(pelicula)
                self.view.show_hora_peli_midder()
            self.view.show_hora_peli_footer()
        else:
            self.view.error('PROBLEMA AL LEER HORARIO PELICULAS: REVISA.')
        return

    def borrar_horario_pelicula(self):
        self.view.ask('Id del horario-pelicula a borrar: ')
        id_hora_peli = input()
        count = self.model.borrar_horario_pelicula(id_hora_peli)
        if count != 0:
            self.view.ok(id_hora_peli, 'borro')
        else:
            if count == 0:
                self.view.error('EL HORARIO NO EXISTE')
            else:
                self.view.error('PROBELEMA AL BORRAR. REVISA.')
        return


    """
    ************************************
    *Controles para los salas_peliculas*
    ************************************
    """
    def sala_peli_menu(self):
        o = '0'
        while o != '4':
            self.view.sala_peli_menu()
            self.view.option('4')
            o = input()
            if o == '1':
                self.crear_sala_pelicula()
            elif o == '2':
                self.leer_costo_pelicula()
            elif o == '3':
                self.borrar_sala_peli()
            #elif o == '5':
            #    self.actualizar_pelicula()
            elif o == '4':
                return
            else:
                self.view.not_valid_option()
        return

    def pedir_sala_pelicula(self):
        self.view.ask('No. Sala: ')
        no_sala = input()
        self.view.ask('ID Pelicula: ')
        id_pelicula = input()
        self.view.ask('Costo: ')
        costo = input()
        return [no_sala, id_pelicula, costo]

    def crear_sala_pelicula(self):
        no_sala, id_pelicula, costo = self.pedir_sala_pelicula()
        out = self.model.crear_sala_pelicula(no_sala, id_pelicula, costo)
        if out == True:
            self.view.ok(no_sala+'-'+id_pelicula, 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR EL ASIENTO. REVISA.')
        return

    def leer_costo_pelicula(self):
        self.view.ask('ID Pelicula: ')
        id_pelicula = input()
        peliculas = self.model.leer_precio_pelicula(id_pelicula)    
        if type(peliculas) == list:
            self.view.show_sala_peli_header(' Datos de la pelicula '+id_pelicula+' ')
            for pelicula in peliculas:
                self.view.show_costo_peli(pelicula)
                self.view.show_sala_peli_midder()
            self.view.show_sala_peli_footer()
        else:
            self.view.error('PROBLEMA AL LEER LA PELICULA: REVISA.')
        return

    def borrar_sala_peli(self):
        self.view.ask('No de sala a borrar: ')
        no_sala = input()
        self.view.ask('ID  de pelicula a borrar: ')
        id_pelicula = input()
        count = self.model.borrar_sala_peli(no_sala, id_pelicula)
        if count != 0:
            self.view.ok(no_sala+ ' - '+id_pelicula+' ', 'borro')
        else:
            if count == 0:
                self.view.error('SALA-PELICULA NO EXISTE')
            else:
                self.view.error('PROBELEMA AL BORRAR SALA-PELICULA. REVISA.')
        return

    """
    ****************************
    *Controles para los tickets*
    ****************************
    """
    def ticket_menu(self):
        o = '0'
        while o != '4':
            self.view.ticket_menu()
            self.view.option('4')
            o = input()
            if o == '1':
                self.crear_ticket()
            elif o == '2':
                self.leer_ticket()
            #elif o == '5':
            #    self.actualizar_pelicula()
            elif o == '3':
                self.borrar_pelicula()
            elif o == '4':
                return
            else:
                self.view.not_valid_option()
        return
    def crear_ticket(self):
        self.view.ask('ID del usuario: ')
        id_usuario = input()
        self.view.ask('ID de la pelicula: ')
        id_pelicula = input()
        self.view.ask('No. sala: ')
        no_sala = input()
        total_asientos = len(self.model.leer_asientos_usuario(id_usuario, no_sala))
        costo =  self.model.leer_precio_P_S(id_pelicula, no_sala)
        total_pago = int(total_asientos * float(costo[1]))
        out = self.model.crear_ticket(id_usuario, total_asientos, total_pago)
        
        if out == True:
            self.view.ok(id_pelicula, 'pago')
        else:
            self.view.error('NO SE PUDO PAGAR. REVISA.')
        return

    def leer_ticket(self):
        self.view.ask('ID del Usuario: ')
        id_usuario = input()
        tickets = self.model.leer_ticket_usuario(id_usuario)    
        if type(tickets) == list:
            self.view.show_ticket_header(' Datos de el duario '+id_usuario+' ')
            for ticket in tickets:
                self.view.show_ticket(ticket)
                self.view.show_ticket_midder()
            self.view.show_ticket_footer()
        else:
            self.view.error('PROBLEMA AL LEER EL TICKET: REVISA.')
        return
    
    def borrar_ticket(self):
        self.view.ask('ID del ticket: ')
        id_ticket = input()
        count = self.model.borrar_ticket(id_ticket)
        if count != 0:
            self.view.ok(id_ticket, 'borro')
        else:
            if count == 0:
                self.view.error('EL TICKET NO EXISTE')
            else:
                self.view.error('PROBELEMA AL BORRAR EL TICKET. REVISA.')
        return

    def ver_sala(self):
        self.view.ask('No. Sala: ')
        no_sala = input()
        a = [' ','A','B','C','D','E','F','G','H','I','J','K','L','M']
        b = [1,2,3,4,5,6,7,8,9,10,11]

        u = self.model.leer_asientos_sala(no_sala)
        s = self.model.leer_sala(no_sala)
        print()
        print('***********',s[3],'***********')
        print()
        for i in a[s[1]:0:-1]:
            print(i+" |",end="")
            for j in b[0:s[2]]:
                aux = int(0)
                for f in range(len(u)):
                    if((i,j,'ocupado') == u[f]):
                        print(' O  ',end="")
                        aux += 1
                    elif((i,j,'apartado') == u[f]):
                        print(' A  ',end="")
                        aux += 1     
                if(aux):
                    continue
                else:
                    print(' L  ',end="")       
            print()

        print("    ",end="")
        for i in b[0:s[2]]:
            print(i,"  ",end="")
        print()
        