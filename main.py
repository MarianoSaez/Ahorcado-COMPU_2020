from ahorcado import Ahorcado

if __name__ == '__main__':
    juego = Ahorcado()
    play = True
    while play:
        play = juego.menu()
        input('Pulse una tecla para continuar...')
