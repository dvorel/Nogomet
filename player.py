import numpy as np
import cv2

class Field:
    def __init__(self, width=109, height=69, color=(0, 255, 0), thickness=2):
        self.width = width
        self.height = height
        self._field = self._make_field(width, height, color)
        self.coords = list()
        self.line_thickness = thickness
    def _make_field(self, width, height, color):
        f = np.empty((height*10, width*10, 3), dtype=np.uint8)
        for i in range(3):
            f[:, :, i] = color[i]
        return f

    def _draw_to_field(self):
        if len(self.coords) < 2:
            return
        cv2.line(self._field, [self.coords[-2][0] * 10, self.coords[-2][1] * 10], [self.coords[-1][0] * 10, self.coords[-1][1] * 10], self.line_thickness)
    
    def add(self, coords, normalize=False):
        """
        Coords should be tuple or list of 2 coords => (x, y)
        """
        if (coords[0] > self.width or coords[1] > self.height):
            if not normalize:
                raise Exception("Coords not inside field")
            else:
                coords[0] = max(0, min(coords[0], self.width))
                coords[1] = max(0, min(coords[1], self.height))
        
        self.coords.append([coords[0], coords[1]])
        self._draw_to_field()
        

    def show_field(self):
        cv2.imshow("Field", self._field)
        cv2.waitKey()



class Player(Field):
    def __init__(self, ):
        pass



if __name__ == "__main__":
    fi = Field()
    fi.add([0, 0])
    fi.add([10, 20])
    fi.add([50, 50])
    fi.show_field()

    