from manim import *
import math

class DemonstracaoClassicaPitagoras(MovingCameraScene):
    def construct(self):
        malha = NumberPlane()
        self.play(FadeIn(malha))

        A = np.array([0, 2, 0])
        B = np.array([3, 0, 0])
        C = np.array([0, 0, 0])

        triangulo1 = Polygon(A, B, C, color=BLUE_C, fill_color = BLUE_C, fill_opacity = 1.0).shift(3*LEFT + 1.5*DOWN)
        triangulo3 = Polygon(A, B, C, color=RED, fill_color = RED, fill_opacity = 1.0).shift(3*LEFT + 1.5*DOWN)
        triangulo2 = Polygon(A, B, C, color=ORANGE, fill_color = ORANGE, fill_opacity = 1.0).shift(3*LEFT + 1.5*DOWN)
        triangulo4 = Polygon(A, B, C, color=PINK, fill_color = PINK, fill_opacity = 1.0).shift(3*LEFT + 1.5*DOWN)

        self.play(FadeIn(triangulo1))

        BA = (A - B)[:2]
        AC = (C - A)[:2]
        # theta = -math.atan2(BA[0], BA[1])         # cerca de -0.98279 rad (-56.3099°)
        theta2 = -math.atan2(AC[1], AC[0])

        # 1) rotaciona em torno de B
        self.play(triangulo4.animate.rotate(theta2, about_point=B), triangulo3.animate.rotate(theta2, about_point=C), run_time=2)
        self.play(triangulo3.animate.shift(0.5*RIGHT + 1.5*UP))
        # 2) aplicar reflexão no eixo x (matriz 3x3 para Manim)
        S_vertical = np.array([[1., 0., 0.],
                      [0., -1., 0.],
                      [0., 0., 1.]])
        
        S_horizontal = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]])
        # apply_matrix aplica a transformação diretamente às coordenadas
        self.play(triangulo4.animate.apply_matrix(S_horizontal, about_point = B), run_time = 2)
        self.play(triangulo4.animate.apply_matrix(S_vertical, about_point = B), run_time = 2)
        self.play(triangulo4.animate.shift(2.5*DOWN + 4.5*LEFT))
        self.play(triangulo2.animate.apply_matrix(S_vertical, about_point=B),run_time = 2)
        self.play(triangulo2.animate.apply_matrix(S_horizontal, about_point=B), run_time = 2)
        self.play(triangulo2.animate.shift(7*LEFT + 2 * UP))

        self.wait()