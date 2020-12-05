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

        self.wait(1)

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


class MoveAlongPathPiece(Animation):
    def __init__(self, mobject, mobject2, path, t_min, t_max, t_min2, t_max2, **kwargs):
        self.mobject = mobject
        self.mobject2 = mobject2
        self.path = path
        self.t_min = t_min
        self.t_max = t_max
        self.t_min2 = t_min2
        self.t_max2 = t_max2
        self.label = kwargs["label"]
        self.labelp = kwargs["labelp"]
        self.label2 = kwargs["label2"]
        self.labelp2 = kwargs["labelp2"]
        super().__init__(mobject, **kwargs)

    def interpolate_mobject(self, alpha):
        self.point = self.path.get_point_from_function(self.t_min+alpha*(self.t_max-self.t_min))
        self.point2 = self.path.get_point_from_function(self.t_min2+alpha*(self.t_max2-self.t_min2))
        self.mobject.move_to(self.point)
        self.label.next_to(self.point,self.labelp)
        self.mobject2.move_to(self.point2)
        self.label2.next_to(self.point2,self.labelp2)


class MovePointsWithLine(MoveAlongPathPiece):
    def __init__(self, line, *args, **kwargs):
        self.line = line
        super().__init__(*args, **kwargs)

    def interpolate_mobject(self, alpha):
        super().interpolate_mobject(alpha)
        self.line.set_angle(angle_of_vector(self.point2-self.point))
        self.line.move_to(self.point)


class MovePointsWithLineAndThirdPoint(MovePointsWithLine):
    def __init__(self, c2p, p2c, mobject3, *args, **kwargs):
        self.mobject3 = mobject3
        self.c2p = c2p
        self.p2c = p2c
        self.label3 = kwargs["label3"]
        self.labelp3 = kwargs["labelp3"]
        super().__init__(*args, **kwargs)

    def interpolate_mobject(self, alpha):
        super().interpolate_mobject(alpha)
        c1,c2 = self.p2c(self.point), self.p2c(self.point2)
        m = (c2[1]-c1[1])/(c2[0]-c1[0])
        self.point3 = [m**2-c1[0]-c2[0]]
        self.point3.append(c1[1]+m*(self.point3[0]-c1[0]))
        self.mobject3.move_to(self.c2p(self.point3[0], self.point3[1]))
        self.label3.next_to(self.c2p(self.point3[0], self.point3[1]),self.labelp3)


class PointAddition(GraphScene):
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

        fn_text = TextMobject("$y^2 = x^3 - 2x + 2$").scale(.75).set_color(BLACK).move_to(3*UL+2*L)

        fn = self.curve(-2, 2, 1.769).set_color(BLUE_E)

        gp = fn.get_point_from_function

        T1 = 0.1
        T2 = 2

        P = Dot(gp(T1), color=BLACK)
        Q = Dot(gp(T2), color=BLACK)

        P_label = TextMobject("$P$",color=BLACK).scale(0.75).next_to(gp(T1), LEFT)
        Q_label = TextMobject("$Q$",color=BLACK).scale(0.75).next_to(gp(T2), 0.707*UR)

        self.play(
            Write(fn_text),
            ShowCreation(fn),
        )

        self.wait(1)

        line = Line()
        line.set_angle(angle_of_vector(gp(T2) - gp(T1)))
        line.move_to(gp(T1))
        line.set_length(20)
        line.set_color(GREEN_C)
        line.set_opacity(0.8)

        self.play(
            ShowCreation(line),
            ShowCreation(P),
            ShowCreation(Q),
            Write(P_label),
            Write(Q_label)
        )

        self.wait(1)

        point1, point2 = self.point_to_coords(gp(T1)), self.point_to_coords(gp(T2))

        negR = Dot(color=RED_E)

        m = (point2[1] - point1[1]) / (point2[0] - point1[0])

        point3 = [m**2 - point1[0] - point2[0]]

        point3.append(point1[1] + m*(point3[0] - point1[0]))

        negR.move_to(self.coords_to_point(point3[0], point3[1]))
        negR_label = TextMobject("$-R$", color=RED_E).scale(0.75).next_to(negR, 0.707*DR).set_fill(RED_E).set_color(RED_E).set_stroke(color=RED_E, width=0)

        self.play(ShowCreation(negR), Write(negR_label))

        self.wait(1)

        vert_line = DashedLine(
            self.coords_to_point(point3[0], point3[1]),
            self.coords_to_point(point3[0], -1*point3[1]),
            color=RED_E
        )

        R = Dot(color=RED_E)
        R.move_to(self.coords_to_point(point3[0], -1*point3[1]))
        R_label = TextMobject("$R$", color=RED_E).scale(0.75).next_to(R, 0.707*UR).set_fill(RED_E).set_color(RED_E).set_stroke(color=RED_E, width=0)

        self.play(
            ShowCreation(vert_line),
        )
        self.play(
            ShowCreation(R),
            Write(R_label)
        )

        eqn = TextMobject("$P + Q = R$").scale(0.75).move_to(DOWN+5*RIGHT).set_fill(BLACK).set_stroke(BLACK).set_color(BLACK)

        self.play(
            Write(eqn)
        )
        

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


