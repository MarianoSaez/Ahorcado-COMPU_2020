import unittest
from parameterized import parameterized
from ahorcado import Ahorcado
from servicesPartidas import ServicesPartidas
from unittest.mock import patch


# Esta clase se encarga de dar cobertura al resto de funciones
#  que nos son cubiertas en otros test
class TestExtra(unittest.TestCase):
    @parameterized.expand([
        ('jugador1'),
        ('jugador2'),
        ('ClaUdio')
    ])
    # Se obtiene el historial de un jugador ingresando su nombre
    # Input: [nombre_jugador]
    # Output: [true]
    def test_consultar_historial(self, nombre_jugador):
        juego = Ahorcado()
        with patch('builtins.input', side_effect=(nombre_jugador, )):
            result = juego.consultar_historial()
            self.assertTrue(result)

    # El metodo recuperar_historial se encarga de leer y devolver
    # el diccionario con la key que se le dio como parametro
    # Input: nombre_jugador
    # Normal output => historial : diccionario
    # Error => 'El jugador no existe' : String
    @parameterized.expand([
        ('Jugador1',
            {
             "_palabra_aciertos": [
                "C",
                "E",
                "L",
                "U",
                "L",
                "A",
                "R"
                ],
             "_palabra": "CELULAR",
             "_tipo_palabra": "ELECTRONICA",
             "_intentos": 2,
             "_nombre_jugador": "JUGADOR1",
             "_result": "Gano"}),
        ('Alguien_que_no_existe', 'El jugador no existe')
    ])
    def test_recuperar_historial(self, nombre_jugador, result):
        historial = ServicesPartidas().recuperar_historial(nombre_jugador)
        self.assertEqual(historial, result)


if __name__ == '__main__':
    unittest.main()
