from manim import *

class Teste(Scene):
    def construct(self):
        quadrado = Square(side_length=3, stroke_color=GREEN, fill_color=BLUE, fill_opacity=0.75)

        retangulo = Rectangle(height=2, width=3, color=PINK)

        self.play(FadeIn(quadrado), FadeIn(retangulo), run_time=2)

        self.wait(2)

        self.play(quadrado.animate.move_to(LEFT*3), retangulo.animate.move_to(RIGHT*3))

        #lambda serve para criar funções anônimas geralmente de única linha 
        # always_redraw recria o objeto visual a cada frame da animação

        seta_q_r = always_redraw( lambda: Line(start=quadrado.get_midpoint(), end=retangulo.get_midpoint(), buff=0.5).add_tip())

        #obs buff critério que usa para diminuir a seta 

        self.wait()

        self.play(Write(seta_q_r))

        self.play(quadrado.animate.move_to(DOWN*3))


        # axes cria um plano cartesiano simples
        ax = Axes()

        self.play(FadeIn(ax))

        self.clear()

        # funcao = MathTex(r'f(x)=2x^2-4x+6')

        # self.play(FadeIn(funcao))
        # self.wait()

        texto = always_redraw(lambda: Text('explorando o Manim!'))
        box = always_redraw(lambda: SurroundingRectangle(texto))
        # texto2 = always_redraw(lambda: Text('testando'))
        # texto2.next_to(box, DOWN, buff=0.5)

        self.play(Create(texto), Create(box))

        self.wait()

        self.play(texto.animate.move_to(RIGHT*2))

        self.wait()