# from re import L
from manim import *

class Vectors(VectorScene):
    def construct(self):

        # code = (
        #     Code(
        #         "Tute3Vectors.py",
        #         style=Code.styles_list[12],
        #         background="window",
        #         language="python",
        #         insert_line_no=True,
        #         tab_width=2,
        #         line_spacing=0.3,
        #         scale_factor=0.5,
        #         font="Monospace",
        #     )
        #     .set_width(6)
        #     .to_edge(UL, buff=0)
        # )

        plane = self.add_plane(animate=True).add_coordinates()
        # self.play(Write(code), run_time=6)
        self.wait()
        vector = self.add_vector([-3, -2], color=YELLOW)

        basis = self.get_basis_vectors()
        self.add(basis)
        self.vector_to_coords(vector=vector)

        vector2 = self.add_vector([2, 2])
        self.write_vector_coordinates(vector=vector2)
