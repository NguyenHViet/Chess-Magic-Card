import pygame

class Cell:
    """
    Tạo ô cờ
    """
    def __init__(self, x, y, image):
        """
        Hàm khởi tạo
        :param x: Tọa độ x của ô cờ (int)
        :param y: Tọa độ y của ô cờ (int)
        :param image: Hình ảnh của ô cờ (pygame.image)
        """
        self.__x = x
        self.__y = y
        self.__image = image

    def get_x(self):
        """
        Lấy giá trị tọa độ x của ô cờ
        :return: Giá trị tọa độ x của ô cờ (int)
        """
        return self.__x

    def get_y(self):
        """
        Lấy giá trị tọa độ y của ô cờ
        :return: Giá trị tọa độ y của ô cờ (int)
        """
        return self.__y

    def get_pos(self):
        """
        Lấy tọa dộ x, y của ô cờ
        :return: Tọa dộ x, y của ô cờ (tuple(x, y))
        """
        return (self.__x, self.__y)

    def set_img(self, new_img):
        """
        Gán hình ảnh mới cho ô cờ
        :param new_img: Hình ảnh mới (pygame.image)
        :return: None
        """
        self.__image = new_img

    def draw(self, WIN, height = 100, width = 100):
        """
        In ô cờ lên cửa sổ hiển thị
        :param WIN: Cửa sổ hiển thị (pygame.display)
        :param height: Chiều cao ô cờ (int)
        :param width: Chiều rộng ô cờ (int)
        :return: None
        """
        try:
            self.__image = pygame.transform.scale(self.__image, (width, height))
            WIN.blit(self.__image, (self.__x, self.__y))
        except:
            pass

    def is_mouse_hovering(self, pos):
        """
        Kiểm tra xem con trỏ chuột có đang nằm trên ô cờ không
        :param pos: Vị trí con trỏ chuột (tuple(int, int))
        :return: Kết quả (bool)
        """
        height = self.__image.get_height()
        width = self.__image.get_width()
        if pos[0] > self.__x and pos[0] < self.__x + width and pos[1] > self.__y and pos[1] < self.__y + height:
            return True
        else:
            return False