from manim import *

class DotProduct(Scene):
    def cross_product(self):
        # Title for the dot product
        text = Tex("e. Cross Product", font_size=36)

        # Define the vectors and cross product equation
        a_vector = MathTex(r"\vec{a} = \begin{pmatrix} a_1 \\ a_2 \\ a_3 \end{pmatrix}", font_size=34)
        b_vector = MathTex(r"\vec{b} = \begin{pmatrix} b_1 \\ b_2 \\ b_3 \end{pmatrix}", font_size=34)
        cross_product_eq = MathTex(r"\vec{a} \times \vec{b} = \begin{pmatrix} a_2 b_3 - a_3 b_2 \\ a_3 b_1 - a_1 b_3 \\ a_1 b_2 - a_2 b_1 \end{pmatrix}", font_size=34)

        # Positioning the title and equations
        text.move_to(UP * 2)
        a_vector.move_to(UP)
        b_vector.next_to(a_vector, DOWN)
        cross_product_eq.next_to(b_vector, DOWN)

        # Display the process of cross product
        self.play(Write(text))
        self.play(Write(a_vector))
        self.play(Write(b_vector))
        self.wait(1)
        self.play(Write(cross_product_eq))

        # Wait and then fade out everything
        self.wait(2)
        self.play(FadeOut(a_vector, b_vector, cross_product_eq, text))

        
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

        # Second vector (red)
        vect2 = Line(
            start=plane.coords_to_point(0, 0),
            end=plane.coords_to_point(1, 3),
            stroke_color=RED,
        ).add_tip()
        vect2_name = MathTex("\\vec{w}").next_to(vect2, LEFT, buff=0.1).set_color(RED)

        # Projection of vector onto the other (green)
        projection = Line(
            start=plane.coords_to_point(0, 0),
            end=plane.coords_to_point(2.4, 1.6),
            stroke_color=GREEN,
        ).add_tip()
        projection_name = MathTex("Projection").next_to(projection, RIGHT, buff=0.1).set_color(GREEN)

        # Group all the elements for later animation
        stuff = VGroup(plane, vect1, vect1_name, vect2, vect2_name, projection, projection_name)

        # Box to encapsulate the animation
        box = RoundedRectangle(
            height=1.5, width=1.5, corner_radius=0.1, stroke_color=PINK
        ).to_edge(DL)

        # Draw the plane and the first two vectors
        self.play(DrawBorderThenFill(plane), run_time=2)
        self.wait()
        self.play(GrowFromPoint(vect1, point=vect1.get_start()), Write(vect1_name), run_time=2)
        self.wait()
        self.play(GrowFromPoint(vect2, point=vect2.get_start()), Write(vect2_name), run_time=2)
        self.wait()

        # Show projection as part of the dot product concept
        self.play(
            GrowFromPoint(projection, point=projection.get_start()),
            Write(projection_name),
            run_time=2,
        )
        self.wait()

        # Box everything into a small section
        self.add(box)
        self.wait()
        self.play(stuff.animate.move_to(box.get_center()).set(width=1.2), run_time=3)
        self.wait()

        # Perform dot product calculation display
        self.cross_product()
