from manim import *

class Tangente(Scene):
    def construct(self):

        k = ValueTracker(-4)
        
        eixos = Axes(x_range=[-4, 4, 1], y_range=[-2, 16, 2], x_length=10, y_length=6).add_coordinates()

        funcao = eixos.plot(lambda x: x**2, x_range=[-6, 6], color=YELLOW_D)

        # recria a reta toda vez que o valor de k muda, ou seja, toda vez que a cena atualiza

        tangente = always_redraw(lambda: eixos.get_secant_slope_group(x=k.get_value(), graph=funcao, dx=0.01, secant_line_color=ORANGE, secant_line_length=3))

        ponto = always_redraw( lambda: Dot().move_to(eixos.c2p(k.get_value(), funcao.underlying_function(k.get_value()))))

        self.play(FadeIn(eixos))
        self.play(Create(funcao))
        self.play(FadeIn(tangente), FadeIn(ponto))
        self.play(k.animate.set_value(4), run_time=3)

        self.wait(3)