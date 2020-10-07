from servicesPartidas import ServicesPartidas


class Ahorcado():
    def __init__(self):
        self.service = ServicesPartidas()

    def menu(self):
        print('====== BIENVENIDO AL AHORCADO ======\n')
        print('1. Un jugador')
        print('2. Dos jugadores')
        seleccion = int(input('Seleccione un tipo de juego: '))
        if seleccion == 1:
            return self.un_jugador()
        elif seleccion == 2:
            return self.dos_jugadores()
        else:
            return False

    def jugar(self, partida):
        resultado = 'Continua'
        while resultado == 'Continua':
            progreso = self.service.mostrar_progreso(partida)
            for i in progreso:
                print(i, end=' ')
            print('\nTipo: ', partida.tipo_palabra)
            try:
                letra = input('\nIngrese una letra: ')
                if letra == 'salir':
                    print('\nCHAU!')
                    return True
                resultado = self.service.intentar_letra(partida, letra)
            except ValueError:
                print('\nYa probaste esa letra!')
                continue
            if resultado == 'Gano' or resultado == 'Perdio':
                print('\n', resultado.upper())
                print(partida)
                self.service.guardar_historial([partida])
                return True
        return False

    def un_jugador(self):
        nombre = input('Ingrese su nombre: ')
        dificultad = int(input('Ingrese una dificultad [1-10]: '))
        partida = self.service.iniciar_partida(nombre, dificultad, '', '')
        jugar = self.jugar(partida)
        return jugar

    def dos_jugadores(self):
        nombre1 = input('Ingrese el nombre del P1: ')
        dificultad1 = int(input('Ingrese la dificultad [1-10]: '))
        palabra_jugador_1 = input('Ingrese la palabra que debera adivinar: ')
        tipo_palabra_jugador_1 = input('Ingrese a que categoria pertenece'
                                       'la palabra: ')
        partida1 = self.service.iniciar_partida(nombre1,
                                                dificultad1,
                                                palabra_jugador_1,
                                                tipo_palabra_jugador_1)
        jugar = self.jugar(partida1)
        nombre2 = input('Ingrese el nombre del P2: ')
        dificultad2 = int(input('Ingrese la dificultad [1-10]: '))
        palabra_jugador_2 = input('Ingrese la palabra que debera adivinar: ')
        tipo_palabra_jugador_2 = input('Ingrese a que categoria pertenece'
                                       'la palabra: ')
        partida2 = self.service.iniciar_partida(nombre2,
                                                dificultad2,
                                                palabra_jugador_2,
                                                tipo_palabra_jugador_2)
        jugar = self.jugar(partida2)
        return jugar
