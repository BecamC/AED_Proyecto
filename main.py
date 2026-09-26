from manim import *

config.background_color = "#111318"


class BFSContactos(Scene):

    def crear_nodo(self, texto, posicion, color=BLUE, radio=0.38):
        circulo = Circle(
            radius=radio,
            color=color,
            stroke_width=3
        )

        circulo.set_fill(color, opacity=0.15)
        circulo.move_to(posicion)

        etiqueta = Text(
            texto,
            font_size=24
        ).move_to(circulo)

        return VGroup(circulo, etiqueta)

    def crear_persona(self, codigo, nombre, posicion):
        circulo = Circle(
            radius=0.38,
            color=WHITE,
            stroke_width=3
        )

        circulo.set_fill(GRAY, opacity=0.20)
        circulo.move_to(posicion)

        codigo_texto = Text(
            codigo,
            font_size=21
        )

        if codigo_texto.width > circulo.width * 0.75:
            codigo_texto.scale_to_fit_width(circulo.width * 0.75)
        codigo_texto.move_to(circulo)

        nombre_texto = Text(
            nombre,
            font_size=20
        ).next_to(circulo, DOWN, buff=0.2)

        return VGroup(circulo, codigo_texto, nombre_texto)

    def crear_arista(self, nodo1, nodo2, color=GRAY):
        linea = Line(
            nodo1[0].get_center(),
            nodo2[0].get_center(),
            buff=0.40,
            color=color,
            stroke_width=3
        )

        linea.set_z_index(-1)

        return linea

    def construct(self):

        titulo = Text(
            "BFS: Busqueda en Amplitud",
            font_size=48,
            color=BLUE
        )

        subtitulo = Text(
            "Rastreo de contactos: del problema a la solucion",
            font_size=27
        ).next_to(titulo, DOWN)

        autores = Text(
            "Alonso Benites  -  Miguel Ucañani  -  David Ortiz",
            font_size=22
        ).next_to(subtitulo, DOWN, buff=0.4)

        self.play(
            FadeIn(titulo),
            run_time=1.5
        )

        self.wait(6)

        self.play(
            FadeIn(subtitulo),
            FadeIn(autores),
            run_time=1
        )

        self.wait(5)

        self.play(
            titulo.animate.scale(0.70).to_edge(UP),
            FadeOut(subtitulo),
            FadeOut(autores),
            run_time=1.5
        )

        self.wait(1)


        seccion_problema = Text(
            "El problema: rastreo de contactos",
            font_size=30,
            color=RED
        ).next_to(titulo, DOWN, buff=0.5)

        self.play(
            FadeIn(seccion_problema),
            run_time=1
        )

        problema = Text(
            "Se detecta un caso de gripe y queremos rastrear\n"
            "sus contactos directos y los contactos de estos.",
            font_size=27,
            line_spacing=1.3
        ).move_to(ORIGIN)

        self.play(
            Write(problema),
            run_time=1.5
        )

        self.wait(5)

        problema2 = Text(
            "¿Como los encontramos a todos de forma ordenada,\n"
            "sin repetir y sin saltarnos a nadie?",
            font_size=27,
            color=YELLOW,
            line_spacing=1.3
        ).move_to(problema)

        self.play(
            Transform(problema, problema2),
            run_time=1
        )

        self.wait(5)

        respuesta = Text(
            "La respuesta: BFS (Busqueda en Amplitud).",
            font_size=28,
            color=BLUE
        ).move_to(problema)

        self.play(
            Transform(problema, respuesta),
            run_time=1
        )

        self.wait(4)

        self.play(
            FadeOut(problema),
            FadeOut(seccion_problema),
            run_time=1
        )


        seccion = Text(
            "¿Que es BFS?",
            font_size=32,
            color=YELLOW
        ).next_to(titulo, DOWN, buff=0.5)

        self.play(
            FadeIn(seccion),
            run_time=1
        )

        definicion = Text(
            "BFS recorre un grafo explorando primero\n"
            "los nodos mas cercanos al nodo inicial.",
            font_size=29,
            line_spacing=1.3
        ).move_to(ORIGIN)

        self.play(
            Write(definicion),
            run_time=1.5
        )

        self.wait(8)

        concepto = Text(
            "Grafo = vertices (nodos) + aristas (conexiones)",
            font_size=29,
            color=GREEN
        ).move_to(definicion)

        self.play(
            Transform(definicion, concepto),
            run_time=1
        )

        self.wait(5)

        self.play(
            FadeOut(definicion),
            FadeOut(seccion),
            run_time=1
        )

        titulo_grafo = Text(
            "Ejemplo de un grafo",
            font_size=30,
            color=YELLOW
        ).next_to(titulo, DOWN, buff=0.35)

        self.play(FadeIn(titulo_grafo), run_time=1)

        nodos = {}

        nodos["A"] = self.crear_nodo(
            "A", [-2.4, 1.5, 0]
        )

        nodos["B"] = self.crear_nodo(
            "B", [-4.2, 0.2, 0]
        )

        nodos["C"] = self.crear_nodo(
            "C", [-0.6, 0.2, 0]
        )

        nodos["D"] = self.crear_nodo(
            "D", [-5.0, -1.4, 0]
        )

        nodos["E"] = self.crear_nodo(
            "E", [-3.2, -1.4, 0]
        )

        nodos["F"] = self.crear_nodo(
            "F", [-0.6, -1.4, 0]
        )

        nodos["G"] = self.crear_nodo(
            "G", [-3.2, -2.7, 0]
        )

        aristas = []

        aristas.append(
            self.crear_arista(nodos["A"], nodos["B"])
        )

        aristas.append(
            self.crear_arista(nodos["A"], nodos["C"])
        )

        aristas.append(
            self.crear_arista(nodos["B"], nodos["D"])
        )

        aristas.append(
            self.crear_arista(nodos["B"], nodos["E"])
        )

        aristas.append(
            self.crear_arista(nodos["C"], nodos["F"])
        )

        aristas.append(
            self.crear_arista(nodos["E"], nodos["G"])
        )

        self.play(
            *[Create(a) for a in aristas],
            run_time=2
        )

        self.play(
            *[FadeIn(n) for n in nodos.values()],
            run_time=2
        )

        self.wait(5)

        explicacion = Text(
            "BFS comienza en un nodo y avanza nivel por nivel.",
            font_size=25
        )

        explicacion.to_edge(RIGHT)
        explicacion.shift(UP * 1.4)

        explicacion.scale_to_fit_width(5)

        self.play(
            Write(explicacion),
            run_time=1
        )

        self.wait(5)

        self.play(
            FadeOut(explicacion),
            run_time=1
        )

        pasos_titulo = Text(
            "Pasos de BFS",
            font_size=28,
            color=YELLOW
        ).move_to([3.6, 1.6, 0])

        self.play(
            FadeIn(pasos_titulo),
            run_time=1
        )

        paso1 = Text(
            "1. Elegir nodo inicial",
            font_size=22
        ).move_to([3.6, 0.8, 0])

        paso2 = Text(
            "2. Marcarlo visitado",
            font_size=22
        ).next_to(paso1, DOWN, buff=0.35)

        paso3 = Text(
            "3. Agregar vecinos a la cola",
            font_size=22
        ).next_to(paso2, DOWN, buff=0.35)

        paso4 = Text(
            "4. Repetir hasta terminar",
            font_size=22
        ).next_to(paso3, DOWN, buff=0.35)

        self.play(FadeIn(paso1), run_time=1)
        self.wait(3.5)

        self.play(FadeIn(paso2), run_time=1)
        self.wait(3.5)

        self.play(FadeIn(paso3), run_time=1)
        self.wait(3.5)

        self.play(FadeIn(paso4), run_time=1)
        self.wait(3.5)

        self.play(
            FadeOut(pasos_titulo),
            FadeOut(paso1),
            FadeOut(paso2),
            FadeOut(paso3),
            FadeOut(paso4),
            run_time=1
        )

        caja_cola = RoundedRectangle(
            width=4.2,
            height=1.5,
            corner_radius=0.15,
            color=WHITE
        )

        caja_cola.move_to([3.5, 0.3, 0])

        titulo_cola = Text(
            "Cola FIFO",
            font_size=25,
            color=YELLOW
        ).next_to(caja_cola, UP)

        cola = Text(
            "[ A ]",
            font_size=28
        ).move_to(caja_cola)

        self.play(
            Create(caja_cola),
            FadeIn(titulo_cola),
            Write(cola),
            run_time=1.5
        )

        self.wait(3.5)

        nivel = Text(
            "Nivel 0",
            font_size=24,
            color=YELLOW
        ).next_to(caja_cola, DOWN)

        self.play(
            nodos["A"][0].animate.set_fill(
                YELLOW,
                opacity=0.8
            ),
            FadeIn(nivel),
            run_time=1
        )

        self.wait(4)

        cola_1 = Text(
            "[ B, C ]",
            font_size=28
        ).move_to(cola)

        nivel_1 = Text(
            "Nivel 1",
            font_size=24,
            color=BLUE
        ).move_to(nivel)

        self.play(
            Transform(cola, cola_1),
            Transform(nivel, nivel_1),

            nodos["B"][0].animate.set_fill(
                BLUE,
                opacity=0.8
            ),

            nodos["C"][0].animate.set_fill(
                BLUE,
                opacity=0.8
            ),

            run_time=1.5
        )

        self.wait(5)

        cola_2 = Text(
            "[ D, E, F ]",
            font_size=28
        ).move_to(cola)

        nivel_2 = Text(
            "Nivel 2",
            font_size=24,
            color=GREEN
        ).move_to(nivel)

        self.play(
            Transform(cola, cola_2),
            Transform(nivel, nivel_2),

            nodos["D"][0].animate.set_fill(
                GREEN,
                opacity=0.8
            ),

            nodos["E"][0].animate.set_fill(
                GREEN,
                opacity=0.8
            ),

            nodos["F"][0].animate.set_fill(
                GREEN,
                opacity=0.8
            ),

            run_time=1.5
        )

        self.wait(5)

        cola_3 = Text(
            "[ G ]",
            font_size=28
        ).move_to(cola)

        nivel_3 = Text(
            "Nivel 3",
            font_size=24,
            color=RED
        ).move_to(nivel)

        self.play(
            Transform(cola, cola_3),
            Transform(nivel, nivel_3),

            nodos["G"][0].animate.set_fill(
                RED,
                opacity=0.8
            ),

            run_time=1.5
        )

        self.wait(5)

        orden = Text(
            "Orden: A -> B -> C -> D -> E -> F -> G",
            font_size=23,
            color=YELLOW
        ).to_edge(DOWN)

        self.play(
            Write(orden),
            run_time=1
        )

        self.wait(5)

        complejidad = Text(
            "Complejidad: O(V + E)",
            font_size=26,
            color=GREEN
        ).move_to([3.5, -2.2, 0])

        self.play(
            FadeIn(complejidad),
            run_time=1
        )

        self.wait(5)

        mensaje_teoria = Text(
            "BFS explora primero los nodos mas cercanos.",
            font_size=27,
            color=BLUE
        ).to_edge(DOWN)

        self.play(
            Transform(orden, mensaje_teoria),
            run_time=1
        )

        self.wait(6)

        elementos_teoria = [
            titulo,
            titulo_grafo,
            caja_cola,
            titulo_cola,
            cola,
            nivel,
            orden,
            complejidad
        ]

        elementos_teoria += aristas
        elementos_teoria += list(nodos.values())

        self.play(
            *[FadeOut(x) for x in elementos_teoria],
            run_time=1.5
        )


        titulo_aplicacion = Text(
            "Rastreo de contactos usando BFS",
            font_size=35,
            color=RED
        ).to_edge(UP)

        self.play(
            FadeIn(titulo_aplicacion),
            run_time=1
        )

        recordatorio = Text(
            "Volvamos al caso inicial y resolvamoslo con BFS.",
            font_size=27,
            color=YELLOW
        ).move_to(ORIGIN)

        self.play(
            Write(recordatorio),
            run_time=1.5
        )

        self.wait(4)

        self.play(
            FadeOut(recordatorio),
            run_time=1
        )


        personas = {}

        personas["P0"] = self.crear_persona(
            "root",
            "Paciente 0",
            [0, 1.7, 0]
        )

        personas["A"] = self.crear_persona(
            "A",
            "Ana",
            [-4.3, 0.3, 0]
        )

        personas["B"] = self.crear_persona(
            "B",
            "Bruno",
            [0, 0.3, 0]
        )

        personas["C"] = self.crear_persona(
            "C",
            "Carla",
            [4.3, 0.3, 0]
        )

        personas["D"] = self.crear_persona(
            "D",
            "Diego",
            [-5.3, -1.4, 0]
        )

        personas["E"] = self.crear_persona(
            "E",
            "Elena",
            [-3.2, -1.4, 0]
        )

        personas["F"] = self.crear_persona(
            "F",
            "Fabio",
            [0, -1.4, 0]
        )

        personas["G"] = self.crear_persona(
            "G",
            "Gabriela",
            [3.5, -1.4, 0]
        )

        personas["H"] = self.crear_persona(
            "H",
            "Hugo",
            [4.8, -2.7, 0]
        )

        contactos = {}

        contactos[("P0", "A")] = self.crear_arista(
            personas["P0"],
            personas["A"]
        )

        contactos[("P0", "B")] = self.crear_arista(
            personas["P0"],
            personas["B"]
        )

        contactos[("P0", "C")] = self.crear_arista(
            personas["P0"],
            personas["C"]
        )

        contactos[("A", "D")] = self.crear_arista(
            personas["A"],
            personas["D"]
        )

        contactos[("A", "E")] = self.crear_arista(
            personas["A"],
            personas["E"]
        )

        contactos[("B", "F")] = self.crear_arista(
            personas["B"],
            personas["F"]
        )

        contactos[("C", "G")] = self.crear_arista(
            personas["C"],
            personas["G"]
        )

        contactos[("G", "H")] = self.crear_arista(
            personas["G"],
            personas["H"]
        )

        self.play(
            FadeIn(personas["P0"]),
            run_time=1
        )

        self.wait(1)

        significado = Text(
            "Nodo = persona       Arista = contacto",
            font_size=23,
            color=YELLOW
        )

        significado.next_to(
            titulo_aplicacion,
            DOWN,
            buff=0.2
        )

        self.play(
            FadeIn(significado),
            run_time=1
        )

        self.wait(3)

        estado = Text(
            "Cola: [Paciente 0]",
            font_size=25,
            color=WHITE
        )

        estado.next_to(
            significado,
            DOWN,
            buff=0.15
        )

        self.play(
            FadeIn(estado),
            run_time=1.2
        )

        self.wait(2)

        nivel0 = Text(
            "Nivel 0",
            font_size=22,
            color=RED
        ).to_edge(LEFT).shift(UP * 2.6)

        raiz_texto = Text(
            "El nodo inicial es la raiz (root):\n"
            "el punto de partida de la busqueda.",
            font_size=22,
            color=RED,
            line_spacing=1.1
        ).to_edge(DOWN)

        self.play(
            personas["P0"][0].animate.set_fill(RED, opacity=0.85),
            personas["P0"][0].animate.set_stroke(RED),
            FadeIn(nivel0),
            FadeIn(raiz_texto),
            run_time=1
        )

        self.wait(4)

        self.play(
            FadeOut(raiz_texto),
            run_time=0.8
        )

        aristas_n1 = [
            contactos[("P0", "A")],
            contactos[("P0", "B")],
            contactos[("P0", "C")],
        ]

        for a in aristas_n1:
            a.set_color(YELLOW).set_stroke(width=7)

        self.play(
            *[Create(a) for a in aristas_n1],
            *[FadeIn(personas[k]) for k in ["A", "B", "C"]],
            run_time=1.2
        )

        estado1 = Text(
            "Cola: [Ana, Bruno, Carla]",
            font_size=25
        ).move_to(estado)

        nivel1 = Text(
            "Nivel 1",
            font_size=22,
            color=BLUE
        ).move_to(nivel0)

        self.play(
            Transform(estado, estado1),
            Transform(nivel0, nivel1),

            personas["A"][0].animate.set_fill(BLUE, opacity=0.85),
            personas["B"][0].animate.set_fill(BLUE, opacity=0.85),
            personas["C"][0].animate.set_fill(BLUE, opacity=0.85),

            run_time=1.5
        )

        self.wait(4)


        self.play(
            *[a.animate.set_color(GRAY).set_stroke(width=3) for a in aristas_n1],
            run_time=0.8
        )

        aristas_n2 = [
            contactos[("A", "D")],
            contactos[("A", "E")],
            contactos[("B", "F")],
            contactos[("C", "G")],
        ]

        for a in aristas_n2:
            a.set_color(YELLOW).set_stroke(width=7)

        self.play(
            *[Create(a) for a in aristas_n2],
            *[FadeIn(personas[k]) for k in ["D", "E", "F", "G"]],
            run_time=1.2
        )

        estado2 = Text(
            "Cola: [Diego, Elena, Fabio, Gabriela]",
            font_size=22
        ).move_to(estado)

        nivel2 = Text(
            "Nivel 2",
            font_size=22,
            color=GREEN
        ).move_to(nivel0)

        self.play(
            Transform(estado, estado2),
            Transform(nivel0, nivel2),

            personas["D"][0].animate.set_fill(GREEN, opacity=0.85),
            personas["E"][0].animate.set_fill(GREEN, opacity=0.85),
            personas["F"][0].animate.set_fill(GREEN, opacity=0.85),
            personas["G"][0].animate.set_fill(GREEN, opacity=0.85),

            run_time=1.5
        )

        self.wait(4)

        self.play(
            FadeIn(personas["H"]),
            run_time=1
        )

        objetivo = SurroundingRectangle(
            personas["H"],
            color=RED,
            buff=0.15
        )

        self.play(
            Create(objetivo),
            run_time=1
        )

        self.wait(1)

        pregunta = Text(
            "¿Cuantos niveles necesitamos para llegar a Hugo?",
            font_size=26,
            color=YELLOW
        ).to_edge(DOWN)

        self.play(
            Write(pregunta),
            run_time=1
        )

        self.wait(5)

        self.play(
            *[a.animate.set_color(GRAY).set_stroke(width=3) for a in aristas_n2],
            run_time=0.8
        )

        aristas_n3 = [
            contactos[("G", "H")],
        ]

        for a in aristas_n3:
            a.set_color(YELLOW).set_stroke(width=7)

        self.play(
            *[Create(a) for a in aristas_n3],
            run_time=1
        )

        estado3 = Text(
            "Cola: [Hugo]",
            font_size=25
        ).move_to(estado)

        nivel3 = Text(
            "Nivel 3",
            font_size=22,
            color=RED
        ).move_to(nivel0)

        self.play(
            Transform(estado, estado3),
            Transform(nivel0, nivel3),

            personas["H"][0].animate.set_fill(RED, opacity=0.85),

            run_time=1.5
        )

        self.wait(5)

        self.play(
            FadeOut(pregunta),
            run_time=1
        )

        self.play(
            *[a.animate.set_color(GRAY).set_stroke(width=3) for a in aristas_n3],
            run_time=0.8
        )

        ruta_texto = Text(
            "Camino encontrado:",
            font_size=25,
            color=YELLOW
        ).to_edge(DOWN)

        self.play(
            FadeIn(ruta_texto),
            run_time=1
        )

        self.play(
            contactos[("P0", "C")].animate.set_color(
                YELLOW
            ).set_stroke(width=7),
            run_time=1
        )

        self.wait(1)

        self.play(
            contactos[("C", "G")].animate.set_color(
                YELLOW
            ).set_stroke(width=7),
            run_time=1
        )

        self.wait(1)

        self.play(
            contactos[("G", "H")].animate.set_color(
                YELLOW
            ).set_stroke(width=7),
            run_time=1
        )

        self.wait(2)

        camino = Text(
            "Paciente 0 -> Carla -> Gabriela -> Hugo",
            font_size=25,
            color=YELLOW
        ).move_to(ruta_texto)

        self.play(
            Transform(ruta_texto, camino),
            run_time=1.5
        )

        self.wait(6)

        distancia = Text(
            "Hugo esta a 3 niveles del paciente cero.",
            font_size=29,
            color=GREEN
        ).to_edge(DOWN)

        self.play(
            Transform(ruta_texto, distancia),
            run_time=1
        )

        self.wait(6)

        explicacion1 = Text(
            "BFS no salta niveles.",
            font_size=29,
            color=BLUE
        ).to_edge(DOWN)

        self.play(
            Transform(ruta_texto, explicacion1),
            run_time=1
        )

        self.wait(6)

        explicacion2 = Text(
            "Primero revisa los contactos mas cercanos.",
            font_size=27,
            color=BLUE
        ).move_to(ruta_texto)

        self.play(
            Transform(ruta_texto, explicacion2),
            run_time=1.5
        )

        self.wait(6)

        explicacion3 = Text(
            "En un grafo no ponderado, BFS permite encontrar\n"
            "el camino con menor numero de aristas.",
            font_size=25,
            color=GREEN,
            line_spacing=1.2
        ).move_to(ruta_texto)

        self.play(
            Transform(ruta_texto, explicacion3),
            run_time=1
        )

        self.wait(5)

        todo_aplicacion = [
            titulo_aplicacion,
            significado,
            estado,
            nivel0,
            ruta_texto,
            objetivo
        ]

        todo_aplicacion += list(personas.values())
        todo_aplicacion += list(contactos.values())

        self.play(
            *[
                FadeOut(x)
                for x in todo_aplicacion
            ],
            run_time=1.5
        )

        conclusion = Text(
            "Conclusiones",
            font_size=45,
            color=YELLOW
        ).to_edge(UP)

        self.play(
            FadeIn(conclusion),
            run_time=1
        )

        self.wait(3)

        punto1 = Text(
            "BFS recorre un grafo nivel por nivel.",
            font_size=28
        ).shift(UP * 1.2)

        self.play(
            FadeIn(punto1),
            run_time=1
        )

        self.wait(3)

        punto2 = Text(
            "Utiliza una cola FIFO para organizar la busqueda.",
            font_size=28
        ).next_to(punto1, DOWN, buff=0.6)

        self.play(
            FadeIn(punto2),
            run_time=1
        )

        self.wait(3)

        punto3 = Text(
            "Puede aplicarse al rastreo de contactos.",
            font_size=28
        ).next_to(punto2, DOWN, buff=0.6)

        self.play(
            FadeIn(punto3),
            run_time=1
        )

        self.wait(3)

        final = Text(
            "BFS: explorar primero lo mas cercano",
            font_size=35,
            color=BLUE
        ).to_edge(DOWN)

        self.play(
            Write(final),
            run_time=1
        )

        self.wait(7)