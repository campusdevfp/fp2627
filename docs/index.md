# CMO-313 · Fundamentos de programación

Materiales del módulo: **6 unidades**, una por cada Resultado de Aprendizaje. Puedes consultarlos online u offline.

## Unidades

| | Unidad | Qué aprendes | Horas |
|:---:|---|---|:---:|
| **1** | [Estructura del programa](ud1/index.md) | Variables, tipos, operadores, conversión, Python tipado | 8 h |
| **2** | [Funciones y librerías](ud2/index.md) | Dividir el problema en funciones y reutilizar código | 8 h |
| **3** | [Control y excepciones](ud3/index.md) | Decidir, repetir y no romperse con datos raros | 12 h |
| **4** | [Orientación a objetos](ud4/index.md) | Clases, objetos, encapsulación y herencia | 8 h |
| **5** | [Entrada/salida y ficheros](ud5/index.md) | Que los datos sobrevivan al cerrar el programa | 6 h |
| **6** | [Bases de datos](ud6/index.md) | SQLite y las cuatro operaciones CRUD | 8 h |

Las unidades van en orden: cada una se apoya en la anterior.

## Recursos

- **[Entorno de trabajo](recursos/entorno.md)** — chuleta de entornos virtuales, `pip` y `mypy`.
- **[Proyectos](proyectos/index.md)** — los **6 proyectos base** con sus tests, uno por unidad.
- **[Todo el material en una página](completo.md)** — para leer del tirón o exportar a PDF.

## Cómo se trabaja cada unidad

1. El profesor **explica** el concepto y ejecuta los ejemplos en clase.
2. Tú **lees** el apartado y **ejecutas los ejemplos** en tu ordenador.
3. Haces los **retos rápidos** que van apareciendo entre la teoría.
4. Practicas con **ejercicios que tienen la solución desplegable** — para ver el patrón.
5. Trabajas el **proyecto de la unidad**: escribes el código en `src/` y ejecutas `pytest` hasta tenerlo todo en verde.
6. **Examen práctico**, con la misma mecánica del paso 5.

!!! warning "La solución no es el objetivo"
    Leer una solución da sensación de haber aprendido, pero no enseña. Si la abres sin haberlo intentado, el ejercicio no ha servido de nada. Atáscate primero: ahí está el aprendizaje.

## Cómo se evalúa

Cada unidad corresponde a un **Resultado de Aprendizaje** y se evalúa con un **examen 100 % práctico**: escribes código y se ejecuta contra una batería de tests, igual que en los proyectos. La nota sale de los tests superados más unos criterios cerrados que conoces desde el primer día, así que es objetiva.

Cada unidad explica su rúbrica exacta en su última sección.

## Uso offline

Descarga la carpeta `site/` (o genérala con `mkdocs build`) y abre `site/index.html`. Todo funciona sin conexión, incluidos los diagramas y la búsqueda.

!!! tip "Herramientas que usarás"
    Python 3 · Visual Studio Code · `pytest` (pruebas) · `mypy` (tipos) · SQLite (UD6)
