from manim import *


class GridDimensions(Scene):
    def construct(self):
        plane = NumberPlane(
            axis_config={"include_numbers": True})  # change colors
        self.play(Write(plane, run_time=5))
        self.wait()


class DrawingCircle(Scene):
    def construct(self):

        circle = Circle(radius=0.3, color=WHITE)

        self.play(Write(circle, run_time=3))
        self.wait()

        self.play(circle.animate.scale(2))
        self.wait()

        self.play(circle.animate.shift(2 * UP))
        self.wait()

        self.play(circle.animate.shift(2 * RIGHT + 2 * DOWN))
        self.wait()

        self.play(circle.animate.move_to(ORIGIN).scale(0.5))
        self.wait()

        circle_left = circle.copy()
        circle_right = circle.copy()
        self.add(circle_left, circle_right)
        self.play(circle_left.animate.shift(2 * LEFT),
                  circle_right.animate.shift(2 * RIGHT), run_time=2)
        self.wait()

        triangle = Triangle(radius=0.5, color=WHITE,
                            fill_color=RED_E, fill_opacity=1)
        self.play(ReplacementTransform(circle, triangle))
        self.wait()

        self.play(circle_left.animate.shift(UP),
                  circle_right.animate.shift(UP),
                  triangle.animate.shift(UP))
        self.wait()

        group = VGroup(circle_left, circle_right, triangle)
        self.play(group.animate.to_edge(RIGHT).scale(0.5))
        self.wait()
        self.play(group.animate.move_to(ORIGIN))
        self.wait()
        self.play(FadeOut(group))
        self.wait()
