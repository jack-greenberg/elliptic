from manimlib.imports import *
from manimlib.mobject.svg.svg_mobject import *
from manimlib.animation.indication import *
from manimlib.animation.transform import *
from manimlib.utils.space_ops import angle_of_vector
import math
import manimlib.constants as consts
from fractions import Fraction

L,U,R,D = LEFT, UP, RIGHT, DOWN


class CurveAnimation(GraphScene):
    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": -4,
        "y_max": 4,
        "graph_origin": ORIGIN,
        "function_color": BLUE_D,
        "axes_color": BLACK,
        "x_axis_label": "",
        "y_axis_label": "",
        "camera_config":{"background_color":"#FFFFFF"},
    }

    def construct(self):
        self.setup_axes(animate=False)

        fn_text = TextMobject("$y^2 = x^3 + Ax + B$").scale(.75).set_color(BLACK).move_to(3*UL+2*L)

        self.play(
            Write(fn_text)
        )

        self.wait(1.5)

        # Curve 1
        fn1 = self.curve(-1, 5, 1.90416).set_color(BLUE_E)
        fn1_text = TextMobject("$y^2 = x^3 - x + 5$").scale(.75).move_to(3*UL+2*L).set_color(BLACK)
        a1 = TextMobject("$a = -1$").scale(.75).set_color(BLACK).next_to(fn1_text, DOWN)
        b1 = TextMobject("$b = 5$").scale(.75).set_color(BLACK).next_to(a1, DOWN)

        self.play(
            ShowCreation(fn1),
            Write(a1),
            Write(b1),
            Transform(fn_text, fn1_text),
        )

        self.wait(1)

        # Curve 2
        fn2 = self.curve(0, 0, 0).set_color(BLUE_E)
        fn2_text = TextMobject("$y^2 = x^3$").scale(.75).move_to(3*UL+2*L).set_color(BLACK)
        a2 = TextMobject("$a = 0$").scale(.75).next_to(fn2_text, DOWN).set_color(BLACK)
        b2 = TextMobject("$b = 0$").scale(.75).next_to(a1, DOWN).set_color(BLACK)

        self.play(
            Transform(
                fn1, fn2
            ),
            Transform(
                a1,
                a2,
            ),
            Transform(
                b1,
                b2,
            ),
            Transform(
                fn_text,
                fn2_text,
            )
        )

        self.wait(1)

        # Curve 3
        fn3 = self.curve(-2, 2, 1.769).set_color(BLUE_E)
        fn3_text = TextMobject("$y^2 = x^3 -2x + 2$").scale(.75).move_to(3*UL+2*L).set_color(BLACK)
        a3 = TextMobject("$a = -2$").scale(.75).next_to(fn2_text, DOWN).set_color(BLACK)
        b3 = TextMobject("$b = 2$").scale(.75).next_to(a1, DOWN).set_color(BLACK)

        self.play(
            Transform(
                fn1, fn3
            ),
            Transform(
                a1,
                a3,
            ),
            Transform(
                b1,
                b3,
            ),
            Transform(
                fn_text,
                fn3_text,
            )
        )

        self.wait(2)

        
    def curve(self, a, b, c):
        """
        Curve constructor
        """
        def inner(t):
            if t <= 0:
                x = -t - c
                return self.coords_to_point(x, -((x**3 + a*x + b)**.5))
            x = t - c
            return self.coords_to_point(x, (x**3 + a*x + b)**.5)
        #  return inner
        return ParametricFunction(function=inner, t_min=-5, t_max=5)
