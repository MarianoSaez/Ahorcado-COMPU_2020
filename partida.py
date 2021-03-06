class Partida():
    def __init__(self, palabra, intentos, tipo_palabra, nombre_jugador):
        self.palabra_aciertos = list()
        self.palabra = palabra
        self.tipo_palabra = tipo_palabra
        self.intentos = intentos
        self.nombre_jugador = nombre_jugador

    @property
    def palabra(self):
        return self._palabra

    @palabra.setter
    def palabra(self, value):
        if value == '':
            raise ValueError
        self._palabra = list(value.upper())
        for i in self.palabra:
            self.palabra_aciertos.append(None)

    @property
    def tipo_palabra(self):
        return self._tipo_palabra

    @tipo_palabra.setter
    def tipo_palabra(self, value):
        if value == '':
            raise ValueError
        self._tipo_palabra = value.upper()

    @property
    def intentos(self):
        return self._intentos

    @intentos.setter
    def intentos(self, value):
        if value < 0:
            raise ValueError
        self._intentos = value

    @property
    def nombre_jugador(self):
        return self._nombre_jugador

    @nombre_jugador.setter
    def nombre_jugador(self, value):
        if value == '':
            raise ValueError
        self._nombre_jugador = value.upper()

    @property
    def palabra_aciertos(self):
        return self._palabra_aciertos

    @palabra_aciertos.setter
    def palabra_aciertos(self, value):
        self._palabra_aciertos = value

    def __str__(self):
        palabra = ''
        for i in self.palabra:
            palabra += i
        return ('Jugador: %s\nPalabra adivinada: %s\nIntentos Restantes: %s\n'
                % (self.nombre_jugador, palabra, self.intentos))
