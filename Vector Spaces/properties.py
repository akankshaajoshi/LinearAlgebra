from manim import *

class VectorSpaceProperties(Scene):

    def title(self):
        #Introduction Section
        intro_title = Text("3.1 Properties of Vector Spaces", font_size=36)
        self.play(Write(intro_title))
        self.wait(1)
        self.play(FadeOut(intro_title))

    def construct(self):
        self.title()
        # Define vectors u and v
        u = np.array([1, 0.5, 0])  # Reduced size
        v = np.array([0.5, 1, 0])  # Reduced size

        # Create vector arrows for u and v
        vec_u = Arrow(start=ORIGIN - [1, 2.5, 0], end=u, buff=0, color=BLUE)
        vec_v = Arrow(start=ORIGIN - [1, 2.5, 0], end=v, buff=0, color=GREEN)

        # Add labels for vectors u and v
        label_u = MathTex(r"\vec{u}").next_to(vec_u.get_end(), UP)
        label_v = MathTex(r"\vec{v}").next_to(vec_v.get_end(), UP)

        # Display the vectors on screen
        self.play(Create(vec_u), Write(label_u))
        self.play(Create(vec_v), Write(label_v))
        self.wait()

        # Closure: Show that u + v is still a vector
        # Calculate u + v
        u_plus_v = u + v
        vec_u_plus_v = Arrow(start=ORIGIN - [1, 2.5, 0], end=u_plus_v, buff=0, color=YELLOW)
        label_u_plus_v = MathTex(r"\vec{u} + \vec{v}").next_to(vec_u_plus_v.get_end(), UP)

        closure_text = Text("Closure Property: \n u + v is still in the vector space").scale(0.7).to_edge(UP)

        # Show closure property
        self.play(Write(closure_text))
        self.wait()
        self.play(Transform(vec_u, vec_u_plus_v), Transform(label_u, label_u_plus_v))
        self.wait()

        # Commutativity: Show u + v = v + u
        # Reverse order of addition: v + u
        vec_v_plus_u = Arrow(start=ORIGIN - [1, 2.5, 0], end=u_plus_v, buff=0, color=YELLOW)
        label_v_plus_u = MathTex(r"\vec{v} + \vec{u}").next_to(vec_v_plus_u.get_end(), UP)

        commutative_text = Text("Commutativity: \n u + v = v + u").scale(0.7).to_edge(UP)

        # Transition from u + v to v + u
        self.play(FadeOut(closure_text), Write(commutative_text))
        self.play(Transform(vec_u_plus_v, vec_v_plus_u), Transform(label_u_plus_v, label_v_plus_u))
        self.wait()