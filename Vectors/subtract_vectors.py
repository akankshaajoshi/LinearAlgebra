from manim import *

class SubtractVectors(Scene):
    def scalar_multiply(self):
        text = Tex("c. Scalar Multiplication", font_size=36)
        text1 = Tex("Multiplication with a scalar results into k times the factor of original vector", font_size=30)

        # Define vector and scalar multiplication using LaTeX
        a_vector = MathTex(r"\vec{a} = \begin{pmatrix} a_1 \\ a_2 \end{pmatrix}", font_size=34)
        scalar_mult = MathTex(r"k \vec{a} = k \begin{pmatrix} a_1 \\ a_2 \end{pmatrix} = \begin{pmatrix} k a_1 \\ k a_2 \end{pmatrix}", font_size=34)

        # Positioning the title and equations
        text.move_to(UP * 2)
        text1.next_to(text, DOWN)
        a_vector.next_to(text1, DOWN)
        scalar_mult.next_to(a_vector, DOWN)

        # Display scalar multiplication process
        self.play(Write(text))
        self.play(Write(text1))
        self.play(Write(a_vector))
        self.wait(1)
        self.play(Write(scalar_mult))

        # Wait and then fade out everything
        self.wait(2)
        self.play(FadeOut(a_vector, scalar_mult, text))

    def construct(self):
        plane = NumberPlane(
            x_range=[-5, 5, 1], y_range=[-4, 4, 1], x_length=10, y_length=7
        )
        plane.add_coordinates()

        # First vector (yellow)
        vect1 = Line(
            start=plane.coords_to_point(0, 0),
            end=plane.coords_to_point(3, 2),
            stroke_color=YELLOW,
        ).add_tip()
        vect1_name = MathTex("\\vec{v}").next_to(vect1, RIGHT, buff=0.1).set_color(YELLOW)

        # Second vector (red) to subtract
        vect2 = Line(
            start=plane.coords_to_point(0, 0),
            end=plane.coords_to_point(-2, 1),
            stroke_color=RED,
        ).add_tip()
        vect2_name = MathTex("\\vec{w}").next_to(vect2, LEFT, buff=0.1).set_color(RED)

        # Resultant vector for subtraction
        vect3 = Line(
            start=plane.coords_to_point(3, 2),
            end=plane.coords_to_point(5, 1),
            stroke_color=RED,
        ).add_tip()

        # Subtracted resultant vector (green)
        vect4 = Line(
            start=plane.coords_to_point(0, 0),
            end=plane.coords_to_point(5, 1),
            stroke_color=GREEN,
        ).add_tip()
        vect4_name = MathTex("\\vec{v} - \\vec{w}").next_to(vect4, LEFT, buff=0.1).set_color(GREEN)

        # Group everything for later animation
        stuff = VGroup(
            plane, vect1, vect1_name, vect2, vect2_name, vect3, vect4, vect4_name
        )

        # Box to shrink the scene into
        box = RoundedRectangle(
            height=1.5, width=1.5, corner_radius=0.1, stroke_color=PINK
        ).to_edge(DL)

        # Draw plane and vectors with animations
        self.play(DrawBorderThenFill(plane), run_time=2)
        self.wait()
        self.play(GrowFromPoint(vect1, point=vect1.get_start()), Write(vect1_name), run_time=2)
        self.wait()
        self.play(GrowFromPoint(vect2, point=vect2.get_start()), Write(vect2_name), run_time=2)
        self.wait()

        # Subtract vect2 from vect1
        self.play(Transform(vect2, vect3), vect2_name.animate.next_to(vect3, UP, buff=0.1), run_time=2)
        self.wait()

        # Show resultant vector subtraction
        self.play(
            LaggedStart(GrowFromPoint(vect4, point=vect4.get_start())),
            Write(vect4_name),
            run_time=3,
            lag_ratio=1,
        )
        self.wait()

        # Box everything into a small section
        self.add(box)
        self.wait()
        self.play(stuff.animate.move_to(box.get_center()).set(width=1.2), run_time=3)
        self.wait()

        # Perform mathematical subtraction display
        self.scalar_multiply()
