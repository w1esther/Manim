from manim import *
import math

class DemonstracaoClassicaPitagoras(MovingCameraScene):
    def construct(self):
        malha = NumberPlane()
        self.play(FadeIn(malha))

        A = np.array([0, 2, 0])
        B = np.array([3, 0, 0])
        C = np.array([0, 0, 0])

        triangulo1 = Polygon(A, B, C, color=BLUE_C, fill_color = BLUE_C, fill_opacity = 1.0).shift(2.5*LEFT + 2.5*DOWN)
        triangulo3 = Polygon(A, B, C, color=RED, fill_color = RED, fill_opacity = 1.0).shift(2.5*LEFT + 2.5*DOWN)
        triangulo2 = Polygon(A, B, C, color=ORANGE, fill_color = ORANGE, fill_opacity = 1.0).shift(2.5*LEFT + 2.5*DOWN)
        triangulo4 = Polygon(A, B, C, color=PINK, fill_color = PINK, fill_opacity = 1.0).shift(2.5*LEFT + 2.5*DOWN)

        label_a_t1 = MathTex('a', color=WHITE).shift(3*LEFT+1.5*DOWN)
        label_a_t2 = MathTex('a', color=WHITE).shift(1.5*LEFT+3*UP)
        label_a_t3 = MathTex('a', color=WHITE).shift(3*RIGHT+1.5*UP)
        label_a_t4 = MathTex('a', color=WHITE).shift(1.5*RIGHT+3*DOWN)

        label_b_t1 = MathTex("b", color=GRAY).shift(1.5*LEFT + 3*DOWN)
        label_b_t2 = MathTex("b", color=GRAY).shift(1.5*UP + 3*LEFT)
        label_b_t3 = MathTex("b", color=GRAY).shift(1.5*RIGHT + 3*UP)
        label_b_t4 = MathTex("b", color=GRAY).shift(1.5*DOWN + 3*RIGHT)

        self.play(FadeIn(triangulo1))

        self.play(triangulo2.animate.rotate(-90*DEGREES).shift(0.5*LEFT + 2.5*UP),triangulo3.animate.rotate(-180*DEGREES).shift(3*UP + 2*RIGHT), triangulo4.animate.rotate(-270*DEGREES).shift(0.5*UP + 2.5*RIGHT))
        
        self.wait()

        self.play(FadeIn(label_a_t2), FadeIn(label_a_t3), FadeIn(label_a_t4), FadeIn(label_a_t1))

        self.wait()

        self.play(FadeIn(label_b_t1), FadeIn(label_b_t2), FadeIn(label_b_t3), FadeIn(label_b_t4))

        # self.play(triangulo3.animate.rotate(-180*DEGREES).shift(3*UP + 2*RIGHT))
        # self.play(FadeIn(label_a_t3))

        # self.play(triangulo4.animate.rotate(-270*DEGREES).shift(0.5*UP + 2.5*RIGHT))
        # self.play(FadeIn(label_a_t4))

        self.wait(2)