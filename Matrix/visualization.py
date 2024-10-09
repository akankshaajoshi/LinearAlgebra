from manim import *

class MatrixVisualization(LinearTransformationScene):
    def __init__(self):
        super().__init__(
            show_coordinates=True,
            show_basis_vectors=True,
            leave_ghost_vectors=True,
        )

    def construct(self):
        # Define the matrix
        matrix = [[2, 1], [1, 2]]
        inverse_matrix = np.linalg.inv(matrix)

        # Apply the matrix transformation
        self.apply_matrix(matrix)
        self.wait(2)

        # Apply the inverse matrix transformation
        self.apply_matrix(inverse_matrix)
        self.wait(2)

if __name__ == "__main__":
    scene = MatrixVisualization()
    scene.render()