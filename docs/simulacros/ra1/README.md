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
IVA = 21
DESCUENTO = 15

precio = 80.0
unidades = 3

base = unidades * precio
base = base - base * DESCUENTO / 100
total = base * (1 + IVA / 100)

print(f"{total:.2f}")
```

- **a)** `246.84`
- **b)** `290.40`
- **c)** `246.83`
- **d)** `205.70`

**2.** ¿Qué imprime?

```python
IVA = 21

precio_unidad = 19.95
unidades = 3

subtotal = unidades * precio_unidad
iva = subtotal * IVA / 100

print(f"Subtotal: {subtotal:.2f} | IVA: {iva:.2f}")
```

- **a)** `Subtotal: 59.85 | IVA: 12.56`
- **b)** `Subtotal: 59.85 | IVA: 72.42`
- **c)** `Subtotal: 60.00 | IVA: 12.60`
- **d)** `Subtotal: 59.85 | IVA: 12.57`

**3.** El descuento se aplica **antes** del IVA. ¿Qué imprime?

```python
IVA = 21
DESCUENTO = 10

base = 100.0
con_descuento = base * (1 - DESCUENTO / 100)
total = con_descuento * (1 + IVA / 100)

print(f"{total:.2f}")
```

- **a)** `108.90`
- **b)** `121.00`
- **c)** `108.89`
- **d)** `110.00`

**4.** ¿Qué imprime?

```python
precio = 1.33
unidades = 2.25

importe = precio * unidades
print(f"{importe:.2f}")
```

- **a)** `2.99`
- **b)** `3`
- **c)** `3.00`
- **d)** `2.9925`

**5.** ¿Qué imprime este programa?

```python
PRECIO_CENTIMOS = 251

dinero = 800
unidades = dinero // PRECIO_CENTIMOS
resto = dinero % PRECIO_CENTIMOS

print(f"Quedan {unidades} unidades y sobran {resto} centimos")
```

- **a)** `Quedan 3 unidades y sobran 53 centimos`
- **b)** `Quedan 4 unidades y sobran 47 centimos`
- **c)** `Quedan 3 unidades y sobran 0.47 centimos`
- **d)** `Quedan 3 unidades y sobran 47 centimos`

**6.** ¿Qué imprime?

```python
centimos = 287

m100 = centimos // 100
centimos = centimos % 100
m50 = centimos // 50
centimos = centimos % 50
m20 = centimos // 20
centimos = centimos % 20

print(m100, m50, m20, centimos)
```

- **a)** `2 1 1 7`
- **b)** `2 0 1 17`
- **c)** `2 1 1 17`
- **d)** `2 1 0 17`

**7.** El usuario escribe `1.234,56`. ¿Qué imprime?

```python
texto = "1.234,56"

limpio = texto.replace(".", "")
limpio = limpio.replace(",", ".")
valor = float(limpio)

print(f"{valor:,.2f}")
```

- **a)** `1234,56`
- **b)** `ValueError`
- **c)** `1.23`
- **d)** `1,234.56`

**8.** ¿Qué error lanza este programa?

```python
cantidad = "12 unidades"
n = int(cantidad)
print(n * 2)
```

- **a)** `ValueError`
- **b)** `AttributeError`
- **c)** `SyntaxError`
- **d)** `TypeError`

**9.** ¿Qué imprime?

```python
entrada_1 = "15"
entrada_2 = "2"

media = int(entrada_1) // int(entrada_2)
print(media)
```

- **a)** `7.5`
- **b)** `7`
- **c)** `8`
- **d)** `TypeError`

**10.** ¿Qué imprime?

```python
entrada_1 = "15"
entrada_2 = "2"

media = int(entrada_1) / int(entrada_2)
print(media)
```

- **a)** `7.5`
- **b)** `8`
- **c)** `7`
- **d)** `'15' / '2'`

**11.** ¿Qué imprime?

```python
edad = "20"
siguiente = edad + "5"
print(siguiente)
```

- **a)** `TypeError`
- **b)** `2005`
- **c)** `205`
- **d)** `25`

**12.** ¿Qué imprime?

```python
a = "10"
b = 10

print(a == b, int(a) == b)
```

- **a)** `False False`
- **b)** `True True`
- **c)** `True False`
- **d)** `False True`

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
| 4 | **a** |
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
