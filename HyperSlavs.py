import numpy as np
import random as rnd
"""Тут еще НИХУЯ не доделано и НИХУЯ не работает"""
class Hyper:
    """Реализация для 2D-матрицы"""
    def __init__(self, size_matrix) -> None:
        self.size_matrix = size_matrix
        self.matrix = self._create_matrix()
        
    def _create_matrix(self):
        return np.array([[node() for _ in range(self.size_matrix)], [node() for _ in range(self.size_matrix)]])

    def _create_connect(self):
        """
        Бежим по нодам и выдаем им рандомные Kernel.
        """
        for idx1, row in enumerate(self.matrix):
            for idx2, noda in enumerate(row):
                np.append(noda.Kernel,self._create_Kernel(3,[idx1,idx2]))

    def _create_Kernel(self, size_Kernel: int, exept_idx:list):
        """
        Генерируем рандомные Kernel со случайными весами от 0.0 до 1.0 и отсутвтием замыкания на себя
        """
        
        Kernel = np.array([])
        Core = np.array([[],[],[]])
        
        for _ in range(size_Kernel):
            Core = np.insert(Core, 0, self._generate_column_pos(exept_idx), axis=1)
            Core = np.insert(Core, 1, self._generate_column_pos(exept_idx), axis=1)
            Core = np.insert(Core, 2, self._generate_column_weight(), axis=1)
            Kernel = np.append(Kernel, Core)
            print(Kernel,"\n")
            Core = np.array([[],[],[]])

        return Kernel

    def _generate_column_pos(self, exept_idx:list):
        column = []
        while True:
            rand_pos = rnd.randrange(0,self.size_matrix-1)
            if rand_pos not in exept_idx:
                column.append(rand_pos)
                break
            else:
                continue
            
        while True:
            rand_pos = rnd.randrange(0,self.size_matrix-1)
            if rand_pos not in exept_idx:
                column.append(rand_pos)
                break
            else:
                continue
            
        while True:
            rand_pos = rnd.randrange(0,self.size_matrix-1)
            if rand_pos not in exept_idx:
                column.append(rand_pos)
                break
            else:
                continue
                    
        return column

    def _generate_column_weight(self):
        column = []
        for _ in range(len(self.matrix)+1):
            column.append(round(rnd.random(),2))
        return column

class node:
    """Главный класс ноды. Описывает характеристики и функции.
    Каждая нода содержит следующие поля:
    1. Ядро (Kernel) с ядрышками (core) связей и их весами. 2. Поле даты. 3. Поле значения активации. 4. Поле сумматора
    """

    def __init__(self) -> None:
        """Инициализация базовых параметров нод"""
        
        self.Kernel = np.array([]) #Внутри будет много core
        self.data = None    #В каком-то виде передаваемая информация
        self.activate = None #Значение активации
        self.summ = None #Предварительный сумматор
    


a = Hyper(10)

a._create_Kernel(3,[1,2])