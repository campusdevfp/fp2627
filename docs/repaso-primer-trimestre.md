# Repaso del primer trimestre

Todo lo de la **UD1** y la **UD2** en una página, para la semana antes del examen.

Dos partes bien distintas, y conviene hacerlas en este orden:

| Parte | Qué es | Cómo se usa |
|---|---|---|
| **Ejercicios de repaso** | 20 ejercicios que **mezclan conceptos**: cada uno necesita dos o tres cosas de la unidad a la vez | con el editor abierto, sin prisa |
| **Dos simulacros de 20 preguntas** | Formato de examen, uno por unidad | contrarreloj, sin ordenador, con las respuestas tapadas |

!!! tip "Primero los ejercicios, después el simulacro"
    Los ejercicios te dicen **qué no sabes hacer**; el simulacro te dice **cuánto sacarías
    hoy**. En ese orden tienes margen para arreglarlo; al revés, solo te llevas el susto.

!!! warning "En qué se diferencian de los del temario"
    Los del temario practican **un** concepto cada uno, el que acabas de leer. Estos
    necesitan varios a la vez: convertir la entrada **y** calcular **y** dar formato. Así es
    como aparecen en el examen, y por eso cuestan más.

---

## Parte 1 · Ejercicios de repaso de la UD1

Diez ejercicios sobre variables y tipos, operadores, conversión de la entrada, formato de
salida y constantes. Todos piden **una función**, para que puedas comprobarla llamándola
con varios valores.

**R1.1 · Ticket de una línea.** Pide producto, unidades y precio, y muestra una línea con este formato exacto:

```text
Camisa          3 x  19.95 =    59.85
```

El producto a la izquierda en 14 huecos, las unidades a la derecha en 3, el precio en 7 con dos decimales y el importe en 9 con dos decimales. Hazlo con una función `linea(producto, unidades, precio)` para poder probarla.
<details><summary>Solución</summary>

```python
def linea(producto: str, unidades: int, precio: float) -> str:
    """Línea de ticket con el formato exacto."""
    importe: float = unidades * precio
    return f"{producto:<14}{unidades:>3} x {precio:>7.2f} = {importe:>9.2f}"


print(linea("Camisa", 3, 19.95))
```
</details>

**R1.2 · Desglose con IVA y descuento.** `desglose(base, descuento)` devuelve una tupla `(con_descuento, iva, total)` redondeada a 2 decimales. El descuento es un porcentaje y **se aplica antes** del IVA, que es una constante del 21 %.
<details><summary>Solución</summary>

```python
IVA: int = 21


def desglose(base: float, descuento: int) -> tuple[float, float, float]:
    """Importe con descuento, IVA y total, a 2 decimales."""
    con_descuento: float = base * (1 - descuento / 100)
    iva: float = con_descuento * IVA / 100
    return (round(con_descuento, 2), round(iva, 2),
            round(con_descuento + iva, 2))


print(desglose(100.0, 15))
```
</details>

**R1.3 · Cambio en monedas.** `cambio(centimos)` devuelve cuántas monedas de 100, 50, 20 y 10 céntimos hacen falta, más lo que sobra, como una tupla de cinco números. Sin bucles: solo `//` y `%`.
<details><summary>Solución</summary>

```python
def cambio(centimos: int) -> tuple[int, int, int, int, int]:
    """Monedas de 100, 50, 20 y 10, y el resto."""
    m100: int = centimos // 100
    resto: int = centimos % 100
    m50: int = resto // 50
    resto = resto % 50
    m20: int = resto // 20
    resto = resto % 20
    m10: int = resto // 10
    return m100, m50, m20, m10, resto % 10


print(cambio(287))
```
</details>

**R1.4 · Precio con coma o con punto.** El usuario puede escribir el precio como `19,95` o como `19.95`. `a_precio(texto)` lo convierte a `float` en los dos casos.
<details><summary>Solución</summary>

```python
def a_precio(texto: str) -> float:
    """Convierte a float admitiendo coma o punto decimal."""
    return float(texto.replace(",", "."))


print(a_precio("19,95"), a_precio("19.95"))
```
</details>

