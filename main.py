import random
from tqdm import tqdm



def benchmark(text):
    """Декоратор для бенчмарка функций."""
    
    def decorator(func):
        import time

        def wrapper(*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)
            end = time.time()
            print(f"[*] {text}: {end-start} секунд.")


        return wrapper
    return decorator

class Bucket:
    """Главный класс. Создает модель с нодами и обеспечивает контроль над ним.  """

    def __init__(self, count_nut_bolt:int) -> None:
        """Инициализация нод"""

        self.size_bucket = count_nut_bolt
        self.nodes = tuple([node() for _ in range(self.size_bucket)])
        self.weight = 0
    
    
    @benchmark("Время инициализации ведра")
    def random_connect(self, n):
        """Создает случайные связи между нодами.
        Можно указать максимальное количество вохможных связей на ноду"""
       
        for noda in tqdm(self.nodes):
            i=0
            while i < n:
                rnd_noda = random.choice(self.nodes)
                if ( rnd_noda.__hash__() != noda.__hash__() ):
                    if ( (len(noda.previous) + len(noda.next)) < n ) and ( ( len(rnd_noda.previous) + len(rnd_noda.next) ) < n ):
                            if (rnd_noda not in sum(noda.next,[])) and ( rnd_noda not in noda.previous) :
                                noda.next.append([rnd_noda, self.weight])
                                rnd_noda.previous.append(noda)
                                i+=1
                else:
                    break
    
    @benchmark("Время распространения сигнала")
    def start_signal(self, number_nodes):
        """Функция запуска распространения сигнала.
        Можно указать количество случайных стартовых нод, с которых начнется распространение"""

        list_nodes = []
        for _ in range(number_nodes):
            list_nodes.append(random.choice(self.nodes))
        for noda in list_nodes:
            noda.send_signal()


class node():
    """Главный класс ноды. Описывает характеристики и функции"""

    def __init__(self) -> None:
        """Инициализация базовых параметров нод"""
        
        self.previous = []
        self.next = []
    
    def final_signal(self):
        """Функция вызываемая нодой не имеющей дальнейших связей"""
        
        print(f"Я последний - {self}")

    def send_signal(self):
        """Функция отправляющая сигнал в каждую следующую ноду из списка связей"""

        if len(self.next)!=0:
            for noda in self.next:
                noda[0].send_signal()
        else:
            self.final_signal()

a = Bucket(100)
a.random_connect(4)
a.start_signal(3)
