import pygame

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
        super().__init__('desert', {'normal': 'img\desert_normal.png', 'speacial': 'img\desert_speacial.png'}, '')

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
        super().__init__('frozen_river', {'normal': 'img\\frozen_river_normal.png', 'speacial': 'img\\frozen_river_speacial.png'}, '')

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
        super().__init__('foggy_forest', {'normal': 'img\\foggy_forest_normal.png', 'speacial': 'img\\foggy_forest_speacial.png'}, 'Glamour')

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
        super().__init__('swamp', {'normal': 'img\swamp_normal.png', 'speacial': 'img\swamp_speacial.png'}, '')

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

class Normal(Enviroment):
    """
    Lớp 'Bình thường'
    """

    def __init__(self, name, image, effect):
        """
        Hàm tạo môi trường bình thường
        :param name: Tên môi trường (str)
        :param image: Danh sách hình ảnh môi trường (ditc(pygame.image))
        :param effect: Hiệu ứng của môi trường (str)
        """
        super().__init__('normal', {'normal': '', 'speacial': ''}, '')

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