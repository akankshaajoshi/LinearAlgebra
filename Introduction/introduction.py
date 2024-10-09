from manim import *

class LinearAlgebraIntro(VoiceoverScene):

    def title(self):
        # Title Slide
        title = Text("Linear Algebra", font_size=48)
        self.play(Write(title))
        self.wait(1)
        
        # Introduction Section
        self.play(FadeOut(title))
        intro_title = Text("1. Introduction to Linear Algebra", font_size=36)
        self.play(Write(intro_title))
        self.wait(1)
        self.play(FadeOut(intro_title))

    def linear_algebra(self):
        # What is Linear Algebra?
        what_is = Text("What is Linear Algebra?", font_size=30)
        what_is.move_to(UP * 2)
        self.play(Write(what_is))
        self.wait(1)
        
        text1 = Tex("Linear algebra is the branch of mathematics concerning linear equations such as:", font_size=24)
        equation1 = MathTex(r"a_{1}x_{1} + \cdots + a_{n}x_{n} = b")
        text2 = Tex("linear maps such as:", font_size=24)
        equation2 = MathTex(r"(x_{1}, \ldots, x_{n}) \mapsto a_{1}x_{1} + \cdots + a_{n}x_{n}")
        text3 = Tex("and their representations in vector spaces and through matrices.", font_size=24)

        # # Position the equations on the screen
        text1.move_to([0, 1, 0])
        equation1.next_to(text1, DOWN, buff=0.5)
        text2.next_to(equation1, DOWN, buff=0.5)
        equation2.next_to(text2, DOWN, buff=0.5)
        text3.next_to(equation2, DOWN, buff=0.5)
        
        # Display the equations
        self.play(Write(text1))
        self.play(Write(equation1))
        self.play(Write(text2))
        self.play(Write(equation2))
        self.play(Write(text3))

        # Keep the equations on the screen for a while
        self.wait(2)
        
        self.play(FadeOut(what_is, text1, text2, text3, equation1, equation2))

    def construct(self):

        self.title()
        self.linear_algebra()
