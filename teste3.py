from manim import *
import numpy as np
import math

class AlinhaTriangulos(Scene):
    def construct(self):

        # malha = NumberPlane()
        # self.play(FadeIn(malha))

        A = np.array([0., 3., 0.])
        B = np.array([-2., 0., 0.])
        C = np.array([4.5, 0., 0.])

        AB = Line(A, B)
        AC = Line(A, C)
        BC = Line(B, C)
        BA = Line(B, A)
        CA = Line(C, A)
        CB = Line(C, B)

        # triângulo maior BAC
        tri_BAC = Polygon(B, A, C, color=BLUE)
        self.play(Create(tri_BAC))

        ang_reto = RightAngle(AB, AC, length=0.4, quadrant=(1, 1), color=YELLOW)

        ang_beta = Angle(BC, BA, radius=0.6, other_angle=False, color=ORANGE)

        ang_alfa = Angle(CA, CB, radius=0.6, other_angle=False, color=GREEN)

        beta_label = MathTex(r"\beta").move_to(ang_beta.point_from_proportion(0.5) + 0.3*UP + 0.5*RIGHT)

        alfa_label = MathTex(r"\alpha").move_to(ang_alfa.point_from_proportion(0.5) + 0.3*UP + 0.5*LEFT)

        guardar_angulos_lados = VGroup()
        guardar_angulos_lados.add(ang_reto, ang_beta, ang_alfa, beta_label, alfa_label)

        self.play(Write(guardar_angulos_lados), run_time=2)
        # calcula H (pé da altura)
        BC_vec = C - B
        t = np.dot(A - B, BC_vec) / np.dot(BC_vec, BC_vec)
        H = B + t * BC_vec  # aqui H = (0,0,0)

        # triângulo menor BAH (que quero transformar)
        tri_BAH = Polygon(B, A, H, color=GREEN)
        self.play(Create(tri_BAH))

        # parâmetros numéricos (2D)
        BA = (A - B)[:2]
        BH = (H - B)[:2]
        # k = np.linalg.norm(BH) / np.linalg.norm(BA)   # ~0.5547002
        theta = -math.atan2(BA[1], BA[0])            # cerca de -0.98279 rad (-56.3099°)

        # 1) rotaciona em torno de B
        self.play(tri_BAH.animate.rotate(theta, about_point=B))

        # 2) aplicar reflexão no eixo x (matriz 3x3 para Manim)
        S = np.array([[1., 0., 0.],
                      [0., -1., 0.],
                      [0., 0., 1.]])
        # apply_matrix aplica a transformação diretamente às coordenadas
        self.play(tri_BAH.animate.apply_matrix(S, about_point=B))

        # 3) escala uniforme em torno de B
        # self.play(tri_BAH.animate.scale(k, about_point=B))

        # agora tri_BAH deve coincidir (orientação e proporção) com tri_BAC

        self.play(tri_BAH.animate.move_to(2.15*UP+0.7*RIGHT))
        self.wait()
        self.play(tri_BAH.animate.move_to(0.85*UP+2.7*RIGHT))
        self.wait()
        self.play(tri_BAH.animate.move_to(2*DOWN+2.7*LEFT))
        self.wait(2)
