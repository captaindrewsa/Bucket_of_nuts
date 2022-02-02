import numpy as np
from Node import Node
from tqdm import tqdm

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
        self._add_Kernel_p()
    
    def _create_matrix(self):
        '''Создает матрицу заданных размеров и заполняет ее пустыми нодами'''
        matrix = np.zeros((self.size_matrix,self.size_matrix), dtype= object)
        for idx1 in tqdm(range(self.size_matrix)):
            matrix[idx1] = [Node() for _ in range(self.size_matrix)]
        return matrix

    def _create_Kernel_n(self):
        '''Генерирует случайное Kernel_n'''
        count = self.count_connect
        Kernel_n = np.array([[np.random.randint(self.size_matrix, dtype=np.int64),np.random.randint(self.size_matrix, dtype=np.int64),round(np.random.random(), 3)] for _ in range(count)])
        return Kernel_n

    def _append_Kernel_p(self, noda: Node, xy_noda: list):
        '''Достает из ноды координты и добавляет данные в другие ноды'''
        for coordinates in noda.Kernel_n[0,:,:]:
            coordinates = tuple(np.array(coordinates, dtype=np.int64))[:2]
            if isinstance(self.matrix[coordinates].Kernel_p, int):
                self.matrix[coordinates].Kernel_p = np.array([xy_noda])
            else:
                self.matrix[coordinates].Kernel_p = np.append(self.matrix[coordinates].Kernel_p, np.array([xy_noda]), axis=0)


    def _add_Kernel_n(self):
        '''Пробегает по нодам и добавляет им Kernel_n'''
        for row in tqdm(self.matrix):
            for elem in row:
                elem.Kernel_n = np.stack(np.array([self._create_Kernel_n()]))
    
    def _add_Kernel_p(self):
        '''Заполняет нодам Kernel_p на основе связей из Kernel_n'''
        for idx1, row in tqdm(enumerate(self.matrix)):
            for idx2, elem in enumerate(row):
                self._append_Kernel_p(elem, [idx1,idx2])
