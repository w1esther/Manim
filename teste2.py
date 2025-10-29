from manim import *

class TeoremaPitagorasRelaçõesMétricas(Scene):
    def construct(self):
        # Pontos do triângulo
        A = np.array([-3, 0, 0])
        B = np.array([3, 0, 0])
        C = np.array([-3, 2, 0])
        
        tri = Polygon(A, B, C, color=BLUE)
        h = DashedLine(C, [C[0], 0, 0], color=YELLOW)
        H = Dot([C[0], 0, 0], color=YELLOW)
        
        # Rótulos
        label_A = MathTex("A").next_to(A, LEFT)
        label_B = MathTex("B").next_to(B, RIGHT)
        label_C = MathTex("C").next_to(C, UP)
        label_H = MathTex("H").next_to(H, DOWN)
        
        self.play(Create(tri))
        self.play(Create(h), FadeIn(H))
        self.play(Write(label_A), Write(label_B), Write(label_C), Write(label_H))
        
        # Relações métricas
        relacoes = MathTex(
            "b^2 = a \\cdot n", "\\quad", "c^2 = a \\cdot m", "\\Rightarrow", "b^2 + c^2 = a^2"
        ).scale(1.2).to_edge(DOWN)
        
        self.play(Write(relacoes[0]))
        self.wait(0.5)
        self.play(Write(relacoes[2]))
        self.wait(0.5)
        self.play(Write(relacoes[4]))
        self.wait(2)
