from manim import *

class LinearTransformationIntro(Scene):

    def title(self):
        # Title Slide
        intro_title = Text("6. Linear Transformation", font_size=36)
        self.play(Write(intro_title))
        self.wait(1)
        self.play(FadeOut(intro_title))

    def construct(self):

        self.title()

class LinearTransformationSummary(Scene):
    def linear_transformation(self):
        # Title for the linear transformation explanation
        title = MathTex(r"\text{Linear Transformation}", font_size=36).to_edge(UP)
        
        # Create the text explaining the concept of linear transformations
        points = VGroup(
            MathTex(r"1.\ \text{A linear transformation maps vectors to new vectors.}", font_size=24),
            MathTex(r"2.\ \text{A transformation is represented by a matrix } A \text{ such that } T(\mathbf{x}) = A\mathbf{x}.", font_size=24),
            MathTex(r"3.\ \text{It preserves vector addition and scalar multiplication.}", font_size=24),
            MathTex(r"4.\ \text{The matrix } A \text{ performs the transformation on a vector.}", font_size=24),
            MathTex(r"5.\ \text{For example: } T(\mathbf{x}) = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix} \mathbf{x}", font_size=24),
            MathTex(r"6.\ \text{The determinant of } A \text{ indicates scaling and orientation.}", font_size=24),
        ).arrange(DOWN, center=True, buff=0.8).move_to(ORIGIN) 
        
        # Animating the title and the text
        self.play(Write(title))
        self.wait(1)
        self.play(FadeIn(points, lag_ratio=0.1))
        self.wait(4)
        self.play(FadeOut(title), FadeOut(points))

    def construct(self):
        self.linear_transformation()