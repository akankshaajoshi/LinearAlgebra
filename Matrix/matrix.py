from manim import *

class MatrixIntroduction(Scene):
    def construct(self):
        # Title for the module
        title = Text("4. Matrices", font_size=48)
        self.play(Write(title))
        self.wait(1)

        # Introduction Section
        self.play(FadeOut(title))
        intro_title = Text("4.1 Introduction to Matrices", font_size=36)
        self.play(Write(intro_title))
        self.wait(1)
        self.play(FadeOut(intro_title))

        # Definition of a Matrix
        matrix_text_heading = Text("Definition of a Matrix", font_size=36).to_edge(UP)
        matrix_text = Text("A Matrix is a rectangular array of numbers.", font_size=24).next_to(matrix_text_heading, DOWN)
        self.play(Write(matrix_text_heading))
        self.play(Write(matrix_text))
        self.wait(1)

        # Show an example of a matrix
        matrix_example = MathTex(r"\mathbf{A} = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}")
        self.play(Write(matrix_example))
        self.wait(2)
        self.play(matrix_example.animate.move_to([0, 1.5, 0]))
        self.wait(1)
        self.play(FadeOut(matrix_example))
        self.wait(1)
        self.play(FadeOut(matrix_text), FadeOut(matrix_text_heading))
        
        intro_title = Text("4.2 Properties of Matrices", font_size=36)
        self.play(Write(intro_title))
        self.wait(1)
        self.play(FadeOut(intro_title))

        # Matrix Operations: Addition
        addition_text = Text("Matrix Addition", font_size=28).to_edge(UP)
        matrix_addition = MathTex(r"\mathbf{A} + \mathbf{B} = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} + \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}")
        result_addition = MathTex(r"= \begin{pmatrix} 6 & 8 \\ 10 & 12 \end{pmatrix}")

        self.play(Transform(matrix_text, addition_text))
        self.play(Write(matrix_addition))
        self.play(matrix_addition.animate.move_to([0, 1.5, 0]))
        self.wait(1)
        self.play(Write(result_addition))
        self.wait(2)
        
        # Transition to Matrix Multiplication
        self.play(FadeOut(matrix_addition), FadeOut(result_addition))
        self.play(FadeOut(addition_text, matrix_text))

        # Matrix Multiplication
        multiplication_text = Text("Matrix Multiplication", font_size=28).to_edge(UP)
        self.play(Write(multiplication_text))

        # Define matrices A and B
        matrix_A = MathTex(r"\mathbf{A} = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}")
        matrix_B = MathTex(r"\mathbf{B} = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}")
        matrix_A.next_to(matrix_B, LEFT, buff=1)

        # Display matrices A and B
        self.play(Write(matrix_A), Write(matrix_B))
        self.wait(1)

        # Highlight the second row of A and the first column of B
        row_A2 = SurroundingRectangle(matrix_A[0][5:7], color=BLUE)
        col_B1 = SurroundingRectangle(matrix_B[0][2:4], color=GREEN)
        self.play(Create(row_A2), Create(col_B1))
        self.wait(1)

        # Show the multiplication and addition for element (2,1)
        element_21 = MathTex(r"3 \cdot 5 + 4 \cdot 7 = 43").to_edge(DOWN)
        self.play(Write(element_21))
        self.wait(1)

        # Remove the green box and show the next step
        self.play(FadeOut(col_B1))

        # Highlight the second row of A and the second column of B
        col_B2 = SurroundingRectangle(matrix_B[0][6:9], color=GREEN)
        self.play(Create(col_B2))
        self.wait(1)

        # Show the multiplication and addition for element (2,2)
        element_22 = MathTex(r"3 \cdot 6 + 4 \cdot 8 = 50").to_edge(DOWN)
        self.play(Transform(element_21, element_22))
        self.play(FadeOut(row_A2, col_B2, element_21))
        self.wait(1)

        # Show the final result
        result_multiplication = MathTex(r"\mathbf{A} \times \mathbf{B} = \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}")
        self.play(FadeOut(matrix_A, matrix_B))
        self.play(Write(result_multiplication))
        self.wait(2)
        self.play(FadeOut(result_multiplication), FadeOut(multiplication_text))

        # Special Matrices: Identity, Diagonal, Zero
        # self.play(FadeOut(matrix_multiplication), FadeOut(result_multiplication))

        special_matrices_text = Text("Special Matrices", font_size=28).to_edge(UP)
        identity_matrix = MathTex(r"\mathbf{I} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}")
        diagonal_matrix = MathTex(r"\mathbf{D} = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}")
        zero_matrix = MathTex(r"\mathbf{0} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}")

        self.play(Write(special_matrices_text))
        self.play(Write(identity_matrix))
        self.wait(1)
        self.play(FadeOut(identity_matrix))
        self.wait(1)
        self.play(Write(diagonal_matrix))
        self.play(FadeOut(diagonal_matrix))
        self.wait(1)
        self.play(Write(zero_matrix))
        self.play(FadeOut(zero_matrix))
        self.wait(2)

        # Matrix Transformations on Vectors

        # transformation_text = Text("Matrix Transformations on Vectors", font_size=28).to_edge(UP)
        # self.play(Transform(matrix_text, transformation_text))

        # # Define a vector and a matrix
        # vector = np.array([2, 1, 0])
        # matrix_transform = MathTex(r"\mathbf{A} = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}")
        # vec_v = Arrow(start=ORIGIN, end=vector, buff=0, color=BLUE)
        # label_v = MathTex(r"\vec{v} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}").next_to(vec_v.get_end(), UP)

        # self.play(Create(vec_v), Write(label_v))
        # self.wait(1)

        # # Apply matrix transformation
        # transformed_vector = np.dot([[1, 2], [3, 4]], [2, 1])
        # vec_Av = Arrow(start=ORIGIN, end=[transformed_vector[0], transformed_vector[1], 0], buff=0, color=YELLOW)
        # label_Av = MathTex(r"\mathbf{A} \vec{v} = \begin{pmatrix} 4 \\ 10 \end{pmatrix}").next_to(vec_Av.get_end(), UP)

        # self.play(Write(matrix_transform))
        # self.wait(1)
        # self.play(Transform(vec_v, vec_Av), Transform(label_v, label_Av))
        # self.wait(2)

        # # Conclusion
        # conclusion_text = Text("Matrix operations transform vectors geometrically.", font_size=24).to_edge(UP)
        # self.play(FadeOut(matrix_transform), FadeOut(vec_Av), FadeOut(label_Av))
        # self.play(Write(conclusion_text))
        # self.wait(2)
