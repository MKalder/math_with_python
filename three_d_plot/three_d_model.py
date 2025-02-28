import numpy as np #type: ignore
class ThreeDModel:
    def __init__(self, verticals = np.array([]), faces = np.array([]), scale=1.0, center=[0.0, 0.0, 0.0]):
        self.verticals = verticals * scale + center
        self.faces = faces
