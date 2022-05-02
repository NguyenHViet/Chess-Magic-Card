import pygame
import cell

class Enviroment:
    """
    Lớp 'Môi trường'
    """

    def __int__(self, name, image, effect):
        """
        Hàm tạo môi trường
        :param name: Tên môi trường (str)
        :param image: Danh sách hình ảnh môi trường (ditc(pygame.image))
        :param effect: Danh sách hiệu ứng của môi trường (list or str)
        """
        self._name = name
        self._image = image
        self._effect = effect

    def get_name(self):
        """
        Hàm lấy tên địa hình
        :return: Tên địa hình (str)
        """
        return self._name

    def get_env_img(self):
        """
        Hàm lấy danh sách hình ảnh môi trường
        :return: Danh sách hình ảnh môi trường (ditc(pygame.image))
        """
        return self._image
    def get_effect(self):
        """
        Hàm lấy danh sách hiệu ứng
        :return: Hiệu ứng của môi trường(str)
        """
        return self._effect


class Desert(Enviroment):
    """
    Lớp 'Sa mạc'
    """
    def __init__(self, name, image, effect):
        """
        Hàm tạo môi trường sa mạc
        :param name: Tên môi trường (str)
        :param image: Danh sách hình ảnh môi trường (ditc(pygame.image))
        :param effect: Hiệu ứng của môi trường (str)
        """
        super().__init__('desert', {'background': '','normal': 'img\desert_normal.png', 'speacial': 'img\desert_speacial.png'}, 'Unmoveable')

    def get_name(self):
        """
        Hàm lấy tên môi trường (str)
        :return: Tên môi trường (str)
        """
        super().get_name(self)

    def get_env_img(self):
        """
        Hàm lấy danh sách hình ảnh môi trường
        :return: Danh sách hình ảnh môi trường (ditc(pygame.image))
        """
        super().get_env_img(self)

    def get_effect(self):
        """
        Hàm lấy danh sách hiệu ứng
        :return: Hiệu ứng của môi trường(str)
        """
        super().get_effect(self)

    def apply_env_effect(self, area):

        if area == 1:
            area_effect = {
                cell.Cell(0 ,1, self.get_env_img()['speacial']), cell.Cell(1 ,1, self.get_env_img()['speacial']),
                cell.Cell(2, 1, self.get_env_img()['speacial']), cell.Cell(3 ,1, self.get_env_img()['speacial']),
                cell.Cell(0, 2, self.get_env_img()['speacial']), cell.Cell(1 ,2, self.get_env_img()['speacial']),
                cell.Cell(2, 2, self.get_env_img()['speacial']), cell.Cell(3 ,2, self.get_env_img()['speacial']),
                cell.Cell(0, 3, self.get_env_img()['speacial']), cell.Cell(1 ,3, self.get_env_img()['speacial']),
                cell.Cell(2, 1, self.get_env_img()['speacial']), cell.Cell(3 ,3, self.get_env_img()['speacial'])
            }
        elif area ==2:
            area_effect = {
                cell.Cell(4, 1, self.get_env_img()['speacial']), cell.Cell(5, 1, self.get_env_img()['speacial']),
                cell.Cell(6, 1, self.get_env_img()['speacial']), cell.Cell(7, 1, self.get_env_img()['speacial']),
                cell.Cell(4, 2, self.get_env_img()['speacial']), cell.Cell(5, 2, self.get_env_img()['speacial']),
                cell.Cell(6, 2, self.get_env_img()['speacial']), cell.Cell(7, 2, self.get_env_img()['speacial']),
                cell.Cell(4, 3, self.get_env_img()['speacial']), cell.Cell(5, 3, self.get_env_img()['speacial']),
                cell.Cell(6, 1, self.get_env_img()['speacial']), cell.Cell(7, 3, self.get_env_img()['speacial'])
            }
        elif area == 3:
            area_effect = {
                cell.Cell(0, 4, self.get_env_img()['speacial']), cell.Cell(1, 4, self.get_env_img()['speacial']),
                cell.Cell(2, 4, self.get_env_img()['speacial']), cell.Cell(3, 4, self.get_env_img()['speacial']),
                cell.Cell(0, 5, self.get_env_img()['speacial']), cell.Cell(1, 5, self.get_env_img()['speacial']),
                cell.Cell(2, 5, self.get_env_img()['speacial']), cell.Cell(3, 5, self.get_env_img()['speacial']),
                cell.Cell(0, 6, self.get_env_img()['speacial']), cell.Cell(1, 6, self.get_env_img()['speacial']),
                cell.Cell(2, 6, self.get_env_img()['speacial']), cell.Cell(3, 6, self.get_env_img()['speacial'])
            }
        elif area == 4:
            area_effect = {
                cell.Cell(4, 4, self.get_env_img()['speacial']), cell.Cell(5, 4, self.get_env_img()['speacial']),
                cell.Cell(6, 4, self.get_env_img()['speacial']), cell.Cell(7, 4, self.get_env_img()['speacial']),
                cell.Cell(4, 5, self.get_env_img()['speacial']), cell.Cell(5, 5, self.get_env_img()['speacial']),
                cell.Cell(6, 5, self.get_env_img()['speacial']), cell.Cell(7, 5, self.get_env_img()['speacial']),
                cell.Cell(4, 6, self.get_env_img()['speacial']), cell.Cell(5, 6, self.get_env_img()['speacial']),
                cell.Cell(6, 6, self.get_env_img()['speacial']), cell.Cell(7, 6, self.get_env_img()['speacial'])
            }
        # In area_effect lên bàn cờ

        # Kiểm tra quân cờ có trong vùng area_effect, gán thêm effect Unmoveable


