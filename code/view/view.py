class View:
    def start(self):
        print('******************')
        print('Bienvenido al cine')
        print('******************')
    
    def end(self):
        print('***********************')
        print('      Hasta luego      ')
        print('***********************')

    def main_menu(self):
        print('***********************')
        print('     Menu principal    ')
        print('***********************')
        print('1.- Clientes')
        print('2.- Administradores')
        print('3.- Regresar')

    def admin_menu(self):
        print('*********************************')
        print('* -- Submenu Administradores -- *')
        print('*********************************')
        print('1.- Clientes')
        print('2.- Administradores')
        print('3.- Pelicula')
        print('4.- Sala')
        print('5.- Horario')
        print('6.- Asiento')
        print('7.- Horario-Pelicula')
        print('8.- Sala-Pelicula')
        print('9.- Ticket')
        print('10.- Regresar')
    
    def user_menu(self):
        print('**************************')
        print('* -- Submenu Clientes -- *')
        print('**************************')
        print('1.- Crear cliente')
        print('2.- Leer una sala')
        print('3.- Leer salas')
        print('4.- Leer estrenos')
        print('5.- Leer preestrenos')
        print('6.- Crear asiento')
        print('7.- Leer asientos sala')
        print('8.- Leer Horario-Pelicula')
        print('9.- Leer costo de pelicula')
        print('10.- Salir')

    def option(self, last):
        print('Seleccione una opcion (1-'+last+'): ', end = '')
    
    def not_valid_option(self):
        print('¡Opcion no valida!\nIntenta de nuevo')

    def ask(self, output):
        print(output, end = '')
    
    def msg(self, output):
            print(output)

    def ok(self, id, op):
        print('+'*(len(str(id))+len(op)+24))
        print('+ !'+str(id)+' se '+op+' correctamente! +')
        print('+'*(len(str(id))+len(op)+24))

    def error(self, err):
        print(' ¡Error! '.center(len(err)+4,'-'))
        print('- '+err+' -')
        print('-'*(len(err)+4)) 

    """
    *********************
    *Vista para usuarios*
    *********************
    """
    def clients_menu(self):
        print('**************************')
        print('* -- Submenu Clientes -- *')
        print('**************************')
        print('1.- Crear cliente')
        print('2.- Leer un cliente')
        print('3.- Leer todos los cliente')
        print('4.- Actualizar un cliente')
        print('5.- Borrar cliente')
        print('6.- Regresar')
        
    def show_a_client(self, record):
        print('ID:', record[0])
        print('Nombre:', record[1])
        print('Apellido:', record[2])
        print('Correo:', record[3])
        print('Telefono:', record[4])
    
    def show_client_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    def show_client_midder(self):
        print('-'*48)

    def show_client_footer(self):
        print('*'*48)
    
    """
    ****************************
    *Vista para administradores*
    ****************************
    """
    def admins_menu(self):
        print('*********************************')
        print('* -- Submenu Administradores -- *')
        print('*********************************')
        print('1.- Crear admin')
        print('2.- Leer un admin')
        print('3.- Leer todos los admin')
        print('4.- Actualizar un admin')
        print('5.- Borrar admin')
        print('6.- Regresar')

    def show_a_admin(self, record):
        print('ID:', record[0])
        print('Nombre:', record[1])
        print('Apellido:', record[2])
        print('Posicion:', record[3])
        print('Correo:', record[4])
        print('Telefono:', record[5])
        print('contraseña:', record[6])
    
    def show_admin_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    def show_admin_midder(self):
        print('-'*48)

    def show_admin_footer(self):
        print('*'*48)
    
    """
    *********************
    *Vista para Pelicuas*
    *********************
    """
    def peliculas_menu(self):
        print('***************************')
        print('* -- Submenu Peliculas -- *')
        print('***************************')
        print('1.- Crear pelicula')
        print('2.- Leer un pelicula')
        print('3.- Leer todas las peliculas')
        print('4.- Leer lenguaje pelicula')
        print('5.- Actualizar pelicula')
        print('6.- Borrar pelicula')
        print('7.- Regresar')

    def show_a_movie(self, record):
        print('ID:', record[0])
        print('Nombre:', record[1])
        print('Lenguaje:', record[2])
        print('Sinopsis:', record[3])
    
    def show_movie_languaje(self, record):
        print('Nombre:', record[0])
        print('Lenguaje:', record[1])

    def show_movie_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    def show_movie_midder(self):
        print('-'*48)

    def show_movie_footer(self):
        print('*'*48)

    """
    ******************
    *Vista para Salas*
    ******************
    """
    def salas_menu(self):
        print('**********************')
        print('* -- Submenu Sala -- *')
        print('**********************')
        print('1.- Crear Sala')
        print('2.- Leer una sala')
        print('3.- Leer todas las salas')
        print('4.- Leer lenguaje de pelicula')
        print('5.- Actualizar sala')
        print('6.- Borrar sala')
        print('7.- Regresar')

    def show_sala(self, record):
        print('Sala:', record[0])
        print('Fila:', record[1])
        print('Pasillos:', record[2])
        print('Tipo:', record[3])

    def show_sala_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    def show_sala_midder(self):
        print('-'*48)

    def show_sala_footer(self):
        print('*'*48)

    """
    *********************
    *Vista para Horarios*
    *********************
    """
    def horario_menu(self):
        print('*************************')
        print('* -- Submenu horario -- *')
        print('*************************')
        print('1.- Crear horario')
        print('2.- Leer un horario')
        print('3.- Leer estrenos')
        print('4.- Leer preestrenos')
        #print('4.- Actualizar sala')
        print('5.- Borrar horario')
        print('6.- Regresar')

    def show_date(self, record):
        print('Dia:', record[0])
        print('Administrador:', record[1])
        print('ID Pelicula:', record[2])
        print('Pelicula:', record[3])

    def show_estrenos(self, record):
        print('Dia:', record[1])
        print('Pelicula:', record[0])

    def show_date_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    def show_date_midder(self):
        print('-'*48)

    def show_date_footer(self):
        print('*'*48)

    """
    *************************
    *Vista para los asientos*
    *************************
    """
    def asiento_menu(self):
        print('*************************')
        print('* -- Submenu Asiento -- *')
        print('*************************')
        print('1.- Crear asiento')
        print('2.- Leer asientos usuario')
        print('3.- Leer asientos sala')
        #print('4.- Actualizar sala')
        print('4.- Borrar asiento')
        print('5.- Regresar')

    def show_asiento(self, record):
        print('Pasillo:', record[0])
        print('Fila:', record[1])
        print('ID Usuario:', record[2])
        print('Sala:', record[3])
        print('Asiento:', record[4])

    def show_asiento_user(self, record):
        print('Nombre:', record[0])
        print('Tipo de Sala:', record[1])
        print('Sala:', record[2])
        print('Estatus de asiento:', record[3])
        print('Asiento:', record[4],end="")
        print(' -', record[5])

    def show_asiento_sala(self, record):
        print('Asiento:', record[0],end="")
        print(' -', record[1])
        print('Estatus de asiento:', record[2])

    def show_asiento_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    def show_asiento_midder(self):
        print('-'*48)

    def show_asiento_footer(self):
        print('*'*48)

    """
    ************************************
    *Vistas para los horarios_peliculas*
    ************************************
    """
    def hora_peli_menu(self):
        print('*******************************')
        print('* -- Submenu Hora-Pelicula -- *')
        print('*******************************')
        print('1.- Crear Horario-Pelicula')
        print('2.- Leer Horario-Pelicula')
        print('3.- Leer fecha de peliculas')
        #print('4.- Actualizar sala')
        print('4.- Borrar Horario-Pelicula')
        print('5.- Regresar')

    def show_hora_peli(self, record):
        print('Pelicula:', record[0])
        print('Dia:', record[1])
        print('Hora:', record[2])

    def show_hora_pelis(self, record):
        print('Nombre:', record[0])
        print('Tipo de Sala:', record[1])
        print('Sala:', record[2])
        print('Estatus de asiento:', record[3])
        print('Asiento:', record[4],end="")
        print(' -', record[5])


    def show_hora_peli_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    def show_hora_peli_midder(self):
        print('-'*48)

    def show_hora_peli_footer(self):
        print('*'*48)

    """
    **********************************
    *Metodos para los salas_peliculas*
    **********************************
    """
    def sala_peli_menu(self):
        print('*******************************')
        print('* -- Submenu Sala-Pelicula -- *')
        print('*******************************')
        print('1.- Crear Sala-Pelicula')
        print('2.- Leer costo de pelicula')
        #print('4.- Actualizar sala')
        print('3.- Borrar Sala-Pelicula')
        print('4.- Regresar')

    def show_sala_peli(self, record):
        print('ID horario:', record[0])
        print('ID pelicula:', record[1])
        print('Costo:', record[2])

    def show_costo_peli(self, record):
        print('Nombre :', record[0])
        print('Costo:', record[1])
        print('Sala:', record[2])

    def show_sala_peli_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    def show_sala_peli_midder(self):
        print('-'*48)

    def show_sala_peli_footer(self):
        print('*'*48)

    """
    ***********************
    *Vitas para los ticket*
    ***********************
    """
    def ticket_menu(self):
        print('*************************')
        print('* -- Submenu Tickets -- *')
        print('*************************')
        print('1.- Crear Tickets')
        print('2.- Leer Tickets de usuario')
        #print('4.- Actualizar sala')
        print('3.- Borrar Ticket')
        print('4.- Regresar')

    def show_ticket(self, record):
        print('Usuario:', record[0])
        print('Asientos:', record[1])
        print('Pago:', record[2])

    def show_ticket_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    def show_ticket_midder(self):
        print('-'*48)

    def show_ticket_footer(self):
        print('*'*48)  