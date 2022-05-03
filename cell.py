import pygame

class Cell:
    """
    Tạo ô cờ
    """
    def __init__(self, x, y, image):
        self.__x = x
        self.__y = y
        self.__image = image

    def get_x(self):
        """
        Lấy giá trị tọa độ X của ô cờ
        """
        return self.__x

    def get_y(self):
        """
        Lấy giá trị tọa độ X của ô cờ
        """
        return self.__y

    def get_pos(self):
        return (self.__x, self.__y)

    def set_img(self, new_img):
        self.__image = new_img

    def draw(self, WIN, height = 100, width = 100):
        """
        Vẽ địa hình của ô cờ
        """
        self.__image = pygame.transform.scale(self.__image, (width, height))
        WIN.blit(self.__image, (self.__x, self.__y))

    def is_mouse_hovering(self, pos):
        height = self.__image.get_height()
        width = self.__image.get_width()
        if pos[0] > self.__x and pos[0] < self.__x + width and pos[1] > self.__y and pos[1] < self.__y + height:
            return True
        else:
            return False