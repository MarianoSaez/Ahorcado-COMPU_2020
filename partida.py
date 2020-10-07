class Partida():
    def __init__(self, palabra, intentos, tipo_palabra, nombre_jugador):
        self.palabra_aciertos = list()
        self.palabra = palabra
        self.tipo_palabra = tipo_palabra
        self.intentos = intentos
        self.nombre_jugador = nombre_jugador

    @property
    def palabra(self):
        return self.__palabra

    @palabra.setter
    def palabra(self, value):
        if value == '':
            raise ValueError
        self.__palabra = list(value.upper())
        for i in self.palabra:
            self.palabra_aciertos.append(None)

    @property
    def tipo_palabra(self):
        return self.__tipo_palabra

    @tipo_palabra.setter
    def tipo_palabra(self, value):
        if value == '':
            raise ValueError
        self.__tipo_palabra = value.upper()

    @property
    def intentos(self):
        return self.__intentos

    @intentos.setter
    def intentos(self, value):
        if value < 0:
            raise ValueError
        self.__intentos = value

    @property
    def nombre_jugador(self):
        return self.__nombre_jugador

    @nombre_jugador.setter
    def nombre_jugador(self, value):
        if value == '':
            raise ValueError
        self.__nombre_jugador = value.upper()

    @property
    def palabra_aciertos(self):
        return self.__palabra_aciertos

    @palabra_aciertos.setter
    def palabra_aciertos(self, value):
        self.__palabra_aciertos = value
