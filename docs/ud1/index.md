# Unidad 1 · Estructura del programa y elementos del lenguaje

> **Módulo:** CMO-313 · Fundamentos de programación
> **Resultado de aprendizaje:** RA1 · **Duración:** 8 h · **Peso:** 15 %
> **Lenguaje:** Python 3 (con **anotaciones de tipo**) · **Nivel:** DAW/DAM · primer curso

Esta es la primera unidad del módulo. Aquí aprendes lo esencial: **qué es un programa, con qué piezas se construye y cómo se ejecuta**. Todo lo demás del curso se apoya en estos cimientos. Al terminar sabrás escribir programas que **leen datos, los procesan con operadores y muestran resultados con formato**, usando **Python tipado** y un **entorno de trabajo profesional** (entorno virtual + pip).

---

## Mapa de la unidad

<figure markdown>
  ![Mapa de la unidad](../assets/diagramas/ud1-mapa.svg#only-light)
  ![Mapa de la unidad](../assets/diagramas/ud1-mapa-dark.svg#only-dark)
  <figcaption>Del problema al programa, y las piezas del lenguaje que intervienen.</figcaption>
</figure>


### Qué vas a saber hacer al terminar

- [ ] Preparar un proyecto con **entorno virtual** e instalar paquetes con **pip**.
- [ ] Crear y ejecutar un programa desde el IDE.
- [ ] Reconocer los bloques **entrada → proceso → salida**.
- [ ] Declarar y usar variables **con anotaciones de tipo** (`int`, `float`, `str`, `bool`).
- [ ] Definir constantes y respetar las normas de nombres.
- [ ] Construir expresiones con operadores y precedencia correcta.
- [ ] Convertir tipos de forma explícita e implícita.
- [ ] Leer del teclado y dar formato a la salida.
- [ ] Documentar con comentarios y **comprobar los tipos con mypy**.

### Cómo se trabaja esta unidad

| | Paso | Dónde |
|:---:|---|---|
| **1** | **Lees** la sección y **ejecutas los ejemplos** en tu ordenador. | secciones 1–11 |
| **2** | Haces el **reto rápido** que cierra la explicación. | en el texto |
| **3** | Haces los **ejercicios de esa sección**, con la solución desplegable. | al final de cada sección |
| **4** | En clase: dudas, actividades guiadas y los ejercicios largos. | sección 12 |
| **5** | Trabajas el **proyecto de la unidad** y ejecutas sus tests hasta tenerlo todo en verde. | `proyectos/ud1/` |
| **6** | Te mides con el **test de práctica** y después vas al examen. | `simulacros/ra1/` |

> Los **«Reto rápido»** son mini-desafíos de 1–2 minutos para afianzar justo lo que acabas de leer. Hazlos en el momento, aunque parezcan sencillos.

!!! tip "Los pasos 1–3 son tuyos"
    Este es el trato del **aula invertida**: la teoría y los ejercicios cortos los haces
    tú, y el tiempo de clase se dedica a lo que de verdad cuesta. Por eso cada sección
    termina con tres o cuatro ejercicios: **hazlos antes de pasar a la siguiente**.

!!! tip "La diferencia entre los pasos 3 y 5"
    En el **3** puedes mirar la solución: sirve para *ver el patrón*.
    En el **5** no hay solución: escribes el código y son **los tests** los que te dicen si está bien. Los dos hacen falta, y en ese orden.

---

## 1. ¿Qué es programar?

Programar es **escribir instrucciones precisas para que un ordenador resuelva un problema**. El ordenador no "entiende" ni improvisa: hace exactamente lo que le dices, en el orden que se lo dices. Esa literalidad es la primera lección del curso: la mayoría de los errores no son del ordenador, son instrucciones nuestras que no decían lo que creíamos.

> **Analogía.** Un programa es como una **receta de cocina**. Los *datos* son los ingredientes, el *algoritmo* son los pasos ("bate dos huevos, añade harina…") y el *programa* es esa receta escrita en un idioma que la cocina (el ordenador) entiende.

### 1.1 Del problema al programa

Antes de escribir código conviene pensar el **algoritmo**: la solución paso a paso, todavía sin lenguaje concreto.

<figure markdown>
  ![Ciclo de trabajo](../assets/diagramas/ud1-ciclo.svg#only-light)
  ![Ciclo de trabajo](../assets/diagramas/ud1-ciclo-dark.svg#only-dark)
  <figcaption>El ciclo de trabajo del programador: se repite hasta que funciona.</figcaption>
</figure>


**Ejemplo de algoritmo** para calcular el área de un rectángulo: (1) pedir la base, (2) pedir la altura, (3) multiplicar base por altura, (4) mostrar el resultado. Este algoritmo **sirve para cualquier lenguaje**; programar es traducirlo a Python.

### 1.2 Lenguajes: compilados vs. interpretados

| | **Compilado** | **Interpretado** |
|---|---|---|
| Cómo funciona | Un *compilador* traduce **todo** antes de ejecutar | Un *intérprete* ejecuta **línea a línea** |
| Ejemplos | C, C++, Rust | **Python**, JavaScript |
| Ventaja | Muy rápido al ejecutarse | Flexible, fácil de probar |
| Inconveniente | Ciclo de prueba más lento | Algo más lento al ejecutarse |

Usamos **Python 3**: interpretado, de sintaxis limpia y enorme comunidad.

> **Reto rápido 1.** Escribe (en lenguaje natural, sin código) el algoritmo para calcular la **media de dos números**. Nombra sus bloques de entrada, proceso y salida.

---

### Practica lo de esta sección

> Hazlos **antes** de pasar a la siguiente sección: son cortos y solo usan lo que acabas de leer. Despliega la solución cuando lo tengas resuelto — o cuando te atasques de verdad.

**1.1.** Descompón en **entrada, proceso y salida** el cálculo del área de un rectángulo. No escribas código todavía: solo los tres bloques.
<details><summary>Solución</summary>

```text
Entrada:  base y altura (los pide el usuario)
Proceso:  area = base * altura
Salida:   mostrar el area por pantalla
```
</details>

**1.2.** Escribe en lenguaje natural el algoritmo para decidir si un número es **par**.
<details><summary>Solución</summary>

```text
1. Pedir un numero
2. Calcular el resto de dividirlo entre 2
3. Si el resto es 0 -> es par
4. Si no -> es impar
5. Mostrar el resultado
```
</details>

**1.3.** Ordena estos pasos del ciclo de desarrollo: *ejecutar*, *analizar el problema*, *escribir el código*, *corregir errores*, *diseñar el algoritmo*.
<details><summary>Solución</summary>

```text
1. Analizar el problema  (que me piden exactamente)
2. Disenar el algoritmo   (como lo resuelvo, en lenguaje natural)
3. Escribir el codigo     (traducirlo a Python)
4. Ejecutar               (probarlo de verdad)
5. Corregir errores       (y volver a ejecutar)
```
</details>


---

## 2. El entorno de trabajo: IDE, entornos virtuales y pip

Programar de forma profesional no es solo escribir código: es preparar un **entorno de proyecto** ordenado. Aquí montamos el que usaremos todo el curso.

### 2.1 IDE

Un **IDE** (Entorno de Desarrollo Integrado) reúne editor, intérprete y depurador. Usaremos **Visual Studio Code** + la extensión de **Python**. Instala primero **Python 3** desde [python.org](https://www.python.org) y comprueba la versión:

```bash
python --version      # p. ej. Python 3.12.3
```

### 2.2 Entornos virtuales (venv): por qué y cómo

Un **entorno virtual** es una **copia aislada de Python** para un proyecto concreto. Sirve para que los paquetes que instales en un proyecto **no se mezclen** con los de otros ni con el Python del sistema.

> **Analogía.** Cada proyecto tiene su propia **mochila** con sus herramientas. Sin entornos virtuales, todo va en una única mochila gigante y compartida: un día actualizas una herramienta para un proyecto y rompes otro sin querer.

<figure markdown>
  ![Entornos virtuales](../assets/diagramas/ud1-entornos.svg#only-light)
  ![Entornos virtuales](../assets/diagramas/ud1-entornos-dark.svg#only-dark)
  <figcaption>Cada proyecto lleva su propio entorno: los paquetes no se mezclan.</figcaption>
</figure>


**Crear y activar** el entorno (se hace una vez por proyecto):

```bash
# 1) Crear el entorno virtual (crea una carpeta .venv)
python -m venv .venv

# 2) Activarlo
# En Windows (PowerShell):
.venv\Scripts\Activate.ps1
# En macOS / Linux:
source .venv/bin/activate

# Cuando está activo, el prompt muestra (.venv) delante.
# Para salir:
deactivate
```

> ✓ Añade la carpeta `.venv/` a tu `.gitignore`: el entorno **no se sube** al repositorio, se recrea con `requirements.txt`.

### 2.3 pip: instalar paquetes

**pip** es el gestor de paquetes de Python. Con el entorno **activado**:

```bash
pip install pytest         # instala un paquete
pip install mypy           # comprobador de tipos (lo usaremos en la sección 5)
pip list                   # ver lo instalado
pip show pytest            # detalles de un paquete
pip uninstall pytest       # desinstalar
```

### 2.4 requirements.txt: dependencias reproducibles

Para que cualquiera (o tú en otro ordenador) recree el entorno exacto, se listan las dependencias en un fichero:

```bash
pip freeze > requirements.txt      # guarda las versiones actuales
pip install -r requirements.txt    # instala todo lo del fichero
```

Ejemplo de `requirements.txt` de esta unidad:

```text
pytest==8.2.0
mypy==1.10.0
```

### 2.5 Tu primer programa

Crea `hola.py`:

```python
print("¡Hola, mundo!")
```

Ejecútalo (con el entorno activo):

```bash
python hola.py
# Salida:  ¡Hola, mundo!
```

`print()` es una **función** que muestra información por pantalla: nuestra herramienta básica de **salida**.

> **Errores típicos al empezar:** olvidar las comillas (`print(Hola)` → `NameError`), comillas sin cerrar (`SyntaxError`), o instalar paquetes **sin** el entorno activado (se instalan en el sistema).

> **Reto rápido 2.** Crea una carpeta `ud1`, dentro un entorno virtual `.venv`, actívalo, instala `pytest` y genera un `requirements.txt`. Comprueba con `pip list` que aparece pytest.

---

### Practica lo de esta sección

> Hazlos **antes** de pasar a la siguiente sección: son cortos y solo usan lo que acabas de leer. Despliega la solución cuando lo tengas resuelto — o cuando te atasques de verdad.

**2.1.** Crea una carpeta `practica1`, dentro un entorno virtual llamado `.venv` y actívalo.
<details><summary>Solución</summary>

```bash
mkdir practica1
cd practica1
python -m venv .venv
source .venv/bin/activate
# En Windows PowerShell:
# .venv\Scripts\Activate.ps1
```
</details>

**2.2.** Con el entorno activado, instala `pytest`, comprueba que aparece en la lista de paquetes y guarda las dependencias en un fichero.
<details><summary>Solución</summary>

```bash
pip install pytest
pip list
pip freeze > requirements.txt
```
</details>

**2.3.** Desactiva el entorno y comprueba que `pytest` ya no está disponible fuera de él. ¿Por qué pasa eso?
<details><summary>Solución</summary>

```bash
deactivate
pip list

# pytest no aparece: se instalo DENTRO del entorno virtual.
# Esa es justo la idea: cada proyecto lleva sus propios paquetes
# y no se mezclan con los de otros ni con los del sistema.
```
</details>


---

## 3. Estructura de un programa: entrada, proceso y salida

Casi todos los programas siguen el mismo esquema. **Saber identificar estos bloques es el criterio *a* del RA1.**

<figure markdown>
  ![Entrada, proceso y salida](../assets/diagramas/ud1-eps.svg#only-light)
  ![Entrada, proceso y salida](../assets/diagramas/ud1-eps-dark.svg#only-dark)
  <figcaption>Los tres bloques que tiene casi cualquier programa.</figcaption>
</figure>


**Ejemplo completo** — saludar por el nombre (con anotaciones de tipo, que veremos en la sección 5):

```python
nombre: str = input("¿Cómo te llamas? ")   # ENTRADA
saludo: str = "Hola, " + nombre             # PROCESO
print(saludo)                               # SALIDA
```

Ejecución:

```text
¿Cómo te llamas? Ada
Hola, Ada
```

> **Reto rápido 3.** Copia el ejemplo y modifícalo para que salude así: `¡Bienvenida al curso, Ada!`.

---

### Practica lo de esta sección

> Hazlos **antes** de pasar a la siguiente sección: son cortos y solo usan lo que acabas de leer. Despliega la solución cuando lo tengas resuelto — o cuando te atasques de verdad.

**3.1.** Escribe un programa con la estructura **entrada → proceso → salida** que pida el nombre del usuario y lo salude.
<details><summary>Solución</summary>

```python
# Entrada
nombre: str = input("¿Cómo te llamas? ")

# Proceso
saludo: str = f"¡Hola, {nombre}!"

# Salida
print(saludo)   # -> ¡Hola, Ada!
```
</details>

**3.2.** Pide dos números enteros y muestra su suma. Marca con comentarios dónde está cada bloque del ciclo.
<details><summary>Solución</summary>

```python
# Entrada
a: int = int(input("Primer número: "))
b: int = int(input("Segundo número: "))

# Proceso
suma: int = a + b

# Salida
print(f"La suma es {suma}")   # -> La suma es 12
```
</details>

**3.3.** Este programa está todo mezclado. Reescríbelo separando los tres bloques:

```python
print(f"Doble: {int(input('Número: ')) * 2}")
```
<details><summary>Solución</summary>

```python
# Entrada
numero: int = int(input("Número: "))

# Proceso
doble: int = numero * 2

# Salida
print(f"Doble: {doble}")   # -> Doble: 42

# Hace lo mismo, pero ahora se lee, se prueba y se corrige por partes.
```
</details>


---

## 4. Variables y tipos de datos

### 4.1 Qué es una variable

Una **variable** es un **nombre que guarda un valor** en memoria y que puede cambiar. Se crea al **asignarle** un valor con `=`:

```python
edad = 25
```

> **Analogía.** Una variable es una **caja con etiqueta**: la etiqueta es el nombre (`edad`) y dentro está el valor (`25`).

<figure markdown>
  ![Variables en memoria](../assets/diagramas/ud1-memoria.svg#only-light)
  ![Variables en memoria](../assets/diagramas/ud1-memoria-dark.svg#only-dark)
  <figcaption>Cada variable guarda un valor bajo su etiqueta.</figcaption>
</figure>

En Python `=` **no** es el "igual" matemático, es "**asigna**": *"calcula lo de la derecha y guárdalo en el nombre de la izquierda"*. Por eso esto es habitual:

```python
contador = 0
contador = contador + 1   # toma 0, le suma 1 y lo vuelve a guardar -> 1
```

### 4.2 Los cuatro tipos básicos

| Tipo | Sirve para | Literales de ejemplo |
|---|---|---|
| `int` | Números enteros | `0`, `25`, `-100` |
| `float` | Números decimales | `1.75`, `-0.5`, `3.0` |
| `str` | Texto (cadenas) | `"Madrid"`, `'A'`, `""` |
| `bool` | Verdadero / falso | `True`, `False` |

### 4.3 Tipado dinámico y `type()`

Python tiene **tipado dinámico**: no *obliga* a declarar el tipo, lo deduce del valor. La función `type()` te lo dice:

```python
x = 25
print(type(x))     # <class 'int'>
x = "hola"
print(type(x))     # <class 'str'>  ← la misma variable cambió de tipo
```

> **Precisión de los decimales.** `0.1 + 0.2` da `0.30000000000000004`, no `0.3`. Es normal en cualquier ordenador; para *mostrar* dinero se redondea con formato (`:.2f`).

> **Reto rápido 4.** Crea tres variables con tu nombre, tu edad y tu altura, y muestra el **tipo** de cada una con `type()`.

---

### Practica lo de esta sección

> Hazlos **antes** de pasar a la siguiente sección: son cortos y solo usan lo que acabas de leer. Despliega la solución cuando lo tengas resuelto — o cuando te atasques de verdad.

**4.1.** Crea cuatro variables, una de cada tipo básico (`str`, `int`, `float`, `bool`), y muestra su valor y su tipo.
<details><summary>Solución</summary>

```python
nombre = "Ada"
edad = 36
altura = 1.68
matriculada = True

print(nombre, type(nombre))         # -> <class 'str'>
print(edad, type(edad))             # -> <class 'int'>
print(altura, type(altura))         # -> <class 'float'>
print(matriculada, type(matriculada))  # -> <class 'bool'>
```
</details>

**4.2.** Tienes `a = 5` y `b = 9`. Intercambia sus valores y compruébalo.
<details><summary>Solución</summary>

```python
a = 5
b = 9

a, b = b, a   # Python permite el intercambio directo

print(a, b)   # -> 9 5
```
</details>

**4.3.** ¿Qué **tipo** devuelven `7 / 2`, `7 // 2` y `7 % 2`? Predícelo antes de ejecutar.
<details><summary>Solución</summary>

```python
print(7 / 2, type(7 / 2))     # -> 3.5 <class 'float'>
print(7 // 2, type(7 // 2))   # -> 3 <class 'int'>
print(7 % 2, type(7 % 2))     # -> 1 <class 'int'>

# La division / SIEMPRE da float, aunque el resultado sea exacto: 6 / 2 -> 3.0
```
</details>


---

## 5. Python tipado: anotaciones de tipo (type hints)

Python te *permite* no declarar tipos, pero en este curso vamos a **anotarlos siempre**. Las **anotaciones de tipo** (o *type hints*) hacen el código más claro, ayudan al IDE a autocompletar y avisar de errores, y permiten comprobar el programa con **mypy** *antes* de ejecutarlo.

### 5.1 Anotar variables

Se añade `: tipo` después del nombre:

```python
edad: int = 25
altura: float = 1.75
ciudad: str = "Madrid"
mayor_edad: bool = True
```

### 5.2 Anotar funciones

Se indica el tipo de cada parámetro y, tras `->`, el tipo que devuelve:

```python
def area_rectangulo(base: float, altura: float) -> float:
    return base * altura

resultado: float = area_rectangulo(3.0, 4.0)   # 12.0
```

Una función que **no devuelve** nada se anota con `-> None`:

```python
def saludar(nombre: str) -> None:
    print(f"Hola, {nombre}")
```

### 5.3 Muy importante: las anotaciones NO se comprueban al ejecutar

Python **no** impide que metas un valor de otro tipo; las anotaciones son una **ayuda**, no una barrera. Quien las verifica es **mypy**:

```bash
mypy presupuesto.py
# Success: no issues found in 1 source file
```

Si te equivocas de tipo, mypy lo detecta sin necesidad de ejecutar:

```python
edad: int = "veinte"   # mypy avisa: Incompatible types (str no es int)
```

> **Para quien venga de Java (DAM):** las anotaciones se parecen a declarar `int edad`, pero en Python son *opcionales* y no se comprueban en tiempo de ejecución, solo con herramientas como mypy.

> ✓ **Norma del curso:** anota **todas** las variables y funciones. Es uno de los hábitos que evaluaremos como *buenas prácticas*.

> **Reto rápido 5.** Escribe una función tipada `doble(n: int) -> int` que devuelva el doble de un número, y llámala con `doble(21)`. Ejecuta `mypy` sobre el fichero.

---

### Practica lo de esta sección

> Hazlos **antes** de pasar a la siguiente sección: son cortos y solo usan lo que acabas de leer. Despliega la solución cuando lo tengas resuelto — o cuando te atasques de verdad.

**5.1.** Escribe una función **tipada** `area_rectangulo(base, altura)` que devuelva el área.
<details><summary>Solución</summary>

```python
def area_rectangulo(base: float, altura: float) -> float:
    """Área de un rectángulo."""
    return base * altura

print(area_rectangulo(3, 4.5))   # -> 13.5
```
</details>

**5.2.** Anota los tipos de estas variables y ejecuta `mypy` sobre el fichero:

```python
nombre = "Ada"
edad = 36
notas = [7.5, 8.0]
```
<details><summary>Solución</summary>

```python
nombre: str = "Ada"
edad: int = 36
notas: list[float] = [7.5, 8.0]

print(nombre, edad, notas)   # -> Ada 36 [7.5, 8.0]

# En la terminal:  mypy fichero.py   ->  Success: no issues found
```
</details>

**5.3.** Escribe `iniciales(nombre, apellido)` que devuelva las iniciales en mayúsculas, con sus anotaciones de tipo.
<details><summary>Solución</summary>

```python
def iniciales(nombre: str, apellido: str) -> str:
    """Devuelve las iniciales, en mayúsculas y separadas por punto."""
    return f"{nombre[0].upper()}.{apellido[0].upper()}."

print(iniciales("ada", "lovelace"))   # -> A.L.
```
</details>


---

## 6. Constantes, literales, identificadores y palabras reservadas

- **Literal:** un valor escrito directamente: `42`, `3.14`, `"hola"`, `True`.
- **Constante:** valor que **no debe cambiar**. Python no tiene constantes reales, así que por **convención** se escriben en **MAYÚSCULAS**:

```python
IVA: int = 21          # constante (convención en mayúsculas)
PI: float = 3.14159
```

> ✓ **Por qué usar constantes.** Si el IVA aparece en diez sitios y cambia, con una constante lo modificas **en un único lugar**.

**Identificador** = nombre de una variable/constante/función. Reglas: empieza por letra o `_`; solo letras, números y `_`; distingue mayúsculas; no puede ser palabra reservada. Estilo **PEP 8**: `snake_case` para variables y funciones, `MAYUSCULAS` para constantes.

| ✓ Correcto | ✗ Evita | Motivo |
|---|---|---|
| `precio_unitario` | `PrecioUnitario` | usa `snake_case` |
| `numero_alumnos` | `número` | sin acentos |
| `total_2024` | `2024_total` | no empezar por número |
| `iva` | `if` | `if` es palabra reservada |

**Palabras reservadas** (no se pueden usar como nombres):

```text
False None True and as assert async await break class continue def del
elif else except finally for from global if import in is lambda nonlocal
not or pass raise return try while with yield
```

> **Reto rápido 6.** De estos nombres, ¿cuáles son válidos como variable? `edad`, `2dias`, `precio_final`, `class`, `_temp`. *(Solución: válidos `edad`, `precio_final`, `_temp`.)*

---

### Practica lo de esta sección

> Hazlos **antes** de pasar a la siguiente sección: son cortos y solo usan lo que acabas de leer. Despliega la solución cuando lo tengas resuelto — o cuando te atasques de verdad.

**6.1.** Define el IVA como **constante** y calcula el precio final de un artículo de 80 €.
<details><summary>Solución</summary>

```python
IVA: int = 21          # constante: en MAYÚSCULAS porque no cambia

precio: float = 80.0
final: float = precio * (1 + IVA / 100)

print(f"{final:.2f}")   # -> 96.80
```
</details>

**6.2.** ¿Cuáles de estos nombres son válidos como variable? `total`, `2pagos`, `precio-final`, `_temp`, `for`, `añoNacimiento`.
<details><summary>Solución</summary>

```text
Validos:    total, _temp, anoNacimiento
No validos: 2pagos        -> no puede empezar por numero
            precio-final  -> el guion es el operador resta; usa precio_final
            for           -> es una palabra reservada del lenguaje
```
</details>

**6.3.** Este código no funciona porque usa una palabra reservada. Arréglalo:

```python
class = "1DAW"
print(class)
```
<details><summary>Solución</summary>

```python
# 'class' esta reservada para declarar clases: hay que renombrar la variable
grupo: str = "1DAW"
print(grupo)   # -> 1DAW
```
</details>


---

## 7. Comentarios y documentación

Los **comentarios** son texto que el intérprete **ignora**; explican el código a las personas (**criterio *i***).

```python
# Comentario de una línea
precio: int = 10  # también al final de una línea

"""
Docstring: comentario de varias líneas,
para documentar un fichero o una función.
"""
```

> ✓ **Comenta el *por qué*, no el *qué*:**
> ```python
> precio = precio * 0.9   # ✓ aplicar 10 % de descuento de rebajas
> ```

> **Reto rápido 7.** Añade a la función `doble` del reto 5 un docstring de una línea que explique qué hace.

---

### Practica lo de esta sección

> Hazlos **antes** de pasar a la siguiente sección: son cortos y solo usan lo que acabas de leer. Despliega la solución cuando lo tengas resuelto — o cuando te atasques de verdad.

**7.1.** Añade un **docstring** de una línea a esta función:

```python
def doble(n: int) -> int:
    return n * 2
```
<details><summary>Solución</summary>

```python
def doble(n: int) -> int:
    """Devuelve el doble del número recibido."""
    return n * 2

print(doble.__doc__)   # -> Devuelve el doble del número recibido.
```
</details>

**7.2.** Estos comentarios sobran porque repiten lo que ya dice el código. Sustitúyelos por uno que explique **el porqué**:

```python
# suma 1 a i
i = i + 1
# multiplica por 1.21
precio = precio * 1.21
```
<details><summary>Solución</summary>

```python
i = 0
precio = 100.0

i = i + 1                 # (sin comentario: el codigo ya se lee solo)
precio = precio * 1.21    # IVA general del 21 % vigente en 2026

print(i, round(precio, 2))   # -> 1 121.0
```
</details>

**7.3.** Documenta un módulo `conversiones.py` con su docstring de módulo y una función documentada.
<details><summary>Solución</summary>

```python
"""Conversiones entre unidades de longitud."""


def metros_a_km(metros: float) -> float:
    """Convierte metros a kilómetros."""
    return metros / 1000

print(metros_a_km(2500))   # -> 2.5
```
</details>


---

## 8. Operadores y expresiones

### 8.1 Aritméticos

| Operador | Operación | Ejemplo | Resultado |
|:---:|---|:---:|:---:|
| `+` | Suma | `7 + 2` | `9` |
| `-` | Resta | `7 - 2` | `5` |
| `*` | Multiplicación | `7 * 2` | `14` |
| `/` | División **real** | `7 / 2` | `3.5` |
| `//` | División **entera** | `7 // 2` | `3` |
| `%` | **Módulo** (resto) | `7 % 2` | `1` |
| `**` | Potencia | `7 ** 2` | `49` |

> `numero % 2 == 0` comprueba si un número es **par**; `segundos % 60` da los segundos sueltos al pasar a minutos.

### 8.2 Relacionales y lógicos

Relacionales (`==`, `!=`, `>`, `<`, `>=`, `<=`) devuelven `True`/`False`. Lógicos: `and`, `or`, `not`.

```python
print(5 > 3 and 2 > 4)   # False
print(5 > 3 or 2 > 4)    # True
print(not 5 > 3)         # False
```

> **`=` no es `==`.** `=` **asigna**; `==` **compara**. Confundirlos es el error nº 1 de quien empieza.

### 8.3 Precedencia

<figure markdown>
  ![Precedencia de operadores](../assets/diagramas/ud1-precedencia.svg#only-light)
  ![Precedencia de operadores](../assets/diagramas/ud1-precedencia-dark.svg#only-dark)
  <figcaption>Orden en que Python evalúa los operadores.</figcaption>
</figure>


```python
print(2 + 3 * 4)      # 14  (primero 3*4)
print((2 + 3) * 4)    # 20  (los paréntesis mandan)
```

> **Reto rápido 8.** Sin ejecutar, ¿cuánto vale `10 - 2 ** 3`? Compruébalo luego en Python. *(Solución: `2`.)*

---

### Practica lo de esta sección

> Hazlos **antes** de pasar a la siguiente sección: son cortos y solo usan lo que acabas de leer. Despliega la solución cuando lo tengas resuelto — o cuando te atasques de verdad.

**8.1.** Sin ejecutar, ¿cuánto valen `10 - 2 ** 3`, `(10 - 2) ** 3` y `10 % 4 * 2`? Compruébalo después.
<details><summary>Solución</summary>

```python
print(10 - 2 ** 3)      # -> 2      la potencia va primero
print((10 - 2) ** 3)    # -> 512    los parentesis mandan
print(10 % 4 * 2)       # -> 4      % y * tienen la misma prioridad: de izquierda a derecha
```
</details>

**8.2.** Comprueba si una persona de 20 años con carnet puede alquilar un coche (mínimo 21 años **y** carnet).
<details><summary>Solución</summary>

```python
edad: int = 20
tiene_carnet: bool = True

puede: bool = edad >= 21 and tiene_carnet

print(puede)   # -> False
```
</details>

**8.3.** Convierte 3725 segundos a horas, minutos y segundos usando `//` y `%`.
<details><summary>Solución</summary>

```python
total: int = 3725

horas: int = total // 3600
resto: int = total % 3600
minutos: int = resto // 60
segundos: int = resto % 60

print(f"{horas}h {minutos}m {segundos}s")   # -> 1h 2m 5s
```
</details>


---

## 9. Conversión de tipos

**Implícita** (automática, sin pérdida de información):

```python
resultado: float = 3 + 2.0    # int + float -> float
print(resultado)              # 5.0
```

**Explícita** (la pides tú con `int()`, `float()`, `str()`). Imprescindible porque `input()` **siempre devuelve texto**:

```python
texto: str = "42"
numero: int = int(texto)      # str -> int
print(numero + 8)             # 50
```

<figure markdown>
  ![Conversión de tipos](../assets/diagramas/ud1-conversion.svg#only-light)
  ![Conversión de tipos](../assets/diagramas/ud1-conversion-dark.svg#only-dark)
  <figcaption>Conversiones explícitas entre los tipos básicos.</figcaption>
</figure>


> **El error clásico con `input()`:**
> ```python
> edad = input("Edad: ")   # "20" (texto)
> print(edad + 1)          # TypeError
> ```
> Solución: `edad: int = int(input("Edad: "))`.

> `int("hola")` lanza `ValueError`. En la UD3 aprenderás a controlarlo con `try/except`.

> **Reto rápido 9.** Pide un número por teclado, conviértelo a `int` y muestra su cuadrado usando `**`.

---

### Practica lo de esta sección

> Hazlos **antes** de pasar a la siguiente sección: son cortos y solo usan lo que acabas de leer. Despliega la solución cuando lo tengas resuelto — o cuando te atasques de verdad.

**9.1.** Este programa falla. ¿Por qué? Arréglalo:

```python
edad = input("Edad: ")
print(edad + 1)
```
<details><summary>Solución</summary>

```python
# input() SIEMPRE devuelve texto: "20" + 1 mezcla str con int y lanza TypeError
edad: int = int(input("Edad: "))
print(edad + 1)   # -> 21
```
</details>

**9.2.** ¿Qué hace `int(9.99)`? ¿Y `round(9.99)`? Comprueba la diferencia.
<details><summary>Solución</summary>

```python
print(int(9.99))     # -> 9    int() TRUNCA: se queda con la parte entera
print(round(9.99))   # -> 10   round() REDONDEA al mas cercano
print(int(-2.7))     # -> -2   ojo: trunca hacia cero, no hacia abajo
```
</details>

**9.3.** El usuario escribe los decimales con coma (`3,5`). Conviértelo a `float` sin que reviente.
<details><summary>Solución</summary>

```python
texto: str = "3,5"

# float("3,5") lanza ValueError: en Python el separador decimal es el punto
numero: float = float(texto.replace(",", "."))

print(numero)   # -> 3.5
```
</details>


---

## 10. Entrada / salida por consola y formato

`input(mensaje)` lee una línea (devuelve `str`). `print(...)` muestra valores; admite `sep` y `end`:

```python
print("a", "b", "c")            # a b c
print("a", "b", sep="-")        # a-b
print("cargando", end="...")    # sin salto de línea
```

**f-strings** para dar formato: cadena con `f` y `{ }`:

```python
precio: float = 3.5
cantidad: int = 4
total: float = cantidad * precio
print(f"{cantidad} uds a {precio:.2f} € = {total:.2f} €")
# Salida:  4 uds a 3.50 € = 14.00 €
```

| Formato | Efecto | Ejemplo | Resultado |
|---|---|---|---|
| `:.2f` | 2 decimales | `f"{3.1:.2f}"` | `3.10` |
| `:.0f` | sin decimales | `f"{3.7:.0f}"` | `4` |
| `:>8` | derecha en 8 | `f"{'ok':>8}"` | `      ok` |
| `:,` | miles | `f"{1000000:,}"` | `1,000,000` |

> **Reto rápido 10.** Muestra el número `1234.5` con dos decimales y separador de miles a la vez. *(Pista: `:,.2f`.)*

---

### Practica lo de esta sección

> Hazlos **antes** de pasar a la siguiente sección: son cortos y solo usan lo que acabas de leer. Despliega la solución cuando lo tengas resuelto — o cuando te atasques de verdad.

**10.1.** Muestra el número `3.14159` con **dos decimales** y el precio `1234.5` con dos decimales y separador de miles.
<details><summary>Solución</summary>

```python
pi: float = 3.14159
precio: float = 1234.5

print(f"{pi:.2f}")        # -> 3.14
print(f"{precio:,.2f}")   # -> 1,234.50
```
</details>

**10.2.** Muestra estos tres productos en columnas: el nombre alineado a la izquierda en 12 huecos y el precio a la derecha en 8, con dos decimales.
<details><summary>Solución</summary>

```python
productos = [("Camisa", 19.9), ("Pantalón", 34.5), ("Gorra", 7.25)]

for nombre, precio in productos:
    print(f"{nombre:<12}{precio:>8.2f}")

# Camisa         19.90
# Pantalón       34.50
# Gorra           7.25
```
</details>

**10.3.** Pide un importe por teclado y muéstralo formateado como `Total:    45.00 €`.
<details><summary>Solución</summary>

```python
importe: float = float(input("Importe: "))
print(f"Total: {importe:>8.2f} €")   # -> Total:    45.00 €
```
</details>


---

## 11. Errores frecuentes (para tener a mano)

| Síntoma | Causa | Solución |
|---|---|---|
| `SyntaxError` | comilla/paréntesis sin cerrar | revisa que todo abre y cierra |
| `NameError` | variable no creada o mal escrita | defínela antes; cuida mayúsculas |
| `TypeError` al sumar | mezclar texto y número | convierte con `int()`/`float()` |
| `ValueError` en `int()` | el texto no es un número | valida la entrada (UD3) |
| decimales raros | precisión de los `float` | formatea con `:.2f` |
| `5 = x` | asignación al revés | la variable va a la izquierda |
| paquete no encontrado | entorno virtual sin activar | activa `.venv` antes de `pip install` |

---

## 12. Practica **con** solución a la vista

> **Primera vía.** Aquí puedes ver la solución. Sirven para *aprender el patrón*: intenta cada uno, y cuando lo tengas (o te atasques de verdad), despliega la solución y compárala con la tuya.

### 12.1 Actividades guiadas

Las hacemos en clase, pero tienes la solución para repasarlas después.

#### Actividad 1 — Ficha de una persona
Crea variables **tipadas** `nombre`, `edad`, `altura` y muéstralas con su tipo.
<details><summary>Solución</summary>

```python
nombre: str = "Ada"
edad: int = 36
altura: float = 1.68
print(nombre, type(nombre))
print(edad, type(edad))
print(altura, type(altura))
```
</details>

#### Actividad 2 — Área del círculo (constantes y operadores)
Define `PI` como constante y calcula el área de un círculo de radio 5.
<details><summary>Solución</summary>

```python
PI: float = 3.14159
radio: int = 5
area: float = PI * radio ** 2
print(f"Área: {area:.2f}")   # Área: 78.54
```
</details>

#### Actividad 3 — Función tipada de operaciones
Escribe `operaciones(a: int, b: int) -> None` que muestre suma, división entera, resto y potencia.
<details><summary>Solución</summary>

```python
def operaciones(a: int, b: int) -> None:
    print("Suma:", a + b)
    print("División entera:", a // b)
    print("Resto:", a % b)
    print("Potencia:", a ** b)

operaciones(17, 5)   # 22 / 3 / 2 / 1419857
```
</details>

#### Actividad 4 — Conversión y entrada
Pide dos enteros por teclado y muestra su suma (recuerda convertir).
<details><summary>Solución</summary>

```python
n1: int = int(input("Primer número: "))
n2: int = int(input("Segundo número: "))
print(f"Suma: {n1 + n2}")
```
</details>

---

### 12.2 Ejercicios propuestos

Trabajo autónomo. ○ básico · ◐ medio · ● avanzado. **Anota los tipos** en todas tus soluciones y pásales `mypy`.

!!! warning "Intenta antes de desplegar"
    Leer la solución sin haberlo intentado da sensación de aprender, pero no enseña. Usa primero la pista.

**E1 ○ · Celsius a Fahrenheit.** `F = C · 9/5 + 32`.
<details><summary>Pista</summary>Convierte la entrada con <code>float()</code>.</details>
<details><summary>Solución</summary>

```python
c: float = float(input("Grados Celsius: "))
f: float = c * 9 / 5 + 32
print(f"{c} °C = {f:.1f} °F")
```
</details>

**E2 ○ · Rectángulo.** Pide base y altura y muestra área y perímetro.
<details><summary>Solución</summary>

```python
base: float = float(input("Base: "))
altura: float = float(input("Altura: "))
print(f"Área: {base * altura:.2f}")
print(f"Perímetro: {2 * (base + altura):.2f}")
```
</details>

**E3 ◐ · Segundos a h:m:s.**
<details><summary>Pista</summary>Usa <code>//</code> y <code>%</code> con 3600 y 60.</details>
<details><summary>Solución</summary>

```python
total: int = int(input("Segundos: "))
horas: int = total // 3600
minutos: int = (total % 3600) // 60
seg: int = total % 60
print(f"{horas}h {minutos}m {seg}s")   # 3661 -> 1h 1m 1s
```
</details>

**E4 ◐ · Descuento.** `DESCUENTO = 15` (constante).
<details><summary>Solución</summary>

```python
DESCUENTO: int = 15
precio: float = float(input("Precio: "))
final: float = precio - precio * DESCUENTO / 100
print(f"Precio final: {final:.2f} €")
```
</details>

**E5 ◐ · Media de tres notas** con función tipada.
<details><summary>Solución</summary>

```python
def media(a: float, b: float, c: float) -> float:
    return (a + b + c) / 3

print(f"Media: {media(5, 7, 9):.2f}")   # 7.00
```
</details>

**E6 ● · Cambio de monedas.** Importe en céntimos → monedas de 50, 20, 10, 5, 2, 1.
<details><summary>Pista</summary>Divide con <code>//</code> y guarda el resto con <code>%</code> para la siguiente moneda.</details>
<details><summary>Solución</summary>

```python
c: int = int(input("Céntimos: "))
for valor in (50, 20, 10, 5, 2, 1):
    print(f"{valor}c: {c // valor}")
    c = c % valor
```
*(Usa un `for`, que verás en la UD3; también vale repetir seis bloques.)*
</details>

**E7 ◐ · Línea de ticket.** `linea_ticket(producto: str, unidades: int, precio: float) -> str` devuelve una línea como `Camisa        2 x  19.90 =    39.80 €`: el producto a la izquierda en 12 huecos, las unidades a la derecha en 3, el precio en 6 con 2 decimales y el importe en 8.
<details><summary>Pista</summary>Una sola f-string con cuatro campos: <code>:&lt;12</code>, <code>:&gt;3</code>, <code>:&gt;6.2f</code> y <code>:&gt;8.2f</code>.</details>
<details><summary>Solución</summary>

```python
def linea_ticket(producto: str, unidades: int, precio: float) -> str:
    """Línea de ticket alineada en columnas."""
    importe: float = unidades * precio
    return f"{producto:<12}{unidades:>3} x {precio:>6.2f} = {importe:>8.2f} €"
```
</details>

**E8 ● · Desglose de una compra.** `desglose(unidades: int, precio: float) -> tuple[float, float, float]` devuelve la base, el IVA y el total, **redondeados a 2 decimales**. El IVA es una constante del 21 %.
<details><summary>Pista</summary><code>round(valor, 2)</code> en cada uno, y devuelve los tres separados por comas: eso ya es una tupla.</details>
<details><summary>Solución</summary>

```python
IVA: int = 21


def desglose(unidades: int, precio: float) -> tuple[float, float, float]:
    """Base, IVA y total de una compra, redondeados a 2 decimales."""
    base: float = unidades * precio
    iva: float = base * IVA / 100
    return round(base, 2), round(iva, 2), round(base + iva, 2)
```
</details>

---

## 13. Proyecto de la unidad

Toda la práctica de esta unidad se hace sobre un **proyecto base**: una calculadora de presupuestos con IVA. Está montado
con la estructura real de un proyecto Python y trae una **batería de tests** que puedes
ejecutar en cualquier momento para ver si va todo bien.

**[Proyecto Presupuesto de tienda →](../proyectos/ud1/README.md)**

```
proyecto-ud1/
├── src/      ← tu código (funciones con TODO)
└── tests/    ← 16 tests que comprueban tu trabajo
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

## 14. Test de práctica

El examen de este RA es un **test de 12 preguntas sobre código** (lo tienes explicado en la
última sección). Aquí hay uno de práctica con el mismo formato y la misma dificultad, y con
**las respuestas al final**.

**[Test de práctica RA1 · Elementos del lenguaje](../simulacros/ra1/README.md)** · 12 preguntas · 45 min

Hazlo **contrarreloj, sin ordenador y sin apuntes**, como el de verdad. Y no ejecutes el
código hasta haber contestado: la gracia está en leerlo.

!!! tip "Después, compruébalo en Python"
    Cuando tengas tus respuestas, pasa cada fragmento por el intérprete. Ahí es donde de
    verdad se aprende: descubres no solo qué contestaste mal, sino por qué.

---

## 15. Retos opcionales

- **R1.** Amplía E5 para que, además de la media, diga `Aprobado`/`Suspenso` comparándola con 5.
- **R2.** Investiga `divmod(a, b)` (devuelve cociente y resto a la vez) y reescribe E3 con él.
- **R3.** Formatea un pequeño ticket con los precios alineados a la derecha (`:>8`), en columnas.
- **R4.** Añade anotaciones de tipo a **todos** tus ejercicios y consigue que `mypy` diga *Success* en cada uno.

- **R5.** Convierte una cantidad de segundos introducida por teclado a días, horas, minutos y segundos, y muéstralo como `2d 3h 04m 05s`.
- **R6.** Formatea un ticket de tres productos con los importes alineados a la derecha y una línea de total separada por guiones del mismo ancho.
---

## 16. Autoevaluación rápida

<details><summary>1. ¿Qué muestra <code>print(7 // 2)</code>?</summary><code>3</code> (división entera).</details>
<details><summary>2. ¿Qué tipo devuelve siempre <code>input()</code>?</summary><code>str</code>.</details>
<details><summary>3. ¿Por qué falla <code>"5" + 1</code>?</summary>Mezcla <code>str</code> e <code>int</code> (<code>TypeError</code>).</details>
<details><summary>4. Diferencia entre <code>=</code> y <code>==</code>.</summary><code>=</code> asigna; <code>==</code> compara.</details>
<details><summary>5. ¿Comprueba Python las anotaciones de tipo al ejecutar?</summary>No; las comprueba <b>mypy</b> de forma estática.</details>
<details><summary>6. ¿Para qué sirve un entorno virtual?</summary>Aislar los paquetes de cada proyecto para que no se mezclen.</details>
<details><summary>7. ¿Qué comando guarda las dependencias?</summary><code>pip freeze > requirements.txt</code>.</details>

---

## 17. Glosario

| Término | Definición |
|---|---|
| **Algoritmo** | Pasos para resolver un problema, independientes del lenguaje. |
| **Variable** | Nombre que guarda un valor y puede cambiar. |
| **Tipo** | Clase de dato: `int`, `float`, `str`, `bool`. |
| **Anotación de tipo** | Indicación `: tipo` que documenta y verifica con mypy. |
| **Literal / Constante** | Valor escrito directamente / valor que no debe cambiar. |
| **Operador / Expresión** | Símbolo que opera / combinación que produce un resultado. |
| **Casting** | Conversión de tipo (`int()`, `float()`, `str()`). |
| **f-string** | Cadena con formato `f"...{valor}..."`. |
| **Entorno virtual (venv)** | Copia aislada de Python por proyecto. |
| **pip** | Gestor de paquetes de Python. |
| **mypy** | Herramienta que comprueba los tipos sin ejecutar. |

---

## 18. Cómo se evalúa esta unidad (RA1)

El RA1 es del **primer trimestre**, y ahí el examen es un **test de 12 preguntas de
opción múltiple**. Pero no de definiciones: **todas las preguntas son de código**.

### Cómo son las preguntas

Se te da un fragmento y tienes que decir qué hace. Hay cuatro formas:

| Tipo | Qué te piden |
|---|---|
| **Qué imprime** | Leer el código y decir la salida exacta, carácter a carácter. |
| **Qué error da** | Identificar la excepción: `TypeError`, `ValueError`, `NameError`… |
| **Cuánto vale** | El valor de una expresión, con su tipo. |
| **Cuál es correcta** | Cuatro versiones de una función; solo una cumple lo que se pide. |

Es exactamente lo que haces en clase cuando lees un error o predices un resultado antes de
ejecutar. Temas del RA1: tipos y variables · conversión de tipos · operadores y precedencia · constantes y nombres · formato de salida.

### Cómo se puntúa

| | |
|---|---|
| Acierto | **+0.83** puntos |
| Error | **−0.28** puntos |
| En blanco | 0 |

`nota = (aciertos − errores ÷ 3) × 0.83`, con un mínimo de 0.

Se resta un tercio por error porque hay cuatro opciones: así **contestar al azar no
compensa**. La regla práctica es sencilla:

- Si lo sabes, marca.
- Si dudas **entre dos**, marca: sigue saliéndote a cuenta.
- Si no tienes ni idea, **déjalo en blanco**.

### Un ejemplo de corrección

| Alumno | Aciertos | Errores | En blanco | Cuenta | Nota |
|---|:---:|:---:|:---:|---|:---:|
| Lo lleva bien | 10 | 2 | 0 | (10 − 0,67) × 0.83 | **7,78** |
| Va justo | 8 | 4 | 0 | (8 − 1,33) × 0.83 | **5,56** |
| Prudente | 6 | 0 | 6 | (6 − 0) × 0.83 | **5,00** |
| A ciegas | 3 | 9 | 0 | (3 − 3) × 0.83 | **0,00** |

Fíjate en las dos últimas filas: quien contesta solo lo que sabe aprueba, y quien marca a
voleo se queda a cero. **No es lo mismo dudar que adivinar.**

### Cómo prepararte

1. Los **ejercicios de sección** y los **ejercicios largos**: el test pregunta justo eso.
2. El **proyecto de la unidad**: escribir el código es lo que te enseña a leerlo.
3. El **[test de práctica](../simulacros/ra1/README.md)**, con las mismas 12 preguntas
   de formato y las respuestas al final.

!!! tip "Lee el código antes de ejecutarlo"
   Durante el curso, cada vez que vayas a ejecutar algo, predice primero qué va a salir.
   Ese hábito es literalmente el examen.

!!! note "En el segundo y tercer trimestre cambia"
    A partir del RA3 los exámenes son **retos de programación**: se escribe código y se
    corrige con una batería de casos de prueba. El test es solo para arrancar.

---

### Material de apoyo de la unidad

- **[Proyecto de la unidad](../proyectos/ud1/README.md)** — `presupuesto`, 16 tests.
- **[Test de práctica](../simulacros/ra1/README.md)** — 12 preguntas de código, con respuestas.
- **[Entorno de trabajo](../recursos/entorno.md)** — chuleta de `venv`, `pip` y `mypy`.
