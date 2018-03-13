from ejercicio7 import Ejercicio7

ej7 = Ejercicio7()
resultado = ej7.findS(ej7.training_set)
print (resultado)
partec = []
for x in range(0,10000):
    resultado = ej7.parteC()
    partec.append(resultado)
resultado = sum(partec)/len(partec)
print (resultado)
