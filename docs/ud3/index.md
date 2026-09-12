# Unidad 3 · Estructuras de control, excepciones y depuración

> **Módulo:** CMO-313 · Fundamentos de programación
> **Resultado de aprendizaje:** RA3 · **Duración:** 12 h · **Peso:** 25 %
> **Lenguaje:** Python 3 (tipado) · **La unidad más importante del módulo**

Hasta ahora tus programas iban en línea recta: siempre las mismas instrucciones, en el mismo orden. Aquí aprenden a **decidir** (hacer una cosa u otra según los datos) y a **repetir** (hacer algo muchas veces sin escribirlo muchas veces). Con esto ya puedes escribir prácticamente cualquier programa.

Es la unidad de **mayor peso** del módulo (25 %), y con razón: todo lo que venga después la usa.

---

## Mapa de la unidad

<figure markdown>
  ![Mapa de la unidad 3](../assets/diagramas/ud3-mapa.svg#only-light)
  ![Mapa de la unidad 3](../assets/diagramas/ud3-mapa-dark.svg#only-dark)
  <figcaption>Decidir, repetir y no romperse cuando llegan datos inesperados.</figcaption>
</figure>

### Qué vas a saber hacer al terminar

- [ ] Tomar decisiones con `if` / `elif` / `else`.
- [ ] Repetir con `while` (mientras se cumpla algo) y con `for` (para cada elemento).
- [ ] Usar `break` y `continue` con criterio.
- [ ] Recorrer listas y diccionarios.
- [ ] **Controlar errores** con `try` / `except` para que el programa no se caiga.
- [ ] **Validar** la entrada del usuario.
- [ ] Depurar: encontrar por qué un programa no hace lo que crees.

---

## 1. Decidir: `if`, `elif`, `else`

### 1.1 La forma básica

```python
nota: float = 7.0

if nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")
```

Lo importante de la sintaxis de Python:

- La condición termina en **dos puntos** `:`.
- El bloque que depende de ella va **indentado** (4 espacios). La indentación **no es decorativa**: es lo que marca qué pertenece al `if`.

```python
if nota >= 5:
    print("Aprobado")        # dentro del if
print("Fin")                 # fuera: se ejecuta siempre
```

### 1.2 Varias opciones con `elif`

```python
nota: float = 7.0

if nota >= 9:
    calificacion = "Sobresaliente"
elif nota >= 7:
    calificacion = "Notable"
elif nota >= 6:
    calificacion = "Bien"
elif nota >= 5:
    calificacion = "Suficiente"
else:
    calificacion = "Insuficiente"

print(calificacion)          # Notable
```

!!! tip "El orden importa"
    Python comprueba de arriba abajo y se queda en **la primera** condición verdadera. Por eso se ponen de mayor a menor: si empezaras por `nota >= 5`, un 9 entraría ahí y nunca llegaría a «Sobresaliente».

### 1.3 Condiciones compuestas

```python
edad: int = 20
tiene_carnet: bool = True

if edad >= 18 and tiene_carnet:
    print("Puede conducir")

if not tiene_carnet or edad < 18:
    print("No puede conducir")
```

> ⚠️ **Error clásico:** `if edad >= 18 and <= 65` no es válido. Hay que repetir la variable: `if edad >= 18 and edad <= 65`. *(En Python también vale `if 18 <= edad <= 65`.)*

> 🎯 **Reto rápido 1.** Escribe un `if` que muestre `"Par"` o `"Impar"` según un número.

---

## 2. Repetir con `while`

`while` repite **mientras** una condición sea verdadera:

```python
contador: int = 1
while contador <= 3:
    print(contador)
    contador = contador + 1     # ¡imprescindible!
```

Salida: `1`, `2`, `3`.

!!! danger "El bucle infinito"
    Si olvidas modificar la variable de la condición, el bucle **no termina nunca**:
    ```python
    contador = 1
    while contador <= 3:
        print(contador)       # ❌ contador nunca cambia
    ```
    Se corta con `Ctrl+C`. Siempre que escribas un `while`, pregúntate: *¿qué hace que esta condición acabe siendo falsa?*

### 2.1 El patrón «menú»

Es el uso más habitual y el que aparece en el examen:

```python
opcion: str = ""
while opcion != "0":
    print("1 - Saludar")
    print("0 - Salir")
    opcion = input("Opción: ")
    if opcion == "1":
        print("¡Hola!")
print("Adiós")
```

> 🎯 **Reto rápido 2.** Escribe un `while` que muestre los números del 10 al 1 (cuenta atrás).

---

## 3. Repetir con `for`

`for` recorre **cada elemento** de una colección. Es el bucle preferido cuando sabes sobre qué iteras.

```python
notas: list[float] = [5.0, 7.5, 9.0]

for nota in notas:
    print(nota)
```

### 3.1 `range()`: repetir un número de veces

```python
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):       # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8  (de dos en dos)
    print(i)
```

!!! tip "`range(n)` llega hasta n-1"
    `range(5)` da cinco valores: del 0 al 4. Es el mismo criterio que los índices de las listas.

### 3.2 Acumular

Patrón fundamental: una variable que va creciendo dentro del bucle.

```python
notas: list[float] = [5.0, 7.5, 9.0]

total: float = 0.0
for nota in notas:
    total = total + nota        # también: total += nota

print(f"Suma: {total}")         # 21.5
print(f"Media: {total / len(notas):.2f}")
```

### 3.3 Contar con condición

```python
aprobados: int = 0
for nota in notas:
    if nota >= 5:
        aprobados += 1
print(aprobados)      # 3
```

### 3.4 `while` o `for`, ¿cuál?

| Usa… | Cuando… |
|---|---|
| `for` | recorres una lista o repites un nº **conocido** de veces |
| `while` | repites **hasta que pase algo** (menús, validaciones) |

> 🎯 **Reto rápido 3.** Con un `for` y `range`, suma los números del 1 al 100. *(Resultado: 5050.)*

---

## 4. Diccionarios

Una lista guarda valores por posición; un **diccionario** los guarda por **clave**:

```python
alumno: dict[str, str] = {
    "nombre": "Ada",
    "grupo": "1DAW",
}

print(alumno["nombre"])         # Ada
alumno["edad"] = "20"           # añadir
```

Recorrerlo:

```python
for clave, valor in alumno.items():
    print(f"{clave}: {valor}")
```

> ⚠️ Acceder a una clave que no existe da `KeyError`. Para evitarlo: `alumno.get("edad", "desconocida")`.

---

## 5. `break` y `continue`

- **`break`** sale del bucle inmediatamente.
- **`continue`** salta a la siguiente vuelta.

```python
for n in [1, 2, 3, 4, 5]:
    if n == 4:
        break              # al llegar al 4, corta
    print(n)               # 1 2 3

for n in [1, 2, 3, 4, 5]:
    if n % 2 == 0:
        continue           # se salta los pares
    print(n)               # 1 3 5
```

!!! warning "Úsalos con moderación"
    Un `break` bien puesto aclara el código; cinco `break` repartidos lo vuelven imposible de seguir. Si puedes expresarlo en la condición del bucle, mejor.

> 🎯 **Reto rápido 4.** Recorre `[3, 8, 2, 9, 4]` y para en cuanto encuentres un número mayor que 5, mostrándolo.

---

## 6. Excepciones: que el programa no se caiga

Ya conoces esto: si el usuario escribe `"hola"` cuando pides un número, el programa **se rompe**.

```python
edad = int(input("Edad: "))     # el usuario escribe "hola" → ValueError, programa muerto
```

### 6.1 `try` / `except`

```python
try:
    edad = int(input("Edad: "))
    print(f"Tienes {edad} años")
except ValueError:
    print("Eso no es un número")
```

- En `try` va el código que **puede fallar**.
- En `except` va **qué hacer si falla**. El programa continúa.

### 6.2 Capturar el error correcto

```python
try:
    resultado = 10 / int(input("Divisor: "))
except ValueError:
    print("No has escrito un número")
except ZeroDivisionError:
    print("No se puede dividir entre cero")
```

!!! danger "No captures `Exception` a secas"
    ```python
    try:
        ...
    except:            # ❌ atrapa TODO, incluso errores tuyos de programación
        pass           # ❌ y encima los oculta
    ```
    Así, un fallo real (una variable mal escrita) se traga en silencio y no te enteras. **Captura la excepción concreta que esperas.**

### 6.3 `else` y `finally`

```python
try:
    numero = int(input("Número: "))
except ValueError:
    print("Entrada no válida")
else:
    print(f"El doble es {numero * 2}")   # solo si NO hubo error
finally:
    print("Fin")                          # siempre, haya error o no
```

### 6.4 El patrón «validar entrada»

La combinación de `while` + `try` que usarás una y otra vez:

```python
def pedir_entero(mensaje: str) -> int:
    """Pide un entero hasta que el usuario escriba uno válido."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada no válida, inténtalo otra vez")
```

> 🎯 **Reto rápido 5.** ¿Qué excepción lanza `int("3.5")`? *(Respuesta: `ValueError`; `int()` no acepta decimales en texto.)*

---

## 7. Depurar: encontrar el fallo

Depurar es averiguar **por qué** el programa no hace lo que crees. Tres herramientas, de menos a más:

### 7.1 `print` de diagnóstico

La más simple y muchas veces suficiente. Muestra el valor de las variables en puntos clave:

```python
for i, nota in enumerate(notas):
    print(f"[debug] i={i} nota={nota} total={total}")
```

Bórralos cuando termines.

### 7.2 El depurador del IDE

En VS Code: haz clic a la izquierda del número de línea para poner un **punto de ruptura** (breakpoint) y pulsa **F5**. El programa se detiene ahí y puedes:

| Tecla | Qué hace |
|---|---|
| **F10** | ejecuta la línea y pasa a la siguiente |
| **F11** | entra dentro de la función |
| **F5** | continúa hasta el siguiente punto de ruptura |

Mientras está parado, el panel **Variables** te enseña cuánto vale cada cosa **en ese instante**. Es incomparablemente mejor que llenar el código de `print`.

### 7.3 Leer el error de verdad

Cuando Python falla, te dice **el fichero, la línea y el tipo de error**. Lee siempre la **última** línea del mensaje: ahí está la causa.

```text
Traceback (most recent call last):
  File "programa.py", line 7, in <module>
    media = total / len(notas)
ZeroDivisionError: division by zero
```

Eso dice: línea 7, división entre cero → `len(notas)` vale 0 → la lista está vacía.

---

## 8. Errores frecuentes

| Síntoma | Causa | Solución |
|---|---|---|
| `IndentationError` | indentación inconsistente | 4 espacios, siempre igual |
| El bucle no termina | no cambias la variable de la condición | modifícala dentro del `while` |
| `if x = 5` da error | `=` asigna, `==` compara | usa `==` |
| El `else` se ejecuta cuando no debe | condiciones en mal orden | ordena de más restrictiva a menos |
| `ZeroDivisionError` en medias | lista vacía | comprueba `len(lista) > 0` antes |
| `KeyError` | clave inexistente en el diccionario | usa `.get(clave, valor_por_defecto)` |
| El error se «traga» | `except:` genérico con `pass` | captura la excepción concreta |
| `range(1,5)` no llega al 5 | el final es exclusivo | usa `range(1, 6)` |

---

## 9. Practica **con** solución a la vista

### 9.1 Actividades guiadas

#### Actividad 1 — Clasificar una nota
Pide una nota y muestra su calificación (Insuficiente / Suficiente / Bien / Notable / Sobresaliente).
<details><summary>💡 Solución</summary>

```python
nota: float = float(input("Nota: "))
if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 6:
    print("Bien")
elif nota >= 5:
    print("Suficiente")
else:
    print("Insuficiente")
```
</details>

#### Actividad 2 — Tabla de multiplicar
Pide un número y muestra su tabla del 1 al 10.
<details><summary>💡 Solución</summary>

```python
n: int = int(input("Número: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
```
</details>

#### Actividad 3 — Media de una lista con control
Calcula la media de una lista, pero devuelve `0.0` si está vacía.
<details><summary>💡 Solución</summary>

```python
def media(numeros: list[float]) -> float:
    if len(numeros) == 0:
        return 0.0
    return sum(numeros) / len(numeros)
```
</details>

#### Actividad 4 — Entrada validada
Pide un número entero y no continúes hasta que sea válido.
<details><summary>💡 Solución</summary>

```python
while True:
    try:
        numero: int = int(input("Número: "))
        break
    except ValueError:
        print("Entrada no válida")
print(f"Has escrito {numero}")
```
</details>

### 9.2 Ejercicios propuestos

**E1 🟢 · Mayor de dos.** `mayor(a: int, b: int) -> int`.
<details><summary>Solución</summary>

```python
def mayor(a: int, b: int) -> int:
    if a > b:
        return a
    return b
```
</details>

**E2 🟢 · Contar hasta N.** Muestra los números del 1 a N, uno por línea.
<details><summary>Solución</summary>

```python
n: int = int(input())
for i in range(1, n + 1):
    print(i)
```
</details>

**E3 🟡 · Suma de pares.** `suma_pares(numeros: list[int]) -> int`.
<details><summary>Solución</summary>

```python
def suma_pares(numeros: list[int]) -> int:
    total = 0
    for n in numeros:
        if n % 2 == 0:
            total += n
    return total
```
</details>

**E4 🟡 · Buscar.** `posicion(numeros: list[int], buscado: int) -> int`: devuelve la posición o `-1`.
<details><summary>Pista</summary>Usa <code>enumerate</code> o <code>range(len(numeros))</code> y <code>return</code> en cuanto lo encuentres.</details>
<details><summary>Solución</summary>

```python
def posicion(numeros: list[int], buscado: int) -> int:
    for i, n in enumerate(numeros):
        if n == buscado:
            return i
    return -1
```
</details>

**E5 🟡 · División segura.** `dividir(a: float, b: float) -> float`: devuelve `0.0` si `b` es cero, usando `try/except`.
<details><summary>Solución</summary>

```python
def dividir(a: float, b: float) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        return 0.0
```
</details>

**E6 🔴 · FizzBuzz.** Del 1 al N: múltiplos de 3 → `Fizz`, de 5 → `Buzz`, de ambos → `FizzBuzz`, resto → el número.
<details><summary>Pista</summary>Comprueba primero el caso de los dos a la vez.</details>
<details><summary>Solución</summary>

```python
n: int = int(input())
for i in range(1, n + 1):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```
</details>

---

## Proyecto de la unidad ⭐

Toda la práctica de esta unidad se hace sobre un **proyecto base**: un analizador de notas que no se rompe con datos raros. Está montado
con la estructura real de un proyecto Python y trae una **batería de tests** que puedes
ejecutar en cualquier momento para ver si va todo bien.

**[Proyecto Gestor de notas →](../proyectos/ud3/README.md)**

```
proyecto-ud3/
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

## 11. Retos opcionales 🚀

- **R1.** Menú completo: añadir notas, ver media, listar y salir, con toda la entrada validada.
- **R2.** Adivina el número: el programa piensa uno con `random.randint(1, 100)` y te dice «mayor» o «menor» hasta acertar.
- **R3.** Cuenta cuántas veces aparece cada palabra en una frase, usando un diccionario.

---

## 12. Autoevaluación rápida

<details><summary>1. ¿Qué imprime <code>for i in range(3)</code>?</summary><code>0</code>, <code>1</code>, <code>2</code>.</details>
<details><summary>2. ¿Cuándo usar <code>while</code> en vez de <code>for</code>?</summary>Cuando no sabes cuántas vueltas hará: repites hasta que ocurra algo.</details>
<details><summary>3. Diferencia entre <code>break</code> y <code>continue</code>.</summary><code>break</code> sale del bucle; <code>continue</code> salta a la siguiente vuelta.</details>
<details><summary>4. ¿Qué excepción lanza <code>int("hola")</code>?</summary><code>ValueError</code>.</details>
<details><summary>5. ¿Por qué es mala idea <code>except:</code> a secas?</summary>Atrapa todos los errores, incluidos los tuyos de programación, y los oculta.</details>
<details><summary>6. ¿Qué falla en <code>if edad >= 18 and <= 65</code>?</summary>Hay que repetir la variable: <code>edad >= 18 and edad <= 65</code>.</details>

---

## 13. Glosario

| Término | Definición |
|---|---|
| **Estructura de selección** | `if`/`elif`/`else`: elige qué código ejecutar. |
| **Estructura de repetición** | `while`/`for`: repite instrucciones. |
| **Iterar** | Recorrer los elementos de una colección. |
| **Acumulador** | Variable que va sumando dentro de un bucle. |
| **Excepción** | Error en tiempo de ejecución que interrumpe el programa. |
| **`try` / `except`** | Bloque que intenta algo y reacciona si falla. |
| **Diccionario** | Colección de pares clave → valor. |
| **Punto de ruptura** | Marca que detiene el programa en el depurador. |

---

## 14. Cómo se evalúa esta unidad (RA3)

Examen **100 % práctico**. Es el RA de mayor peso del módulo (25 %).

| # | Qué se valora | Cómo se mide | Puntos |
|:---:|---|---|:---:|
| 1 | **Que funcione** | casos de prueba superados × 7 | **7,0** |
| 2 | **Control de excepciones** | las entradas inválidas no rompen el programa | **1,0** |
| 3 | **Tipado** | `mypy` sin errores | **1,0** |
| 4 | **Documentación** | comentarios o docstring que expliquen la lógica | **1,0** |
| | | **TOTAL** | **10** |

**Se supera con 5.** La batería incluye entradas inválidas: si tu programa se cae con ellas, pierdes esos casos.
