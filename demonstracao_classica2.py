from manim import *
import math

class DemonstracaoClassicaPitagoras(MovingCameraScene):
    def construct(self):

        self.play(self.camera.frame.animate.scale(1.3))

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

        label_c_t1 = MathTex("c", color = WHITE).shift(1.2*LEFT+1*DOWN)
        label_c_t2 = MathTex("c", color = WHITE).shift(1.2*LEFT+1*UP)
        label_c_t3 = MathTex("c", color = WHITE).shift(1.2*RIGHT+1*UP)
        label_c_t4 = MathTex("c", color = WHITE).shift(1.2*RIGHT+1*DOWN)

        c_quadrado = MathTex("c^2")

        t1 = VGroup()
        t1.add(triangulo1, label_a_t1, label_b_t1)
        t2 = VGroup()
        t2.add(triangulo2, label_a_t2, label_b_t2)
        t3 = VGroup()
        t3.add(triangulo3, label_a_t3, label_b_t3)
        t4 = VGroup()
        t4.add(triangulo4, label_a_t4, label_b_t4)

        self.play(FadeIn(triangulo1))

        self.play(triangulo2.animate.rotate(-90*DEGREES).shift(0.5*LEFT + 2.5*UP),triangulo3.animate.rotate(-180*DEGREES).shift(3*UP + 2*RIGHT), triangulo4.animate.rotate(-270*DEGREES).shift(0.5*UP + 2.5*RIGHT))
        
        self.wait()

        self.play(FadeIn(label_a_t2), FadeIn(label_a_t3), FadeIn(label_a_t4), FadeIn(label_a_t1))

        self.wait()

        self.play(FadeIn(label_b_t1), FadeIn(label_b_t2), FadeIn(label_b_t3), FadeIn(label_b_t4))

        quadrado = Square(side_length=3.55, fill_color = GREEN, fill_opacity = 1)
        quadrado.rotate(-33.5*DEGREES, about_point=quadrado.get_center())
        quadrado.set_stroke(GREEN)

        quadrado2 = Square(side_length=5)

        self.play(FadeIn(quadrado), FadeIn(quadrado2))

        self.play(FadeIn(label_c_t1), FadeIn(label_c_t2), FadeIn(label_c_t3), FadeIn(label_c_t4))

        self.wait()

        self.play(Transform(label_c_t1, c_quadrado), Transform(label_c_t2, c_quadrado), Transform(label_c_t3, c_quadrado), Transform(label_c_t4, c_quadrado))

        self.play(FadeOut(label_c_t1), FadeOut(label_c_t2), FadeOut(label_c_t3), FadeOut(label_c_t4))

        self.play(self.camera.frame.animate.shift(2*RIGHT), quadrado.animate.shift(6*RIGHT), c_quadrado.animate.shift(6*RIGHT))

        self.wait()

        self.play(t3.animate.shift(1.95*LEFT), t2.animate.shift(3.0*RIGHT + 2.0*DOWN), t1.animate.shift(3*UP))

        # self.play(quadrado.animate.shift(5*RIGHT))

        # self.play(triangulo3.animate.rotate(-180*DEGREES).shift(3*UP + 2*RIGHT))
        # self.play(FadeIn(label_a_t3))

        # self.play(triangulo4.animate.rotate(-270*DEGREES).shift(0.5*UP + 2.5*RIGHT))
        # self.play(FadeIn(label_a_t4))

        self.wait(2)