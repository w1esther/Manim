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

        label_a_t1 = MathTex("a", color=WHITE).shift(3*LEFT+1.5*DOWN)
        label_a_t2 = MathTex("a", color=WHITE).shift(1.5*LEFT+3*UP)
        label_a_t3 = MathTex("a", color=WHITE).shift(3*RIGHT+1.5*UP)
        label_a_t4 = MathTex("a", color=WHITE).shift(1.5*RIGHT+3*DOWN)

        label_b_t1 = MathTex("b", color=GRAY).shift(1.5*LEFT + 3*DOWN)
        label_b_t2 = MathTex("b", color=GRAY).shift(1.5*UP + 3*LEFT)
        label_b_t3 = MathTex("b", color=GRAY).shift(1.5*RIGHT + 3*UP)
        label_b_t4 = MathTex("b", color=GRAY).shift(1.5*DOWN + 3*RIGHT)

        label_c_t1 = MathTex("c", color = WHITE).shift(1*LEFT+1*DOWN)

        self.play(FadeIn(triangulo1))
        self.play(FadeIn(label_a_t1), FadeIn(label_b_t1))

        self.play(triangulo2.animate.rotate(-90*DEGREES).shift(0.5*LEFT + 2.5*UP))
        self.play(FadeIn(label_a_t2), FadeIn(label_b_t2))

        self.play(triangulo3.animate.rotate(-180*DEGREES).shift(3*UP + 2*RIGHT))
        self.play(FadeIn(label_a_t3), FadeIn(label_b_t3))

        self.play(triangulo4.animate.rotate(-270*DEGREES).shift(0.5*UP + 2.5*RIGHT))
        self.play(FadeIn(label_a_t4), FadeIn(label_b_t4))

        quadrado = Square(side_length=3.55, fill_color = GREEN, fill_opacity = 1)
        quadrado.rotate(-33.5*DEGREES, about_point=quadrado.get_center())
        quadrado.set_stroke(GREEN)

        quadrado2 = Square(side_length=5)
        self.play(FadeIn(quadrado2))

        self.play(FadeIn(quadrado))
        
        self.play(FadeIn(label_c_t1))

        self.wait(2)

        # BA = (A - B)[:2]
        # AC = (C - A)[:2]
        # # theta = -math.atan2(BA[0], BA[1])         # cerca de -0.98279 rad (-56.3099°)
        # theta2 = -math.atan2(AC[1], AC[0])

        # # 1) rotaciona em torno de B
        # self.play(triangulo4.animate.rotate(theta2, about_point=B), triangulo3.animate.rotate(theta2, about_point=C), run_time=2)
        # self.play(triangulo3.animate.shift(0.5*RIGHT + 1.5*UP))
        # # 2) aplicar reflexão no eixo x (matriz 3x3 para Manim)
        # S_vertical = np.array([[1., 0., 0.],
        #               [0., -1., 0.],
        #               [0., 0., 1.]])
        
        # S_horizontal = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]])
        # # apply_matrix aplica a transformação diretamente às coordenadas
        # self.play(triangulo4.animate.apply_matrix(S_horizontal, about_point = B), run_time = 2)
        # self.play(triangulo4.animate.apply_matrix(S_vertical, about_point = B), run_time = 2)
        # self.play(triangulo4.animate.shift(2.5*DOWN + 4.5*LEFT))
        # self.play(triangulo2.animate.apply_matrix(S_vertical, about_point=B),run_time = 2)
        # self.play(triangulo2.animate.apply_matrix(S_horizontal, about_point=B), run_time = 2)
        # self.play(triangulo2.animate.shift(7*LEFT + 2 * UP))

        self.wait()