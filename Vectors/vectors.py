from manim import *

class Introduction(Scene):

    def title(self):
        title = Text("2. Vectors", font_size=48)
        self.play(Write(title))
        self.wait(1)

        #Introduction Section
        self.play(FadeOut(title))
        intro_title = Text("2.1 Introduction to Vectors", font_size=36)
        self.play(Write(intro_title))
        self.wait(1)
        self.play(FadeOut(intro_title))

    def introduction(self):
        # What is a Vector?
        what_is = Text("What is a Vector?", font_size=30)
        what_is.move_to(UP * 2)
        self.play(Write(what_is))
        self.wait(1)

        text1 = Tex("A vector is a mathematical object that has both a magnitude and a direction.", font_size=24)
        text2 = Tex("It is often represented as an arrow in space, with its tail at the origin and its head at a point in space.", font_size=24)

        # Position the equations on the screen
        text1.move_to([0, 1, 0])
        text2.next_to(text1, DOWN, buff=0.5)

        # Display the equations
        self.play(Write(text1))
        self.play(Write(text2))

        # Keep the equations on the screen for a while

        text3 = Tex("A vector can be represented as:", font_size=24, color=BLUE)
        equation = MathTex("\\vec{v} = \\begin{bmatrix} v_1 \\\\ v_2 \end{bmatrix}", font_size=24, color=BLUE)
        
        text3.next_to(text2, DOWN, buff=0.5)
        equation.next_to(text3, DOWN, buff=0.5)

        self.play(Write(text3))
        self.play(Write(equation))

        self.wait(1)

        self.play(FadeOut(what_is, text1, text2))

    def construct(self):

        self.title()
        self.introduction()


class Vectors(VectorScene):

    def construct(self):

        self.add_plane(animate=True).add_coordinates()
        
        self.wait(1)

        basis = self.get_basis_vectors()
        self.add(basis)
        unit_labels = self.get_basis_vector_labels()
        self.add(unit_labels)
       
        vector = self.add_vector([3, 2], color=YELLOW)
        self.vector_to_coords(vector=vector)

        vector2 = self.add_vector([-3, -2])
        self.write_vector_coordinates(vector=vector2)