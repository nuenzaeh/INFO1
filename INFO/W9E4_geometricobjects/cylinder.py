from geometric_object import GeometricObject


class Cylinder(GeometricObject):

    def __init__(self, radius, height, color, filled):
        super().__init__(color, filled)
        self.radius = radius
        self.height = height

    def get_radius(self):
        return self.radius

    def get_height(self):
        return self.height

    def get_area(self):
        return round(self.PI*(self.radius**2) * self.height,2)

    def get_volume(self):
        return round(2*self.PI*self.radius(self.radius+self.height),2)
