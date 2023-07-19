import pytest
from main import calcular_valor_total

def test_calculo_qtd_menor_que_10():
    assert calcular_valor_total(10.0, 5) == (50.0, 50.0)
    
def test_calculo_qtd_entre_10_e_99():
    assert calcular_valor_total(10.0, 50) == (500.0, 475.0)

def test_calculo_qtd_entre_100_e_999():
    assert calcular_valor_total(10.0, 999) == (9990.0, 8991.0)
    
def test_calculo_qtd_maior_que_999():   
    assert calcular_valor_total(10.0, 1000) == (10000.0, 8500.0)

def test_calculo_qtd_limite_int32():
    assert calcular_valor_total(10.0, 2147483647) == (21474836470.0, 18253610999.5)