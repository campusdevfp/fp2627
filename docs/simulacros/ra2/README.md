# Simulacro RA2 — Cálculos de un viaje

Una pequeña calculadora de viajes: combustible, coste, distancias y plazas. Practicas funciones con parámetros y el uso de un módulo de la librería estándar.

**Duración orientativa:** 45 min · **Entrega:** nada, es un ensayo

!!! tip "Para qué sirve esto"
    Es un **examen de mentira**: mismo formato, misma dificultad y misma rúbrica que el de
    verdad, pero **con los tests publicados**. Hazlo la sesión anterior al examen y llegarás
    con la mecánica rodada.

    El día del examen el proyecto vendrá **sin tests**: solo los docstrings y unos ejemplos.
    Por eso conviene que aquí te acostumbres a leer el docstring *antes* de mirar el test.

## Cómo trabajar

```bash
pip install -r requirements.txt
pytest
```

1. Abre `src/viajes.py`. Cada función lleva un **docstring** que dice qué debe hacer: esa es
   la especificación.
2. Escríbela, borra el `raise NotImplementedError` y vuelve a lanzar `pytest`.
3. Termina cuando esté **todo en verde** y `mypy src` diga *Success*.

!!! warning "Entrénate para el examen"
    Intenta resolver cada función **leyendo solo el docstring**. Mira el test únicamente
    cuando falle. Si te acostumbras a programar contra el test, el día del examen te faltará
    esa muleta.

## Qué se valora

Es la rúbrica real del examen, para que sepas dónde se van los puntos. **La nota sale
solo de los casos de prueba**, repartidos por apartados:

`nota del apartado = (casos superados ÷ casos del apartado) × puntos del apartado`

| # | Apartado | Casos | Puntos |
|:---:|---|:---:|:---:|
| **A** | `km_a_millas()` | 3 | **2,50** |
| **B** | `area_circulo()` | 3 | **2,50** |
| **C** | `hipotenusa()` | 3 | **2,50** |
| **D** | `media()` | 3 | **2,50** |
| | **TOTAL** | **12** | **10,00** |

El examen de verdad tiene esta misma estructura, con un módulo de la librería estándar entre lo que se
comprueba. Aquí tienes 18 casos publicados; en el examen no verás ninguno.

Obligatorio en la entrega, aunque no puntúe por separado: `mypy src` sin errores y cada
función con su docstring.

## Comandos útiles

```bash
pytest -x
pytest -k media
mypy src
```
