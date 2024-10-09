from manim import *

class VectorSpaces(Scene):

    def title(self):
        title = Text("3. Vector Space", font_size=48)
        self.play(Write(title))
        self.wait(1)

        #Introduction Section
        self.play(FadeOut(title))
        intro_title = Text("3.1 Introduction to Vector Spaces", font_size=36)
        self.play(Write(intro_title))
        self.wait(1)
        self.play(FadeOut(intro_title))


    def construct(self):

        self.title()
        # Title
        title = Tex("Vector Spaces")
        title.scale(1.5)
        title.to_edge(UP)
        self.play(Write(title))

        # Definition
        definition = Tex(r"A vector space is a set $V$ together with two operations:")
        definition.next_to(title, DOWN, buff=1)
        self.play(Write(definition))

        operations = BulletedList(
            "Vector addition: $V \\times V \\to V$",
            "Scalar multiplication: $\\mathbb{F} \\times V \\to V$",
        )
        operations.next_to(definition, DOWN, buff=0.5)
        self.play(Write(operations))

        self.wait(2)
    # Vector Space Example
        example = Tex("Example: $\\mathbb{R}^2$")
        example.next_to(operations, DOWN, buff=1)
        self.play(Write(example))
    
        vectors = VGroup(
            Arrow(start=ORIGIN, end=RIGHT, color=BLUE),
            Arrow(start=ORIGIN, end=UP, color=RED),
            Arrow(start=ORIGIN, end=RIGHT+UP, color=GREEN),
        )
        vectors.arrange(RIGHT, buff=1)
        vectors.next_to(example, DOWN, buff=0.5)
        self.play(Create(vectors))
    
        self.wait(2)