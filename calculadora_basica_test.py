import unittest
from calculadora_basica import Calculadora


def test_soma():
    print("***************")
    print("teste_soma_1")
    try:
        teste = Calculadora().calcular(30, 20, "soma")
        assert teste == 50
        print("Saída correta")
    except AssertionError:
        print('ERRO:')
        print('Resultado esperado: 50')
        print('Resultado obtido: ', teste)
    print("teste_soma_2")
    try:
        teste = Calculadora().calcular(30, 2, "soma")
        assert teste == 50
        print("Saída correta")
    except AssertionError:
        print('ERRO:')
        print('Resultado esperado: 50')
        print('Resultado obtido: ', teste)



def test_subtracao():
    print("***************")
    print("teste_subtracao_1")
    try:
        teste = Calculadora().calcular(200, 97, "subtracao")
        assert teste == 103
        print("Saída correta")
    except AssertionError:
        print('ERRO:')
        print('Resultado esperado: 103')
        print('Resultado obtido: ', teste)
    print("teste_subtracao_2")
    try:
        teste = Calculadora().calcular(200, 9, "subtracao")
        assert teste == 103
        print("Saída correta")
    except AssertionError:
        print('ERRO:')
        print('Resultado esperado: 103')
        print('Resultado obtido: ', teste)



def test_multiplicacao():
    print("***************")
    print("teste_multiplicacao_1")
    try:
        teste = Calculadora().calcular(5, 38, "multiplicacao")
        assert teste == 190
        print("Saída correta")
    except AssertionError:
        print('ERRO:')
        print('Resultado esperado: 190')
        print('Resultado obtido: ', teste)
    print("teste_multiplicacao_2")
    try:
        teste = Calculadora().calcular(5, 5, "multiplicacao")
        assert teste == 190
        print("Saída correta")
    except AssertionError:
        print('ERRO:')
        print('Resultado esperado: 190')
        print('Resultado obtido: ', teste)


def test_divisao():
    print("***************")
    print("teste_divisao_1")
    try:
        teste = Calculadora().calcular(500, 4, "divisao")
        assert teste == 125
        print("Saída correta")
    except AssertionError:
        print('ERRO:')
        print('Resultado esperado: 125')
        print('Resultado obtido: ', teste)
    print("teste_divisao_2")
    try:
        teste = Calculadora().calcular(500, 9, "divisao")
        assert teste == 125
        print("Saída correta")
    except AssertionError:
        print('ERRO:')
        print('Resultado esperado: 125')
        print('Resultado obtido: ', teste)
        print("***************")


test_soma()
test_subtracao()
test_multiplicacao()
test_divisao()