**R1.5 · Duración en h:mm:ss.** `duracion(segundos)` devuelve el tiempo como `1:02:05`, con dos dígitos en minutos y segundos.
<details><summary>Solución</summary>

```python
def duracion(segundos: int) -> str:
    """Duración como h:mm:ss."""
    horas: int = segundos // 3600
    resto: int = segundos % 3600
    return f"{horas}:{resto // 60:02d}:{resto % 60:02d}"


print(duracion(3725))
```
</details>

**R1.6 · Céntimos a euros.** `a_euros(centimos)` devuelve el importe como `2.87 €`, siempre con dos decimales.
<details><summary>Solución</summary>

```python
def a_euros(centimos: int) -> str:
    """Céntimos a euros, con dos decimales y el símbolo."""
    return f"{centimos / 100:.2f} €"


print(a_euros(287), a_euros(5))
```
</details>

**R1.7 · Media de tres notas, redondeada.** `media(a, b, c)` devuelve la media de tres notas con **un** decimal. Cuidado: si usas `//` en vez de `/` el resultado será otro.
<details><summary>Solución</summary>

```python
def media(a: float, b: float, c: float) -> float:
    """Media de tres notas, a un decimal."""
    return round((a + b + c) / 3, 1)


print(media(7.0, 8.0, 6.5))
```
</details>

**R1.8 · ¿Entra en el presupuesto?.** `cabe(precio, unidades, presupuesto)` devuelve `True` si el importe total **no supera** el presupuesto. El importe justo sí entra.
<details><summary>Solución</summary>

```python
def cabe(precio: float, unidades: int, presupuesto: float) -> bool:
    """Indica si el importe no supera el presupuesto."""
    return precio * unidades <= presupuesto


print(cabe(19.95, 3, 60.0), cabe(19.95, 3, 59.85), cabe(19.95, 4, 60.0))
```
</details>

**R1.9 · Tabla con cabecera y total.** `tabla(filas)` devuelve un texto de varias líneas: una cabecera, una línea por fila con el concepto a la izquierda en 14 y el importe a la derecha en 9 con dos decimales, una línea de guiones y el total.
<details><summary>Solución</summary>

```python
ANCHO: int = 23


def tabla(filas: list[tuple[str, float]]) -> str:
    """Tabla de importes con cabecera y total."""
    lineas: list[str] = [f"{'CONCEPTO':<14}{'IMPORTE':>9}", "-" * ANCHO]
    total: float = 0.0
    for concepto, importe in filas:
        lineas.append(f"{concepto:<14}{importe:>9.2f}")
        total += importe
    lineas.append("-" * ANCHO)
    lineas.append(f"{'TOTAL':<14}{total:>9.2f}")
    return "\n".join(lineas)


print(tabla([("Camisa", 59.85), ("Gorra", 7.25)]))
```
</details>

**R1.10 · Porcentaje de ocupación.** `ocupacion(ocupadas, total)` devuelve el porcentaje con un decimal y el símbolo, como `75.0%`. Si el total es 0, devuelve `0.0%` en lugar de romperse.
<details><summary>Solución</summary>

```python
def ocupacion(ocupadas: int, total: int) -> str:
    """Porcentaje de ocupación, con un decimal."""
    if total == 0:
        return "0.0%"
    return f"{ocupadas / total:.1%}"


print(ocupacion(15, 20), ocupacion(0, 0))
```
</details>


---

## Parte 2 · Ejercicios de repaso de la UD2

Diez ejercicios sobre funciones, parámetros, listas, librería estándar y módulos.

**R2.1 · Resumen de una lista de precios.** `resumen(precios)` devuelve `(minimo, maximo, media)` con la media a dos decimales. Con la lista vacía devuelve `(0.0, 0.0, 0.0)`.
<details><summary>Solución</summary>

```python
def resumen(precios: list[float]) -> tuple[float, float, float]:
    """Mínimo, máximo y media; ceros si la lista está vacía."""
    if len(precios) == 0:
        return 0.0, 0.0, 0.0
    return (min(precios), max(precios),
            round(sum(precios) / len(precios), 2))


print(resumen([19.95, 34.5, 7.25]))
```
</details>

