import abc


class Operacao:

    def executar(self, valor1, valor2):
        return


class Calculadora:
    def calcular(self, valor1, valor2, operador):
        resultado = OperacaoFabrica().criar(operador)
        return resultado.executar(valor1, valor2)


class OperacaoFabrica:
    def criar(self, operador):
        if operador == "soma":
            return Soma()
        elif operador == "subtracao":
            return Subtracao()
        elif operador == "multiplicacao":
            return Multiplicacao()
        else:
            return Divisao()


class Soma:
    def executar(self, valor1, valor2):
        resultado = valor1 + valor2
        return resultado


class Subtracao:
    def executar(self, valor1, valor2):
        resultado = valor1 - valor2
        return resultado


class Multiplicacao:
    def executar(self, valor1, valor2):
        resultado = valor1 * valor2
        return resultado


class Divisao:
    def executar(self, valor1, valor2):
        resultado = valor1 / valor2
        return resultado
