"""Tests de cafeteria."""
import pytest

from cafeteria import a_entero, a_decimal, importe, recargo_terraza, total, formatear
from cafeteria import RECARGO


def test_constante():
    assert RECARGO == 10


@pytest.mark.parametrize("args,esperado", [
    (('4',), 4),
    (('0',), 0),
    (('-2',), -2),
    (('12',), 12),
])
def test_a_entero(args, esperado):
    resultado = a_entero(*args)
    if isinstance(esperado, float):
        assert resultado == pytest.approx(esperado)
    else:
        assert resultado == esperado


@pytest.mark.parametrize("args,esperado", [
    (('2.50',), 2.5),
    (('0.80',), 0.8),
    (('0',), 0.0),
])
def test_a_decimal(args, esperado):
    resultado = a_decimal(*args)
    if isinstance(esperado, float):
        assert resultado == pytest.approx(esperado)
    else:
        assert resultado == esperado


@pytest.mark.parametrize("args,esperado", [
    ((2, 1.25), 2.5),
    ((0, 3.0), 0.0),
    ((3, 0.95), 2.8499999999999996),
    ((10, 0.1), 1.0),
])
def test_importe(args, esperado):
    resultado = importe(*args)
    if isinstance(esperado, float):
        assert resultado == pytest.approx(esperado)
    else:
        assert resultado == esperado


@pytest.mark.parametrize("args,esperado", [
    ((10.0,), 1.0),
    ((0.0,), 0.0),
    ((2.5,), 0.25),
    ((37.4,), 3.74),
])
def test_recargo_terraza(args, esperado):
    resultado = recargo_terraza(*args)
    if isinstance(esperado, float):
        assert resultado == pytest.approx(esperado)
    else:
        assert resultado == esperado


@pytest.mark.parametrize("args,esperado", [
    ((10.0, 1.0), 11.0),
    ((0.0, 0.0), 0.0),
    ((2.5, 0.25), 2.75),
])
def test_total(args, esperado):
    resultado = total(*args)
    if isinstance(esperado, float):
        assert resultado == pytest.approx(esperado)
    else:
        assert resultado == esperado


@pytest.mark.parametrize("args,esperado", [
    (('Consumiciones', 2.5), 'Consumiciones: 2.50 €'),
    (('Total', 1.2), 'Total: 1.20 €'),
    (('X', 0.0), 'X: 0.00 €'),
])
def test_formatear(args, esperado):
    resultado = formatear(*args)
    if isinstance(esperado, float):
        assert resultado == pytest.approx(esperado)
    else:
        assert resultado == esperado
