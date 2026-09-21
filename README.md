# BFS: Búsqueda en Amplitud aplicada al rastreo de contactos

Proyecto 1 — Animando Estructuras de Datos
**CS2023 · Algoritmos y Estructuras de Datos · UNIVERSIDAD DE INGENIERÍA Y TECNOLOGÍA**

## Descripción del proyecto

Este proyecto es una animación creada con [Manim](https://www.manim.community/) que
ilustra, paso a paso, el algoritmo **BFS (Breadth-First Search / Búsqueda en Amplitud)**
sobre un grafo. La animación tiene dos partes:

1. **Parte teórica:** qué es BFS, cómo recorre un grafo nivel por nivel usando una
   cola FIFO, el orden de visita de los nodos y su complejidad.
2. **Aplicación práctica:** un caso de *rastreo de contactos* de una enfermedad, donde
   cada persona es un nodo y cada contacto una arista. Se usa BFS para encontrar a qué
   "nivel" de distancia está cada persona respecto al paciente cero.

## Autores

| Nombre y Apellido | Contribución |
|---|---|
| Alonso Aarón Benites Camacho | código y informes |
| Miguel Fernando Ucañani Tintaya | código |
| David Alonso Ortiz Palomino | código |

## El algoritmo: BFS (Búsqueda en Amplitud)

BFS es un algoritmo para recorrer o buscar en un grafo. Parte de un nodo inicial y
explora **primero todos los vecinos más cercanos** antes de avanzar al siguiente nivel.
Para lograrlo utiliza una **cola FIFO** (el primero en entrar es el primero en salir):

1. Se elige un nodo inicial y se marca como visitado.
2. Se agregan sus vecinos a la cola.
3. Se saca el siguiente nodo de la cola, se marca como visitado y se encolan sus
   vecinos no visitados.
4. Se repite hasta que la cola quede vacía.

En un grafo **no ponderado**, BFS garantiza encontrar el camino con el **menor número
de aristas** entre el nodo inicial y cualquier otro nodo.

- **Complejidad temporal:** `O(V + E)` (V = vértices, E = aristas)
- **Complejidad espacial:** `O(V)`

## Software requerido

- **Python** 3.9 o superior
- **Manim Community Edition** (v0.18 o superior)
- **FFmpeg** (para exportar el video)
- **LaTeX** (opcional, solo si se usan fórmulas con `MathTex`/`Tex`)

Instalación de dependencias de Python:

```bash
pip install manim
```

> En Windows/macOS/Linux, revisa la [guía oficial de instalación de Manim](https://docs.manim.community/en/stable/installation.html)
> para instalar FFmpeg y (si hace falta) LaTeX.

## Cómo compilar y ejecutar

Clona el repositorio y entra a la carpeta:

```bash
git clone https://github.com/BecamC/AED_Proyecto.git
cd AED_Proyecto
```

Renderiza la animación en **alta resolución (1080p, 60 fps)**:

```bash
manim -qh main.py BFSContactos
```

Opciones útiles de calidad:

| Comando | Calidad | Uso |
|---|---|---|
| `manim -ql main.py BFSContactos` | Baja (480p) | Pruebas rápidas |
| `manim -qm main.py BFSContactos` | Media (720p) | Revisión |
| `manim -qh main.py BFSContactos` | Alta (1080p) | **Entrega final** |

El video generado se guarda en la carpeta `media/videos/main/1080p60/`.

## Video demo

🎬 Link del video: <URL_DE_YOUTUBE>

## Estructura del repositorio

```
.
├── main.py        # Código de la animación en Manim
└── README.md      # Este archivo
```
