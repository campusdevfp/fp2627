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
def saludar(nombre):
    mensaje = f"Hola, {nombre}"

print(saludar("Ada"))
```

- **a)** `Hola, Ada`
- **b)** `TypeError`
- **c)** `Ada`
- **d)** `None`

**2.** ¿Qué imprime?

```python
def doble(x):
    print(x * 2)

print(doble(5))
```

- **a)** `10 ⏎ None`
- **b)** `10 ⏎ 10`
- **c)** `5 ⏎ None`
- **d)** `None ⏎ 10`

**3.** ¿Qué error lanza?

```python
def doble(x):
    print(x * 2)

print(doble(5) + 1)
```

- **a)** `TypeError`
- **b)** `AttributeError`
- **c)** `ValueError`
- **d)** `NameError`

**4.** ¿Qué imprime?

```python
def doble(x):
    return x * 2

print(doble(5) + doble(3))
```

- **a)** `TypeError`
- **b)** `None`
- **c)** `8`
- **d)** `16`

**5.** ¿Qué imprime?

```python
def f():
    return 1
    return 2

print(f())
```

- **a)** `1 2 3`
- **b)** `3`
- **c)** `1`
- **d)** `None`

**6.** ¿Qué imprime?

```python
def medidas(b, h):
    return b * h, 2 * (b + h)

print(medidas(4, 3))
```

- **a)** `12`
- **b)** `[12, 14]`
- **c)** `12 14`
- **d)** `(12, 14)`

**7.** ¿Qué imprime?

```python
def saludar(nombre, saludo="Hola"):
    return f"{saludo}, {nombre}"

print(saludar("Ada"))
```

- **a)** `Hola, Ada`
- **b)** `TypeError`
- **c)** `Hola Ada`
- **d)** `Ada, Hola`

**8.** ¿Qué imprime?

```python
def saludar(nombre, saludo="Hola"):
    return f"{saludo}, {nombre}"

print(saludar(saludo="Buenas", nombre="Ada"))
```

- **a)** `Ada, Buenas`
- **b)** `Buenas, Ada`
- **c)** `Hola, Ada`
- **d)** `TypeError`

**9.** ¿Qué error lanza este programa?

```python
def f(a=1, b):
    return a + b

print(f(2, 3))
```

- **a)** `SyntaxError`
- **b)** `NameError`
- **c)** `TypeError`
- **d)** `ValueError`

**10.** ¿Qué error lanza?

```python
def area(base, altura):
    return base * altura

print(area(3))
```

- **a)** `IndexError`
- **b)** `ValueError`
- **c)** `TypeError`
- **d)** `NameError`

**11.** ¿Qué imprime?

```python
def potencia(base, exponente=2):
    return base ** exponente

print(potencia(2, 10))
```

- **a)** `32`
- **b)** `25`
- **c)** `TypeError`
- **d)** `1024`

**12.** ¿Qué imprime?

```python
x = 10

def f():
    x = 99

f()
print(x)
```

- **a)** `None`
- **b)** `NameError`
- **c)** `99`
- **d)** `10`

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
