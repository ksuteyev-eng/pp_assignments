class Camera:
    def take_photo(self): print("Фото сделано")

class Player:
    def play_music(self): print("Музыка играет")

class MobilePhone(Camera, Player):
    """Наследование от нескольких классов одновременно."""
    pass

phone = MobilePhone()
phone.take_photo()
phone.play_music()