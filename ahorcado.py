from servicesPartidas import ServicesPartidas


class Ahorcado():
    def __init__(self):
        self.service = ServicesPartidas()

    def un_jugador(self):
        nombre = input('Ingrese su nombre: ')
        dificultad = int(input('Ingrese una dificultad [1-10]: '))
        partida = self.service.iniciar_partida(nombre, dificultad, '', '')
        resultado = 'Continua'
        while resultado == 'Continua':
            try:
                letra = input('Ingrese un letra: ')
                if letra == 'salir':
                    # Mensaje de despedida
                    return True
                resultado = self.service.intentar_letra(partida, letra)
            except ValueError:
                # Mensaje de intentos repetidos
                continue
            if resultado == 'Gano' or resultado == 'Perdio':
                # Mostrar un resumen o algo asi
                return True
        return False

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
        resultado = 'Continua'
        while resultado == 'Continua':
            try:
                letra = input('Ingrese un letra: ')
                if letra == 'salir':
                    # Mensaje de despedida
                    return True
                resultado = self.service.intentar_letra(partida1, letra)
            except ValueError:
                # Mensaje de intentos repetidos
                continue
            if resultado == 'Gano' or resultado == 'Perdio':
                # Mostrar un resumen o algo asi
                break
        nombre2 = input('Ingrese el nombre del P1: ')
        dificultad2 = int(input('Ingrese la dificultad [1-10]: '))
        palabra_jugador_2 = input('Ingrese la palabra que debera adivinar: ')
        tipo_palabra_jugador_2 = input('Ingrese a que categoria pertenece'
                                       'la palabra: ')
        partida2 = self.service.iniciar_partida(nombre2,
                                                dificultad2,
                                                palabra_jugador_2,
                                                tipo_palabra_jugador_2)
        resultado = 'Continua'
        while resultado == 'Continua':
            try:
                letra = input('Ingrese un letra: ')
                if letra == 'salir':
                    # Mensaje de despedida
                    return True
                resultado = self.service.intentar_letra(partida2, letra)
            except ValueError:
                # Mensaje de intentos repetidos
                continue
            if resultado == 'Gano' or resultado == 'Perdio':
                # Mostrar un resumen o algo asi
                return True
        return False
