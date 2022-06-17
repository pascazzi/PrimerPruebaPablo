def letra_a_texto(numero):
    diccionario_texto = {1: "uno", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco",
                         6: "seis", 7: "siete", 8: "ocho", 9: "nueve", 0: "cero"}
    return diccionario_texto[numero]



def cadenaATexto(numero):
    cadena = str(numero)
    texto = ''
    for x in cadena:
        texto = texto + letra_a_texto(int(x)) + ' '
    return texto


class MiNumero:
    texto = 'Cinco'

    valorNro = 0

    def getValor(self):
        return self.valorNro

    def __init__(self, valorNro):
        self.valorNro = valorNro

        self.texto = cadenaATexto((self.valorNro))

    def __str__(self):
        return self.texto

    def __add__(self, other):
        nuevo = MiNumero(self.valorNro + other.valorNro)
        return nuevo