class PointDouble(GraphScene):
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
        fn_text = TextMobject("$y^2 = x^3 - 2x + 2$").scale(.75).set_color(BLACK).move_to(3*UL+2*L)
        fn = self.curve(-2, 2, 1.769).set_color(BLUE_E)
        gp = fn.get_point_from_function
        T1 = 0.1
        T2 = 2
        P = Dot(gp(T1), color=BLACK)
        Q = Dot(gp(T2), color=BLACK)
        P_label = TextMobject("$P$",color=BLACK).scale(0.75).next_to(gp(T1), .707*UL)
        Q_label = TextMobject("$Q$",color=BLACK).scale(0.75).next_to(gp(T2), .707*UR)

        line = Line()
        line.set_angle(angle_of_vector(gp(T2) - gp(T1)))
        line.move_to(gp(T1))
        line.set_length(20)
        line.set_color(GREEN_C)
        line.set_opacity(0.8)

        self.add(fn_text, fn, P, P_label, Q, Q_label, line)

        self.wait(1)

        self.play(
            MovePointsWithLine(
                line,
                P,
                Q,
                fn,
                T1, T1+.75,
                T2, T1+.7501,
                label=P_label,
                labelp=.707*UL,
                label2=Q_label,
                labelp2=0.707*UR
            )
        )


        self.wait(1)

        point = self.point_to_coords(gp(T1+.75))

        negR = Dot(color=RED_E)

        m = (3*(point[0]**2) + (-2)) / (2*point[1])
        point3 = [m**2 - point[0] - point[0]]
        point3.append(point[1] + m*(point3[0] - point[0]))

        negR.move_to(self.coords_to_point(point3[0], point3[1]))
        negR_label = TextMobject("$-R$", color=RED_E).scale(0.75).next_to(negR, 0.707*DR).set_fill(RED_E).set_color(RED_E).set_stroke(color=RED_E, width=0)

        self.play(ShowCreation(negR), Write(negR_label))

        self.wait(1)

        vert_line = DashedLine(
            self.coords_to_point(point3[0], point3[1]),
            self.coords_to_point(point3[0], -1*point3[1]),
            color=RED_E
        )

        R = Dot(color=RED_E)
        R.move_to(self.coords_to_point(point3[0], -1*point3[1]))
        R_label = TextMobject("$R$", color=RED_E).scale(0.75).next_to(R, 0.707*UR).set_fill(RED_E).set_color(RED_E).set_stroke(color=RED_E, width=0)

        self.play(
            ShowCreation(vert_line),
        )
        self.play(
            ShowCreation(R),
            Write(R_label)
        )

        eqn = TextMobject("$P + P = 2P = R$").scale(0.75).move_to(DOWN+5*RIGHT).set_fill(BLACK).set_stroke(BLACK).set_color(BLACK)

        self.play(Write(eqn))

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
