import numpy as np
from Node import Node

class Matrix:
    '''Класс ядер. Заниамет созданием и можифидацией Kernel'сов. Настраивается в основном в ручную,
    если не по гиперпараметрам из Hyper.'''
    
    def __init__(self, size_matrix, deep_connect):
        '''Реализация параметров матрицы. (Пока что для 2D)'''
        
        self.size_matrix = size_matrix
        '''Размер квардратной матрицы'''
        self.deep_connect = deep_connect
        '''Сколько нейрон будет иметь связей на входе И на выходе. Пока что кратным
        2 и 3'''
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
        '''Генерирует случайное Kernel_n. Кратным 3'''
        count = self.deep_connect
        Kernel_n = np.array([[[np.random.randint(self.size_matrix, dtype=np.int64),np.random.randint(self.size_matrix, dtype=np.int64),round(np.random.random(), 3)],
                              [np.random.randint(self.size_matrix, dtype=np.int64),np.random.randint(self.size_matrix, dtype=np.int64),round(np.random.random(), 3)],
                              [np.random.randint(self.size_matrix, dtype=np.int64),np.random.randint(self.size_matrix, dtype=np.int64),round(np.random.random(), 3)]] 
                               for _ in range(count)])
        return Kernel_n

    def _add_Kernel_n(self):
        '''Пробегает по нодам и добавляет им Kernel_n'''
        for row in self.matrix:
            for elem in row:
                elem.Kernel = np.stack(np.array([self._create_Kernel_n()]))
    
    def _add_Kernel_p(self):
        '''Заполняет нодам Kernel_p на основе связей из Kernel_n'''
        for row in self.matrix:
            for elem in row:
                
                
                pass
    

