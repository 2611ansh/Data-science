from manim import *


class GrowingSquare(Scene):
    def construct(self):
        square = Square(color=BLUE, fill_opacity=0.5)
        self.play(GrowFromCenter(square))
        self.wait()

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()
        square.rotate(PI / 4)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))

class CustomBackground(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        square = Square(color=BLUE, fill_opacity=0.5)
        circle = Circle(color=RED, fill_opacity=0.5)

        self.play(Create(square))
        self.wait()
        self.play(Transform(square, circle))
        self.wait()


