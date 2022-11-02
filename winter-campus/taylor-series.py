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


class GraphBasics(Scene):
    def construct(self):

        func_title = MathTex(r"f(x) = cos(x)")
        self.play(Write(func_title), run_time=3)
        self.wait()

        self.play(func_title.animate.scale(0.8).to_edge(UP))
        self.wait()

        plane = NumberPlane(x_length=10, y_length=4,
                            x_range=[-5, 5], y_range=[-2, 2], axis_config={"include_numbers": True, "font_size": 16})

        self.play(DrawBorderThenFill(plane))
        self.wait()

        def func(x): return np.cos(x)

        cos_graph = plane.plot(func, color=RED)
        self.play(Create(cos_graph, run_time=7))

        neg_x, pos_x = -1, 3

        neg_dot = Dot(plane.c2p(neg_x, func(neg_x)))
        self.play(FadeIn(neg_dot))
        self.play(Flash(neg_dot))
        self.wait()

        pos_dot = Dot(plane.c2p(pos_x, func(pos_x)))
        self.play(FadeIn(pos_dot))
        self.play(Flash(pos_dot))
        self.wait()

        self.play(FadeOut(pos_dot))
        self.wait()

        # control the dot with a value tracker

        x = ValueTracker(0)
        # dot = Dot(plane.c2p(x.get_value(), np.cos(x.get_value())))
        dot = always_redraw(lambda: Dot(
            plane.c2p(x.get_value(), np.cos(x.get_value()))))

        self.play(FadeIn(dot), Flash(dot))
        self.wait()

        self.play(x.animate.set_value(2.5), run_time=4)
        self.wait()

        # h_line = plane.get_horizontal_line(plane.c2p(
        #     x.get_value(), np.cos(x.get_value())))

        h_line = always_redraw(lambda: plane.get_horizontal_line(plane.c2p(
            x.get_value(), np.cos(x.get_value()))))

        self.play(Create(h_line))
        self.wait()

        # v_line = plane.get_vertical_line(plane.c2p(
        #     x.get_value(), np.cos(x.get_value())))
        v_line = always_redraw(lambda: plane.get_vertical_line(plane.c2p(
            x.get_value(), np.cos(x.get_value()))))
        self.play(Create(v_line))
        self.wait()

        self.play(x.animate.set_value(0.5), run_time=3)
        self.wait()

        area = always_redraw(lambda: plane.get_area(
            graph=cos_graph, x_range=[neg_x, x.get_value()]))
        self.play(FadeIn(area))
        self.wait()
        self.play(x.animate.set_value(4), run_time=3)
        self.wait()
