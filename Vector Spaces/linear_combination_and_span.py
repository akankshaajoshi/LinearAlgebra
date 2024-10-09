from manim import *

class Vector3DVisualization(ThreeDScene):
    def construct(self):
        # Set up the 3D axes
        axes = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            z_range=[-4, 4, 1],
            x_length=8,
            y_length=8,
            z_length=8,
        )

        # Define the vectors in 3D space with reduced size
        u = np.array([1, 0.5, 0])
        v = np.array([0.5, 1, 0])

        # Create vector arrows for u and v
        vec_u = Arrow3D(start=axes.c2p(0, 0, 0), end=axes.c2p(*u), color=BLUE)
        vec_v = Arrow3D(start=axes.c2p(0, 0, 0), end=axes.c2p(*v), color=GREEN)

        # Add labels for vectors u and v
        label_u = MathTex(r"\vec{u}").next_to(vec_u.get_end(), UP)
        label_v = MathTex(r"\vec{v}").next_to(vec_v.get_end(), UP)

        # Set camera position for 3D visualization
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # Add the 3D axes to the scene
        self.play(Create(axes), run_time=2)
        self.wait()

        # Add the vectors and their labels to the scene
        self.play(Create(vec_u), Write(label_u))
        self.play(Create(vec_v), Write(label_v))
        self.wait()

        self.move_camera(phi=60 * DEGREES, theta=-60 * DEGREES, run_time=3)
        self.wait()
        
        # Example 1: Show a linear combination: 2u + v
        scalar_u1 = 2
        scalar_v1 = 1
        linear_comb_1 = scalar_u1 * u + scalar_v1 * v
        vec_linear_comb_1 = Arrow3D(start=axes.c2p(0, 0, 0), end=axes.c2p(*linear_comb_1), color=ORANGE)
        label_comb_1 = MathTex(f"2\\vec{{u}} + 1\\vec{{v}}").next_to(vec_linear_comb_1.get_end(), UP)

        self.play(Create(vec_linear_comb_1), Write(label_comb_1))
        self.wait(2)

        # Example 2: Show another combination: -u + 2v
        scalar_u2 = -1
        scalar_v2 = 2
        linear_comb_2 = scalar_u2 * u + scalar_v2 * v
        vec_linear_comb_2 = Arrow3D(start=axes.c2p(0, 0, 0), end=axes.c2p(*linear_comb_2), color=ORANGE)
        label_comb_2 = MathTex(f"-\\vec{{u}} + 2\\vec{{v}}").next_to(vec_linear_comb_2.get_end(), UP)

        self.play(Create(vec_linear_comb_2), Write(label_comb_2))
        self.wait(2)

        # Span explanation: Highlight that any point in the plane formed by u and v can be reached
        span_plane = Polygon(axes.c2p(0, 0, 0), axes.c2p(*u), axes.c2p(*linear_comb_1), axes.c2p(*linear_comb_2), fill_opacity=0.3, color=PURPLE)
        span_text = Text("Span of {u, v}", font_size=28, color=PURPLE).move_to(2 * DOWN)

        self.play(FadeOut(label_comb_1, label_comb_2), FadeIn(span_plane), Write(span_text))
        self.wait(2)

        # Clear the scene
        self.play(FadeOut(span_plane), FadeOut(span_text), FadeOut(vec_u), FadeOut(vec_v), FadeOut(vec_linear_comb_1), FadeOut(vec_linear_comb_2))
        self.wait()