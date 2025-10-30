from manim import *

class Demonstracao_Pitagoras(Scene):
    def construct(self):
        
        malha = NumberPlane()
        self.play(FadeIn(malha))

        A = np.array([0, 3, 0])
        B = np.array([-3, -1, 0])
        C = np.array([5, -1, 0])

        triangulo = Polygon(A, B, C, color=RED)
        self.play(Create(triangulo))

        triangulo_mover = VGroup()
        triangulo_mover.add(triangulo)

        ponto1 = np.array([0, -1, 0])

        AB = Line(A, B)
        AC = Line(A, C)
        BC = Line(B, C)
        BA = Line(B, A)
        CA = Line(C, A)
        CB = Line(C, B)
        AH = Line(A, ponto1)

        triangulo_mover.add(AB, AC, BC, BA, CA, CB)

        # cria o simbolo do angulo reto entre dois segmentos de reta que têm origem no mesmo vértice

        ang_reto = RightAngle(AB, AC, length=0.4, quadrant=(1, 1), color=YELLOW)

        # cria o arco cuvo do angulo entre dois segmentos de reta que têm origem no mesmo vértice

        ang_beta = Angle(BC, BA, radius=0.6, other_angle=False, color=ORANGE)

        ang_alfa = Angle(CA, CB, radius=0.6, other_angle=False, color=GREEN)

        beta_label = MathTex(r"\beta").move_to(ang_beta.point_from_proportion(0.5) + 0.3*UP + 0.5*RIGHT)

        alfa_label = MathTex(r"\alpha").move_to(ang_alfa.point_from_proportion(0.5) + 0.3*UP + 0.5*LEFT)

        triangulo_mover.add(ang_reto, beta_label, alfa_label, ang_beta, ang_alfa)

        self.play(FadeIn(ang_reto), FadeIn(beta_label), FadeIn(alfa_label), FadeIn(ang_alfa), FadeIn(ang_beta))

        BC_vec = C - B
        t = np.dot(A - B, BC_vec) / np.dot(BC_vec, BC_vec)
        ponto = B + t * BC_vec

        altura = DashedLine(A, ponto, color=PINK, stroke_width=3, dash_length=0.2, dashed_ratio=0.5)

        linha_altura = Line(ponto1, A)
        linha_BC = Line(ponto1, B)
        linha_BC_direita = Line(ponto, C)

        ang_reto2 = RightAngle(linha_altura, linha_BC, length=0.4, quadrant=(1, 1), color=YELLOW)

        ang_reto3 = RightAngle(linha_altura, linha_BC_direita, length=0.4, quadrant=(1, 1), color=YELLOW)

        triangulo_mover.add(altura, linha_altura, linha_BC, linha_BC_direita, ang_reto2, ang_reto3)

        self.play(Create(altura), FadeIn(ang_reto2), FadeIn(ang_reto3))

        trianguloBAH = Polygon(A, B, ponto1, color=RED)
        trianguloACH = Polygon(A, C, ponto1, color=RED)

        trianguloACH_mover = VGroup()
        trianguloACH_mover.add(trianguloACH)

        trianguloBAH_mover = VGroup()
        trianguloBAH_mover.add(trianguloBAH)

        ang_beta_BAH = Angle(BC, BA, radius=0.6, other_angle=False, color=ORANGE)

        ang_alfa_ACH = Angle(CA, CB, radius=0.6, other_angle=False, color=GREEN)

        beta_label_BAH = MathTex(r"\beta").move_to(ang_beta.point_from_proportion(0.5) + 0.3*UP + 0.5*RIGHT)

        alfa_label_ACH = MathTex(r"\alpha").move_to(ang_alfa.point_from_proportion(0.5) + 0.3*UP + 0.5*LEFT)

        # alfa_label_BAH = MathTex(r"\alpha").move_to(ang_alfa.point_from_proportion(0.5) + 0.3*UP + 0.5*LEFT)

        # beta_label_ACH = MathTex(r"\beta").move_to(ang_beta.point_from_proportion(0.5) + 0.3*UP + 0.5*RIGHT)

        ang_alfa_BAH = Angle(AB, AH, radius=0.6, other_angle=False, color=GREEN)

        ang_beta_ACH = Angle(AH, AC, radius=0.6, other_angle=False, color=ORANGE)

        trianguloBAH_mover.add(beta_label_BAH, ang_beta_BAH, ang_alfa_BAH)
        trianguloACH_mover.add(alfa_label_ACH, ang_alfa_ACH, ang_beta_ACH)

        self.play(Create(trianguloBAH_mover), Create(trianguloACH_mover))

        self.play(FadeIn(beta_label_BAH), FadeIn(ang_beta_BAH), FadeIn(ang_alfa_ACH), FadeIn(alfa_label_ACH))

        self.wait(2)

        self.play(triangulo_mover.animate.move_to(UP*2 + 3*LEFT))
        self.play(triangulo_mover.animate.scale(0.5))

        self.play(trianguloBAH_mover.animate.shift((0.5*DOWN)+(3.5*RIGHT)))

        self.play(trianguloBAH_mover.animate.rotate(-90*DEGREES))

        self.wait()

        self.play(trianguloBAH_mover.animate.shift(RIGHT))

        self.play(trianguloBAH_mover.animate.shift(-1*RIGHT))
        self.play(trianguloBAH_mover.animate.shift(UP))
        self.play(trianguloBAH_mover.animate.shift(-1*UP))

        self.wait(2)

        
