import random

class Ejercicio7():
    def __init__(self):
        self.training_set = [
        {'dedicacion': 'alta',  'dificultad': 'alta',  'horario': 'nocturno', 'humedad': 'media', 'humor_doc': 'bueno', 'salva': 'si' },
        {'dedicacion': 'baja',  'dificultad': 'media', 'horario': 'matutino', 'humedad': 'alta',  'humor_doc': 'malo',  'salva': 'no' },
        {'dedicacion': 'media', 'dificultad': 'alta',  'horario': 'nocturno', 'humedad': 'media', 'humor_doc': 'malo',  'salva': 'si' },
        {'dedicacion': 'media', 'dificultad': 'alta',  'horario': 'matutino', 'humedad': 'alta',  'humor_doc': 'bueno', 'salva': 'no' }]

    def findS(self, training_set):
        # empiezo con la hipotesis más específica
        hipotesis = {'dedicacion': '_',  'dificultad': '_',  'horario': '_', 'humedad': '_', 'humor_doc': '_'}

        for train_elem in training_set:
            # si no salva entonces no se va a cumplir en la función que define h
            if train_elem['salva'] == 'no':
                continue
            hipotesis = self.actualizarHipotesis(hipotesis,train_elem)

        return hipotesis

    def actualizarHipotesis(self,hipotesis,train_elem):
        for key, value in train_elem.items():
        # salva no pertenece a la tupla de hipotesis
            if key == 'salva':
                continue

            # si es vacio, seteo el valor de train_elem
            if hipotesis[key] == '_':
                hipotesis[key] = train_elem[key]

            # si no igual a train_elem ni es lo mas general (?) entonces lo vuelvo lo más general
            if hipotesis[key] != train_elem[key] and train_elem[key] != '?':
                hipotesis[key] = '?'
        return hipotesis

    def generateRandom(self):
        dedicacion = ['alta','baja', 'media']
        dificultad = ['alta', 'media']
        horario = ['nocturno', 'matutino']
        humedad = ['alta','baja', 'media']
        humor_doc = ['bueno', 'malo']
        tupla = {'dedicacion':random.choice(dedicacion),
                'dificultad': random.choice(dificultad),
                'horario': random.choice(horario),
                'humedad': random.choice(humedad),
                'humor_doc': random.choice(humor_doc)}
        if tupla['dificultad'] == 'media':
            tupla['salva'] = 'si'
        else:
            tupla['salva'] = 'no'

        return tupla

    def parteC(self):
        # escribo el objetivo
        objetivo = {'dedicacion': '?',  'dificultad': 'media',  'horario': '?', 'humedad': '?', 'humor_doc': '?'}
        # empiezo con las hipotesis mas generales
        hipotesis = {'dedicacion': '_',  'dificultad': '_',  'horario': '_', 'humedad': '_', 'humor_doc': '_'}
        # voy a usar un set para guardar las tuplas y evitar elementos repetidos
        training_set = []
        # contador de tuplas
        contador = 0
        while hipotesis != objetivo:
            contador += 1
            new_generated = False

            # mientras no me toque un elemento que no este en el training_set genero uno nuevo
            while not new_generated:
                new_elem = self.generateRandom()
                new_generated = training_set.count(new_elem) == 0
                training_set.append(new_elem)
                
                # actualizo las hipotesis con ese nuevo elemento
                if new_elem['salva'] == 'no':
                    continue
                hipotesis = self.actualizarHipotesis(hipotesis,training_set[-1])

        return (contador)
