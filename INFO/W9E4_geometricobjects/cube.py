from geometric_object import GeometricObject


class Cube(GeometricObject):
    def __init__(self, side_length, color, filled):
        super().__init__(color, filled)
        self.side_length = side_length

    def get_side_length(self):
        return self.side_length

    def set_side_length(self, side_length):
        pass

    def get_area(self):
        return round(6*self.side_length**2, 2)

    def get_volume(self):
        return round(self.side_length**3, 2)
