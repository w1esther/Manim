from manim import *
import numpy as np
import math

class AlinhaTriangulos(Scene):
    def construct(self):
        A = np.array([0., 3., 0.])
        B = np.array([-2., 0., 0.])
        C = np.array([4.5, 0., 0.])

        # triângulo maior BAC
        tri_BAC = Polygon(B, A, C, color=BLUE)
        self.play(Create(tri_BAC))

        # calcula H (pé da altura)
        BC_vec = C - B
        t = np.dot(A - B, BC_vec) / np.dot(BC_vec, BC_vec)
        H = B + t * BC_vec  # aqui H = (0,0,0)

        # triângulo menor BAH (que queremos transformar)
        tri_BAH = Polygon(B, A, H, color=GREEN)
        self.play(Create(tri_BAH))

        # parâmetros numéricos (2D)
        BA = (A - B)[:2]
        BH = (H - B)[:2]
        k = np.linalg.norm(BH) / np.linalg.norm(BA)   # ~0.5547002
        theta = -math.atan2(BA[1], BA[0])            # cerca de -0.98279 rad (-56.3099°)

        # 1) rotaciona em torno de B
        self.play(tri_BAH.animate.rotate(theta, about_point=B))

        # 2) aplicar reflexão no eixo x (matriz 3x3 para Manim)
        S = np.array([[1., 0., 0.],
                      [0., -1., 0.],
                      [0., 0., 1.]])
        # apply_matrix aplica a transformação diretamente às coordenadas
        tri_BAH.apply_matrix(S, about_point=B)

        # 3) escala uniforme em torno de B
        # self.play(tri_BAH.animate.scale(k, about_point=B))

        # agora tri_BAH deve coincidir (orientação e proporção) com tri_BAC
        self.wait(2)
