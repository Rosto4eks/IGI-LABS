from matplotlib import pyplot as plt

class Figure:
    def area():
        pass

class Color:
    def __init__(self, color):
        self.__color = color

    @property
    def color(self) -> str:
        """
        Color getter
        """
        return self.__color
    
    @color.setter
    def color(self, value):
        """
        Color setter    
        """
        self.__color = value


class Trapeze(Figure):
    def __init__(self, base: float, midline: float, height: float, color: Color, name: str):
        self._base = base
        self._midline = midline
        self._height = height
        self._color = color
        self._name = name


    def area(self):
        '''
        return area of figure
        '''
        return self._midline * self._height
    
    @property
    def name(self) -> str:
        """
        Property of name.
        """
        return self._name
    
    @name.setter
    def name(self, value : str):
        """
        Setter of color.
        """
        self._name = value
    

    def info(self):
        return "trapeze name: {0}, base: {1}, midline: {2}, height: {3}, color: {4}, area: {5}".format(self._name, self._base, self._midline, self._height, self._color, self.area())


    def plot(self):
        '''
        display plot and data
        '''
        coords = [(0, 0), (self._base, 0), (self._midline, self._height),  (self._base - self._midline, self._height)]
        plt.figure(figsize=(6, 6))
        plt.title(self._name)
        plt.axis('equal')
        plt.grid()
        try:
            plt.plot(*zip(*coords), linestyle='-', color=self._color)
            plt.fill(*zip(*coords), alpha=0.6, color=self._color)
            plt.show()
        except ValueError as e:
            print(f"Something went wrong: {e}")