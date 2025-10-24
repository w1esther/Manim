from manim import *

class Quadratica(Scene):
    def construct(self):
        
        plano = (
            NumberPlane(x_range=[-4, 4, 1], x_length=7, y_range=[0, 16, 4], y_length=5, color=PURPLE)
            .add_coordinates().set_color(PURPLE)
        )

        texto = plano.get_axis_labels(x_label= 'x', y_label= 'f(x)')

        funcao = MathTex('f(x)={x}^{2}').scale(0.7).next_to(plano, UP+LEFT, buff=0.5).set_color(PURPLE_D)

        parabola = plano.plot(lambda x: x**2, x_range=[-4, 4], color=PINK)

        area = plano.get_riemann_rectangles(graph=parabola, x_range=[-4, 4.1], dx= 0.1, stroke_width=0.1,stroke_color=RED_C, color=RED_A)

        self.play(DrawBorderThenFill(plano), Create(texto))
        self.play(Create(parabola), Create(funcao))
        self.play(FadeIn(area))
        self.wait()