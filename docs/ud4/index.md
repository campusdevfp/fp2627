# Unidad 4 · Fundamentos de la programación orientada a objetos

> **Módulo:** CMO-313 · Fundamentos de programación
> **Resultado de aprendizaje:** RA4 · **Duración:** 8 h · **Peso:** 15 %
> **Lenguaje:** Python 3 (tipado)

Hasta ahora has separado el programa en **funciones** (acciones) y has guardado los datos en variables sueltas. La programación orientada a objetos (POO) da un paso más: **junta los datos y las acciones que operan sobre ellos** en una sola pieza, el objeto.

Es el modelo con el que están escritos casi todos los programas grandes, y el que usarás en segundo curso constantemente.

---

## Mapa de la unidad

<figure markdown>
  ![Mapa de la unidad 4](../assets/diagramas/ud4-mapa.svg#only-light)
  ![Mapa de la unidad 4](../assets/diagramas/ud4-mapa-dark.svg#only-dark)
  <figcaption>Una clase define cómo son los objetos; la herencia permite especializarla.</figcaption>
</figure>

### Qué vas a saber hacer al terminar

- [ ] Distinguir **clase** de **objeto**.
- [ ] Definir una clase con `__init__`, atributos y métodos.
- [ ] Entender qué es `self` y por qué está en todos los métodos.
- [ ] Controlar el acceso a los atributos (**encapsulación**) con `property`.
- [ ] Crear clases derivadas mediante **herencia** y usar `super()`.
- [ ] Sobrescribir métodos y definir `__str__`.

---

## 1. Clase y objeto

Una **clase** es un molde: describe qué datos tiene algo y qué sabe hacer. Un **objeto** es cada ejemplar concreto creado a partir de ese molde.

> 🧠 **Analogía.** La clase es el **plano de un piso**; los objetos son los pisos construidos con ese plano. Todos comparten la estructura, pero cada uno tiene sus propios muebles.

```python
class Coche:
    pass

mi_coche = Coche()          # un objeto
otro_coche = Coche()        # otro objeto distinto
```

| Concepto | Qué es | Ejemplo |
|---|---|---|
| **Clase** | El molde | `Coche` |
| **Objeto / instancia** | Un ejemplar | `mi_coche` |
| **Atributo** | Un dato del objeto | `marca`, `velocidad` |
| **Método** | Una acción del objeto | `describir()`, `acelerar()` |

---

## 2. Atributos y `__init__`

`__init__` es el **constructor**: se ejecuta automáticamente al crear el objeto y sirve para darle sus datos iniciales.

```python
class Coche:
    def __init__(self, marca: str, velocidad: int) -> None:
        self.marca = marca              # atributo del objeto
        self.velocidad = velocidad

mi_coche = Coche("Seat", 120)
print(mi_coche.marca)        # Seat
print(mi_coche.velocidad)    # 120
```

### 2.1 Qué es `self`

`self` es **el propio objeto**. Python lo pasa automáticamente como primer parámetro de todos los métodos, para que dentro sepas sobre qué objeto trabajas.

```python
mi_coche = Coche("Seat", 120)     # self será mi_coche
otro = Coche("Ford", 90)          # aquí self será otro
```

Por eso `self.marca` significa «la marca **de este** objeto».

!!! warning "Los tres errores de `self`"
    ```python
    class Coche:
        def __init__(marca):          # ❌ falta self
            self.marca = marca

        def describir(self) -> str:
            return marca              # ❌ falta self. delante

    mi_coche.describir(mi_coche)      # ❌ self no se pasa a mano
    ```
    Lo correcto: `def __init__(self, marca)`, `return self.marca`, y llamar `mi_coche.describir()`.

> 🎯 **Reto rápido 1.** Crea una clase `Alumno` con atributos `nombre` y `nota`, y crea dos objetos.

---

## 3. Métodos

Un **método** es una función definida dentro de la clase. Siempre lleva `self` como primer parámetro.

```python
class Coche:
    def __init__(self, marca: str, velocidad: int) -> None:
        self.marca = marca
        self.velocidad = velocidad

    def describir(self) -> str:
        """Devuelve una descripción del coche."""
        return f"Coche {self.marca} a {self.velocidad} km/h"

    def acelerar(self, incremento: int) -> None:
        """Aumenta la velocidad."""
        self.velocidad = self.velocidad + incremento


mi_coche = Coche("Seat", 120)
print(mi_coche.describir())      # Coche Seat a 120 km/h
mi_coche.acelerar(20)
print(mi_coche.velocidad)        # 140
```

!!! tip "Métodos que consultan y métodos que modifican"
    `describir()` **devuelve** información (`-> str`).
    `acelerar()` **cambia** el objeto y no devuelve nada (`-> None`).
    Conviene no mezclar ambas cosas en un mismo método.

### 3.1 `__str__`: cómo se ve el objeto

Sin `__str__`, imprimir un objeto da algo ilegible:

```python
print(mi_coche)     # <__main__.Coche object at 0x7f8b1c0>
```

Definiéndolo, decides tú qué se muestra:

```python
class Coche:
    def __init__(self, marca: str) -> None:
        self.marca = marca

    def __str__(self) -> str:
        return f"Coche {self.marca}"

print(Coche("Seat"))     # Coche Seat
```

> 🎯 **Reto rápido 2.** Añade a `Alumno` un método `aprueba(self) -> bool` que indique si su nota es ≥ 5.

---

## 4. Encapsulación: proteger los datos

Por defecto cualquiera puede tocar los atributos, incluso poniendo valores absurdos:

```python
mi_coche.velocidad = -500      # 😱 nadie lo impide
```

**Encapsular** es controlar cómo se accede a los datos del objeto.

### 4.1 La convención del guion bajo

En Python no existen atributos verdaderamente privados; se usa una **convención**:

| Nombre | Significado |
|---|---|
| `velocidad` | público: cualquiera puede usarlo |
| `_velocidad` | «uso interno, no lo toques desde fuera» |
| `__velocidad` | Python le cambia el nombre para dificultar el acceso |

### 4.2 `property`: la forma correcta

Permite validar al asignar, manteniendo una sintaxis cómoda:

```python
class Coche:
    def __init__(self, marca: str, velocidad: int) -> None:
        self.marca = marca
        self._velocidad = 0
        self.velocidad = velocidad      # pasa por el setter y valida

    @property
    def velocidad(self) -> int:
        """Velocidad actual en km/h."""
        return self._velocidad

    @velocidad.setter
    def velocidad(self, valor: int) -> None:
        if valor < 0:
            raise ValueError("La velocidad no puede ser negativa")
        self._velocidad = valor


coche = Coche("Seat", 120)
print(coche.velocidad)        # 120   (llama al getter)
coche.velocidad = 140         # ✅     (llama al setter y valida)
coche.velocidad = -10         # ❌ ValueError
```

Lo bueno: **quien usa la clase no nota nada**, sigue escribiendo `coche.velocidad`. Pero ahora es imposible dejar el objeto en un estado inválido.

> 🎯 **Reto rápido 3.** Protege la `nota` de `Alumno` para que solo admita valores entre 0 y 10.

---

## 5. Herencia

La **herencia** permite crear una clase nueva a partir de otra, aprovechando lo que ya tiene y añadiendo o cambiando lo que haga falta.

```python
class Vehiculo:
    def __init__(self, marca: str, velocidad: int) -> None:
        self.marca = marca
        self.velocidad = velocidad

    def describir(self) -> str:
        return f"Vehículo {self.marca} a {self.velocidad} km/h"


class Coche(Vehiculo):          # Coche hereda de Vehiculo
    def describir(self) -> str:  # sobrescribe el método
        return f"Coche {self.marca} a {self.velocidad} km/h"


class Moto(Vehiculo):
    def describir(self) -> str:
        return f"Moto {self.marca} a {self.velocidad} km/h"


print(Coche("Seat", 120).describir())    # Coche Seat a 120 km/h
print(Moto("Honda", 90).describir())     # Moto Honda a 90 km/h
```

`Coche` y `Moto` **no repiten** el `__init__`: lo heredan de `Vehiculo`.

Vocabulario: `Vehiculo` es la clase **base** (o padre); `Coche` y `Moto` son **derivadas** (o hijas). **Sobrescribir** es redefinir en la hija un método que ya existía en la madre.

### 5.1 `super()`: reutilizar lo de la clase base

Cuando la hija necesita añadir algo pero también quiere lo de la madre:

```python
class Camion(Vehiculo):
    def __init__(self, marca: str, velocidad: int, carga: float) -> None:
        super().__init__(marca, velocidad)     # ejecuta el __init__ de Vehiculo
        self.carga = carga                      # y añade lo suyo

    def describir(self) -> str:
        base = super().describir()              # aprovecha el texto de la madre
        return f"{base} con {self.carga} t de carga"
```

!!! tip "Cuándo usar herencia"
    Solo cuando puedas decir «**X es un** Y»: un coche **es un** vehículo. Si lo que quieres decir es «X **tiene un** Y» (un coche tiene un motor), eso no es herencia: es un atributo.

> 🎯 **Reto rápido 4.** Crea `Bicicleta(Vehiculo)` que sobrescriba `describir()`.

---

## 6. Errores frecuentes

| Síntoma | Causa | Solución |
|---|---|---|
| `TypeError: __init__() takes 2 positional arguments but 3 were given` | falta `self` en la definición | `def __init__(self, ...)` |
| `NameError` dentro de un método | usaste `marca` en vez de `self.marca` | pon `self.` delante |
| `AttributeError: 'Coche' object has no attribute 'x'` | no se creó en `__init__` o hay una errata | créalo en el constructor |
| Al imprimir sale `<object at 0x…>` | falta `__str__` | defínelo |
| La clase hija pierde los atributos | olvidaste `super().__init__(...)` | llámalo al principio |
| El `property` entra en bucle infinito | dentro del setter asignas a `self.velocidad` | asigna a `self._velocidad` |

---

## 7. Practica **con** solución a la vista

### 7.1 Actividades guiadas

#### Actividad 1 — Tu primera clase
`Persona` con `nombre` y `edad`, y un método `saludar()` que devuelva `"Hola, soy Ada"`.
<details><summary>💡 Solución</summary>

```python
class Persona:
    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self.edad = edad

    def saludar(self) -> str:
        return f"Hola, soy {self.nombre}"

print(Persona("Ada", 36).saludar())
```
</details>

#### Actividad 2 — Método que modifica
Añade `cumplir_anios()` que sume 1 a la edad.
<details><summary>💡 Solución</summary>

```python
    def cumplir_anios(self) -> None:
        self.edad = self.edad + 1
```
</details>

#### Actividad 3 — Encapsular
Protege `edad` para que no admita valores negativos.
<details><summary>💡 Solución</summary>

```python
class Persona:
    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self._edad = 0
        self.edad = edad

    @property
    def edad(self) -> int:
        return self._edad

    @edad.setter
    def edad(self, valor: int) -> None:
        if valor < 0:
            raise ValueError("La edad no puede ser negativa")
        self._edad = valor
```
</details>

#### Actividad 4 — Herencia
`Empleado(Persona)` con un atributo `sueldo`, usando `super()`.
<details><summary>💡 Solución</summary>

```python
class Empleado(Persona):
    def __init__(self, nombre: str, edad: int, sueldo: float) -> None:
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def saludar(self) -> str:
        return f"Hola, soy {self.nombre} y cobro {self.sueldo} €"
```
</details>

### 7.2 Ejercicios propuestos

**E1 🟢 · Rectángulo.** Clase con `base` y `altura` y métodos `area()` y `perimetro()`.
<details><summary>Solución</summary>

```python
class Rectangulo:
    def __init__(self, base: float, altura: float) -> None:
        self.base = base
        self.altura = altura

    def area(self) -> float:
        return self.base * self.altura

    def perimetro(self) -> float:
        return 2 * (self.base + self.altura)
```
</details>

**E2 🟢 · Cuenta bancaria.** `saldo`, `ingresar(cantidad)` y `saldo_actual()`.
<details><summary>Solución</summary>

```python
class Cuenta:
    def __init__(self, saldo: float = 0.0) -> None:
        self.saldo = saldo

    def ingresar(self, cantidad: float) -> None:
        self.saldo += cantidad

    def saldo_actual(self) -> float:
        return self.saldo
```
</details>

**E3 🟡 · Retirar con control.** Añade `retirar(cantidad)` que lance `ValueError` si no hay saldo.
<details><summary>Solución</summary>

```python
    def retirar(self, cantidad: float) -> None:
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= cantidad
```
</details>

**E4 🟡 · `__str__`.** Haz que imprimir un `Rectangulo` muestre `"Rectangulo 4x3"`.
<details><summary>Solución</summary>

```python
    def __str__(self) -> str:
        return f"Rectangulo {self.base}x{self.altura}"
```
</details>

**E5 🔴 · Jerarquía de figuras.** `Figura` con `area()` que devuelva `0.0`, y `Circulo` y `Cuadrado` que la sobrescriban.
<details><summary>Solución</summary>

```python
import math

class Figura:
    def area(self) -> float:
        return 0.0

class Circulo(Figura):
    def __init__(self, radio: float) -> None:
        self.radio = radio
    def area(self) -> float:
        return math.pi * self.radio ** 2

class Cuadrado(Figura):
    def __init__(self, lado: float) -> None:
        self.lado = lado
    def area(self) -> float:
        return self.lado ** 2
```
</details>

---

## Proyecto de la unidad ⭐

Toda la práctica de esta unidad se hace sobre un **proyecto base**: una jerarquía de clases con encapsulación y herencia. Está montado
con la estructura real de un proyecto Python y trae una **batería de tests** que puedes
ejecutar en cualquier momento para ver si va todo bien.

**[Proyecto Flota de vehículos →](../proyectos/ud4/README.md)**

```
proyecto-ud4/
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

## 9. Retos opcionales 🚀

- **R1.** Añade `Camion(Vehiculo)` con carga, usando `super()` en `__init__` y en `describir()`.
- **R2.** Crea una lista de vehículos distintos y recórrela llamando a `describir()` en cada uno. Fíjate en que cada objeto responde a su manera: eso es **polimorfismo**.
- **R3.** Investiga `@dataclass` y reescribe `Rectangulo` con él.

---

## 10. Autoevaluación rápida

<details><summary>1. Diferencia entre clase y objeto.</summary>La clase es el molde; el objeto es un ejemplar creado con ese molde.</details>
<details><summary>2. ¿Qué es <code>self</code>?</summary>El propio objeto. Python lo pasa solo como primer parámetro de cada método.</details>
<details><summary>3. ¿Cuándo se ejecuta <code>__init__</code>?</summary>Automáticamente, al crear el objeto.</details>
<details><summary>4. ¿Para qué sirve <code>super()</code>?</summary>Para llamar a un método de la clase base desde la derivada.</details>
<details><summary>5. ¿Qué hace <code>__str__</code>?</summary>Define el texto que se muestra al imprimir el objeto.</details>
<details><summary>6. ¿Qué aporta <code>property</code>?</summary>Validar al leer o asignar un atributo sin cambiar la forma de usarlo.</details>

---

## 11. Glosario

| Término | Definición |
|---|---|
| **Clase** | Molde que define atributos y métodos. |
| **Objeto / instancia** | Ejemplar concreto de una clase. |
| **Atributo** | Dato asociado a un objeto. |
| **Método** | Función definida dentro de una clase. |
| **`self`** | Referencia al propio objeto. |
| **`__init__`** | Constructor: inicializa el objeto. |
| **Encapsulación** | Controlar el acceso a los datos internos. |
| **`property`** | Mecanismo para validar el acceso a un atributo. |
| **Herencia** | Crear una clase a partir de otra. |
| **Sobrescribir** | Redefinir en la hija un método de la madre. |

---

## 12. Cómo se evalúa esta unidad (RA4)

Examen **100 % práctico**: escribir una jerarquía de clases según una especificación.

| # | Qué se valora | Cómo se mide | Puntos |
|:---:|---|---|:---:|
| 1 | **Que las clases funcionen** | casos de prueba superados × 7 | **7,0** |
| 2 | **Herencia** | la clase derivada hereda y sobrescribe correctamente | **1,0** |
| 3 | **Encapsulación** | el atributo protegido valida de verdad | **1,0** |
| 4 | **Tipado y documentación** | `mypy` limpio y docstrings | **1,0** |
| | | **TOTAL** | **10** |

**Se supera con 5.** Los tests crean objetos y llaman a los métodos: respeta **exactamente** los nombres de clases, atributos y métodos del enunciado.
