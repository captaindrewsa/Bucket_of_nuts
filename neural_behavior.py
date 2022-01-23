import numpy as np

class Param:
    def __init__(self, matrixsize):
        self.value = np.zeros(matrixsize)
        self.electricity = 0

    def numbers(self, value):
        self.value = value
        return self.value, self.electricity


class Neuron:
    def __init__(self, num_inputs, matrixsize):
        self.num_inputs = num_inputs # Ammount of inputs, int
        param = Param(matrixsize)
        self.value, self.electricity = param.numbers(0.001 * np.random.randint(-10,10,matrixsize))

    def accumulation(self, inputs):

        '''
        Accumulates all incoming signals

        inputs = All incoming signals - 3d array with size num_inputs, matrixsize
        '''
        
        self.value = np.sum(inputs, axis=0)
        self.electricity = np.linalg.det(self.value)

        return


    def params(self):
        return {'value': self.value, 'electricity': self.electricity}



#a = np.arange(9) + 1.25
a = np.random.randint(-10,10,(3,3))
a = np.reshape(a, (3,3))
print(np.linalg.det(a))
a = np.array([a-1,a-3,a-2.3,a+1.2,a])

neuron = Neuron(a.shape[0], (3,3))
neuron.accumulation(a)
print(neuron.params())