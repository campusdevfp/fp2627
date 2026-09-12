# Unidad 5 · Entrada/salida y ficheros

> **Módulo:** CMO-313 · Fundamentos de programación
> **Resultado de aprendizaje:** RA5 · **Duración:** 6 h · **Peso:** 10 %
> **Lenguaje:** Python 3 (tipado)

Todos tus programas hasta ahora tenían un problema: **al cerrarlos, los datos desaparecían**. Esta unidad lo resuelve. Aprenderás a guardar información en ficheros y a recuperarla después, que es lo que convierte un ejercicio en una aplicación de verdad.

---

## Mapa de la unidad

<figure markdown>
  ![Mapa de la unidad 5](../assets/diagramas/ud5-mapa.svg#only-light)
  ![Mapa de la unidad 5](../assets/diagramas/ud5-mapa-dark.svg#only-dark)
  <figcaption>Los ficheros permiten que los datos sobrevivan al programa.</figcaption>
</figure>

### Qué vas a saber hacer al terminar

- [ ] Dar formato profesional a la salida por consola (columnas alineadas).
- [ ] Abrir ficheros correctamente con `with open(...)`.
- [ ] Escribir y leer **ficheros de texto**.
- [ ] Trabajar con **CSV** usando el módulo `csv`.
- [ ] Guardar y recuperar datos estructurados en **JSON**.
- [ ] Gestionar los errores típicos: fichero que no existe, permisos, codificación.

---

## 1. Salida por consola con formato

Ya conoces las f-strings. Aquí las llevamos al punto en que la salida parece profesional.

### 1.1 Alinear en columnas

```python
productos = [("Camisa", 19.99), ("Pantalón", 34.5), ("Gorra", 8.0)]

print(f"{'PRODUCTO':<12}{'PRECIO':>10}")
print("-" * 22)
for nombre, precio in productos:
    print(f"{nombre:<12}{precio:>10.2f}")
```

```text
PRODUCTO        PRECIO
----------------------
Camisa           19.99
Pantalón         34.50
Gorra             8.00
```

| Formato | Efecto |
|---|---|
| `:<12` | alinea a la **izquierda** en 12 caracteres |
| `:>10` | alinea a la **derecha** en 10 |
| `:^10` | **centra** en 10 |
| `:>10.2f` | derecha, 10 de ancho, 2 decimales |
| `:,` | separador de miles |

!!! tip "Los números, siempre a la derecha"
    Alineados a la derecha, las unidades quedan una debajo de otra y la tabla se lee de un vistazo.

> 🎯 **Reto rápido 1.** Muestra tres nombres a la izquierda en 15 caracteres y sus edades a la derecha en 5.

---

## 2. Abrir ficheros: `with open(...)`

### 2.1 La forma correcta

```python
with open("datos.txt", "w", encoding="utf-8") as fichero:
    fichero.write("Hola\n")
# aquí el fichero YA está cerrado, automáticamente
```

Tres cosas, y las tres importan:

| Parte | Para qué |
|---|---|
| `with` | **cierra el fichero solo**, incluso si hay un error |
| `"w"` | el **modo** de apertura |
| `encoding="utf-8"` | para que las tildes y la ñ no se rompan |

!!! danger "Sin `with`, tarde o temprano pierdes datos"
    ```python
    f = open("datos.txt", "w")
    f.write("Hola")        # si algo falla aquí, el fichero queda abierto
    f.close()              # ...y esto no se ejecuta: se pierde lo escrito
    ```
    **Usa siempre `with`.**

### 2.2 Modos de apertura

| Modo | Qué hace | Cuidado |
|:---:|---|---|
| `"r"` | **leer** (por defecto) | error si no existe |
| `"w"` | **escribir** | ⚠️ **borra** el contenido anterior |
| `"a"` | **añadir** al final | no borra |
| `"x"` | crear nuevo | error si ya existe |

!!! warning "`w` borra sin avisar"
    Abrir con `"w"` un fichero que ya tiene datos lo deja **vacío** al instante. Si quieres conservar lo anterior, usa `"a"`.

> 🎯 **Reto rápido 2.** ¿Qué modo usarías para un fichero de registro (log) al que se van añadiendo líneas? *(Respuesta: `"a"`.)*

---

## 3. Ficheros de texto

### 3.1 Escribir

```python
lineas = ["Ada", "Linus", "Grace"]

with open("nombres.txt", "w", encoding="utf-8") as f:
    for nombre in lineas:
        f.write(nombre + "\n")      # \n = salto de línea
```

!!! tip "`write()` no añade el salto de línea"
    A diferencia de `print()`, hay que ponerlo a mano con `\n`. Si lo olvidas, todo queda pegado en una sola línea.

### 3.2 Leer

Tres formas, según lo que necesites:

```python
# a) todo el contenido en una cadena
with open("nombres.txt", encoding="utf-8") as f:
    contenido: str = f.read()

# b) una lista con todas las líneas
with open("nombres.txt", encoding="utf-8") as f:
    lineas: list[str] = f.readlines()

# c) línea a línea (la mejor para ficheros grandes)
with open("nombres.txt", encoding="utf-8") as f:
    for linea in f:
        print(linea.rstrip())       # rstrip quita el \n final
```

!!! warning "Acuérdate de `rstrip()`"
    Cada línea leída **incluye el `\n`**. Si comparas `linea == "Ada"` fallará, porque en realidad vale `"Ada\n"`. Límpiala con `linea.rstrip()`.

### 3.3 Si el fichero no existe

```python
try:
    with open("nombres.txt", encoding="utf-8") as f:
        contenido = f.read()
except FileNotFoundError:
    print("El fichero no existe todavía")
    contenido = ""
```

---

## 4. Ficheros CSV

Un **CSV** (*comma-separated values*) es un fichero de texto con datos en forma de tabla: una fila por línea y las columnas separadas por comas. Es lo que exporta cualquier hoja de cálculo.

```text
nombre,telefono,email
Ada,600111222,ada@ejemplo.com
Linus,600333444,linus@ejemplo.com
```

Se puede tratar como texto, pero el módulo `csv` gestiona solo los casos peliagudos (comas dentro de un campo, comillas…).

### 4.1 Escribir un CSV

```python
import csv

contactos = [
    ["Ada", "600111222", "ada@ejemplo.com"],
    ["Linus", "600333444", "linus@ejemplo.com"],
]

with open("contactos.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f)
    escritor.writerow(["nombre", "telefono", "email"])   # cabecera
    escritor.writerows(contactos)                        # todas las filas
```

!!! tip "`newline=\"\"` no es opcional"
    Sin él, en Windows aparece una línea en blanco entre cada fila. Póngase siempre al abrir un CSV.

### 4.2 Leer un CSV

```python
import csv

with open("contactos.csv", encoding="utf-8") as f:
    lector = csv.reader(f)
    cabecera = next(lector)          # se salta la primera fila
    for fila in lector:
        nombre, telefono, email = fila
        print(f"{nombre:<10}{telefono:>12}")
```

### 4.3 Con nombres de columna: `DictReader`

Más legible, porque accedes por nombre en vez de por posición:

```python
import csv

with open("contactos.csv", encoding="utf-8") as f:
    for fila in csv.DictReader(f):
        print(fila["nombre"], fila["email"])
```

> ⚠️ Todo lo que se lee de un CSV es **texto**. Si una columna es numérica, hay que convertirla: `int(fila["edad"])`.

> 🎯 **Reto rápido 3.** ¿Por qué `csv.reader` es mejor que hacer `linea.split(",")`? *(Porque gestiona las comas que van dentro de un campo entrecomillado.)*

---

## 5. JSON

**JSON** guarda datos con estructura (diccionarios y listas anidados), no solo tablas. Es el formato que usan casi todas las APIs web.

```python
import json

datos = {
    "nombre": "Ada",
    "edad": 36,
    "lenguajes": ["Python", "C"],
}

# guardar
with open("datos.json", "w", encoding="utf-8") as f:
    json.dump(datos, f, indent=2, ensure_ascii=False)

# recuperar
with open("datos.json", encoding="utf-8") as f:
    recuperado = json.load(f)

print(recuperado["nombre"])          # Ada
print(recuperado["lenguajes"][0])    # Python
```

| Parámetro | Para qué |
|---|---|
| `indent=2` | lo escribe con sangría, legible para personas |
| `ensure_ascii=False` | conserva tildes y ñ en lugar de escaparlas |

### CSV o JSON, ¿cuál?

| Usa **CSV** si… | Usa **JSON** si… |
|---|---|
| los datos son una tabla plana | hay estructura anidada |
| se van a abrir en Excel | los consume otro programa |
| todas las filas tienen los mismos campos | los campos varían |

---

## 6. Errores frecuentes

| Síntoma | Causa | Solución |
|---|---|---|
| `FileNotFoundError` | el fichero no existe o la ruta está mal | contrólalo con `try/except` |
| Se borró el contenido | abriste con `"w"` | usa `"a"` para añadir |
| Todo en una sola línea | falta `\n` en `write()` | añádelo |
| `Ada\n` al comparar | la línea conserva el salto | usa `.rstrip()` |
| Tildes raras (`Ã¡`) | falta el encoding | `encoding="utf-8"` siempre |
| Líneas en blanco en el CSV | falta `newline=""` | añádelo al abrir |
| `TypeError` al sumar del CSV | los datos leídos son texto | convierte con `int()`/`float()` |
| El fichero queda bloqueado | no usaste `with` | usa `with` |

---

## 7. Practica **con** solución a la vista

### 7.1 Actividades guiadas

#### Actividad 1 — Escribir un fichero
Guarda tres nombres, uno por línea, en `nombres.txt`.
<details><summary>💡 Solución</summary>

```python
nombres: list[str] = ["Ada", "Linus", "Grace"]
with open("nombres.txt", "w", encoding="utf-8") as f:
    for n in nombres:
        f.write(n + "\n")
```
</details>

#### Actividad 2 — Leerlo y contarlo
Lee `nombres.txt` y muestra cuántas líneas tiene.
<details><summary>💡 Solución</summary>

```python
with open("nombres.txt", encoding="utf-8") as f:
    lineas = [ln.rstrip() for ln in f]
print(f"{len(lineas)} nombres")
```
</details>

#### Actividad 3 — Tabla con formato
Muestra una lista de productos en columnas alineadas.
<details><summary>💡 Solución</summary>

```python
productos = [("Camisa", 19.99), ("Gorra", 8.0)]
print(f"{'PRODUCTO':<12}{'PRECIO':>10}")
for nombre, precio in productos:
    print(f"{nombre:<12}{precio:>10.2f}")
```
</details>

#### Actividad 4 — CSV de ida y vuelta
Guarda dos contactos en CSV y vuelve a leerlos.
<details><summary>💡 Solución</summary>

```python
import csv

with open("contactos.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["nombre", "telefono"])
    w.writerow(["Ada", "600111222"])
    w.writerow(["Linus", "600333444"])

with open("contactos.csv", encoding="utf-8") as f:
    for fila in csv.DictReader(f):
        print(fila["nombre"], fila["telefono"])
```
</details>

### 7.2 Ejercicios propuestos

**E1 🟢 · Guardar una lista.** `guardar(ruta: str, lineas: list[str]) -> None`.
<details><summary>Solución</summary>

```python
def guardar(ruta: str, lineas: list[str]) -> None:
    with open(ruta, "w", encoding="utf-8") as f:
        for ln in lineas:
            f.write(ln + "\n")
```
</details>

**E2 🟢 · Leer una lista.** `leer(ruta: str) -> list[str]`, devolviendo `[]` si no existe.
<details><summary>Solución</summary>

```python
def leer(ruta: str) -> list[str]:
    try:
        with open(ruta, encoding="utf-8") as f:
            return [ln.rstrip() for ln in f]
    except FileNotFoundError:
        return []
```
</details>

**E3 🟡 · Añadir al final.** `anadir(ruta: str, linea: str) -> None` sin borrar lo anterior.
<details><summary>Solución</summary>

```python
def anadir(ruta: str, linea: str) -> None:
    with open(ruta, "a", encoding="utf-8") as f:
        f.write(linea + "\n")
```
</details>

**E4 🟡 · Contar líneas.** `contar_lineas(ruta: str) -> int` (0 si no existe).
<details><summary>Solución</summary>

```python
def contar_lineas(ruta: str) -> int:
    try:
        with open(ruta, encoding="utf-8") as f:
            return sum(1 for _ in f)
    except FileNotFoundError:
        return 0
```
</details>

**E5 🔴 · Media desde CSV.** Lee un CSV con columna `nota` y devuelve la media.
<details><summary>Pista</summary>Recuerda que <code>fila["nota"]</code> es texto: conviértelo con <code>float()</code>.</details>
<details><summary>Solución</summary>

```python
import csv

def media_csv(ruta: str) -> float:
    notas: list[float] = []
    with open(ruta, encoding="utf-8") as f:
        for fila in csv.DictReader(f):
            notas.append(float(fila["nota"]))
    if not notas:
        return 0.0
    return sum(notas) / len(notas)
```
</details>

---

## Proyecto de la unidad ⭐

Toda la práctica de esta unidad se hace sobre un **proyecto base**: una agenda que guarda y recupera datos en CSV y JSON. Está montado
con la estructura real de un proyecto Python y trae una **batería de tests** que puedes
ejecutar en cualquier momento para ver si va todo bien.

**[Proyecto Agenda de contactos →](../proyectos/ud5/README.md)**

```
proyecto-ud5/
├── src/      ← tu código (funciones con TODO)
└── tests/    ← 10 tests que comprueban tu trabajo
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

## 9. Retos opcionales 🚀

- **R1.** Programa que lea un CSV de notas y escriba otro CSV añadiendo la columna `apto`.
- **R2.** Registro (log): función que añada una línea con fecha y hora usando `datetime`.
- **R3.** Convierte un CSV a JSON y comprueba que al volver atrás obtienes lo mismo.

---

## 10. Autoevaluación rápida

<details><summary>1. ¿Por qué usar <code>with open(...)</code>?</summary>Cierra el fichero automáticamente, incluso si hay un error.</details>
<details><summary>2. Diferencia entre los modos <code>"w"</code> y <code>"a"</code>.</summary><code>"w"</code> borra el contenido; <code>"a"</code> añade al final.</details>
<details><summary>3. ¿Qué excepción salta si el fichero no existe?</summary><code>FileNotFoundError</code>.</details>
<details><summary>4. ¿Por qué <code>newline=""</code> al abrir un CSV?</summary>Para que no aparezcan líneas en blanco entre filas.</details>
<details><summary>5. ¿De qué tipo son los datos leídos de un CSV?</summary>Texto (<code>str</code>): hay que convertirlos.</details>
<details><summary>6. ¿Cuándo JSON en vez de CSV?</summary>Cuando los datos tienen estructura anidada, no forma de tabla.</details>

---

## 11. Glosario

| Término | Definición |
|---|---|
| **Fichero de texto** | Archivo con caracteres legibles. |
| **Modo de apertura** | `r` leer, `w` escribir, `a` añadir, `x` crear. |
| **`with`** | Bloque que cierra el recurso automáticamente. |
| **Encoding** | Cómo se codifican los caracteres (`utf-8`). |
| **CSV** | Texto con valores separados por comas: una tabla. |
| **JSON** | Formato de datos estructurados y anidados. |
| **Persistencia** | Que los datos sobrevivan al cierre del programa. |

---

## 12. Cómo se evalúa esta unidad (RA5)

Examen **100 % práctico**: un programa que guarde y recupere información.

| # | Qué se valora | Cómo se mide | Puntos |
|:---:|---|---|:---:|
| 1 | **Que funcione** | casos de prueba superados × 7 | **7,0** |
| 2 | **Dos formatos** | usa fichero de texto **y** CSV (o JSON) | **1,0** |
| 3 | **Control de errores** | fichero inexistente gestionado | **1,0** |
| 4 | **Formato de salida** | tabla alineada con f-strings | **1,0** |
| | | **TOTAL** | **10** |

**Se supera con 5.** Los tests leen los ficheros que genera tu programa: respeta los nombres, la cabecera y el orden de las columnas del enunciado.
