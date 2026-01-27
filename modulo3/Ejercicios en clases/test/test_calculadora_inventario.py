import pytest
from calculador_inventario import CalculadoraInventario


def test_calcular_total():
    calculadora = CalculadoraInventario()
    cantidades = [11, 5, 3]
    resultado = calculadora.calcular_total(cantidades)
    assert resultado == 19


@pytest.fixture
def calculadora():
    return CalculadoraInventario()

def test_calcular_total_con_fixture(calculadora):
    assert calculadora.calcular_total([2, 3, 4]) == 9


from unittest.mock import Mock
from calculador_inventario import Transaccion

def test_guardar_transaccion_mock(calculadora):
    mock_db = Mock()
    mock_db.guardar.return_value = True

    transaccion = Transaccion("Laptop", 2)
    resultado = calculadora.guardar_transaccion(transaccion, mock_db)

    assert resultado is True
    mock_db.guardar.assert_called_once_with(transaccion)
