from manim import *

class Malha(Scene):
    def construct(self):
        
        malha = NumberPlane()

        self.play(FadeIn(malha))

        self.wait(3)