**R2.2 · Cajas necesarias.** `cajas(unidades, por_caja)` devuelve cuántas cajas hacen falta **sin dejar unidades fuera**. Usa el módulo `math`.
<details><summary>Solución</summary>

```python
import math


def cajas(unidades: int, por_caja: int) -> int:
    """Cajas necesarias para no dejar unidades fuera."""
    return math.ceil(unidades / por_caja)


print(cajas(47, 10), cajas(40, 10), cajas(1, 5))
```
</details>

**R2.3 · Contar aprobados y suspensos.** `recuento(notas)` devuelve `(aprobados, suspensos)`. El 5 cuenta como aprobado.
<details><summary>Solución</summary>

```python
def recuento(notas: list[float]) -> tuple[int, int]:
    """Cuántas notas aprueban y cuántas no."""
    aprobados: int = 0
    for n in notas:
        if n >= 5:
            aprobados += 1
    return aprobados, len(notas) - aprobados


print(recuento([3.0, 5.0, 9.0, 4.0]))
```
</details>

**R2.4 · Añadir sin modificar la original.** `con_extra(precios, extra)` devuelve una lista **nueva** con el precio añadido al final. La lista que recibe **no se toca**.
<details><summary>Solución</summary>

```python
def con_extra(precios: list[float], extra: float) -> list[float]:
    """Lista nueva con el precio añadido al final."""
    return precios + [extra]


original = [19.95, 34.5]
print(con_extra(original, 7.25), original)
```
</details>

**R2.5 · Impuesto con tipo por defecto.** `con_impuesto(base, tipo=21)` devuelve el importe con el impuesto aplicado, a dos decimales. Tiene que funcionar llamándola con uno o con dos argumentos.
<details><summary>Solución</summary>

```python
def con_impuesto(base: float, tipo: int = 21) -> float:
    """Importe con el impuesto aplicado, a 2 decimales."""
    return round(base * (1 + tipo / 100), 2)


print(con_impuesto(100.0), con_impuesto(100.0, 10))
```
</details>

**R2.6 · El más caro y el más barato, por nombre.** `extremos(productos)` recibe una lista de tuplas `(nombre, precio)` y devuelve los **nombres** del más barato y del más caro. Con la lista vacía devuelve `("", "")`.
<details><summary>Solución</summary>

```python
def extremos(productos: list[tuple[str, float]]) -> tuple[str, str]:
    """Nombre del más barato y del más caro."""
    if len(productos) == 0:
        return "", ""
    barato = productos[0]
    caro = productos[0]
    for producto in productos:
        if producto[1] < barato[1]:
            barato = producto
        if producto[1] > caro[1]:
            caro = producto
    return barato[0], caro[0]


print(extremos([("Camisa", 19.95), ("Gorra", 7.25), ("Botas", 45.0)]))
```
</details>

**R2.7 · Descomponer en tres funciones.** Parte el cálculo de una factura en tres funciones de **una sola responsabilidad**: una que calcule la base, otra el IVA y otra que las use para dar el total. Las tres devuelven, ninguna imprime.
<details><summary>Solución</summary>

```python
IVA: int = 21


def base(unidades: int, precio: float) -> float:
    """Importe sin impuestos."""
    return unidades * precio


def iva(importe: float) -> float:
    """Importe del IVA."""
    return importe * IVA / 100


def total(unidades: int, precio: float) -> float:
    """Importe final, a 2 decimales."""
    sin_iva: float = base(unidades, precio)
    return round(sin_iva + iva(sin_iva), 2)


print(total(3, 19.95))
```
</details>

**R2.8 · Filtrar por precio.** `caros(productos, minimo)` devuelve los nombres de los productos que cuestan **más** que el mínimo, en el mismo orden en que venían.
<details><summary>Solución</summary>

```python
def caros(productos: list[tuple[str, float]], minimo: float) -> list[str]:
    """Nombres de los productos que superan el mínimo."""
    nombres: list[str] = []
    for nombre, precio in productos:
        if precio > minimo:
            nombres.append(nombre)
    return nombres


print(caros([("Camisa", 19.95), ("Gorra", 7.25), ("Botas", 45.0)], 10.0))
```
</details>

