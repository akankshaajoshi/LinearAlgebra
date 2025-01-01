from manim import *

class LinearTransformationExplained(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            show_basis_vectors=True,
        )

    def construct(self):
        # Title Slide
        title = Text("Linear Transformation", font_size=48).to_edge(UP)
        subtitle = Text("Visualizing Matrix Transformations in 2D Space", font_size=24, color=GRAY).next_to(title, DOWN)
        self.add(title, subtitle)
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))

        # Scene Setup
        matrix = [[1, 2], [2, 1]]
        matrix_tex = (
            MathTex(r"A = \begin{bmatrix} 1 & 2 \\ 2 & 1 \end{bmatrix}")
            .to_edge(UL)
            .add_background_rectangle()
        )

        unit_square = self.get_unit_square()
        self.add_transformable_mobject(unit_square)
        self.add_background_mobject(matrix_tex)

        # Vector Transformation
        vect = self.get_vector([1, -2], color=PURPLE_B)
        self.add_transformable_mobject(vect)
        self.play(Write(vect))
        self.wait(1)

        # Display Determinant Text
        determinant_text = MathTex("\text{Det}(A) = -3", color=YELLOW).scale(0.8).to_corner(UR).add_background_rectangle()
        self.add_background_mobject(determinant_text)
        self.wait(1)

        # Add unit square text
        unit_square_text = always_redraw(
            lambda: Text("Det(A)", font_size=24, color=BLUE).move_to(unit_square.get_center())
        )
        self.add(unit_square_text)

        # Apply Transformation
        self.apply_matrix(matrix)
        self.wait(2)

        # Explain Transformation
        explanation = Text(
            "The unit square transforms into a parallelogram,\nscaled and flipped based on the determinant.",
            font_size=24,
            color=GRAY
        ).to_edge(DOWN).add_background_rectangle()
        self.play(Write(explanation))
        self.wait(4)
        self.play(FadeOut(explanation))