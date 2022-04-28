import pygame

class Cell:
    """
    Tạo ô cờ
    """
    def __init__(self, x, y, image):
        self.__x = x
        self.__y = y
        self.image = image

    def get_x(self):
        """
        Lấy giá trị tọa độ X của ô cờ
        """
        return self.x

    def get_y(self):
        """
            Lấy giá trị tọa độ X của ô cờ
        """
        return self.y

    def draw(self, WIN):
        """
            Vẽ địa hình của ô cờ
        """
        WIN.blit(self.image)
