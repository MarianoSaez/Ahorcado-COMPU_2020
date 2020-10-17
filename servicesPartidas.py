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

# Adicionales
    def guardar_historial(self, partidas):
        with open('saves/historial.json', 'r') as f:
            resumen = json.load(f)
            f.close()
        with open('saves/historial.json', 'w') as f:
            for i in partidas:
                resumen[i.nombre_jugador] = i.__dict__
            json.dump(resumen, f, indent=4)
            f.close()
        return resumen

    def mostrar_progreso(self, partida):
        progreso = list()
        for i in partida.palabra_aciertos:
            if i is None:
                progreso.append('_')
            else:
                progreso.append(i)
        return progreso

    def recuperar_historial(self, nombre):
        nombre = nombre.upper()
        with open('saves/historial.json', 'r') as f:
            historial = json.load(f)
            f.close()
        try:
            if None in historial[nombre]['_palabra_aciertos']:
                historial[nombre]['_result'] = 'Perdio'
            else:
                historial[nombre]['_result'] = 'Gano'
            palabra = ''
            for i in historial[nombre]['_palabra']:
                palabra += i
            historial[nombre]['_palabra'] = palabra
            return historial[nombre]
        except KeyError:
            return 'El jugador no existe'