**R2.9 · Distancia entre dos puntos.** `distancia(x1, y1, x2, y2)` devuelve la distancia en línea recta, a dos decimales. Usa `math`.
<details><summary>Solución</summary>

```python
import math


def distancia(x1: float, y1: float, x2: float, y2: float) -> float:
    """Distancia en línea recta entre dos puntos."""
    return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)


print(distancia(0.0, 0.0, 3.0, 4.0))
```
</details>

**R2.10 · Un módulo que se puede importar.** Escribe un módulo con una función `redondear_euros(importe)` y una prueba que **solo se ejecute al lanzar el fichero**, no al importarlo.
<details><summary>Solución</summary>

```python
"""Utilidades de importes."""


def redondear_euros(importe: float) -> float:
    """Importe redondeado a 2 decimales."""
    return round(importe, 2)


if __name__ == "__main__":
    print(redondear_euros(72.41850000000001))
```
</details>


---

## Parte 3 · Simulacro de la UD1 — 20 preguntas

**20 preguntas, 45 minutos, sin ordenador y sin apuntes.** Las respuestas están
al final de la página: no bajes hasta terminar.

### Cómo se puntúa

| | |
|---|---|
| Acierto | **+0,50** puntos |
| Error | **−0,17** puntos |
| En blanco | 0 |

`nota = (aciertos − errores ÷ 3) × 0,50`, con un mínimo de 0.

Se resta porque hay cuatro opciones: **marcar al azar no compensa**. Si dudas entre dos,
marca; si no tienes ni idea, déjalo en blanco.

**1.** ¿Qué imprime?

```python
importe = 1234567.891
ratio = 0.1567

print(f"{importe:,.2f} | {ratio:.1%}")
```

- **a)** `1.234.567,89 | 15.7%`
- **b)** `1,234,567.89 | 15.7%`
- **c)** `1234567.89 | 15.67%`
- **d)** `1,234,567.89 | 0.2%`

**2.** ¿Qué imprime?

```python
resultado = 6 / 3
print(type(resultado))
```

- **a)** `<class 'bool'>`
- **b)** `<class 'str'>`
- **c)** `<class 'float'>`
- **d)** `<class 'int'>`

**3.** Necesitas una función que aplique un descuento en porcentaje. ¿Cuál cumple los cuatro casos?

**a)**

```python
DESCUENTO = 15


def rebajar(precio: float) -> float:
    """Precio con el descuento aplicado, a 2 decimales."""
    return round(precio * (1 - DESCUENTO / 100), 2)
```

**b)**

```python
DESCUENTO = 15


def rebajar(precio: float) -> float:
    """Precio con el descuento aplicado, a 2 decimales."""
    return round(precio * DESCUENTO / 100, 2)
```

**c)**

```python
DESCUENTO = 15


def rebajar(precio: float) -> float:
    """Precio con el descuento aplicado, a 2 decimales."""
    return round(precio - DESCUENTO, 2)
```

**d)**

```python
DESCUENTO = 15


def rebajar(precio: float) -> float:
    """Precio con el descuento aplicado, a 2 decimales."""
    return round(precio / (1 + DESCUENTO / 100), 2)
```


**4.** ¿Qué imprime?

```python
entrada_1 = "15"
entrada_2 = "2"

media = int(entrada_1) / int(entrada_2)
print(media)
```

- **a)** `'15' / '2'`
- **b)** `7.5`
- **c)** `7`
- **d)** `8`

**5.** ¿Qué imprime?

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

- **a)** `2 1 1 17`
- **b)** `2 0 1 17`
- **c)** `2 1 0 17`
- **d)** `2 1 1 7`

**6.** ¿Qué imprime? Fíjate en el orden de las líneas.

```python
unidades = 3
precio = 19.95
base = unidades * precio
print(round(base, 2))
```

- **a)** `NameError`
- **b)** `59.85`
- **c)** `None`
- **d)** `0`

**7.** ¿Qué error lanza este programa?

```python
cantidad = "12 unidades"
n = int(cantidad)
print(n * 2)
```

- **a)** `SyntaxError`
- **b)** `TypeError`
- **c)** `AttributeError`
- **d)** `ValueError`

