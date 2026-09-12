# Unidad 2 · Programas sencillos: funciones y librerías

> **Módulo:** CMO-313 · Fundamentos de programación
> **Resultado de aprendizaje:** RA2 · **Duración:** 8 h · **Peso:** 15 %
> **Lenguaje:** Python 3 (tipado) · **Requisito:** haber superado la UD1

En la UD1 escribías programas «de un tirón»: leer, calcular, mostrar. Eso funciona con problemas pequeños, pero se vuelve inmanejable en cuanto crecen. Esta unidad enseña la herramienta que lo resuelve: **dividir el problema en funciones** y **reutilizar código ya hecho** mediante librerías.

---

## Mapa de la unidad

<figure markdown>
  ![Mapa de la unidad 2](../assets/diagramas/ud2-mapa.svg#only-light)
  ![Mapa de la unidad 2](../assets/diagramas/ud2-mapa-dark.svg#only-dark)
  <figcaption>Un problema grande se parte en funciones; las librerías aportan funciones ya hechas.</figcaption>
</figure>

### Qué vas a saber hacer al terminar

- [ ] Descomponer un problema en **funciones** con una responsabilidad clara.
- [ ] Definir funciones con **parámetros** y **valor de retorno**, anotando los tipos.
- [ ] Distinguir `return` de `print` (el error más común de esta unidad).
- [ ] Usar **parámetros por defecto** y llamadas por nombre.
- [ ] Entender el **ámbito** de las variables (local y global).
- [ ] Manejar **listas** para trabajar con conjuntos de datos.
- [ ] Importar y usar la **librería estándar** (`math`, `random`, `statistics`).
- [ ] Crear tu **propio módulo** e importarlo desde otro programa.

### Cómo se trabaja esta unidad

Igual que la UD1: explicación → lectura y ejemplos → **ejercicios con solución** (sección 10) → **ejercicios autocorregidos** (sección 11) → examen.

---

## 1. Por qué funciones

Imagina que necesitas calcular la media de notas en cinco sitios distintos de un programa. Sin funciones, copias el cálculo cinco veces. Y cuando descubras un fallo, tendrás que corregirlo… cinco veces (y olvidarás alguna).

Una **función** es un trozo de código con nombre que hace **una cosa concreta** y puede reutilizarse cuantas veces quieras.

> 🧠 **Analogía.** Una función es como una **receta con nombre**: «hacer masa». La escribes una vez y luego dices «hago masa» sin repetir los pasos. Le pasas ingredientes (parámetros) y te devuelve un resultado (return).

Las tres razones para usarlas:

| Razón | Qué significa |
|---|---|
| **No repetirse** | El código se escribe una vez y se usa muchas. |
| **Dividir el problema** | Un problema grande se convierte en varios pequeños que sí sabes resolver. |
| **Poder probarlo** | Una función se puede comprobar por separado (es lo que hacen tus tests). |

> 🎯 **Reto rápido 1.** Piensa en el programa de la UD1 (presupuesto). ¿Qué parte convertirías en función y cómo la llamarías?

---

## 2. Definir y llamar funciones

### 2.1 La estructura

```python
def area_rectangulo(base: float, altura: float) -> float:
    """Devuelve el área de un rectángulo."""
    return base * altura
```

Pieza a pieza:

| Parte | Qué es |
|---|---|
| `def` | palabra reservada que inicia la definición |
| `area_rectangulo` | **nombre** (en `snake_case`, describe lo que hace) |
| `base: float, altura: float` | **parámetros** con su tipo: los datos que necesita |
| `-> float` | el tipo que **devuelve** |
| `"""..."""` | *docstring*: qué hace la función |
| `return` | **devuelve** el resultado a quien la llamó |

Para **usarla** (llamarla):

```python
resultado: float = area_rectangulo(3.0, 4.0)
print(resultado)        # 12.0
```

!!! warning "El error nº 1 de esta unidad: `return` no es `print`"
    ```python
    def suma_mal(a: int, b: int) -> None:
        print(a + b)          # ❌ muestra, pero no devuelve

    def suma_bien(a: int, b: int) -> int:
        return a + b          # ✅ devuelve: puedes usar el resultado
    ```
    Con `suma_mal` no puedes hacer `total = suma_mal(2, 3) * 10`, porque `total` valdría `None`. **La función calcula y devuelve; quien la llama decide si lo muestra.**

### 2.2 Funciones que no devuelven nada

Algunas funciones solo *hacen* algo (mostrar por pantalla, por ejemplo). Se anotan con `-> None`:

```python
def saludar(nombre: str) -> None:
    print(f"Hola, {nombre}")

saludar("Ada")          # Hola, Ada
```

### 2.3 Devolver varios valores

Con una tupla, separando por comas:

```python
def area_y_perimetro(base: float, altura: float) -> tuple[float, float]:
    return base * altura, 2 * (base + altura)

area, perimetro = area_y_perimetro(4, 3)    # 12.0  y  14.0
```

> 🎯 **Reto rápido 2.** Escribe `cuadrado(n: int) -> int` que devuelva el cuadrado de un número. Llámala con 7 y muestra el resultado.

---

## 3. Parámetros

### 3.1 Posicionales y por nombre

```python
def presentar(nombre: str, edad: int) -> str:
    return f"{nombre} tiene {edad} años"

print(presentar("Ada", 36))              # por posición
print(presentar(edad=36, nombre="Ada"))  # por nombre: el orden da igual
```

### 3.2 Parámetros por defecto

Un parámetro puede tener valor por defecto; entonces es opcional al llamar:

```python
def precio_con_iva(precio: float, iva: int = 21) -> float:
    return precio * (1 + iva / 100)

print(precio_con_iva(100))        # 121.0  (usa 21)
print(precio_con_iva(100, 10))    # 110.0  (usa 10)
```

!!! tip "Los parámetros con valor por defecto van al final"
    `def f(a, b=2, c)` es un error de sintaxis. Primero los obligatorios, después los opcionales.

> 🎯 **Reto rápido 3.** Añade a `presentar` un parámetro `saludo: str = "Hola"` y haz que el texto empiece por él.

---

## 4. Ámbito de las variables

Una variable creada **dentro** de una función solo existe ahí: es **local**. Cuando la función termina, desaparece.

```python
def calcular() -> int:
    total = 10        # variable LOCAL
    return total

calcular()
print(total)          # ❌ NameError: 'total' no existe fuera
```

Las variables de fuera son **globales** y sí se pueden *leer* desde dentro:

```python
IVA = 21                       # global (constante)

def con_iva(precio: float) -> float:
    return precio * (1 + IVA / 100)   # puede leer IVA
```

!!! warning "No modifiques variables globales desde una función"
    Existe la palabra `global`, pero usarla convierte el programa en algo imposible de seguir. **Lo correcto es pasar los datos por parámetro y devolver el resultado.** Una función que solo depende de sus parámetros se llama *función pura* y es la más fácil de probar.

> 🎯 **Reto rápido 4.** ¿Qué imprime este código? *(Piensa antes de ejecutarlo.)*
> ```python
> x = 5
> def cambiar() -> None:
>     x = 99
> cambiar()
> print(x)
> ```
> *(Respuesta: `5`. La `x` de dentro es otra variable distinta.)*

---

## 5. Listas: trabajar con varios datos

Hasta ahora cada variable guardaba **un** valor. Una **lista** guarda **muchos** bajo un solo nombre:

```python
notas: list[float] = [5.0, 7.5, 9.0, 4.5]

print(notas[0])        # 5.0    primer elemento (se empieza en 0)
print(notas[-1])       # 4.5    último
print(len(notas))      # 4      cuántos hay
```

Operaciones básicas:

```python
notas.append(6.0)      # añadir al final
print(sum(notas))      # 32.0   suma de todos
print(max(notas))      # 9.0    el mayor
print(min(notas))      # 4.5    el menor
```

Con esto ya puedes escribir funciones que reciben listas:

```python
def media(numeros: list[float]) -> float:
    return sum(numeros) / len(numeros)

print(media([5.0, 7.5, 9.0]))      # 7.166666666666667
```

!!! warning "Cuidado con la lista vacía"
    `media([])` provoca `ZeroDivisionError`, porque `len([])` es 0. En la UD3 aprenderás a controlarlo; de momento, tenlo presente.

> 🎯 **Reto rápido 5.** Escribe `cuantos(numeros: list[int]) -> int` que devuelva cuántos elementos tiene la lista.

---

## 6. Librerías: código ya escrito

Una **librería** (o módulo) es un conjunto de funciones ya hechas que puedes usar. Python trae muchas incluidas: es la **librería estándar**.

### 6.1 Importar

```python
import math

print(math.sqrt(16))      # 4.0     raíz cuadrada
print(math.pi)            # 3.141592653589793
print(math.floor(3.7))    # 3       redondea hacia abajo
print(math.ceil(3.2))     # 4       redondea hacia arriba
```

También puedes importar solo lo que necesitas:

```python
from math import sqrt, pi

print(sqrt(25))     # 5.0    ya no hace falta escribir math.
```

### 6.2 Tres librerías útiles ya

```python
import random
print(random.randint(1, 6))        # número al azar entre 1 y 6
print(random.choice(["a", "b"]))   # elemento al azar de una lista

import statistics
print(statistics.mean([2, 4, 6]))     # 4      media
print(statistics.median([1, 5, 9]))   # 5      mediana
```

!!! tip "Antes de programar algo, mira si ya existe"
    `statistics.mean()` ya calcula medias. Escribir tu propia versión está bien **para aprender**, pero en un proyecto real se usa la librería: está probada por miles de personas.

### 6.3 Tu propio módulo

Cualquier fichero `.py` es un módulo importable. Si creas `utilidades.py`:

```python
# utilidades.py
def doble(n: int) -> int:
    return n * 2

def triple(n: int) -> int:
    return n * 3
```

lo usas desde otro fichero de la misma carpeta:

```python
# principal.py
import utilidades

print(utilidades.doble(5))     # 10
```

o importando funciones sueltas:

```python
from utilidades import doble, triple
print(doble(5), triple(5))     # 10 15
```

> 🎯 **Reto rápido 6.** Crea `mis_utiles.py` con una función `mitad(n: float) -> float` e impórtala desde otro fichero.

---

## 7. `if __name__ == "__main__":`

Cuando importas un módulo, Python **ejecuta todo su código suelto**. Si tu fichero tiene pruebas o `input()` fuera de las funciones, se dispararán al importarlo, que no es lo que quieres.

La solución es este guardián:

```python
def doble(n: int) -> int:
    return n * 2

if __name__ == "__main__":
    # esto SOLO se ejecuta si lanzas este fichero directamente
    print(doble(21))
```

- Si ejecutas `python utilidades.py` → se ejecuta el bloque.
- Si haces `import utilidades` desde otro sitio → **no** se ejecuta.

!!! tip "Regla práctica de esta unidad"
    En un módulo de funciones, **todo el código suelto va dentro de ese `if`**. Tus tests importan el fichero, así que si dejas un `input()` fuera, se quedarán colgados.

---

## 8. Cómo descomponer un problema

El método, paso a paso:

1. **Escribe qué hay que hacer** en frases cortas.
2. Cada frase con un verbo claro → **una función**.
3. Decide qué **necesita** cada una (parámetros) y qué **da** (return).
4. Escríbelas y **pruébalas por separado**.
5. Monta el programa principal llamándolas.

**Ejemplo.** «Calcular la nota final de un alumno a partir de sus notas, y decir si aprueba.»

```python
def media(notas: list[float]) -> float:
    """Devuelve la media de una lista de notas."""
    return sum(notas) / len(notas)


def aprueba(nota: float) -> bool:
    """Indica si una nota es de aprobado."""
    return nota >= 5


def main() -> None:
    notas: list[float] = [6.0, 7.0, 4.0]
    nota_final: float = media(notas)
    print(f"Media: {nota_final:.2f}")
    print("Aprobado" if aprueba(nota_final) else "Suspenso")


if __name__ == "__main__":
    main()
```

Fíjate: `media` y `aprueba` **no muestran nada**; devuelven datos. Solo `main` imprime. Esa separación es la clave y es lo que permite probarlas automáticamente.

---

## 9. Errores frecuentes

| Síntoma | Causa | Solución |
|---|---|---|
| La función devuelve `None` | usaste `print` en vez de `return` | devuelve el valor con `return` |
| `TypeError: takes 2 positional arguments but 3 were given` | llamas con más argumentos de los definidos | revisa los parámetros |
| `NameError` al usar una variable de la función | es **local**, no existe fuera | devuélvela con `return` |
| `ModuleNotFoundError` | el módulo no existe o está en otra carpeta | mismo directorio y nombre exacto |
| El test se queda colgado | hay un `input()` suelto en el módulo | mételo en `if __name__ == "__main__":` |
| `ZeroDivisionError` en `media` | lista vacía | contémplalo (UD3) |

---

## 10. Practica **con** solución a la vista

> **Primera vía.** Intenta cada uno y luego despliega la solución para comparar.

### 10.1 Actividades guiadas

#### Actividad 1 — Tu primera función
Escribe `saludo(nombre: str) -> str` que **devuelva** (no imprima) `"Hola, Ada"`.
<details><summary>💡 Solución</summary>

```python
def saludo(nombre: str) -> str:
    return f"Hola, {nombre}"

print(saludo("Ada"))     # Hola, Ada
```
</details>

#### Actividad 2 — Varias operaciones
Escribe `operaciones(a: int, b: int) -> tuple[int, int, int]` que devuelva suma, resta y producto.
<details><summary>💡 Solución</summary>

```python
def operaciones(a: int, b: int) -> tuple[int, int, int]:
    return a + b, a - b, a * b

s, r, p = operaciones(7, 3)
print(s, r, p)      # 10 4 21
```
</details>

#### Actividad 3 — Usar una librería
Con `math`, escribe `hipotenusa(a: float, b: float) -> float`.
<details><summary>💡 Solución</summary>

```python
import math

def hipotenusa(a: float, b: float) -> float:
    return math.sqrt(a ** 2 + b ** 2)

print(hipotenusa(3, 4))     # 5.0
```
</details>

#### Actividad 4 — Trabajar con listas
Escribe `resumen(numeros: list[float]) -> tuple[float, float, float]` que devuelva media, mínimo y máximo.
<details><summary>💡 Solución</summary>

```python
def resumen(numeros: list[float]) -> tuple[float, float, float]:
    return sum(numeros) / len(numeros), min(numeros), max(numeros)

print(resumen([4.0, 8.0, 6.0]))     # (6.0, 4.0, 8.0)
```
</details>

### 10.2 Ejercicios propuestos

**E1 🟢 · Área del círculo.** `area_circulo(radio: float) -> float` usando `math.pi`.
<details><summary>Solución</summary>

```python
import math

def area_circulo(radio: float) -> float:
    return math.pi * radio ** 2
```
</details>

**E2 🟢 · Conversión.** `a_fahrenheit(celsius: float) -> float`.
<details><summary>Solución</summary>

```python
def a_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32
```
</details>

**E3 🟡 · Precio final.** `precio_final(precio: float, iva: int = 21, descuento: int = 0) -> float`: aplica primero el descuento y después el IVA.
<details><summary>Pista</summary>Calcula el precio con descuento y sobre ese resultado aplica el IVA.</details>
<details><summary>Solución</summary>

```python
def precio_final(precio: float, iva: int = 21, descuento: int = 0) -> float:
    con_descuento = precio * (1 - descuento / 100)
    return con_descuento * (1 + iva / 100)

print(precio_final(100))            # 121.0
print(precio_final(100, 21, 10))    # 108.9
```
</details>

**E4 🟡 · Contar pares.** `cuenta_pares(numeros: list[int]) -> int`.
<details><summary>Pista</summary>Recorre con un bucle y usa <code>% 2 == 0</code>. También vale <code>sum(1 for n in numeros if n % 2 == 0)</code>.</details>
<details><summary>Solución</summary>

```python
def cuenta_pares(numeros: list[int]) -> int:
    total = 0
    for n in numeros:
        if n % 2 == 0:
            total += 1
    return total
```
</details>

**E5 🟡 · Módulo propio.** Crea `estadistica.py` con `media`, `maximo` y `minimo`, e impórtalo desde `principal.py`.
<details><summary>Solución</summary>

```python
# estadistica.py
def media(numeros: list[float]) -> float:
    return sum(numeros) / len(numeros)

def maximo(numeros: list[float]) -> float:
    return max(numeros)

def minimo(numeros: list[float]) -> float:
    return min(numeros)
```
```python
# principal.py
import estadistica

datos = [4.0, 8.0, 6.0]
print(estadistica.media(datos))     # 6.0
```
</details>

**E6 🔴 · Redondeo a múltiplo.** `redondear_a(valor: float, multiplo: int = 5) -> int`: redondea al múltiplo más cercano.
<details><summary>Pista</summary><code>round(valor / multiplo) * multiplo</code></details>
<details><summary>Solución</summary>

```python
def redondear_a(valor: float, multiplo: int = 5) -> int:
    return round(valor / multiplo) * multiplo

print(redondear_a(23))       # 25
print(redondear_a(23, 10))   # 20
```
</details>

---

## Proyecto de la unidad ⭐

Toda la práctica de esta unidad se hace sobre un **proyecto base**: un paquete de funciones reutilizables en tres módulos. Está montado
con la estructura real de un proyecto Python y trae una **batería de tests** que puedes
ejecutar en cualquier momento para ver si va todo bien.

**[Proyecto Biblioteca de utilidades →](../proyectos/ud2/README.md)**

```
proyecto-ud2/
├── src/      ← tu código (funciones con TODO)
└── tests/    ← 31 tests que comprueban tu trabajo
```

### Cómo se trabaja

```bash
pip install -r requirements.txt
pytest
```

La primera vez falla casi todo: aún no has escrito nada. A partir de ahí, lee una función,
escríbela, vuelve a lanzar `pytest` y comprueba si ese test ya pasa. Terminas cuando está
**todo en verde** y `mypy src` dice *Success*.

!!! tip "De uno en uno"
    `pytest -x` se detiene en el primer fallo. Arreglas esa función y sigues. Mucho más
    llevadero que enfrentarse a todos los errores a la vez.

!!! warning "Los tests son la especificación"
    No los modifiques para que pasen: describen exactamente lo que tu código debe hacer, y
    el examen usará una batería equivalente.

Detalles y comandos útiles en **[Proyectos](../proyectos/index.md)**.

---

## 12. Retos opcionales 🚀

- **R1.** Añade a P1 una función `mediana(numeros: list[float]) -> float` sin usar `statistics`.
- **R2.** Investiga `*args` y escribe `suma_todos(*numeros)` que sume cuantos números le pases.
- **R3.** Compara tu `media` con `statistics.mean` sobre la misma lista: ¿dan exactamente lo mismo?

---

## 13. Autoevaluación rápida

<details><summary>1. ¿Qué diferencia hay entre <code>return</code> y <code>print</code>?</summary><code>return</code> devuelve el valor a quien llamó (se puede seguir usando); <code>print</code> solo lo muestra.</details>
<details><summary>2. ¿Qué devuelve una función sin <code>return</code>?</summary><code>None</code>.</details>
<details><summary>3. ¿Se puede leer una variable global desde una función?</summary>Sí, leerla sí. Modificarla es mala práctica: mejor pasarla por parámetro.</details>
<details><summary>4. ¿Para qué sirve <code>if __name__ == "__main__":</code>?</summary>Para que el código suelto solo se ejecute al lanzar el fichero directamente, no al importarlo.</details>
<details><summary>5. ¿Cómo se importa solo <code>sqrt</code> de <code>math</code>?</summary><code>from math import sqrt</code></details>
<details><summary>6. ¿Qué vale <code>len([3, 5, 7])</code>?</summary><code>3</code>.</details>

---

## 14. Glosario

| Término | Definición |
|---|---|
| **Función** | Bloque de código con nombre que hace una tarea y puede devolver un resultado. |
| **Parámetro / argumento** | Dato que la función declara / valor concreto que se le pasa. |
| **`return`** | Devuelve un valor y termina la función. |
| **Función pura** | Solo depende de sus parámetros y no toca nada de fuera. |
| **Ámbito** | Zona donde existe una variable (local o global). |
| **Lista** | Colección ordenada de valores: `[1, 2, 3]`. |
| **Módulo / librería** | Fichero (o conjunto) con funciones reutilizables. |
| **`import`** | Trae a tu programa el contenido de un módulo. |

---

## 15. Cómo se evalúa esta unidad (RA2)

Examen **100 % práctico**: escribir un módulo de funciones que cumpla una especificación.

| # | Qué se valora | Cómo se mide | Puntos |
|:---:|---|---|:---:|
| 1 | **Que las funciones funcionen** | casos de prueba superados × 7 | **7,0** |
| 2 | **Uso de librería** | importas y usas correctamente un módulo | **1,0** |
| 3 | **Tipado** | anotaciones y `mypy` sin errores | **1,0** |
| 4 | **Documentación** | docstring o comentarios en cada función | **1,0** |
| | | **TOTAL** | **10** |

**Se supera con 5.** Los tests llaman a tus funciones directamente, así que **usa `return`**, respeta los nombres del enunciado y no dejes código suelto que pida datos.

### Cómo prepararte

1. Haz los ejercicios de la sección 10 y compara con las soluciones.
2. Haz los **autocorregidos** de la sección 11: son la misma mecánica del examen.
3. Comprueba siempre con `pytest` y `mypy`.
