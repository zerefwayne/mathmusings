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


class TaylorSeries(Scene):
    def construct(self):
        title = Text("Taylor Series")
        self.play(Write(title))
        self.wait()

        self.play(title.animate.scale(0.8).to_edge(UP, buff=1))
        self.wait()

        description = Text(
            "The Taylor series of a real or complex-valued function f(x) \nthat is infinitely differentiable at a real or complex number a is the power series:", font_size=24)
        self.play(Write(description))
        self.wait()
        self.play(description.animate.shift(UP*1.5))
        self.wait()
        long_formula = MathTex("g(x)=", "\\frac{f^{(0)}(x-a)}{0!}", "(x-a)^0", "+", "\\frac{f^{(1)}(x-a)}{1!}", "(x-a)^1", "+", "\\frac{f^{(2)}(x-a)}{2!}",
                               "(x-a)^2", "+", "\\frac{f^{(3)}(x-a)}{3!}", "(x-a)^3", "+", "...", font_size=24)

        colors = [YELLOW, PURPLE_A, RED, ORANGE]

        for i, color in enumerate(colors):
            long_formula[1 + 3*i].set_color(color)

        self.play(Write(long_formula))
        self.wait()

        mclauren_formula = MathTex("g(x)=", "\\frac{f(0)}{0!}", "x^0", "+", "\\frac{f^{'}(0)}{1!}", "x^1", "+", "\\frac{f^{''}(0)}{2!}",
                                   "x^2", "+", "\\frac{f^{'''}(0)}{3!}", "x^3", "+", "...", font_size=28).move_to(long_formula.get_center())

        for i, color in enumerate(colors):
            mclauren_formula[1 + 3*i].set_color(color)

        self.play(ReplacementTransform(long_formula, mclauren_formula))
        self.wait()

        title_new = Text("Maclaurin Series").scale(
            0.8).move_to(title.get_center())
        self.play(ReplacementTransform(title, title_new), FadeOut(description))
        self.wait()

        self.play(FadeOut(title_new), mclauren_formula.animate.to_edge(UR))
        self.wait()

        func_text = MathTex("g(x)", "=", "cos(x)")
        func_text[0].set_color(TEAL)
        self.play(Write(func_text))
        self.wait()
        self.play(func_text.animate.scale(0.7).to_edge(
            UL, buff=DEFAULT_MOBJECT_TO_EDGE_BUFFER * 1.5))
        self.wait()

        plane = NumberPlane(x_length=10, y_length=4,
                            x_range=[-5, 5], y_range=[-2, 2], axis_config={"include_numbers": True, "font_size": 16, "stroke_color": GRAY}, background_line_style={
                                "stroke_color": GRAY_D})

        self.play(DrawBorderThenFill(plane))
        self.wait()

        def func_cos(x): return np.cos(x)
        plot_cos = plane.plot(
            func_cos, x_range=[-5, 5], stroke_color=TEAL, stroke_opacity=0.75)
        self.play(Create(plot_cos, run_time=3))
        self.wait()

        p0_coeff = MathTex("1").set_color(YELLOW).scale(
            0.75).move_to(mclauren_formula[1].get_center())
        self.play(ReplacementTransform(mclauren_formula[1], p0_coeff))
        self.wait(2)

        def p0_func(x): return 1
        p0_graph = plane.plot(p0_func, x_range=[-5, 5], stroke_color=YELLOW)
        self.play(Create(p0_graph, run_time=3))
        self.wait(2)

        p1_coeff = MathTex("0").set_color(PURPLE_A).scale(
            0.75).move_to(mclauren_formula[4].get_center())
        self.play(ReplacementTransform(mclauren_formula[4], p1_coeff))
        self.wait(2)

        def p1_func(x): return 1
        p1_graph = plane.plot(p1_func, x_range=[-5, 5], stroke_color=PURPLE_A)
        self.play(ReplacementTransform(p0_graph, p1_graph))
        self.wait(2)

        p2_group = VGroup(mclauren_formula[6], mclauren_formula[7])

        p2_coeff = MathTex("-", "1").set_color(RED).scale(
            0.8).move_to(p2_group.get_center())
        self.play(ReplacementTransform(p2_group, p2_coeff))
        self.wait(2)

        def p2_func(x): return 1 - x**2
        p2_graph = plane.plot(p2_func, x_range=[-5, 5], stroke_color=RED)
        self.play(ReplacementTransform(p1_graph, p2_graph))
        self.wait(2)
