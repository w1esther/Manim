from manim import *
import math

class DemonstracaoAlgebricaPitagoras(MovingCameraScene):
    def construct(self):

        self.play(self.camera.frame.animate.scale(1.4))

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
        c_quadrado_copia = c_quadrado.copy()
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

        quadrado = Square(side_length=3.55, fill_color = GREEN, fill_opacity = 1)
        quadrado.rotate(-33.5*DEGREES, about_point=quadrado.get_center())
        quadrado.set_stroke(GREEN)

        quadrado2 = Square(side_length=5, color=RED, fill_color = RED, fill_opacity = 1)

        self.play(FadeIn(quadrado2))
        self.play(quadrado2.animate.shift(7*RIGHT), self.camera.frame.animate.shift(4*RIGHT))

        a_b = MathTex(r"(a + b)").shift(3*DOWN+7*RIGHT)
        a_bcopia = MathTex(r"a + b").shift(3*DOWN+7*RIGHT)
        a_b2 = MathTex(r"(a + b)").shift(10.7*RIGHT)
        a_b2copia = MathTex(r"a + b").shift(10.7*RIGHT)
        area = MathTex(r"(a + b)^2").shift(7*RIGHT)
        area_copia = area.copy()

        self.play(FadeIn(a_b), FadeIn(a_b2), FadeIn(a_b2copia), FadeIn(a_bcopia))
        mult2 = MathTex(r"\cdot").shift(6.8*RIGHT)

        self.wait()

        self.play(a_b.animate.shift(1*LEFT+3*UP), a_b2.animate.shift(3*LEFT), FadeIn(mult2))
        self.wait()
        self.play(Transform(a_b, area), Transform(a_b2, area), FadeOut(mult2), FadeIn(area_copia))

        area_tri1 = MathTex(r"\frac{ab}{2}").shift(1.8*LEFT+1.8*DOWN)
        area_tri1_copia = area_tri1.copy()
        area_tri2 = MathTex(r"\frac{ab}{2}").shift(1.8*LEFT +1.8*UP)
        area_tri2_copia = area_tri2.copy()
        area_tri3 = MathTex(r"\frac{ab}{2}").shift(1.8*RIGHT+1.8*UP)
        area_tri3_copia = area_tri3.copy()
        area_tri4 = MathTex(r"\frac{ab}{2}").shift(1.8*RIGHT +1.8*DOWN)
        area_tri4_copia = area_tri4.copy()

        self.play(FadeIn(area_tri1), FadeIn(area_tri2), FadeIn(area_tri3), FadeIn(area_tri4), FadeIn(area_tri1_copia), FadeIn(area_tri2_copia), FadeIn(area_tri3_copia), FadeIn(area_tri4_copia))

        self.play(FadeIn(quadrado))
        self.bring_to_front(label_c_t1)
        self.bring_to_front(label_c_t2)
        self.bring_to_front(label_c_t4)
        self.bring_to_front(label_c_t3)

        mult = MathTex(r"\cdot").shift(0.2*LEFT)

        self.wait()

        self.play(label_c_t1.animate.shift(1*UP+0.5*RIGHT), label_c_t2.animate.shift(1*DOWN+1.5*RIGHT), FadeIn(mult))

        self.play(Transform(label_c_t1, c_quadrado), Transform(label_c_t2, c_quadrado), FadeOut(mult), FadeIn(c_quadrado_copia))

        self.wait()

        self.play(self.camera.frame.animate.shift(2*DOWN))

        mais1 = MathTex(r"+").shift(2.8*LEFT+5.3*DOWN)
        mais2 = MathTex(r"+").shift(5.3*DOWN+0.7*LEFT)
        mais3 = MathTex(r"+").shift(5.3*DOWN + 1.3*RIGHT)
        mais4 = MathTex(r"+").shift(5.3*DOWN + 3.2*RIGHT)
        
        igual = MathTex(r"=").shift(5.3*DOWN + 5.2*RIGHT)

        self.play(area_tri1.animate.shift(3.5*DOWN+2*LEFT), area_tri2.animate.shift(7.1*DOWN), area_tri3.animate.shift(7.1*DOWN + 1.5*LEFT), area_tri4.animate.shift(3.5*DOWN + 0.5*RIGHT), c_quadrado.animate.shift(5.3*DOWN + 4*RIGHT), area.animate.shift(5.3*DOWN), FadeIn(mais1), FadeIn(mais2), FadeIn(mais3), FadeIn(mais4), FadeIn(igual))

        self.wait()

        resultado = MathTex(r"4 \cdot \frac{ab}{2}").shift(5.3*DOWN + 2.2*RIGHT)

        self.play(Transform(area_tri1, resultado), Transform(area_tri2, resultado), Transform(area_tri3, resultado), Transform(area_tri4, resultado), FadeOut(mais2), FadeOut(mais1), FadeOut(mais3))
        self.play(FadeOut(area_tri2), FadeOut(area_tri3), FadeOut(area_tri4))

        base11 = Line(LEFT * 0.4, RIGHT * 0.4).shift(1.9*RIGHT + 5.3*DOWN)
        base22 = Line(LEFT * 0.4, RIGHT * 0.4).shift(2.4*RIGHT + 5.6*DOWN)
        base11.rotate(45*DEGREES)
        base22.rotate(45*DEGREES)
        linha_pontilhada11 = DashedVMobject(base11, num_dashes=10).set_color(YELLOW)
        linha_pontilhada22 = DashedVMobject(base22, num_dashes=10).set_color(YELLOW)
        self.play(Write(linha_pontilhada11), Write(linha_pontilhada22))

        resultado_2 = MathTex(r"2ab").shift(5.3*DOWN+2.2*RIGHT)

        self.play(Transform(area_tri1, resultado_2), FadeOut(linha_pontilhada11), FadeOut(linha_pontilhada22))

        resultado_3 = MathTex(r"a^2 + 2ab + b^2").shift(5.3*DOWN + 7.5*RIGHT)

        self.play(Transform(area, resultado_3))

        base1 = Line(LEFT * 0.4, RIGHT * 0.4).shift(2.1*RIGHT + 5.3*DOWN)
        base2 = Line(LEFT * 0.4, RIGHT * 0.4).shift(7.5*RIGHT + 5.3*DOWN)
        base1.rotate(45*DEGREES)
        base2.rotate(45*DEGREES)
        linha_pontilhada1 = DashedVMobject(base1, num_dashes=10).set_color(YELLOW)
        linha_pontilhada2 = DashedVMobject(base2, num_dashes=10).set_color(YELLOW)
        self.play(Write(linha_pontilhada1), Write(linha_pontilhada2))
        self.wait()

        resultado_4 = MathTex(r"a^2  +  b^2").shift(5.3*DOWN + 4.2*RIGHT)

        self.play(FadeOut(linha_pontilhada1), FadeOut(linha_pontilhada2), Transform(area, resultado_4), FadeOut(area_tri1), FadeOut(mais4), igual.animate.shift(2.4*LEFT), c_quadrado.animate.shift(2*LEFT) )

        teorema = Text('Teorema de Pitágoras').shift(4.2*DOWN + 3.5*RIGHT)

        self.play(FadeIn(teorema))

        self.wait()
