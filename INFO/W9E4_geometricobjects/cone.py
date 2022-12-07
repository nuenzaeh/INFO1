from geometric_object import GeometricObject


class Cone(GeometricObject):

    def __init__(self, radius, vertical_height, slant_height, color, filled):
        super().__init__(color, filled)  # do i need this? => yes, the child initializer overrides
        self.radius = radius
        self.vertical_height = vertical_height
        self.slant_height = slant_height


    def get_radius(self):
        return self.radius

    def get_vertical_height(self):
        return self.vertical_height

    def get_slant_height(self):
        return self.slant_height

    def get_area(self):
        return round(self.PI*((self.radius**2)+self.radius*self.slant_height), 2)

    def get_volume(self):
        return round(1/3 * self.PI* (self.radius**2)*self.vertical_height, 2)