**8.** ¿Qué imprime este programa?

```python
print("Ticket")
print("-" * 8)
print("Camisa")
```

- **a)** `Ticket Camisa`
- **b)** `TypeError`
- **c)** `Ticket ⏎ Camisa`
- **d)** `Ticket ⏎ -------- ⏎ Camisa`

**9.** ¿Qué imprime?

```python
a = "10"
b = 10

print(a == b, int(a) == b)
```

- **a)** `True False`
- **b)** `False False`
- **c)** `False True`
- **d)** `True True`

**10.** ¿Qué error lanza este programa?

```python
for = 3
print(for)
```

- **a)** `TypeError`
- **b)** `NameError`
- **c)** `ValueError`
- **d)** `SyntaxError`

**11.** ¿Qué imprime?

```python
a = 0.1 + 0.2
b = 0.3

print(round(a, 10) == b)
```

- **a)** `True`
- **b)** `False`
- **c)** `0.30000000000000004`
- **d)** `TypeError`

**12.** ¿Qué imprime?

```python
edad = 17
carnet = True
acompanado = True

puede = edad >= 18 and (carnet or acompanado)
print(puede)
```

- **a)** `False`
- **b)** `TypeError`
- **c)** `True`
- **d)** `None`

**13.** ¿Qué imprime?

```python
cuota = 39.9
material = 12.0
descuento = -5.5

total = cuota + material + descuento
print(f"Total: {total:>8.2f} EUR")
```

- **a)** `Total: 46.40 EUR`
- **b)** `Total:     46.4 EUR`
- **c)** `Total:46.40 EUR`
- **d)** `Total:    46.40 EUR`

**14.** ¿Qué imprime?

```python
aciertos = 2
total = 3

print(f"{aciertos / total:.2f}")
```

- **a)** `0.7`
- **b)** `0.66`
- **c)** `0.67`
- **d)** `2/3`

**15.** ¿Cuál de estos cuatro resultados **no** es el que devuelve la función?

```python
IVA = 21


def desglose(unidades: int, precio: float) -> tuple[float, float, float]:
    """Base, IVA y total, redondeados a 2 decimales."""
    base = unidades * precio
    iva = base * IVA / 100
    return round(base, 2), round(iva, 2), round(base + iva, 2)
```

- **a)** `desglose(1, 1.0)` devuelve `(1.0, 0.21, 1.21)`
- **b)** `desglose(0, 5.0)` devuelve `(0.0, 0.0, 0.0)`
- **c)** `desglose(3, 9.99)` devuelve `(29.97, 6.29, 36.27)`
- **d)** `desglose(2, 10.0)` devuelve `(20.0, 4.2, 24.2)`

**16.** ¿Qué imprime?

```python
total = -7
partes = 2

print(total // partes, total % partes - 2)
```

- **a)** `-4 -1`
- **b)** `-4 1`
- **c)** `-3 -1`
- **d)** `-3 1`

**17.** ¿Qué imprime?

```python
IVA = 21

precio = 10.0
con_iva = precio * (1 + IVA / 100)
precio = 20.0

print(f"{con_iva:.2f} {precio * (1 + IVA / 100):.2f}")
```

- **a)** `24.20 24.20`
- **b)** `10.00 24.20`
- **c)** `12.10 12.10`
- **d)** `12.10 24.20`

**18.** ¿Qué imprime?

```python
unidades = 3
print(unidades, "unidades")
```

- **a)** `3 ⏎ unidades`
- **b)** `3 unidades`
- **c)** `3unidades`
- **d)** `TypeError`

**19.** ¿Qué imprime?

```python
hay_stock = 3 > 0
print(hay_stock, type(hay_stock))
```

- **a)** `True <class 'bool'>`
- **b)** `True <class 'int'>`
- **c)** `False <class 'bool'>`
- **d)** `1 <class 'int'>`

**20.** ¿Qué error lanza este programa?

```python
print(mensaje)
producto = "Camisa"
mensaje = "Has elegido: " + producto
```

- **a)** `ValueError`
- **b)** `TypeError`
- **c)** `SyntaxError`
- **d)** `NameError`

