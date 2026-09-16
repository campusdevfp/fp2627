# Test de práctica · RA1 — Elementos del lenguaje

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
print(7 / 2)
```

- **a)** `3.5`
- **b)** `3`
- **c)** `4`
- **d)** `3.0`

**2.** ¿Qué imprime?

```python
print(7 // 2)
```

- **a)** `3.5`
- **b)** `4`
- **c)** `3.0`
- **d)** `3`

**3.** ¿Qué imprime?

```python
print(-7 // 2)
```

- **a)** `-4`
- **b)** `-3`
- **c)** `3`
- **d)** `-3.5`

**4.** ¿Qué imprime?

```python
print(-7 % 2 - 2)
```

- **a)** `1`
- **b)** `ValueError`
- **c)** `-1`
- **d)** `0`

**5.** ¿Qué tipo se muestra?

```python
print(type(6 / 3))
```

- **a)** `<class 'bool'>`
- **b)** `<class 'str'>`
- **c)** `<class 'int'>`
- **d)** `<class 'float'>`

**6.** ¿Qué imprime?

```python
print(6 / 3 == 2)
```

- **a)** `False`
- **b)** `1`
- **c)** `True`
- **d)** `TypeError`

**7.** ¿Qué imprime?

```python
a = 5
b = 9
a, b = b, a
print(a, b)
```

- **a)** `9 9`
- **b)** `5 5`
- **c)** `5 9`
- **d)** `9 5`

**8.** ¿Qué imprime?

```python
x = 5
y = x
x = 10
print(x)
```

- **a)** `10`
- **b)** `TypeError`
- **c)** `15`
- **d)** `5`

**9.** ¿Qué error lanza este programa?

```python
edad = "20"
print(edad + 1)
```

- **a)** `ValueError`
- **b)** `TypeError`
- **c)** `NameError`
- **d)** `SyntaxError`

**10.** ¿Qué error lanza?

```python
print(int("3.5"))
```

- **a)** `ValueError`
- **b)** `SyntaxError`
- **c)** `TypeError`
- **d)** `ZeroDivisionError`

**11.** ¿Qué imprime?

```python
print(int(9.99))
```

- **a)** `ValueError`
- **b)** `9.99`
- **c)** `9`
- **d)** `10`

**12.** ¿Qué imprime?

```python
print(int(-2.7))
```

- **a)** `-2.7`
- **b)** `-3`
- **c)** `2`
- **d)** `-2`

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
| 1 | **a** |
| 2 | **d** |
| 3 | **a** |
| 4 | **c** |
| 5 | **d** |
| 6 | **c** |
| 7 | **d** |
| 8 | **a** |
| 9 | **b** |
| 10 | **a** |
| 11 | **c** |
| 12 | **d** |

Si has fallado más de tres, vuelve a la unidad antes del examen: no es cuestión de suerte,
es que hay algo del temario que no está asentado.

</details>
