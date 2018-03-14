from ejercicio7 import Ejercicio7

ej7 = Ejercicio7()
resultado = ej7.findS(ej7.training_set)
print(resultado)
partec = []
partec2 = []
for x in range(0,10000):
    (con_neg, sin_neg) = ej7.parteC()
    partec.append(con_neg)
    partec2.append(sin_neg)
resultado_con_neg = sum(partec)/len(partec)
resultado_sin_neg = sum(partec2)/len(partec2)
print(resultado_con_neg)
print(resultado_sin_neg)
