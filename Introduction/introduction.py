from manim import *

class LinearAlgebraIntro(Scene):

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
        text1.to_edge([0, -1, 0])
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

    def add_vectors(self):

        plane = NumberPlane(
            x_range=[-5, 5, 1], y_range=[-4, 4, 1], x_length=10, y_length=7
        )
        plane.add_coordinates()
        # plane.shift(RIGHT * 2)

        vect1 = Line(
            start=plane.coords_to_point(0, 0),
            end=plane.coords_to_point(3, 2),
            stroke_color=YELLOW,
        ).add_tip()
        vect1_name = (
            MathTex("\\vec{v}").next_to(vect1, RIGHT, buff=0.1).set_color(YELLOW)
        )

        vect2 = Line(
            start=plane.coords_to_point(0, 0),
            end=plane.coords_to_point(-2, 1),
            stroke_color=RED,
        ).add_tip()
        vect2_name = MathTex("\\vec{w}").next_to(vect2, LEFT, buff=0.1).set_color(RED)

        vect3 = Line(
            start=plane.coords_to_point(3, 2),
            end=plane.coords_to_point(1, 3),
            stroke_color=RED,
        ).add_tip()

        vect4 = Line(
            start=plane.coords_to_point(0, 0),
            end=plane.coords_to_point(1, 3),
            stroke_color=GREEN,
        ).add_tip()
        vect4_name = (
            MathTex("\\vec{v} + \\vec{w}")
            .next_to(vect4, LEFT, buff=0.1)
            .set_color(GREEN)
        )

        stuff = VGroup(
            plane, vect1, vect1_name, vect2, vect2_name, vect3, vect4, vect4_name
        )

        box = RoundedRectangle(
            height=1.5, width=1.5, corner_radius=0.1, stroke_color=PINK
        ).to_edge(DL)

        self.play(DrawBorderThenFill(plane), run_time=2)
        self.wait()
        self.play(
            GrowFromPoint(vect1, point=vect1.get_start()), Write(vect1_name), run_time=2
        )
        self.wait()
        self.play(
            GrowFromPoint(vect2, point=vect2.get_start()), Write(vect2_name), run_time=2
        )
        self.wait()
        self.play(
            Transform(vect2, vect3),
            vect2_name.animate.next_to(vect3, UP, buff=0.1),
            run_time=2,
        )
        self.wait()
        self.play(
            LaggedStart(GrowFromPoint(vect4, point=vect4.get_start())),
            Write(vect4_name),
            run_time=3,
            lag_ratio=1,
        )
        self.wait()
        self.add(box)
        self.wait()
        self.play(stuff.animate.move_to(box.get_center()).set(width=1.2), run_time=3)
        self.wait()

    def construct(self):

        self.title()
        self.linear_algebra()
        self.add_vectors()