---

## Parte 4 · Simulacro de la UD2 — 20 preguntas

Mismas condiciones: 20 preguntas, 45 minutos, sin ordenador.

**1.** ¿Qué imprime?

```python
def doble(n):
    return n * 2
    return n * 4


print(doble(5))
```

- **a)** `None`
- **b)** `10\n20`
- **c)** `10`
- **d)** `20`

**2.** ¿Qué imprime?

```python
def area(base, altura):
    return base * altura


print(area(3.0, 4.0))
print(area(4.0, 5.0))
```

- **a)** `12.0 ⏎ 20.0`
- **b)** `20.0`
- **c)** `12.0`
- **d)** `TypeError`

**3.** ¿Qué imprime este programa?

```python
IVA = 21


def con_iva(precio):
    print(round(precio * (1 + IVA / 100), 2))


resultado = con_iva(25.0)
print(resultado)
```

- **a)** `30.25 ⏎ 30.25`
- **b)** `None ⏎ 30.25`
- **c)** `30.25 ⏎ None`
- **d)** `25 ⏎ None`

**4.** ¿Qué imprime?

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

- **a)** `[1, 2, 3] ⏎ [1, 2, 3]`
- **b)** `[1, 2] ⏎ [1, 2]`
- **c)** `[1, 2] ⏎ [1, 2, 3]`
- **d)** `TypeError`

**5.** ¿Qué imprime?

```python
def potencia(base, exponente=3):
    return float(base ** exponente)


print(potencia(2), potencia(2, 10))
```

- **a)** `1024.0 1024.0`
- **b)** `TypeError`
- **c)** `8.0 8.0`
- **d)** `8.0 1024.0`

**6.** ¿Cuál cumple los cuatro casos, incluida la lista vacía y el redondeo?

**a)**

```python
def media_redondeada(notas: list[float]) -> float:
    """Media a 2 decimales; 0.0 si la lista está vacía."""
    return round(sum(notas) / len(notas), 2)
```

**b)**

```python
def media_redondeada(notas: list[float]) -> float:
    """Media a 2 decimales; 0.0 si la lista está vacía."""
    if len(notas) == 0:
        return 0.0
    return round(sum(notas) // len(notas), 2)
```

**c)**

```python
def media_redondeada(notas: list[float]) -> float:
    """Media a 2 decimales; 0.0 si la lista está vacía."""
    if len(notas) == 0:
        return 0.0
    return round(sum(notas) / len(notas), 2)
```

**d)**

```python
def media_redondeada(notas: list[float]) -> float:
    """Media a 2 decimales; 0.0 si la lista está vacía."""
    if notas == 0:
        return 0.0
    return round(sum(notas) / len(notas), 2)
```


**7.** ¿Qué imprime?

```python
import math


def hipotenusa(a, b):
    return math.sqrt(a ** 2 + b ** 2)


def area_circulo(r):
    return math.pi * r ** 2


print(hipotenusa(3.0, 4.0), f"{area_circulo(3.0):.2f}")
```

- **a)** `5.0 28.27`
- **b)** `25.0 28.27`
- **c)** `5 28.27`
- **d)** `5.0 78.54`

**8.** ¿Qué imprime?

```python
import math

print(f"{math.pi:.4f}", f"{math.pi:.2f}")
```

- **a)** `3.1416 3.14`
- **b)** `3.1416 3.1416`
- **c)** `3.14 3.14`
- **d)** `3.14 3.1416`

**9.** ¿Qué error lanza?

```python
def area_triangulo(base, altura):
    """Área de un triángulo."""
    return base * altura / 2


print(area_triangulo(10.0))
```

- **a)** `TypeError`
- **b)** `IndexError`
- **c)** `NameError`
- **d)** `ValueError`

**10.** ¿Qué imprime?

```python
def con_impuesto(base, tipo=21):
    """Importe con el impuesto aplicado."""
    return base * (1 + tipo / 100)


print(f"{con_impuesto(100.0):.2f} | {con_impuesto(100.0, 30):.2f}")
```

- **a)** `121.00 | 121.00`
- **b)** `TypeError`
- **c)** `121.00 | 130.00`
- **d)** `130.00 | 130.00`

