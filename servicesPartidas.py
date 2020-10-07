from partida import Partida
import json
from random import randint


class ServicesPartidas():
    def iniciar_partida(self, nombre, intentos, palabra, tipo_palabra):
        if intentos > 10 or intentos < 1:
            raise ValueError
        if palabra == '' and tipo_palabra == '':
            random = self.get_random_palabra()
            palabra = random['palabra']
            tipo_palabra = random['tipo_palabra']
        intentos *= len(palabra)
        return Partida(palabra, intentos, tipo_palabra, nombre)

    def get_random_palabra(self):
        with open("saves/pool_palabras.json") as f:
            pool_palabras = json.load(f)
            index = str(randint(0, len(pool_palabras)-1))
            palabra = pool_palabras[index]['_palabra']
            tipo_palabra = pool_palabras[index]['_tipo_palabra']
            f.close()
        return {'palabra': palabra, 'tipo_palabra': tipo_palabra}

    def intentar_letra(self, partida, letra):
        letra = letra.upper()
        if letra in partida.palabra_aciertos:
            raise ValueError
        for i in range(len(partida.palabra)):
            if partida.palabra[i] == letra:
                partida.palabra_aciertos[i] = letra
        diferencia = [i for i in partida.palabra
                      if i in partida.palabra_aciertos]
        if len(diferencia) == len(partida.palabra):
            return 'Gano'
        partida.intentos -= 1
        if partida.intentos == 0:
            return 'Perdio'
        return 'Continua'
