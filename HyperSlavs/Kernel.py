import numpy as np
from Node import Node

class Kernel:
    '''Класс ядер. Заниамет созданием и можификацией Kernel'сов. Настраивается в основном в ручную,
    если не по параметрам из Hyper.'''
    deep_connect = 5
    '''Сколько нейрон будет иметь связей на входе И на выходе'''
    
    def __init__(self, size_matrix):
        '''Реализация параметров матрицы. (Пока что для 2D)'''
        
        self.size_matrix = size_matrix
        '''Размер квардратной матрицы'''
        self.matrix = self._create_matrix()
        '''Переменная для доступа к матрице'''
    
    def _create_matrix(self):
        '''Создает матрицу заданных размеров и заполняет ее пустыми нодами'''
        matrix = np.zeros((self.size_matrix,self.size_matrix), dtype= object)
        for idx1 in range(self.size_matrix):
            matrix[idx1] = [Node() for _ in range(self.size_matrix)]
        return matrix

    def _random_Kernel(self):
        '''Генерирует случайное Kernel'''
        Kernel_p = self._create_Kernel_p() #np.array()
        Kernel_n = self._create_Kernel_n() #np.array()
        
        return np.array([Kernel_p,Kernel_n])

    def _create_Kernel_p(self):        
        pass
    
    def _create_Kernel_n(self):
        pass