from manim import *

class BasesAndDimension(Scene):
    def construct(self):
        # Title for the module
        title = Text("5.2 Basis and Dimension", font_size=36)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # Definition of a Basis

        slide_title = Text("Basis", font_size=24).to_edge(UP)
        self.play(Write(slide_title))

        basis_text = Text("Basis: A set of linearly independent vectors that span a vector space.", font_size=24).next_to(slide_title, DOWN)
        self.play(Write(basis_text))
        self.wait(2)

        # Define two basis vectors u and v
        u = np.array([2, 1, 0])
        v = np.array([1, 2, 0])

        vec_u = Arrow(start=ORIGIN, end=u, buff=0, color=BLUE)
        vec_v = Arrow(start=ORIGIN, end=v, buff=0, color=GREEN)

        # Show vectors u and v on the screen
        label_u = MathTex(r"\vec{u}").next_to(vec_u.get_end(), UP)
        label_v = MathTex(r"\vec{v}").next_to(vec_v.get_end(), UP)

        self.play(Create(vec_u), Write(label_u))
        self.play(Create(vec_v), Write(label_v))
        self.wait()

        # Spanning the vector space (2D plane)
        span_plane = Polygon(ORIGIN, u, v, color=PURPLE, fill_opacity=0.3)
        span_text = Text("Span: u and v span a 2D plane", font_size=24, color=PURPLE).next_to(vec_u, DOWN)
        
        self.play(Create(span_plane), Write(span_text))
        self.wait(2)
        self.play(FadeOut(span_plane), FadeOut(vec_u), FadeOut(vec_v), FadeOut(label_u), FadeOut(label_v), FadeOut(span_text), FadeOut(basis_text), FadeOut(slide_title))

        # Highlighting the concept of dimension
        
   # Dimension Title and Text
        dimension_title = Text("Dimension", font_size=36).to_edge(UP)
        self.play(Write(dimension_title))

        dimension_text = Text(
            "Dimension: The number of vectors in a basis.", 
            font_size=24
        ).next_to(dimension_title, DOWN, buff=0.8)  # Add extra space using buff
        self.play(Write(dimension_text))
        self.wait(2)

        # Dimension Example
        dim_example = MathTex(r"\text{dim}(V) = 2").next_to(dimension_text, DOWN, buff=0.8)  # Add extra space using buff
        self.play(Write(dim_example))
        self.wait(2)

        # Transition to Transforming Bases
        self.play(FadeOut(dimension_text), FadeOut(dim_example), FadeOut(dimension_title))

        # Transforming Bases
        transforming_text = Text("Transforming Basis", font_size=28).to_edge(UP)
        self.play(Write(transforming_text))
        self.wait(1)

        # Define a new basis w and z
        w = np.array([3, 1, 0])
        z = np.array([1, -1, 0])

        vec_w = Arrow(start=ORIGIN, end=w, buff=0, color=YELLOW)
        vec_z = Arrow(start=ORIGIN, end=z, buff=0, color=ORANGE)

        # Display the new basis w and z
        label_w = MathTex(r"\vec{w}").next_to(vec_w.get_end(), UP)
        label_z = MathTex(r"\vec{z}").next_to(vec_z.get_end(), UP)

        self.play(Create(vec_w), Write(label_w))
        self.play(Create(vec_z), Write(label_z))
        self.wait()

        # Geometrically visualize transforming the old basis {u, v} to the new basis {w, z}
        self.play(Transform(vec_u, vec_w), Transform(vec_v, vec_z))
        self.wait(2)

        # Highlight that the span remains the same, though the basis changes
        span_plane_wz = Polygon(ORIGIN, w, z, color=PURPLE, fill_opacity=0.3)
        span_text_wz = Text("New Basis: w and z span the same plane", font_size=24, color=PURPLE).next_to(transforming_text, DOWN)

        self.play(Create(span_plane_wz), Write(span_text_wz))
        self.wait(2)
        self.play(FadeOut(span_plane_wz) ,FadeOut(vec_u), FadeOut(vec_v), FadeOut(vec_w), FadeOut(vec_z), FadeOut(label_w), FadeOut(label_z), FadeOut(span_text_wz), FadeOut(transforming_text))

        # Wrapping up with basis and dimension concepts
        summary_text = Text("Summary: Basis and Dimension", font_size=28).move_to(ORIGIN + UP * 1.5)  # Centered at the top
        summary_basis = Text(
            "A basis is a set of independent vectors that span the space.", 
            font_size=24, 
            color=BLUE
        ).next_to(summary_text, DOWN, buff=0.5)  # Below summary_text
        summary_dim = Text(
            "Dimension is the number of vectors in a basis.", 
            font_size=24, 
            color=GREEN
        ).next_to(summary_basis, DOWN, buff=0.5)  # Below summary_basis

        self.play(Write(summary_text), Write(summary_basis), Write(summary_dim))
        self.wait(2)

        # Fade out the scene
        self.play(FadeOut(summary_text), FadeOut(summary_basis), FadeOut(summary_dim))
