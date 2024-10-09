from manim import *

class CrossProduct(ThreeDScene):
    # def cross_product_formula(self):
    #     # Title for the cross product
    #     text = Tex("e. Cross Product", font_size=36)

    #     # Define the vectors and cross product equation
    #     a_vector = MathTex(r"\vec{a} = \begin{pmatrix} a_1 \\ a_2 \\ a_3 \end{pmatrix}", font_size=34)
    #     b_vector = MathTex(r"\vec{b} = \begin{pmatrix} b_1 \\ b_2 \\ b_3 \end{pmatrix}", font_size=34)
    #     cross_product_eq = MathTex(
    #         r"\vec{a} \times \vec{b} = |\vec{a}| |\vec{b}| \sin\theta \hat{n}", font_size=34
    #     )
    #     detailed_eq = MathTex(
    #         r"= \begin{pmatrix} a_2 b_3 - a_3 b_2 \\ a_3 b_1 - a_1 b_3 \\ a_1 b_2 - a_2 b_1 \end{pmatrix}", font_size=34
    #     )

    #     # Positioning the title and equations
    #     text.move_to(UP * 2)
    #     a_vector.move_to(UP)
    #     b_vector.next_to(a_vector, DOWN)
    #     cross_product_eq.next_to(b_vector, DOWN)
    #     detailed_eq.next_to(cross_product_eq, DOWN)

    #     # Display the process of cross product
    #     self.play(Write(text))
    #     self.play(Write(a_vector))
    #     self.play(Write(b_vector))
    #     self.wait(1)
    #     self.play(Write(cross_product_eq))
    #     self.wait(1)
    #     self.play(Write(detailed_eq))

    #     # Wait and then fade out everything
    #     self.wait(2)
    #     self.play(FadeOut(a_vector, b_vector, cross_product_eq, detailed_eq, text))

    def construct(self):
        # Create a 3D scene with axes
        axes = ThreeDAxes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            z_range=[-5, 5, 1],
            x_length=8,
            y_length=8,
            z_length=8,
        )

        # Define vectors for the cross product (3D vectors)
        vector_a = Arrow3D(start=[0, 0, 0], end=[2, 1, 0], color=YELLOW)
        vector_b = Arrow3D(start=[0, 0, 0], end=[0, 2, 1], color=RED)
        vector_cross = Arrow3D(start=[0, 0, 0], end=[1, -2, 3], color=GREEN)

        # Label the vectors
        a_label = MathTex(r"\vec{a}").next_to(vector_a, RIGHT, buff=0.1).set_color(YELLOW)
        b_label = MathTex(r"\vec{b}").next_to(vector_b, RIGHT, buff=0.1).set_color(RED)
        cross_label = MathTex(r"\vec{a} \times \vec{b}").next_to(vector_cross, RIGHT, buff=0.1).set_color(GREEN)

        # Draw axes and vectors
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        self.play(Create(axes))
        self.wait()

        # Draw the vectors
        self.play(Create(vector_a), Write(a_label))
        self.wait()
        self.play(Create(vector_b), Write(b_label))
        self.wait()

        # Show the cross product result
        self.play(Create(vector_cross), Write(cross_label))
        self.wait()

        # Switch to the formula explanation
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, run_time=3)
        # self.cross_product_formula()