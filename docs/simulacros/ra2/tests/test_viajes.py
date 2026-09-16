"""Tests de viajes."""
import pytest

from viajes import litros_necesarios, coste, distancia, plazas_necesarias, media


@pytest.mark.parametrize("args,esperado", [
    ((100.0, 6.5), 6.5),
    ((0.0, 5.0), 0.0),
    ((250.0, 7.2), 18.0),
    ((37.5, 4.8), 1.8),
])
def test_litros_necesarios(args, esperado):
    resultado = litros_necesarios(*args)
    if isinstance(esperado, float):
        assert resultado == pytest.approx(esperado)
    else:
        assert resultado == esperado


@pytest.mark.parametrize("args,esperado", [
    ((30.0, 1.549), 46.47),
    ((0.0, 1.5), 0.0),
    ((12.5, 1.6), 20.0),
])
def test_coste(args, esperado):
    resultado = coste(*args)
    if isinstance(esperado, float):
        assert resultado == pytest.approx(esperado)
    else:
        assert resultado == esperado


@pytest.mark.parametrize("args,esperado", [
    ((0.0, 0.0, 3.0, 4.0), 5.0),
    ((1.0, 1.0, 1.0, 1.0), 0.0),
    ((-2.0, 0.0, 2.0, 0.0), 4.0),
])
def test_distancia(args, esperado):
    resultado = distancia(*args)
    if isinstance(esperado, float):
        assert resultado == pytest.approx(esperado)
    else:
        assert resultado == esperado


@pytest.mark.parametrize("args,esperado", [
    ((10, 4), 3),
    ((8, 4), 2),
    ((1, 5), 1),
    ((0, 5), 0),
])
def test_plazas_necesarias(args, esperado):
    resultado = plazas_necesarias(*args)
    if isinstance(esperado, float):
        assert resultado == pytest.approx(esperado)
    else:
        assert resultado == esperado


@pytest.mark.parametrize("args,esperado", [
    (([1.0, 2.0, 3.0],), 2.0),
    (([],), 0.0),
    (([5.0],), 5.0),
    (([2.0, 3.0],), 2.5),
])
def test_media(args, esperado):
    resultado = media(*args)
    if isinstance(esperado, float):
        assert resultado == pytest.approx(esperado)
    else:
        assert resultado == esperado
