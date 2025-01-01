from manim import *

class Preface(Scene):
    def construct(self):
        # Preface Screen 1: Course Name
        course_name = Text("Linear Algebra",font_size=72, color=BLUE)
        subtext = Text("A Comprehensive Guide", font_size=36, color=WHITE).next_to(course_name, DOWN, buff=0.5)

        self.play(Write(course_name))
        self.wait(1)
        self.play(FadeIn(subtext, shift=UP))
        self.wait(3)
        self.play(FadeOut(course_name, scale=0.8), FadeOut(subtext, scale=0.8))

        # Preface Screen 2: Table of Contents
        toc_title = Text("Table of Contents", font_size=48, color=BLUE).to_edge(UP)
        toc_content = BulletedList(
            "1. Introduction to Linear Algebra",
            "2. Vectors (Definition and Operations)",
            "3. Vector Spaces: (Subspace, Span, Linear Combination)",
            "4. Matrices: (Introduction, Visualization, Inverses)",
            "5. Linear Independence",
            "6. Linear Transformation",
            "7. Determinants",
            font_size=28
        ).next_to(toc_title, DOWN, buff=0.5)

        self.play(Write(toc_title))
        self.play(FadeIn(toc_content, shift=UP, lag_ratio=0.2))
        self.wait(5)
        self.play(FadeOut(toc_title, scale=0.8), FadeOut(toc_content, scale=0.8))
