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

        # calcula H (pé da altura)
        BC_vec = C - B
        t = np.dot(A - B, BC_vec) / np.dot(BC_vec, BC_vec)
        H = B + t * BC_vec  # aqui H = (0,0,0)

        AB = Line(A, B)
        AC = Line(A, C)
        BC = Line(B, C)
        BA = Line(B, A)
        CA = Line(C, A)
        CB = Line(C, B)
        AH = Line(A, H)

        linha_altura = Line(H, A, color=PINK)

        ponto_A = Dot(point=A, color=RED)
        ponto_A2 = Dot(point=A, color=RED)
        ponto_A3 = Dot(point=A, color=RED)
        ponto_B = Dot(point=B, color=RED)
        ponto_B2 = Dot(point=B, color=RED)
        ponto_C = Dot(point=C, color=RED)
        ponto_C2 = Dot(point=C, color=RED)
        pontoH = Dot(point=H, color=RED)
        pontoH2 = Dot(point=H, color=RED)
        pontoH3 = Dot(point=H, color=RED)

        label_A = MathTex("A").next_to(A, UP, buff=0.1).scale(0.6)
        label_A2 = MathTex("A").next_to(A, UP, buff=0.1).scale(0.6)
        label_A3 = MathTex("A").next_to(A, UP, buff=0.1).scale(0.6)
        label_B = MathTex("B").next_to(B, DOWN+LEFT, buff=0.1).scale(0.6)
        label_B2 = MathTex("B").next_to(B, DOWN+LEFT, buff=0.1).scale(0.6)
        label_C = MathTex("C").next_to(C, DOWN+RIGHT, buff=0.1).scale(0.6)
        label_C2 = MathTex("C").next_to(C, DOWN+RIGHT, buff=0.1).scale(0.6)
        label_H = MathTex("H").next_to(H, DOWN, buff=0.1).scale(0.6)
        label_H2 = MathTex("H").next_to(H, DOWN, buff=0.1).scale(0.6)
        label_H3 = MathTex("H").next_to(H, DOWN, buff=0.1).scale(0.6)

        # a → oposto de A (entre B e C)
        label_a = MathTex("a").move_to((B + C) / 2 + 0.5*DOWN)
        # b → oposto de B (entre A e C)
        label_b = MathTex("b").move_to((A + C) / 2 + 0.5*UP)
        label_b2 = MathTex("b").move_to((A + C) / 2 + 0.5*UP)
        # c → oposto de C (entre A e B)
        label_c = MathTex("c").move_to((A + B) / 2 + 0.5*LEFT)
        label_c2 = MathTex("c").move_to((A + B) / 2 + 0.5*LEFT)

        label_m = MathTex("m").move_to((B + C)/2 + 0.2 * DOWN + 2*LEFT).scale(0.6)
        label_m2 = MathTex("m").move_to((B + C)/2 + 0.2 * DOWN + 2*LEFT).scale(0.6)

        label_n = MathTex("n").move_to((B + C)/2 + 0.2 * DOWN + RIGHT).scale(0.6)
        label_n2 = MathTex("n").move_to((B + C)/2 + 0.2 * DOWN + RIGHT).scale(0.6)


        linha_BC = Line(H, B)
        linha_BC_direita = Line(H, C)

        ang_reto2 = RightAngle(linha_altura, linha_BC, length=0.4, quadrant=(1, 1), color=YELLOW)

        ang_reto3 = RightAngle(linha_altura, linha_BC_direita, length=0.4, quadrant=(1, 1), color=YELLOW)

        # triângulo maior BAC
        tri_BAC = Polygon(B, A, C, color=BLUE)
        guardar_tri_BAC = VGroup()
        guardar_tri_BAC.add(tri_BAC, ponto_A, ponto_B, ponto_C, label_A, label_B, label_C, label_a, label_b, label_c, linha_altura, label_m, label_n, label_H, pontoH)

        self.play(Create(guardar_tri_BAC), run_time=4)

        ang_reto = RightAngle(AB, AC, length=0.4, quadrant=(1, 1), color=YELLOW)

        ang_beta = Angle(BC, BA, radius=0.6, other_angle=False, color=ORANGE)

        ang_alfa = Angle(CA, CB, radius=0.6, other_angle=False, color=PURPLE)

        ang_alfa_BAH = Angle(AB, AH, radius=0.6, other_angle=False, color=PURPLE)

        ang_beta_BAH = Angle(BC, BA, radius=0.6, other_angle=False, color=ORANGE)

        ang_beta_CAH = Angle(AH, AC, radius=0.6, other_angle=False, color=ORANGE)

        ang_alfa_CAH = Angle(CA, CB, radius=0.6, other_angle=False, color=PURPLE)

        beta_label = MathTex(r"\beta").move_to(ang_beta.point_from_proportion(0.5) + 0.3*UP + 0.5*RIGHT)

        alfa_label = MathTex(r"\alpha").move_to(ang_alfa.point_from_proportion(0.5) + 0.2*UP + 0.5*LEFT)

        guardar_angulos_lados = VGroup()
        guardar_angulos_lados.add(ang_reto, ang_beta, ang_alfa, beta_label, alfa_label)

        self.play(Write(guardar_angulos_lados), run_time=2)
        
        # triângulo menor BAH (que quero transformar)
        tri_BAH = Polygon(B, A, H, color=GREEN)
        guardar_tri_BAH = VGroup()
        guardar_tri_BAH.add(ang_alfa_BAH, ang_beta_BAH, tri_BAH, ang_reto2, label_H2, pontoH2, label_m2, label_A2, ponto_A2, label_B2, ponto_B2, label_c2)

        tri_CAH = Polygon(C, A, H, color=RED)
        guardar_tri_CAH = VGroup()
        guardar_tri_CAH.add(tri_CAH, ang_alfa_CAH, ang_beta_CAH, ang_reto3, label_H3, pontoH3, label_n2, label_A3, ponto_A3, label_C2, ponto_C2, label_b2)

        self.play(Create(guardar_tri_CAH), Create(guardar_tri_BAH))

        # parâmetros numéricos (2D)
        BA = (A - B)[:2]
        BH = (H - B)[:2]
        AC = (C - A)[:2]
        theta = -math.atan2(BA[1], BA[0])         # cerca de -0.98279 rad (-56.3099°)
        theta2 = -math.atan2(AC[1], AC[0])

        # 1) rotaciona em torno de B
        self.play(guardar_tri_BAH.animate.rotate(theta, about_point=B), guardar_tri_CAH.animate.rotate(theta2, about_point=C))

        # 2) aplicar reflexão no eixo x (matriz 3x3 para Manim)
        S = np.array([[1., 0., 0.],
                      [0., -1., 0.],
                      [0., 0., 1.]])
        # apply_matrix aplica a transformação diretamente às coordenadas
        self.play(guardar_tri_BAH.animate.apply_matrix(S, about_point=B), guardar_tri_CAH.animate.apply_matrix(S, about_point=C))

        self.play(guardar_tri_CAH.animate.move_to(2*DOWN+2*RIGHT))

        self.play(guardar_tri_BAH.animate.move_to(2.08*UP+0.6*RIGHT))
        self.wait()
        self.play(guardar_tri_BAH.animate.move_to(0.75*UP+2.6*RIGHT))
        self.wait()
        self.play(guardar_tri_BAH.animate.move_to(2*DOWN+2.7*LEFT))

        self.play(guardar_tri_CAH.animate.move_to(1.15*UP+1.95*RIGHT))
        self.wait()
        self.play(guardar_tri_CAH.animate.shift(0.76*LEFT+0.5*UP))
        self.wait()
        self.play(guardar_tri_CAH.animate.shift(0.35*LEFT+0.5*DOWN))
        self.wait()
        self.play(guardar_tri_CAH.animate.shift(2.5*RIGHT+3*DOWN))

        self.play(guardar_tri_BAC.animate.shift(4*LEFT), guardar_angulos_lados.animate.shift(4*LEFT))
        self.wait()

        label_m2.shift(LEFT)

        self.play(label_a.animate.scale(2.5), label_c.animate.scale(2.5), label_m2.animate.scale(2.5), label_c2.animate.scale(2.5))

        self.wait(2)
