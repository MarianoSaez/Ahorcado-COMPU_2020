from ahorcado import Ahorcado

if __name__ == '__main__':
    juego = Ahorcado()
    print('====== BIENVENIDO AL AHORCADO ======')
    print('1. Un jugador')
    print('2. Dos jugadores')
    seleccion = int(input('Seleccione un tipo de juego: '))
    if seleccion == 1:
        juego.un_jugador()
    if seleccion == 2:
        juego.dos_jugadores()
