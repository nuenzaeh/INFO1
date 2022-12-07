from abc import ABC, abstractmethod


class GeometricObject(ABC):
    PI = 3.14
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def get_color(self):
        return self.color

    def set_color(self, color):
        return self.color

    def get_filled(self):
        pass

    def set_filled(self, filled):
        pass

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_volume(self):
        pass
