from manim import *
class Vector3DVisualization(ThreeDScene):
    def construct(self):
        # Set up the 3D axes
        axes = ThreeDAxes(
            x_range=[-4, 4, 2],
            y_range=[-4, 4, 2],
            z_range=[-4, 4, 2],
            x_length=8,
            y_length=8,
            z_length=8,
        )

        # Define the vector in 3D space
        vector = Arrow(
            start=axes.c2p(0, 0, 0),
            end=axes.c2p(2, 2, 1),
            color=YELLOW,
        ).set_stroke(width=6)
        vector_label = MathTex("\\vec{v}").scale(1.5).set_color(YELLOW)
        vector_label.move_to(axes.c2p(2, 2, 1) + RIGHT * 0.5)

        # Matrix representation of the vector
        vector_matrix = MathTex("\\vec{v} = \\begin{pmatrix} 2 \\\\ 2 \\\\ 1 \\end{pmatrix}")\
            .scale(1.2).to_edge([-8, -4, 1]).set_color(YELLOW)

        # Axis labels
        x_axis_label = MathTex("x").scale(1.2).set_color(BLUE)
        y_axis_label = MathTex("y").scale(1.2).set_color(BLUE)
        z_axis_label = MathTex("z").scale(1.2).set_color(BLUE)
        
        # Explicitly position the axis labels
        x_axis_label.move_to(axes.c2p(4, 0, 0) + OUT * 0.5)
        y_axis_label.move_to(axes.c2p(0, 4, 0) + OUT * 0.5)
        z_axis_label.move_to(axes.c2p(0, 0, 4) + OUT * 0.5)

        # Set camera position for 3D visualization
        self.set_camera_orientation(phi=20 * DEGREES, theta=-45 * DEGREES)

        # Add the 3D axes to the scene
        self.play(Create(axes), run_time=2)
        self.wait()

        # Add axis labels
        self.play(Write(x_axis_label))
        self.play(Write(y_axis_label))
        self.play(Write(z_axis_label))
        self.wait()

        # Draw the vector and its label
        self.play(GrowArrow(vector), Write(vector_label), run_time=3)
        self.wait()

        # Display the matrix representation of the vector
        self.play(Write(vector_matrix))
        self.wait()

        # Rotate the scene for better visualization
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(6)
        self.stop_ambient_camera_rotation()
        self.wait()