class Frozen_river(Enviroment):
    """
    Lớp 'Sông băng'
    """

    def __init__(self, name, image, effect):
        """
        Hàm tạo môi trường sông băng
        :param name: Tên môi trường (str)
        :param image: Danh sách hình ảnh môi trường (ditc(pygame.image))
        :param effect: Hiệu ứng của môi trường (str)
        """
        super().__init__('frozen_river', {'background': '', 'normal': 'img\\frozen_river_normal.png', 'speacial': 'img\\frozen_river_speacial.png'}, '')

    def get_name(self):
        """
        Hàm lấy tên môi trường (str)
        :return: Tên môi trường (str)
        """
        super().get_name(self)

    def get_env_img(self):
        """
        Hàm lấy danh sách hình ảnh môi trường
        :return: Danh sách hình ảnh môi trường (ditc(pygame.image))
        """
        super().get_env_img(self)

    def get_effect(self):
        """
        Hàm lấy danh sách hiệu ứng
        :return: Hiệu ứng của môi trường(str)
        """
        super().get_effect(self)

class Foggy_forest(Enviroment):
    """
    Lớp 'Rừng sương mù'
    """

    def __init__(self, name, image, effect):
        """
        Hàm tạo môi trường sông băng
        :param name: Tên môi trường (str)
        :param image: Danh sách hình ảnh môi trường (ditc(pygame.image))
        :param effect: Hiệu ứng của môi trường (str)
        """
        super().__init__('foggy_forest', {'background': '', 'normal': 'img\\foggy_forest_normal.png', 'speacial': 'img\\foggy_forest_speacial.png'}, 'Glamour')

    def get_name(self):
        """
        Hàm lấy tên môi trường (str)
        :return: Tên môi trường (str)
        """
        super().get_name(self)

    def get_env_img(self):
        """
        Hàm lấy danh sách hình ảnh môi trường
        :return: Danh sách hình ảnh môi trường (ditc(pygame.image))
        """
        super().get_env_img(self)

    def get_effect(self):
        """
        Hàm lấy danh sách hiệu ứng
        :return: Hiệu ứng của môi trường(str)
        """
        super().get_effect(self)

    def apply_env_effect(self):

        "Đổi toàn bộ ô cờ sang ô speacial"
        "Thay đổi giá trị di chuyển của quân cờ trừ mã xuống còn 4"

class Swamp(Enviroment):
    """
    Lớp 'Đầm lầy'
    """

    def __init__(self, name, image, effect):
        """
        Hàm tạo môi trường đầm lầy
        :param name: Tên môi trường (str)
        :param image: Danh sách hình ảnh môi trường (ditc(pygame.image))
        :param effect: Hiệu ứng của môi trường (str)
        """
        super().__init__('swamp', {'background': '', 'normal': 'img\swamp_normal.png', 'speacial': 'img\swamp_speacial.png'}, '')

    def get_name(self):
        """
        Hàm lấy tên môi trường (str)
        :return: Tên môi trường (str)
        """
        super().get_name(self)

    def get_env_img(self):
        """
        Hàm lấy danh sách hình ảnh môi trường
        :return: Danh sách hình ảnh môi trường (ditc(pygame.image))
        """
        super().get_env_img(self)

    def get_effect(self):
        """
        Hàm lấy danh sách hiệu ứng
        :return: Hiệu ứng của môi trường(str)
        """
        super().get_effect(self)

    def apply_env_effect(self):

        "Random vị trí 10 ô speacial"
        "Đổi ô cờ sang ô speacial"
        "Cài ô speacial như là 1 quân cờ"

class Grassland(Enviroment):
    """
    Lớp 'Thảo nguyên'
    """

    def __init__(self, name, image, effect):
        """
        Hàm tạo môi trường bình thường
        :param name: Tên môi trường (str)
        :param image: Danh sách hình ảnh môi trường (ditc(pygame.image))
        :param effect: Hiệu ứng của môi trường (str)
        """
        super().__init__('grassland', {'background': '', 'normal': 'img\grassland.png', 'speacial': ''}, '')

    def get_name(self):
        """
        Hàm lấy tên môi trường (str)
        :return: Tên môi trường (str)
        """
        super().get_name(self)

    def get_env_img(self):
        """
        Hàm lấy danh sách hình ảnh môi trường
        :return: Danh sách hình ảnh môi trường (ditc(pygame.image))
        """
        super().get_env_img(self)

    def get_effect(self):
        """
        Hàm lấy danh sách hiệu ứng
        :return: Hiệu ứng của môi trường(str)
        """
        super().get_effect(self)