# Unidad 6 · Bases de datos relacionales

> **Módulo:** CMO-313 · Fundamentos de programación
> **Resultado de aprendizaje:** RA6 · **Duración:** 8 h · **Peso:** 20 %
> **Lenguaje:** Python 3 (tipado) + SQLite

En la UD5 guardaste datos en ficheros. Funciona para poca información, pero cuando hay miles de registros y hace falta buscarlos, ordenarlos o modificarlos, el fichero se queda corto. La solución es una **base de datos**.

Es el segundo RA de más peso (20 %) y la puerta de entrada a los módulos de bases de datos del ciclo.

---

## Mapa de la unidad

<figure markdown>
  ![Mapa de la unidad 6](../assets/diagramas/ud6-mapa.svg#only-light)
  ![Mapa de la unidad 6](../assets/diagramas/ud6-mapa-dark.svg#only-dark)
  <figcaption>Tu programa habla con la base de datos mediante sqlite3 y sentencias SQL.</figcaption>
</figure>

### Qué vas a saber hacer al terminar

- [ ] Explicar qué aporta una base de datos frente a un fichero.
- [ ] Conectarte a **SQLite** desde Python con `sqlite3`.
- [ ] Crear tablas con `CREATE TABLE`.
- [ ] Hacer las cuatro operaciones **CRUD**: insertar, consultar, modificar y borrar.
- [ ] Usar **consultas parametrizadas** y entender por qué son obligatorias.
- [ ] Filtrar y ordenar con `WHERE` y `ORDER BY`.
- [ ] Confirmar cambios con `commit()` y cerrar bien la conexión.

---

## 1. Por qué una base de datos

Con un CSV de 50 000 productos, buscar uno obliga a leer el fichero entero; y si dos personas escriben a la vez, los datos se corrompen.

Un **SGBD** (Sistema Gestor de Bases de Datos) resuelve eso:

| Ventaja | Qué significa |
|---|---|
| **Búsquedas rápidas** | encuentra un registro entre millones sin leerlo todo |
| **Integridad** | impide datos inválidos o duplicados |
| **Concurrencia** | varios programas a la vez sin corromper nada |
| **Consultas potentes** | filtrar, ordenar y agrupar con una sola instrucción |

En una base de datos **relacional**, los datos se organizan en **tablas**: cada fila es un registro y cada columna un campo.

**Usaremos SQLite**: viene incluido en Python, guarda todo en un único fichero `.db` y no necesita instalar ningún servidor. Es el mismo motor que llevan dentro tu móvil y tu navegador.

---

## 2. Conectarse desde Python

```python
import sqlite3

conexion = sqlite3.connect("inventario.db")   # crea el fichero si no existe
cursor = conexion.cursor()                    # el que ejecuta las sentencias

# ... operaciones ...

conexion.commit()                             # confirma los cambios
conexion.close()                              # cierra
```

| Pieza | Para qué sirve |
|---|---|
| `connect()` | abre (o crea) la base de datos |
| `cursor()` | objeto con el que se ejecutan las sentencias SQL |
| `commit()` | **confirma** los cambios: sin esto no se guardan |
| `close()` | cierra la conexión |

!!! danger "Sin `commit()` no se guarda nada"
    Es el error más frecuente de esta unidad: el programa parece funcionar, no da ningún error… y al volver a abrir la base de datos está vacía. **Después de insertar, modificar o borrar, hay que llamar a `commit()`.**

### 2.1 Mejor con `with`

Igual que con los ficheros, `with` se encarga del cierre:

```python
import sqlite3

with sqlite3.connect("inventario.db") as conexion:
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO productos (nombre, precio) VALUES (?, ?)",
                   ("Camisa", 19.99))
    # el commit lo hace with al salir sin errores
```

> 🎯 **Reto rápido 1.** ¿Qué pasa si ejecutas un `INSERT` y cierras el programa sin `commit()`? *(No se guarda nada.)*

---

## 3. Crear la tabla

```python
cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id     INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL,
        stock  INTEGER NOT NULL DEFAULT 0
    )
""")
```

| Elemento | Qué significa |
|---|---|
| `IF NOT EXISTS` | no falla si la tabla ya existe (imprescindible) |
| `INTEGER PRIMARY KEY AUTOINCREMENT` | identificador único que se genera solo |
| `NOT NULL` | el campo es obligatorio |
| `DEFAULT 0` | valor por defecto si no se indica |

Tipos de SQLite: `INTEGER`, `REAL` (decimales), `TEXT` y `BLOB`.

---

## 4. CRUD: las cuatro operaciones

**CRUD** = *Create, Read, Update, Delete*. Con esas cuatro se hace todo.

### 4.1 Create — `INSERT`

```python
cursor.execute(
    "INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)",
    ("Camisa", 19.99, 10)
)
conexion.commit()
```

Varios de golpe:

```python
productos = [("Gorra", 8.0, 25), ("Pantalón", 34.5, 7)]
cursor.executemany(
    "INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)",
    productos
)
conexion.commit()
```

### 4.2 Read — `SELECT`

```python
cursor.execute("SELECT id, nombre, precio FROM productos")

filas = cursor.fetchall()        # todas, como lista de tuplas
for id_, nombre, precio in filas:
    print(f"{id_:>3} {nombre:<12} {precio:>8.2f} €")
```

| Método | Devuelve |
|---|---|
| `fetchall()` | todas las filas (lista de tuplas) |
| `fetchone()` | la siguiente fila, o `None` si no hay |
| `fetchmany(n)` | como mucho `n` filas |

### 4.3 Update — `UPDATE`

```python
cursor.execute("UPDATE productos SET precio = ? WHERE id = ?", (24.99, 1))
conexion.commit()
```

!!! danger "`UPDATE` sin `WHERE` cambia TODAS las filas"
    `UPDATE productos SET precio = 0` pone a cero el precio de todo el inventario. Igual con `DELETE FROM productos`, que lo borra entero. **El `WHERE` no es opcional en la práctica.**

### 4.4 Delete — `DELETE`

```python
cursor.execute("DELETE FROM productos WHERE id = ?", (3,))
conexion.commit()
```

> ⚠️ Ojo a la coma en `(3,)`: sin ella no es una tupla, y `execute` la necesita.

---

## 5. Consultas parametrizadas (obligatorio)

Fíjate en que **nunca** hemos metido los valores dentro del texto SQL. Siempre `?` y una tupla aparte. Esta es la razón:

```python
nombre = input("Buscar: ")

# ❌ MAL: concatenando
cursor.execute("SELECT * FROM productos WHERE nombre = '" + nombre + "'")

# ✅ BIEN: parametrizada
cursor.execute("SELECT * FROM productos WHERE nombre = ?", (nombre,))
```

Con la primera forma, si el usuario escribe `'; DROP TABLE productos; --` la base de datos **ejecuta ese comando** y se pierde la tabla. Es la **inyección SQL**, una de las vulnerabilidades más explotadas de la historia.

!!! success "La regla, sin excepciones"
    Los datos van **siempre** con `?` y una tupla. Nunca se concatenan ni se interpolan en la cadena SQL. En el examen esto se comprueba.

> 🎯 **Reto rápido 2.** Reescribe de forma segura: `cursor.execute(f"SELECT * FROM productos WHERE precio > {p}")`.
> *(Solución: `cursor.execute("SELECT * FROM productos WHERE precio > ?", (p,))`.)*

---

## 6. Filtrar y ordenar

```python
# filtrar
cursor.execute("SELECT nombre FROM productos WHERE precio > ?", (20,))

# ordenar
cursor.execute("SELECT nombre, precio FROM productos ORDER BY precio DESC")

# combinar y limitar
cursor.execute("""
    SELECT nombre, precio FROM productos
    WHERE stock > ?
    ORDER BY precio ASC
    LIMIT 5
""", (0,))
```

| Cláusula | Qué hace |
|---|---|
| `WHERE` | filtra las filas |
| `ORDER BY campo ASC / DESC` | ordena ascendente / descendente |
| `LIMIT n` | como mucho n resultados |
| `LIKE '%algo%'` | búsqueda por texto parcial |

Búsqueda parcial parametrizada:

```python
texto = "cam"
cursor.execute("SELECT nombre FROM productos WHERE nombre LIKE ?", (f"%{texto}%",))
```

Funciones de agregado:

```python
cursor.execute("SELECT COUNT(*), AVG(precio), MAX(precio) FROM productos")
total, media, maximo = cursor.fetchone()
```

---

## 7. Estructura de una aplicación con BD

Conviene separar el acceso a datos de la interfaz:

```python
import sqlite3

BD = "inventario.db"


def crear_tabla() -> None:
    """Crea la tabla si no existe."""
    with sqlite3.connect(BD) as con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id     INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                precio REAL NOT NULL,
                stock  INTEGER NOT NULL DEFAULT 0
            )
        """)


def insertar(nombre: str, precio: float, stock: int) -> None:
    """Añade un producto."""
    with sqlite3.connect(BD) as con:
        con.execute(
            "INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)",
            (nombre, precio, stock),
        )


def listar() -> list[tuple]:
    """Devuelve todos los productos."""
    with sqlite3.connect(BD) as con:
        return con.execute(
            "SELECT id, nombre, precio, stock FROM productos"
        ).fetchall()


def main() -> None:
    crear_tabla()
    insertar("Camisa", 19.99, 10)
    for fila in listar():
        print(fila)


if __name__ == "__main__":
    main()
```

Cada función hace **una** operación y **devuelve** datos; solo `main` imprime. Igual que en la UD2, esto es lo que permite probarlo automáticamente.

---

## 8. Errores frecuentes

| Síntoma | Causa | Solución |
|---|---|---|
| Los datos no se guardan | falta `commit()` | llámalo tras insertar/modificar/borrar |
| `no such table` | no creaste la tabla | `CREATE TABLE IF NOT EXISTS` al arrancar |
| `no such column` | nombre de columna mal escrito | revisa el `CREATE TABLE` |
| `Incorrect number of bindings` | los `?` no coinciden con la tupla | cuenta ambos |
| Se cambiaron todas las filas | `UPDATE`/`DELETE` sin `WHERE` | añade siempre el `WHERE` |
| `(3)` no funciona como parámetro | no es una tupla | escribe `(3,)` |
| `database is locked` | conexión sin cerrar | usa `with` |
| Inyección SQL | concatenaste la entrada del usuario | usa `?` siempre |

---

## 9. Practica **con** solución a la vista

### 9.1 Actividades guiadas

#### Actividad 1 — Crear la base de datos
Crea `prueba.db` con una tabla `alumnos` (id, nombre, nota).
<details><summary>💡 Solución</summary>

```python
import sqlite3

with sqlite3.connect("prueba.db") as con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS alumnos (
            id     INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            nota   REAL NOT NULL
        )
    """)
```
</details>

#### Actividad 2 — Insertar y listar
<details><summary>💡 Solución</summary>

```python
with sqlite3.connect("prueba.db") as con:
    con.execute("INSERT INTO alumnos (nombre, nota) VALUES (?, ?)", ("Ada", 9.5))

with sqlite3.connect("prueba.db") as con:
    for fila in con.execute("SELECT id, nombre, nota FROM alumnos"):
        print(fila)
```
</details>

#### Actividad 3 — Modificar y borrar
<details><summary>💡 Solución</summary>

```python
with sqlite3.connect("prueba.db") as con:
    con.execute("UPDATE alumnos SET nota = ? WHERE nombre = ?", (10.0, "Ada"))
    con.execute("DELETE FROM alumnos WHERE nota < ?", (5.0,))
```
</details>

#### Actividad 4 — Buscar
Muestra los alumnos aprobados ordenados por nota descendente.
<details><summary>💡 Solución</summary>

```python
with sqlite3.connect("prueba.db") as con:
    filas = con.execute(
        "SELECT nombre, nota FROM alumnos WHERE nota >= ? ORDER BY nota DESC",
        (5.0,)
    ).fetchall()
print(filas)
```
</details>

### 9.2 Ejercicios propuestos

**E1 🟢 · Contar registros.** `cuantos(bd: str) -> int` con `COUNT(*)`.
<details><summary>Solución</summary>

```python
import sqlite3

def cuantos(bd: str) -> int:
    with sqlite3.connect(bd) as con:
        return int(con.execute("SELECT COUNT(*) FROM alumnos").fetchone()[0])
```
</details>

**E2 🟢 · Nota media.** `nota_media(bd: str) -> float` con `AVG`, devolviendo `0.0` si no hay filas.
<details><summary>Pista</summary><code>AVG</code> devuelve <code>None</code> con la tabla vacía.</details>
<details><summary>Solución</summary>

```python
def nota_media(bd: str) -> float:
    with sqlite3.connect(bd) as con:
        resultado = con.execute("SELECT AVG(nota) FROM alumnos").fetchone()[0]
    return float(resultado) if resultado is not None else 0.0
```
</details>

**E3 🟡 · Buscar por nombre.** Búsqueda parcial parametrizada con `LIKE`.
<details><summary>Solución</summary>

```python
def buscar(bd: str, texto: str) -> list[tuple]:
    with sqlite3.connect(bd) as con:
        return con.execute(
            "SELECT nombre, nota FROM alumnos WHERE nombre LIKE ?",
            (f"%{texto}%",)
        ).fetchall()
```
</details>

**E4 🔴 · Menú CRUD.** Programa con menú (alta, listado, modificación, baja, salir) y entrada validada.
<details><summary>Solución</summary>

```python
def menu() -> None:
    crear_tabla()
    opcion = ""
    while opcion != "0":
        print("1-Alta  2-Listar  3-Modificar  4-Baja  0-Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            insertar(input("Nombre: "), float(input("Precio: ")), 0)
        elif opcion == "2":
            for fila in listar():
                print(fila)
```
*(Añade `try/except` en las conversiones, como en la UD3.)*
</details>

---

## Proyecto de la unidad ⭐

Toda la práctica de esta unidad se hace sobre un **proyecto base**: un inventario sobre una base de datos SQLite. Está montado
con la estructura real de un proyecto Python y trae una **batería de tests** que puedes
ejecutar en cualquier momento para ver si va todo bien.

**[Proyecto Inventario →](../proyectos/ud6/README.md)**

```
proyecto-ud6/
├── src/      ← tu código (funciones con TODO)
└── tests/    ← 13 tests que comprueban tu trabajo
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

- **R1.** Añade una segunda tabla `categorias` y relaciónala con `productos` mediante una clave ajena.
- **R2.** Investiga `GROUP BY` y cuenta cuántos productos hay por categoría.
- **R3.** Exporta el contenido de la tabla a un CSV, reutilizando lo de la UD5.

---

## 12. Autoevaluación rápida

<details><summary>1. ¿Qué pasa si olvidas <code>commit()</code>?</summary>Los cambios no se guardan, aunque no dé ningún error.</details>
<details><summary>2. ¿Por qué usar <code>?</code> en vez de concatenar?</summary>Para evitar la inyección SQL.</details>
<details><summary>3. ¿Qué hace <code>UPDATE productos SET precio = 0</code> sin <code>WHERE</code>?</summary>Pone el precio a 0 en TODAS las filas.</details>
<details><summary>4. Diferencia entre <code>fetchall()</code> y <code>fetchone()</code>.</summary>El primero devuelve todas las filas; el segundo, solo la siguiente.</details>
<details><summary>5. ¿Para qué <code>IF NOT EXISTS</code>?</summary>Para que crear la tabla no falle si ya existe.</details>
<details><summary>6. ¿Qué devuelve <code>AVG</code> con la tabla vacía?</summary><code>None</code>: hay que contemplarlo.</details>

---

## 13. Glosario

| Término | Definición |
|---|---|
| **SGBD** | Sistema gestor de bases de datos. |
| **Tabla / fila / columna** | Estructura, registro y campo. |
| **Clave primaria** | Campo que identifica cada fila de forma única. |
| **SQL** | Lenguaje para consultar y manipular la base de datos. |
| **CRUD** | Crear, leer, actualizar y borrar. |
| **Cursor** | Objeto que ejecuta sentencias y recorre resultados. |
| **`commit`** | Confirma los cambios pendientes. |
| **Consulta parametrizada** | La que pasa los datos con `?` en vez de concatenarlos. |
| **Inyección SQL** | Ataque que aprovecha el SQL construido por concatenación. |

---

## 14. Cómo se evalúa esta unidad (RA6)

Examen **100 % práctico**: una aplicación que gestione datos en SQLite.

| # | Qué se valora | Cómo se mide | Puntos |
|:---:|---|---|:---:|
| 1 | **Que funcione el CRUD** | casos de prueba superados × 7 | **7,0** |
| 2 | **Consultas parametrizadas** | usa `?`, nunca concatenación | **1,0** |
| 3 | **Integridad** | `commit()` y conexiones cerradas | **1,0** |
| 4 | **Tipado y documentación** | `mypy` limpio y docstrings | **1,0** |
| | | **TOTAL** | **10** |

**Se supera con 5.** Concatenar la entrada del usuario en una sentencia SQL cuesta el punto 2 completo, aunque el programa funcione.