**11.** ¿Cuál de estos cuatro resultados **no** es el que devuelve la función?

```python
import math


def cajas(unidades: int, por_caja: int) -> int:
    """Cajas necesarias para no dejar unidades fuera."""
    return math.ceil(unidades / por_caja)
```

- **a)** `cajas(1, 5)` devuelve `1`
- **b)** `cajas(47, 10)` devuelve `5`
- **c)** `cajas(0, 5)` devuelve `1`
- **d)** `cajas(40, 10)` devuelve `4`

**12.** ¿Qué imprime?

```python
IVA = 21


def subir():
    IVA = 50
    return IVA


print(IVA, subir(), IVA)
```

- **a)** `21 50 21`
- **b)** `NameError`
- **c)** `21 21 21`
- **d)** `50 50 50`

**13.** ¿Qué imprime?

```python
unidades = 3


def cuantas():
    return unidades


print(cuantas())
```

- **a)** `None`
- **b)** `NameError`
- **c)** `0`
- **d)** `3`

**14.** ¿Qué imprime?

```python
print(__name__ == "__main__")
```

- **a)** `False`
- **b)** `NameError`
- **c)** `__main__`
- **d)** `True`

**15.** ¿Qué imprime?

```python
contador = 0


def contar(lista):
    contador = len(lista)
    return contador


print(contar([1, 2, 3]), contador)
```

- **a)** `NameError`
- **b)** `3 0`
- **c)** `3 3`
- **d)** `0 3`

**16.** ¿Qué imprime?

```python
"""Utilidades de cálculo."""


def doble(n):
    """Devuelve el doble."""
    return n * 2


print(doble.__doc__)
```

- **a)** `None`
- **b)** `Utilidades de cálculo.`
- **c)** `42`
- **d)** `Devuelve el doble.`

**17.** ¿Qué imprime?

```python
def suma(numeros):
    total = 0
    for n in numeros:
        total = n
    return total


print(suma([1, 2, 3]))
```

- **a)** `6`
- **b)** `3`
- **c)** `1`
- **d)** `0`

**18.** ¿Qué imprime?

```python
print(__name__)
```

- **a)** `modulos`
- **b)** `None`
- **c)** `__main__`
- **d)** `main`

**19.** ¿Qué imprime?

```python
def saludar(nombre):
    print(f"Hola, {nombre}")


saludar("Ada")
saludar("Alan")
```

- **a)** `None`
- **b)** `Hola, Ada ⏎ Hola, Alan`
- **c)** `Hola, Ada`
- **d)** `Hola, Alan`

**20.** ¿Qué imprime?

```python
precios = [19.95, 34.5, 7.25]
print(len(precios))
```

- **a)** `3`
- **b)** `[19.95, 34.5, 7.25]`
- **c)** `19.95`
- **d)** `IndexError`

---

## Respuestas de los simulacros

!!! danger "No mires esto antes de terminar"
    Un simulacro con las respuestas delante no mide nada.

### Simulacro de la UD1

| # | Correcta | Qué es | Por qué |
|:---:|:---:|---|---|
| **1** | **b** | `1,234,567.89 | 15.7%` | — |
| **2** | **c** | `<class 'float'>` | La división `/` devuelve `float` siempre, aunque el resultado sea exacto. Para obtener un entero hay que usar `//`. |
| **3** | **a** | `DESCUENTO = 15 ⏎  ⏎  ⏎ def rebajar(precio: float) -> float: ⏎     """Precio con el descuento aplicado, a 2 decimales.""" ⏎     return round(precio * (1 - DESCUENTO / 100), 2)` | — |
| **4** | **b** | `7.5` | — |
| **5** | **a** | `2 1 1 17` | — |
| **6** | **b** | `59.85` | Python ejecuta de arriba abajo. Cuando llega al `print`, `base` ya tiene el valor calculado en la línea anterior. |
| **7** | **d** | `ValueError` | — |
| **8** | **d** | `Ticket ⏎ -------- ⏎ Camisa` | Cada `print` escribe en una línea nueva. Multiplicar un texto lo repite, que es cómo se dibuja la línea separadora. |
| **9** | **c** | `False True` | — |
| **10** | **d** | `SyntaxError` | `for` es una palabra reservada del lenguaje: no se puede usar como nombre de variable. Hay que renombrarla. |
| **11** | **a** | `True` | — |
| **12** | **a** | `False` | — |
| **13** | **d** | `Total:    46.40 EUR` | — |
| **14** | **c** | `0.67` | — |
| **15** | **c** | `desglose(3, 9.99) (ese par es el falso)` | — |
| **16** | **a** | `-4 -1` | — |
| **17** | **d** | `12.10 24.20` | — |
| **18** | **b** | `3 unidades` | `print` con varios argumentos separados por comas los muestra en una línea con un espacio entre ellos. |
| **19** | **a** | `True <class 'bool'>` | El resultado de una comparación es un valor de tipo `bool`: `True` o `False`. |
| **20** | **d** | `NameError` | El `print` va antes de crear `mensaje`. Python ejecuta línea a línea: cuando llega al print, ese nombre todavía no existe. |

