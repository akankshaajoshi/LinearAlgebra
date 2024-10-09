from manim import *

class LinearIndependenceAndBases(Scene):
    def construct(self):
        # Title for the module
        title = Text("Linear Independence and Bases", font_size=36)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # Linear Independence explanation
        linear_indep_text = Text("Linear Independence", font_size=28).to_edge(UP)
        self.play(Write(linear_indep_text))
        self.wait(1)

        # Concept of Linear Independence
        concept_text = Text("Vectors are linearly independent if no vector can be written as a linear combination of the others.", font_size=24)
        concept_text.next_to(linear_indep_text, DOWN)
        self.play(Write(concept_text))
        self.wait(2)

        # Define two linearly independent vectors u and v
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

        # Visualizing the span of independent vectors (spans a plane)
        span_plane = Polygon(ORIGIN, u, v, color=PURPLE, fill_opacity=0.3)
        span_text = Text("Independent: u and v span a plane", font_size=24, color=PURPLE).to_edge(UP)

        self.play(Create(span_plane), Write(span_text))
        self.wait(2)

        # Checking for Linear Independence - no scalar multiple relationship
        check_text = Text("No scalar multiple relationship exists.", font_size=24).next_to(span_text, DOWN)
        self.play(Write(check_text))
        self.wait(2)

        # Transition to dependent vectors
        self.play(FadeOut(span_plane), FadeOut(vec_u), FadeOut(vec_v), FadeOut(label_u), FadeOut(label_v), FadeOut(span_text), FadeOut(check_text))

        # Linear Dependence explanation
        linear_dep_text = Text("Linear Dependence", font_size=28).to_edge(UP)
        self.play(Write(linear_dep_text))
        self.wait(1)

        # Concept of Linear Dependence
        dep_concept_text = Text("Vectors are linearly dependent if one vector can be written as a scalar multiple of the other.", font_size=24)
        dep_concept_text.next_to(linear_dep_text, DOWN)
        self.play(Write(dep_concept_text))
        self.wait(2)

        # Define linearly dependent vectors u and 2*u
        vec_u = Arrow(start=ORIGIN, end=u, buff=0, color=BLUE)
        vec_2u = Arrow(start=ORIGIN, end=2 * u, buff=0, color=GREEN)

        label_u = MathTex(r"\vec{u}").next_to(vec_u.get_end(), UP)
        label_2u = MathTex(r"2\vec{u}").next_to(vec_2u.get_end(), UP)

        # Show dependent vectors
        self.play(Create(vec_u), Write(label_u))
        self.play(Create(vec_2u), Write(label_2u))
        self.wait()

        # Visualizing dependence: Both vectors lie on the same line
        dep_line = DashedLine(start=ORIGIN, end=2 * u, color=YELLOW)
        dep_text = Text("Dependent: Both vectors lie on the same line", font_size=24, color=YELLOW).to_edge(UP)

        self.play(Create(dep_line), Write(dep_text))
        self.wait(2)

        # Wrap-up: Independent vs Dependent Summary
        self.play(FadeOut(dep_line), FadeOut(vec_u), FadeOut(vec_2u), FadeOut(label_u), FadeOut(label_2u), FadeOut(dep_text), FadeOut(linear_dep_text), FadeOut(dep_concept_text))

        summary_text = Text("Summary: Independent vs Dependent Vectors", font_size=28).to_edge(UP)
        self.play(Write(summary_text))
        summary_indep = Text("Independent: Vectors span a plane (or higher)", font_size=24, color=PURPLE)
        summary_dep = Text("Dependent: Vectors lie on the same line", font_size=24, color=YELLOW)
        summary_indep.next_to(summary_text, DOWN)
        summary_dep.next_to(summary_indep, DOWN)

        self.play(Write(summary_indep), Write(summary_dep))
        self.wait(2)

        # Fade out the scene
        self.play(FadeOut(summary_text), FadeOut(summary_indep), FadeOut(summary_dep))
