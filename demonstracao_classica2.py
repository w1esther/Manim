from manim import *
import math

class DemonstracaoClassicaPitagoras(MovingCameraScene):
    def construct(self):

        self.play(self.camera.frame.animate.scale(1.3))

        # malha = NumberPlane()
        # self.play(FadeIn(malha))

        A = np.array([0, 2, 0])
        B = np.array([3, 0, 0])
        C = np.array([0, 0, 0])

        triangulo1 = Polygon(A, B, C, color=PINK, fill_color = PINK, fill_opacity = 1.0).shift(2.5*LEFT + 2.5*DOWN)
        triangulo3 = Polygon(A, B, C, color=PINK, fill_color = PINK, fill_opacity = 1.0).shift(2.5*LEFT + 2.5*DOWN)
        triangulo2 = Polygon(A, B, C, color=PINK, fill_color = PINK, fill_opacity = 1.0).shift(2.5*LEFT + 2.5*DOWN)
        triangulo4 = Polygon(A, B, C, color=PINK, fill_color = PINK, fill_opacity = 1.0).shift(2.5*LEFT + 2.5*DOWN)

        label_a_t1 = MathTex('a', color=WHITE).shift(3*LEFT+1.5*DOWN)
        label_a_t2 = MathTex('a', color=WHITE).shift(1.5*LEFT+3*UP)
        label_a_t3 = MathTex('a', color=WHITE).shift(3*RIGHT+1.5*UP)
        label_a_t4 = MathTex('a', color=WHITE).shift(1.5*RIGHT+3*DOWN)

        label_b_t1 = MathTex("b", color=WHITE).shift(1.5*LEFT + 3*DOWN)
        label_b_t2 = MathTex("b", color=WHITE).shift(1.5*UP + 3*LEFT)
        label_b_t3 = MathTex("b", color=WHITE).shift(1.5*RIGHT + 3*UP)
        label_b_t4 = MathTex("b", color=WHITE).shift(1.5*DOWN + 3*RIGHT)

        label_c_t1 = MathTex("c", color = WHITE).shift(1.2*LEFT+1*DOWN)
        label_c_t2 = MathTex("c", color = WHITE).shift(1.2*LEFT+1*UP)
        label_c_t3 = MathTex("c", color = WHITE).shift(1.2*RIGHT+1*UP)
        label_c_t4 = MathTex("c", color = WHITE).shift(1.2*RIGHT+1*DOWN)

        c_quadrado = MathTex("c^2")
        b_quadrado = MathTex("b^2").shift(1*DOWN+1*LEFT)
        a_quadrado = MathTex("a^2").shift(1.5*RIGHT + 1.5*UP)

        t1 = VGroup()
        t1.add(triangulo1, label_a_t1, label_b_t1)
        t2 = VGroup()
        t2.add(triangulo2, label_a_t2, label_b_t2)
        t3 = VGroup()
        t3.add(triangulo3, label_a_t3, label_b_t3, label_c_t3)
        t4 = VGroup()
        t4.add(triangulo4, label_a_t4, label_b_t4, label_c_t4)

        self.play(FadeIn(triangulo1))
        self.play(FadeIn(label_a_t1), FadeIn(label_b_t1), FadeIn(label_c_t1))

        self.play(triangulo2.animate.rotate(-90*DEGREES).shift(0.5*LEFT + 2.5*UP))
        self.play(FadeIn(label_a_t2), FadeIn(label_b_t2),FadeIn(label_c_t2))
        self.play(triangulo3.animate.rotate(-180*DEGREES).shift(3*UP + 2*RIGHT))
        self.play(FadeIn(label_a_t3), FadeIn(label_b_t3), FadeIn(label_c_t3)) 
        self.play(triangulo4.animate.rotate(-270*DEGREES).shift(0.5*UP + 2.5*RIGHT))
        self.play(FadeIn(label_a_t4), FadeIn(label_b_t4), FadeIn(label_c_t4))
        
        self.wait()

        quadrado_inv = Square(side_length=3, stroke_width = 0, fill_opacity = 0).shift(1*LEFT + 1*DOWN)
        quadrado_inv2 = Square(side_length=2, stroke_width = 0, fill_opacity = 0).shift(1.5*UP + 1.5*RIGHT)

        self.play(FadeIn(quadrado_inv), FadeIn(quadrado_inv2))

        # self.play(FadeIn(label_a_t2), FadeIn(label_a_t3), FadeIn(label_a_t4))

        self.wait()

        # self.play(FadeIn(label_b_t2), FadeIn(label_b_t3), FadeIn(label_b_t4))

        quadrado = Square(side_length=3.55, fill_color = GREEN, fill_opacity = 1)
        quadrado.rotate(-33.5*DEGREES, about_point=quadrado.get_center())
        quadrado.set_stroke(GREEN)

        quadrado2 = Square(side_length=5)

        self.play(FadeIn(quadrado), FadeIn(quadrado2))
        self.bring_to_front(label_c_t1)
        self.bring_to_front(label_c_t2)
        self.bring_to_front(label_c_t4)
        self.bring_to_front(label_c_t3)

        # self.play(FadeIn(label_c_t1), FadeIn(label_c_t2), FadeIn(label_c_t3), FadeIn(label_c_t4))

        mult = MathTex(r"\cdot").shift(0.2*LEFT)

        self.wait()

        self.play(label_c_t1.animate.shift(1*UP+0.5*RIGHT), label_c_t2.animate.shift(1*DOWN+1.5*RIGHT), FadeIn(mult))

        self.play(Transform(label_c_t1, c_quadrado), Transform(label_c_t2, c_quadrado), FadeOut(mult))

        self.wait()

        self.play(self.camera.frame.animate.shift(2*RIGHT), quadrado.animate.shift(6*RIGHT), c_quadrado.animate.shift(6*RIGHT), FadeOut(label_c_t1), FadeOut(label_c_t2))

        self.wait()

        self.play(t3.animate.shift(1.955*LEFT), t2.animate.shift(2.955*RIGHT +2*DOWN), t1.animate.shift(2.965*UP), t4.animate.shift(0.02*RIGHT))
        self.bring_to_front(label_c_t4)
        self.bring_to_front(label_c_t3)

        self.wait()

        self.play(quadrado_inv.animate.set_fill(color=YELLOW_E, opacity=1))

        mult2 = MathTex(r"\cdot").shift(1*LEFT+1*DOWN)

        self.play(label_b_t1.animate.shift(1*DOWN), label_b_t2.animate.shift(0.5*DOWN + 0.5*LEFT), FadeIn(mult2))

        self.play(Transform(label_b_t1, b_quadrado), Transform(label_b_t2, b_quadrado), FadeOut(mult2))

        self.play(quadrado_inv2.animate.set_fill(color=BLUE_E, opacity=1))

        mult3 = MathTex(r"\cdot").shift(1.5*RIGHT+1.5*UP)

        self.play(label_a_t2.animate.shift(0.5*UP + 0.5*RIGHT), FadeIn(mult3))

        self.play(Transform(label_a_t2, a_quadrado), Transform(label_a_t3, a_quadrado), FadeOut(mult3))

        self.play(self.camera.frame.animate.scale(1.5).shift(2*RIGHT + 2* DOWN))

        self.play(quadrado.animate.shift(3*RIGHT+6*DOWN).rotate(33.5*DEGREES), c_quadrado.animate.shift(3*RIGHT + 6*DOWN), quadrado_inv.animate.shift(5*DOWN +1*LEFT), label_b_t1.animate.shift(5*DOWN + 1*LEFT), FadeOut(label_b_t2), quadrado_inv2.animate.shift(7.5*DOWN + 1.5*RIGHT), label_a_t2.animate.shift(7.5*DOWN +1.5*RIGHT), FadeOut(label_a_t3))

        teorema = Text('Teorema  de \n   Pitágoras', font_size=60).shift(7.5*RIGHT)

        mais = MathTex("+").shift(0.8*RIGHT + 6*DOWN)
        mais_2 = mais.copy()
        igual = MathTex("=").shift(6*DOWN + 5.5*RIGHT)
        igual_2 = igual.copy()

        grupo_teorema = VGroup()
        grupo_teorema.add(c_quadrado, igual_2, label_a_t2, mais_2, label_b_t1)

        self.play(FadeIn(mais), FadeIn(igual), FadeIn(teorema))
        self.play(c_quadrado.animate.shift(4*UP + 0.45*RIGHT), igual_2.animate.shift(3.9*UP+3*RIGHT),label_a_t2.animate.shift(4*UP+4.5*RIGHT), mais_2.animate.shift(3.9*UP+5.7*RIGHT), label_b_t1.animate.shift(4*UP + 7.6*RIGHT))

        # self.play(quadrado.animate.shift(5*RIGHT))

        # self.play(triangulo3.animate.rotate(-180*DEGREES).shift(3*UP + 2*RIGHT))
        # self.play(FadeIn(label_a_t3))

        # self.play(triangulo4.animate.rotate(-270*DEGREES).shift(0.5*UP + 2.5*RIGHT))
        # self.play(FadeIn(label_a_t4))

        self.wait(2)