### Simulacro de la UD2

| # | Correcta | Qué es | Por qué |
|:---:|:---:|---|---|
| **1** | **c** | `10` | — |
| **2** | **a** | `12.0 ⏎ 20.0` | Cada llamada es independiente: los parámetros toman los valores de esa llamada y nada se queda guardado entre una y otra. |
| **3** | **c** | `30.25 ⏎ None` | — |
| **4** | **a** | `[1, 2, 3] ⏎ [1, 2, 3]` | — |
| **5** | **d** | `8.0 1024.0` | — |
| **6** | **c** | `def media_redondeada(notas: list[float]) -> float: ⏎     """Media a 2 decimales; 0.0 si la lista está vacía.""" ⏎     if len(notas) == 0: ⏎         return 0.0 ⏎     return round(sum(notas) / len(notas), 2)` | — |
| **7** | **a** | `5.0 28.27` | — |
| **8** | **a** | `3.1416 3.14` | — |
| **9** | **a** | `TypeError` | — |
| **10** | **c** | `121.00 | 130.00` | — |
| **11** | **c** | `cajas(0, 5) (ese par es el falso)` | — |
| **12** | **a** | `21 50 21` | — |
| **13** | **d** | `3` | Dentro de la función se lee la variable de fuera sin problema. Lo que no se puede es asignarle un valor sin declararla `global`. |
| **14** | **d** | `True` | Al ejecutar el fichero, la comparación es verdadera. Al importarlo sería falsa. |
| **15** | **b** | `3 0` | — |
| **16** | **d** | `Devuelve el doble.` | `__doc__` guarda el docstring. El del módulo (la primera cadena del fichero) y el de la función son distintos: aquí se pide el de la función. |
| **17** | **b** | `3` | — |
| **18** | **c** | `__main__` | Es la variable que permite distinguir «me están ejecutando» de «me están importando». |
| **19** | **b** | `Hola, Ada ⏎ Hola, Alan` | Una función se escribe una vez y se llama tantas veces como haga falta. Ese es todo el motivo de usarlas. |
| **20** | **a** | `3` | `len()` cuenta los elementos. Los índices van de 0 a `len - 1`. |

---

## Qué hacer con tu nota

| Nota del simulacro | Qué significa | Qué hacer esta semana |
|:---:|---|---|
| **8 o más** | Lo tienes | Repasa solo lo que hayas fallado y no toques más |
| **5 a 8** | Aprobado justo | Mira **de qué tema** son los fallos y vuelve a esos ejercicios del temario |
| **menos de 5** | Hay un concepto sin asentar | Vuelve a la teoría de los temas fallados y rehaz sus ejercicios desde cero |
| **muchos en blanco** | Falta práctica de lectura | Coge ejemplos del temario y predice la salida antes de ejecutarlos |

!!! tip "Lo importante no es la nota, es de dónde vienen los fallos"
    Dos personas con un 6 pueden estar en situaciones muy distintas: una ha fallado cosas
    sueltas de cinco temas y otra ha fallado un tema entero. La segunda tiene un problema
    concreto y se arregla en una tarde.
