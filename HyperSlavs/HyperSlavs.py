import numpy as np

class Hyper:
    '''Главный класс матрицы'''
    
    deep_connect = None
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

    

class Node:
    """Главный класс ноды. Описывает характеристики и функции.
    Каждая нода содержит следующие поля:
    1. Ядро (Kernel) с ядрышками (core) связей и их весами. 2. Поле значения активации. 3. Поле сумматора
    """

    def __init__(self) -> None:
        """Инициализация базовых параметров нод"""
        
        self.Kernel = np.array([]) #Внутри будет Kernel_previous (дендриты) и Kernel-next(аксоны)
        '''Kernel содержит два подъядра: Kernel_previous и Kernel_next.
        Каждое из подъядер содержит множество Core, размерность которых в K_p-2x2, а в K_n-3x3.
        Core_p состоит из координат двух (максимум) предыдщуих нейронов.
        Core_n состоит из координат трех (максимум) следующих нейронов и веса синапса. 
        '''
        self.activate = None #Предел активации
        '''Значение, по превышении которого сработает функция  отправки сигнала'''
        self.summ = None #Предварительный сумматор сигналов
        '''Промежуточное значение входящих сигналов'''
    

a = Hyper(3)

print(a.matrix)