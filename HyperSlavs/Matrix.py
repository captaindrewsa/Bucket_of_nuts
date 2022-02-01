import numpy as np
from Node import Node

class Matrix:
    '''Класс ядер. Заниамет созданием и можифидацией Kernel'сов. Настраивается в основном в ручную,
    если не по гиперпараметрам из Hyper.'''
    
    def __init__(self, size_matrix, count_connect):
        '''Реализация параметров матрицы. (Пока что для 2D)'''
        
        self.size_matrix = size_matrix
        '''Размер квардратной матрицы'''
        self.count_connect = count_connect
        '''Сколько будет связей'''
        self.matrix = self._create_matrix()
        '''Переменная для доступа к матрице'''
        self._add_Kernel_n()
    
    def _create_matrix(self):
        '''Создает матрицу заданных размеров и заполняет ее пустыми нодами'''
        matrix = np.zeros((self.size_matrix,self.size_matrix), dtype= object)
        for idx1 in range(self.size_matrix):
            matrix[idx1] = [Node() for _ in range(self.size_matrix)]
        return matrix

    def _create_Kernel_n(self):
        '''Генерирует случайное Kernel_n'''
        count = self.count_connect
        Kernel_n = np.array([[np.random.randint(self.size_matrix, dtype=np.int64),np.random.randint(self.size_matrix, dtype=np.int64),round(np.random.random(), 3)] for _ in range(count)])
        return Kernel_n

    def _create_Kernel_p(self, noda: Node, xy_noda: list):
        '''Достает из ноды координты и добавляет данные в другие ноды'''
        for coordinates in noda.Kernel_n[0,:,:]:
            if np.sum(self.matrix[tuple(np.array(coordinates, dtype=np.int64))]) == 0.5:
                pass
                    


    def _add_Kernel_n(self):
        '''Пробегает по нодам и добавляет им Kernel_n'''
        for row in self.matrix:
            for elem in row:
                elem.Kernel_n = np.stack(np.array([self._create_Kernel_n()]))
    
    def _add_Kernel_p(self):
        '''Заполняет нодам Kernel_p на основе связей из Kernel_n'''
        pass

