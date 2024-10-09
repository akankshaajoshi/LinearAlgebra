from manim import *

class DeterminantsIntroduction(Scene):
    def construct(self):
        # Title for the module
        title = Text("Introduction to Determinants", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Definition of Determinants
        determinant_text = Text("Definition of Determinants", font_size=28).to_edge(UP)
        self.play(Write(determinant_text))
        
        determinant_formula = MathTex(r"\det(\mathbf{A}) = ad - bc \text{ for a 2x2 matrix } \mathbf{A} = \begin{pmatrix} a & b \\ c & d \end{pmatrix}")
        self.play(Write(determinant_formula))
        self.wait(2)

        # Geometric Interpretation
        self.play(FadeOut(determinant_text, determinant_formula))
        
        geo_text = Text("Geometric Interpretation of Determinants", font_size=28).to_edge(UP)
        self.play(Write(geo_text))
        
        # 2D Parallelogram (Determinant as Area)
        square = Square(side_length=2, color=BLUE).shift(LEFT)
        label_square = Text("Unit Square", font_size=24).next_to(square, DOWN)
        self.play(Create(square), Write(label_square))
        self.wait(1)
        
        parallelogram = Polygon(ORIGIN, RIGHT, 2 * RIGHT + 1.5 * UP, 1.5 * UP, color=YELLOW)
        label_parallelogram = Text("Transformed Parallelogram", font_size=24).next_to(parallelogram, DOWN)
        self.play(Transform(square, parallelogram), Transform(label_square, label_parallelogram))
        self.wait(1)

        # Show area scaling
        determinant_area_text = Text("Determinant as Area Scaling Factor", font_size=24).to_edge(UP)
        area_text = Text("Area of Transformed Parallelogram = |det(A)|", font_size=20).next_to(parallelogram, RIGHT)

        self.play(Transform(geo_text, determinant_area_text))
        self.play(Write(area_text))
        self.wait(2)

        # Move to 3D Volume Visualization
        self.play(FadeOut(parallelogram, label_parallelogram, area_text, determinant_area_text))

        volume_text = Text("Determinant in 3D: Volume Scaling", font_size=28).to_edge(UP)
        self.play(Write(volume_text))
        
        # Cube and Transformed Parallelepiped
        cube = Cube(side_length=2, color=BLUE).shift(LEFT)
        label_cube = Text("Unit Cube", font_size=24).next_to(cube, DOWN)
        self.play(Create(cube), Write(label_cube))
        self.wait(1)

        # Transformed parallelepiped
        transformed_cube = Prism(dimensions=[2, 3, 1.5], color=YELLOW).shift(LEFT)
        label_transformed_cube = Text("Transformed Parallelepiped", font_size=24).next_to(transformed_cube, DOWN)
        self.play(Transform(cube, transformed_cube), Transform(label_cube, label_transformed_cube))
        self.wait(2)

        # Volume Scaling
        determinant_volume_text = Text("Volume = |det(A)|", font_size=24).to_edge(UP)
        self.play(Write(determinant_volume_text))
        self.wait(2)

        # Conclusion
        conclusion_text = Text("Determinants Scale Area/Volume in 2D/3D", font_size=24).to_edge(UP)
        self.play(FadeOut(volume_text, transformed_cube, label_transformed_cube, determinant_volume_text))
        self.play(Write(conclusion_text))
        self.wait(2)