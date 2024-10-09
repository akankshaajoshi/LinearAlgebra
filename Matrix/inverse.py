from manim import *

class MatrixInverses(Scene):
    def construct(self):
        # Title for the module
        title = Text("4.3 Matrix Inverses", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Conditions for Invertibility
        invertibility_text = Text("Conditions for Invertibility", font_size=36).to_edge(ORIGIN)
        conditions = Tex(r"A matrix $\mathbf{A}$ is invertible if:", font_size=28).next_to(invertibility_text, DOWN)
        condition_1 = Tex(r"1. $\mathbf{A}$ is square", font_size=28).next_to(conditions, DOWN)
        condition_2 = Tex(r"2. $\det(\mathbf{A}) \neq 0$", font_size=28).next_to(condition_1, DOWN)

        vgroup = VGroup(invertibility_text, conditions, condition_1, condition_2)

        vgroup.arrange(DOWN, buff=1)

        self.play(Write(vgroup))
        self.wait(2)

        # Transition to Finding Inverse
        self.play(FadeOut(vgroup))

        finding_inverse_text = Text("Finding the Inverse", font_size=28).to_edge(UP)
        self.play(Write(finding_inverse_text))

        # Show the formula for a 2x2 matrix inverse
        matrix_inverse_formula = MathTex(r"\mathbf{A}^{-1} = \frac{1}{\det(\mathbf{A})} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}")
        self.play(Write(matrix_inverse_formula))
        self.wait(2)
        self.play(FadeOut(matrix_inverse_formula))

        # Show a specific 2x2 matrix example
        example_matrix = MathTex(r"\mathbf{A} = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}")
        det_text = MathTex(r"\det(\mathbf{A}) = 1 \cdot 4 - 2 \cdot 3 = -2").next_to(example_matrix, DOWN)

        self.play(Write(example_matrix))
        self.wait(1)
        self.play(Write(det_text))
        self.wait(2)
        self.play(FadeOut(example_matrix, det_text))

        # Compute the inverse of the matrix
        inverse_example = MathTex(r"\mathbf{A}^{-1} = \frac{1}{-2} \begin{pmatrix} 4 & -2 \\ -3 & 1 \end{pmatrix} = \begin{pmatrix} -2 & 1 \\ \frac{3}{2} & -\frac{1}{2} \end{pmatrix}")
        self.play(Write(inverse_example))
        self.wait(2)
        self.play(FadeOut(inverse_example))

        # Transition to Matrix Inverse as Reverse Transformation
        # self.play(FadeOut(finding_inverse_text, matrix_inverse_formula, example_matrix, det_text, inverse_example))
