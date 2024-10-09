from manim import *

class Operations(Scene):
    def title(self):
        # Introduction Section
        intro_title = Text("2.2 Operations on Vectors", font_size=36)
        self.play(Write(intro_title))
        self.wait(1)
        self.play(FadeOut(intro_title))

    def introduction(self):
        # What is a Vector?
        what_is = Text("Vector Operations", font_size=30)
        what_is.move_to(UP * 2.8)
        self.play(Write(what_is))
        self.wait(1)

        text1 = Tex(r"Assuming we have two vectors,", font_size=28) 
        
        addition_eq = MathTex(r"\text{Addition: } \vec{a} + \vec{b} = \begin{pmatrix} a_1 + b_1 \\ a_2 + b_2 \end{pmatrix}", font_size =26 )
        subtraction_eq = MathTex(r"\text{Subtraction: } \vec{a} - \vec{b} = \begin{pmatrix} a_1 - b_1 \\ a_2 - b_2 \end{pmatrix}", font_size =26)
        scalar_mult_eq = MathTex(r"\text{Scalar multiplication: } k \vec{a} = k \begin{pmatrix} a_1 \\ a_2 \end{pmatrix}", font_size =26)
        dot_product_eq = MathTex(r"\text{Dot product: } \vec{a} \cdot \vec{b} = a_1 b_1 + a_2 b_2", font_size =26)
        cross_product_eq = MathTex(r"\text{Cross product: } \vec{a} \times \vec{b} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \end{vmatrix} = \left( (a_2 b_3 - a_3 b_2), (a_3 b_1 - a_1 b_3), (a_1 b_2 - a_2 b_1) \right)", font_size =26)

        # Position the equations on the screen
        text1.next_to(what_is, DOWN)
        addition_eq.next_to(text1, DOWN)
        subtraction_eq.next_to(addition_eq, DOWN)
        scalar_mult_eq.next_to(subtraction_eq, DOWN)
        dot_product_eq.next_to(scalar_mult_eq, DOWN)
        cross_product_eq.next_to(dot_product_eq, DOWN)

        # Display the equations
        self.play(Write(text1))
        self.play(Write(addition_eq))
        self.play(Write(subtraction_eq))
        self.play(Write(scalar_mult_eq))
        self.play(Write(dot_product_eq))
        self.play(Write(cross_product_eq))

        self.wait(1)

        self.play(FadeOut(what_is, text1, addition_eq, subtraction_eq, scalar_mult_eq, dot_product_eq, cross_product_eq))

    def construct(self):
        self.title()
        self.introduction()

class Addition(Scene):
    def construct(self):

        text = Tex("a. Vector addition", font_size = 36)
        a_vector = MathTex(r"\vec{a} = \begin{pmatrix} a_1 \\ a_2 \end{pmatrix}", font_size = 34)
        b_vector = MathTex(r"\vec{b} = \begin{pmatrix} b_1 \\ b_2 \end{pmatrix}", font_size = 34)
        addition_eq = MathTex(r"\vec{a} + \vec{b} = \begin{pmatrix} a_1 + b_1 \\ a_2 + b_2 \end{pmatrix}", font_size = 34)

        # Position vectors and equation
        text.move_to(UP * 2)

        a_vector.move_to(UP)
        b_vector.next_to(a_vector, DOWN)
        addition_eq.next_to(b_vector, DOWN)

        # Display vectors and the addition process
        self.play(Write(text))
        self.play(Write(a_vector))
        self.play(Write(b_vector))
        self.wait(1)

        # Perform the addition operation
        self.play(Write(addition_eq))

        # Wait and then fade out everything
        self.wait(2)
        self.play(FadeOut(a_vector, b_vector, addition_eq))

