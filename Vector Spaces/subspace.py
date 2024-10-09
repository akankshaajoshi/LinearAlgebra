from manim import *

class SubspacesAndProperties(Scene):
    def construct(self):
        # Introduction text
        intro_text = Text("3.3 Subspaces: Definition and Properties", font_size=36)
        self.play(Write(intro_text))
        self.wait(2)
        self.play(FadeOut(intro_text))

        # Subspace definition
        definition_text = Text(
            "A subspace is a subset of a vector space that is closed ",
            font_size=24
        ).to_edge(UP)
        definition_text2 = Text("under vector addition and scalar multiplication.", font_size = 24).next_to(definition_text, DOWN)
        self.play(Write(definition_text))
        self.play(Write(definition_text2))
        self.wait(2)

        # Property 1: Closure under addition
        closure_add_text = Text("1. Closed under vector addition", font_size=24)
        closure_add_text.to_edge(UP)
        self.play(Transform(definition_text, closure_add_text))

        # Define two vectors u and v (in the subspace)
        u = np.array([1, 0.5, 0])  # Reduced size
        v = np.array([0.5, 1, 0])  # Reduced size

        vec_u = Arrow(start=ORIGIN, end=u, buff=0, color=BLUE)
        vec_v = Arrow(start=ORIGIN, end=v, buff=0, color=GREEN)

        # Show that u + v is still in the subspace
        u_plus_v = u + v
        vec_u_plus_v = Arrow(start=ORIGIN, end=u_plus_v, buff=0, color=YELLOW)

        self.play(Create(vec_u), Create(vec_v))
        self.play(Create(vec_u_plus_v))
        self.wait(2)

        # Property 2: Closure under scalar multiplication
        closure_scalar_text = Text("2. Closed under scalar multiplication", font_size=24)
        closure_scalar_text.to_edge(UP)
        self.play(Transform(definition_text, closure_scalar_text))

        # Show a scalar multiple of u
        scalar = 1.5
        vec_scalar_u = Arrow(start=ORIGIN, end=scalar * u, buff=0, color=RED)
        self.play(Create(vec_scalar_u))
        self.wait(2)

        # Transition to Column Space, Null Space, Row Space
        self.play(FadeOut(vec_u), FadeOut(vec_v), FadeOut(vec_u_plus_v), FadeOut(vec_scalar_u))
        self.play(FadeOut(closure_scalar_text), FadeOut(definition_text))

        # Column Space
        col_space_text = Text("Column Space", font_size=36)
        self.play(Write(col_space_text))
        self.wait(1)

        matrix_A = MathTex(
            r"A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}"
        ).to_edge(UP)
        self.play(Write(matrix_A))

        # Show two column vectors as vectors in 3D space
        col1 = np.array([1, 3, 5])
        col2 = np.array([2, 4, 6])
        vec_col1 = Arrow3D(start=ORIGIN, end=col1, color=BLUE)
        vec_col2 = Arrow3D(start=ORIGIN, end=col2, color=GREEN)

        # Geometric plane to show the column space (span of the column vectors)
        col_space_plane = Polygon(ORIGIN, col1, col2, color=PURPLE, fill_opacity=0.3)

        self.play(Create(vec_col1), Create(vec_col2))
        self.play(Create(col_space_plane))
        self.wait(2)

        # Null Space
        null_space_text = Text("Null Space", font_size=36)
        self.play(Transform(col_space_text, null_space_text))
        self.wait(1)

        # Introduce Ax = 0, show null space concept
        null_space_eq = MathTex(r"A \vec{x} = 0").next_to(matrix_A, DOWN)
        self.play(Write(null_space_eq))

        # Null space as vectors in the plane orthogonal to the column space
        null_vec = np.array([-2, 1, 0])
        vec_null = Arrow3D(start=ORIGIN, end=null_vec, color=YELLOW)

        self.play(Create(vec_null))
        self.wait(2)

        # Row Space
        row_space_text = Text("Row Space", font_size=36)
        self.play(Transform(null_space_text, row_space_text))
        self.wait(1)

        # Show row space as the span of row vectors
        row1 = np.array([1, 2, 0])
        row2 = np.array([3, 4, 0])
        vec_row1 = Arrow3D(start=ORIGIN, end=row1, color=ORANGE)
        vec_row2 = Arrow3D(start=ORIGIN, end=row2, color=PINK)

        # Row space plane
        row_space_plane = Polygon(ORIGIN, row1, row2, color=RED, fill_opacity=0.3)

        self.play(Create(vec_row1), Create(vec_row2))
        self.play(Create(row_space_plane))
        self.wait(2)

        # Final fade out
        self.play(FadeOut(vec_col1), FadeOut(vec_col2), FadeOut(vec_null),
                  FadeOut(vec_row1), FadeOut(vec_row2), FadeOut(col_space_plane),
                  FadeOut(row_space_plane), FadeOut(matrix_A), FadeOut(null_space_eq),
                  FadeOut(row_space_text))