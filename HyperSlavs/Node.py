import numpy as np


class Node:
    """Главный класс ноды. Описывает характеристики и функции.
    Каждая нода содержит следующие поля:
    1. Ядро (Kernel) с ядрышками (core) связей и их весами. 2. Поле значения активации. 3. Поле сумматора
    """

    def __init__(self) -> None:
        """Инициализация базовых параметров нод"""

        self.Kernel = 0 #Внутри будет Kernel_previous (дендриты) и Kernel-next(аксоны)
        '''Kernel содержит два подъядра: Kernel_previous и Kernel_next.
        Каждое из подъядер содержит множество Core, размерность которых в K_p-2x2, а в K_n-3x3.
        Core_p состоит из координат двух (максимум) предыдщуих нейронов.
        Core_n состоит из координат трех (максимум) следующих нейронов и веса синапса. 
        '''
        self.activate = None #Предел активации
        '''Значение, по превышении которого сработает функция  отправки сигнала'''
        self.summ = None #Предварительный сумматор сигналов
        '''Промежуточное значение входящих сигналов'''
    