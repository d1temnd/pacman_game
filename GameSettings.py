from typing import List

class GameSettings:
    """
    Класс для описания основных констант игры

    Атрибуты:
    WINDOW_WIDTH : int
        Ширина дисплея игры
    WINDOW_HEIGHT : int
        Высота дисплея игры
    MAP_CONFIGURATION : list[str]
        Описание карты
    """
    WINDOW_WIDTH: int
    WINDOW_HEIGHT: int
    MAP_CONFIGURATION: List[str]

    def __init__(self):
        self.WINDOW_WIDTH = 720
        self.WINDOW_HEIGHT = 720
        self.MAP_CONFIGURATION = ["888888888888888888",
                                  "880808888888808088",
                                  "80000000P000000008",
                                  "880888008800888088",
                                  "88000001880G000088",
                                  "888808888888808888",
                                  "800000000000000008",
                                  "888808888888808888",
                                  "8800G1000000000088",
                                  "880808888888808088",
                                  "800800000000018008",
                                  "808888008800888888",
                                  "800000008800000008",
                                  "808801888888008808",
                                  "800000000000000008",
                                  "888088808808880888",
                                  "888080008800080888",
                                  "888888888888888888"]
        