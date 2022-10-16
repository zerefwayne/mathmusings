import numpy as np
from manim import *


class Charge(Dot):
    def __init__(self, location=ORIGIN, magnitude=1, is_positive=True, **kwargs):
        super().__init__(
            location, radius=magnitude * DEFAULT_DOT_RADIUS, color=RED if is_positive else BLUE, **kwargs)
        self.location = location
        self.magnitude = magnitude
        self.charge = self.magnitude if is_positive else -1 * self.magnitude

    def diff(self, pos):
        vec = pos - self.location
        # makes the vectors smaller and prettier
        r = (np.linalg.norm(vec) + 1e-10) * 2
        return vec * (self.charge / (r ** 2))


class ChargesField(Scene):
    def construct(self):
        charges = [
            Charge(LEFT, magnitude=1, is_positive=True),
            Charge(RIGHT, magnitude=1, is_positive=True),
            Charge(4 * UP, magnitude=2, is_positive=False),
        ]
        self.play(FadeIn(charges[0], charges[1]))
        self.play(FadeIn(charges[2]))

        def func(pos):
            res = ORIGIN
            for charge in charges:
                res = res + charge.diff(pos)
            return res

        def length_func(length): return min(length * 5, 0.3)

        electric_field = ArrowVectorField(func, length_func=length_func)

        self.play(Write(electric_field))

        electric_field.add_updater(lambda mob: mob.become(
            ArrowVectorField(func, length_func=length_func)))

        def charge_updater(mob, dt):
            mob.shift(DOWN*dt)
            mob.location = mob.get_center()

        charges[2].add_updater(charge_updater)
        self.wait(10)
        charges[2].clear_updaters()
