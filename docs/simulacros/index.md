# Simulacros de examen

Un **examen de mentira** por cada RA: mismo formato, misma dificultad y misma rúbrica que el
de verdad, pero **con los tests publicados**.

Hazlo la sesión anterior al examen. Así llegas con la mecánica rodada y el día de la prueba
no descubres nada nuevo: solo te falta la red de los tests.

| RA | Simulacro | Qué se evalúa | Tests | Descargar |
|:---:|---|---|:---:|:---:|
| **1** | [Cuenta de una cafetería](ra1/README.md) | constantes, conversión, operadores y formato | 22 | [descargar](simulacro-ra1.zip) |
| **2** | [Cálculos de un viaje](ra2/README.md) | funciones, parámetros y el módulo `math` | 18 | [descargar](simulacro-ra2.zip) |
| **3** | [Registro de pulsaciones](ra3/README.md) | condiciones, bucles y excepciones | 21 | [descargar](simulacro-ra3.zip) |
| **4** | [Catálogo de dispositivos](ra4/README.md) | `property`, herencia y sobrescritura | 14 | [descargar](simulacro-ra4.zip) |
| **5** | [Recetario en CSV y JSON](ra5/README.md) | ficheros, CSV, JSON y codificación | 13 | [descargar](simulacro-ra5.zip) |
| **6** | [Museo en SQLite](ra6/README.md) | CRUD y consultas parametrizadas | 11 | [descargar](simulacro-ra6.zip) |

## En qué se diferencian de los proyectos de unidad

| | Proyecto de unidad | Simulacro | Examen |
|---|---|---|---|
| Cuándo | durante toda la unidad | la sesión previa al examen | el día del examen |
| Duración | varias sesiones | 45–50 min | 45–50 min |
| Tests | sí, publicados | sí, publicados | **no** |
| Se califica | no | no | sí |

El proyecto de unidad es para **aprender**: es largo y lo haces con calma. El simulacro es
para **medirte**: mismo tamaño que el examen, contrarreloj, y al terminar sabes exactamente
qué nota habrías sacado.

## Cómo se trabaja

Igual que un proyecto normal:

```bash
pip install -r requirements.txt
pytest
```

!!! warning "Léelo antes de empezar"
    Resuelve cada función **leyendo solo su docstring**, y mira el test únicamente cuando
    falle. Si te acostumbras a programar mirando el test, el día del examen te faltará esa
    muleta: allí solo tendrás el docstring y unos pocos ejemplos.

## La rúbrica es la de verdad

| Concepto | Cómo se calcula |
|---|---|
| Nota de un apartado | (casos superados ÷ casos del apartado) × puntos del apartado |
| Nota del examen | suma de todos los apartados, sobre **10** |

Los puntos de cada apartado son **proporcionales a sus casos**, así que todos los casos
valen lo mismo. El reparto viene en el enunciado.

Cada simulacro trae su tabla de apartados, idéntica en formato a la del examen. Cuando
termines, aplícala y tendrás la nota que sacarías.

!!! tip "Si te sobra tiempo"
    Borra tu solución y vuelve a hacerla **sin mirar los tests**, solo con los docstrings.
    Es el mejor ensayo posible de lo que te vas a encontrar.
