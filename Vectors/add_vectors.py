from manim import *

class AddVectors(Scene):

    def subtract(self):
        text = Tex("b. Vector Subtraction", font_size=36)

        # Define vectors using LaTeX
        a_vector = MathTex(r"\vec{a} = \begin{pmatrix} a_1 \\ a_2 \end{pmatrix}", font_size=34)
        b_vector = MathTex(r"\vec{b} = \begin{pmatrix} b_1 \\ b_2 \end{pmatrix}", font_size=34)
        subtraction_eq = MathTex(r"\vec{a} - \vec{b} = \begin{pmatrix} a_1 - b_1 \\ a_2 - b_2 \end{pmatrix}", font_size=34)

        # Position vectors and equation
        text.move_to(UP * 2)
        a_vector.move_to(UP)
        b_vector.next_to(a_vector, DOWN)
        subtraction_eq.next_to(b_vector, DOWN)

        # Display vectors and the subtraction process
        self.play(Write(text))
        self.play(Write(a_vector))
        self.play(Write(b_vector))
        self.wait(1)

        # Perform the subtraction operation
        self.play(Write(subtraction_eq))

        # Wait and then fade out everything
        self.wait(2)
        self.play(FadeOut(a_vector, b_vector, subtraction_eq, text))

    def construct(self):
        plane = NumberPlane(
            x_range=[-5, 5, 1], y_range=[-4, 4, 1], x_length=10, y_length=7
        )
        plane.add_coordinates()
        # plane.shift(RIGHT * 2)

        vect1 = Line(
            start=plane.coords_to_point(0, 0),
            end=plane.coords_to_point(3, 2),
            stroke_color=YELLOW,
        ).add_tip()
        vect1_name = (
            MathTex("\\vec{v}").next_to(vect1, RIGHT, buff=0.1).set_color(YELLOW)
        )

        vect2 = Line(
            start=plane.coords_to_point(0, 0),
            end=plane.coords_to_point(-2, 1),
            stroke_color=RED,
        ).add_tip()
        vect2_name = MathTex("\\vec{w}").next_to(vect2, LEFT, buff=0.1).set_color(RED)

        vect3 = Line(
            start=plane.coords_to_point(3, 2),
            end=plane.coords_to_point(1, 3),
            stroke_color=RED,
        ).add_tip()

        vect4 = Line(
            start=plane.coords_to_point(0, 0),
            end=plane.coords_to_point(1, 3),
            stroke_color=GREEN,
        ).add_tip()
        vect4_name = (
            MathTex("\\vec{v} + \\vec{w}")
            .next_to(vect4, LEFT, buff=0.1)
            .set_color(GREEN)
        )

        stuff = VGroup(
            plane, vect1, vect1_name, vect2, vect2_name, vect3, vect4, vect4_name
        )

        box = RoundedRectangle(
            height=1.5, width=1.5, corner_radius=0.1, stroke_color=PINK
        ).to_edge(DL)

        self.play(DrawBorderThenFill(plane), run_time=2)
        self.wait()
        self.play(
            GrowFromPoint(vect1, point=vect1.get_start()), Write(vect1_name), run_time=2
        )
        self.wait()
        self.play(
            GrowFromPoint(vect2, point=vect2.get_start()), Write(vect2_name), run_time=2
        )
        self.wait()
        self.play(
            Transform(vect2, vect3),
            vect2_name.animate.next_to(vect3, UP, buff=0.1),
            run_time=2,
        )
        self.wait()
        self.play(
            LaggedStart(GrowFromPoint(vect4, point=vect4.get_start())),
            Write(vect4_name),
            run_time=3,
            lag_ratio=1,
        )
        self.wait()
        self.add(box)
        self.wait()
        self.play(stuff.animate.move_to(box.get_center()).set(width=1.2), run_time=3)
        self.wait()
        self.subtract()

