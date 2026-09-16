# Test de práctica · RA2 — Funciones y librerías

El examen del **primer trimestre** es un test de 12 preguntas **sobre código**: se te da
un fragmento y tienes que decir qué imprime, qué error da o cuál de cuatro versiones es la
correcta. No hay preguntas de definiciones.

Este test de práctica tiene el mismo formato, la misma dificultad y la misma corrección que
el de verdad. La diferencia es que aquí **tienes las respuestas al final**.

## Cómo se puntúa

| | |
|---|---|
| Acierto | **+0.83** puntos |
| Error | **−0.28** puntos |
| En blanco | 0 |

`nota = (aciertos − errores ÷ 3) × 0.83`, con un mínimo de 0.

Se resta para que contestar al azar no compense. **Si dudas entre dos opciones, marca; si
no tienes ni idea, déjalo en blanco.**

!!! tip "Hazlo como el de verdad"
    45 minutos, sin ordenador y sin apuntes. Y **no ejecutes el código** hasta haber
    contestado: la gracia está en leerlo. Después compruébalo en Python, que es donde de
    verdad se aprende.

---

## Preguntas

**1.** ¿Qué imprime este programa?

```python
IVA = 21


def con_iva(precio):
    print(round(precio * (1 + IVA / 100), 2))


resultado = con_iva(25.0)
print(resultado)
```

- **a)** `30.25 ⏎ 30.25`
- **b)** `25 ⏎ None`
- **c)** `None ⏎ 30.25`
- **d)** `30.25 ⏎ None`

**2.** ¿Qué error lanza este programa?

```python
def media(notas):
    print(sum(notas) / len(notas))


total = media([5.0, 7.0]) * 2
print(total)
```

- **a)** `TypeError`
- **b)** `ValueError`
- **c)** `AttributeError`
- **d)** `NameError`

**3.** ¿Qué imprime?

```python
def base(unidades, precio):
    return unidades * precio


def con_iva(importe):
    return round(importe * 1.21, 2)


print(con_iva(base(3, 10.0)))
```

- **a)** `36.3`
- **b)** `TypeError`
- **c)** `18.15`
- **d)** `None`

**4.** ¿Qué imprime?

```python
def medidas(base, altura):
    """Área y perímetro de un rectángulo."""
    return base * altura, 2 * (base + altura)


print(medidas(4.0, 3.0))
```

- **a)** `[12.0, 14.0]`
- **b)** `12.0`
- **c)** `12.0 14.0`
- **d)** `(12.0, 14.0)`

**5.** ¿Qué imprime?

```python
def medidas(base, altura):
    return base * altura, 2 * (base + altura)


area, perimetro = medidas(4.0, 3.0)
print(area, perimetro)
```

- **a)** `(12.0, 14.0)`
- **b)** `12.0`
- **c)** `12.0 14.0`
- **d)** `TypeError`

**6.** ¿Qué imprime?

```python
def doble(n):
    return n * 2
    return n * 4


print(doble(5))
```

- **a)** `None`
- **b)** `10\n20`
- **c)** `20`
- **d)** `10`

**7.** ¿Qué imprime?

```python
def con_impuesto(base, tipo=21):
    """Importe con el impuesto aplicado."""
    return base * (1 + tipo / 100)


print(f"{con_impuesto(100.0):.2f} | {con_impuesto(100.0, 30):.2f}")
```

- **a)** `121.00 | 130.00`
- **b)** `TypeError`
- **c)** `130.00 | 130.00`
- **d)** `121.00 | 121.00`

**8.** ¿Qué imprime?

```python
def con_impuesto(base, tipo=21):
    return base * (1 + tipo / 100)


print(f"{con_impuesto(tipo=21, base=100.0):.2f}")
```

- **a)** `110.00`
- **b)** `121.00`
- **c)** `100.00`
- **d)** `TypeError`

**9.** ¿Qué error lanza?

```python
def linea(etiqueta="Total", valor):
    return f"{etiqueta}: {valor:.2f}"


print(linea("Base", 10.0))
```

- **a)** `SyntaxError`
- **b)** `NameError`
- **c)** `TypeError`
- **d)** `ValueError`

**10.** ¿Qué error lanza?

```python
def area_triangulo(base, altura):
    """Área de un triángulo."""
    return base * altura / 2


print(area_triangulo(10.0))
```

- **a)** `NameError`
- **b)** `ValueError`
- **c)** `TypeError`
- **d)** `IndexError`

**11.** ¿Qué imprime?

```python
def potencia(base, exponente=3):
    return float(base ** exponente)


print(potencia(2), potencia(2, 10))
```

- **a)** `1024.0 1024.0`
- **b)** `8.0 8.0`
- **c)** `TypeError`
- **d)** `8.0 1024.0`

**12.** ¿Qué imprime?

```python
def acumular(lista, valor):
    """Añade el valor a la lista."""
    lista.append(valor)
    return lista


original = [1, 2]
nueva = acumular(original, 3)
print(original)
print(nueva)
```

- **a)** `[1, 2] ⏎ [1, 2]`
- **b)** `TypeError`
- **c)** `[1, 2] ⏎ [1, 2, 3]`
- **d)** `[1, 2, 3] ⏎ [1, 2, 3]`

---

## Hoja de respuestas

Marca **una sola** opción por pregunta. Lo que quede en blanco no resta.

| # | a | b | c | d |
|:---:|:---:|:---:|:---:|:---:|
| **1** |  |  |  |  |
| **2** |  |  |  |  |
| **3** |  |  |  |  |
| **4** |  |  |  |  |
| **5** |  |  |  |  |
| **6** |  |  |  |  |
| **7** |  |  |  |  |
| **8** |  |  |  |  |
| **9** |  |  |  |  |
| **10** |  |  |  |  |
| **11** |  |  |  |  |
| **12** |  |  |  |  |

---

## Respuestas

<details><summary>Ver las respuestas</summary>

| # | Correcta |
|:---:|:---:|
| 1 | **d** |
| 2 | **a** |
| 3 | **a** |
| 4 | **d** |
| 5 | **c** |
| 6 | **d** |
| 7 | **a** |
| 8 | **b** |
| 9 | **a** |
| 10 | **c** |
| 11 | **d** |
| 12 | **d** |

Si has fallado más de tres, vuelve a la unidad antes del examen: no es cuestión de suerte,
es que hay algo del temario que no está asentado.

</details>
