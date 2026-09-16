"""Cuenta de una cafetería."""
# Constante del enunciado (en MAYÚSCULAS porque no cambia)
RECARGO: int = 10


def a_entero(texto: str) -> int:
    """Convierte un texto a número entero."""
    # TODO: input() devuelve texto; conviértelo a int
    raise NotImplementedError

def a_decimal(texto: str) -> float:
    """Convierte un texto a número decimal."""
    # TODO: igual que el anterior, pero con decimales
    raise NotImplementedError

def importe(unidades: int, precio: float) -> float:
    """Importe de una línea: unidades por precio."""
    # TODO: multiplica los dos valores
    raise NotImplementedError

def recargo_terraza(base: float) -> float:
    """Importe del recargo de terraza sobre la base."""
    # TODO: aplica el porcentaje de la constante RECARGO
    raise NotImplementedError

def total(base: float, recargo: float) -> float:
    """Suma de la base y el recargo."""
    # TODO: suma los dos importes
    raise NotImplementedError

def formatear(etiqueta: str, valor: float) -> str:
    """Devuelve una línea del tipo  'Total: 3.50 €'  (2 decimales)."""
    # TODO: usa una f-string con :.2f y el símbolo €
    raise NotImplementedError
