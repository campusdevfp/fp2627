"""Cálculos de un viaje."""
import math


def litros_necesarios(km: float, consumo: float) -> float:
    """Litros para recorrer km con un consumo dado por cada 100 km."""
    # TODO: el consumo viene por cada 100 km, así que hay que escalarlo
    raise NotImplementedError

def coste(litros: float, precio_litro: float) -> float:
    """Lo que cuesta repostar esos litros."""
    # TODO: multiplica los dos valores
    raise NotImplementedError

def distancia(x1: float, y1: float, x2: float, y2: float) -> float:
    """Distancia en línea recta entre dos puntos."""
    # TODO: teorema de Pitágoras con math.sqrt
    raise NotImplementedError

def plazas_necesarias(viajeros: int, capacidad: int) -> int:
    """Vehículos necesarios: nunca se deja a nadie fuera."""
    # TODO: una división que redondea SIEMPRE hacia arriba (math.ceil)
    raise NotImplementedError

def media(valores: list[float]) -> float:
    """Media aritmética; 0.0 si la lista está vacía."""
    # TODO: cuidado con la lista vacía: dividir entre 0 rompe
    raise NotImplementedError
