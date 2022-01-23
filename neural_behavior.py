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

        # Variable properties:
        self.value, self.electricity = param.numbers(0.01 * np.random.randint(-10,10,matrixsize))

        # Unvariable properties, cannot be changed during transmission:
        self.defaults = param.numbers(0.01 * np.random.randint(-10,10,matrixsize))

        # Conditions:
        self.firing = False




    def accumulation(self, inputs):

        '''
        Accumulates all incoming signals

        inputs = All incoming signals - 3d array with size num_inputs, matrixsize
        '''
        
        self.value = np.sum(inputs, axis=0)
        self.electricity = np.linalg.det(self.value)

        return


    def fire(self):
        '''
        Neural output
        
        returns:
        self.firing - is this neuron firng now or not - bool
        answer - kind of fire, inhibitory or excitatory - np.array (matrixsize)
        '''
        if self.electricity < 1 and self.electricity >-1:
            self.firing = False
            answer = None
        else:
            self.firing = True
            answer = self.value
        return self.firing, answer


    def exhaust(self):
        '''
        Neural recovery, if transmission has been performed
        '''
        
        if self.firing == True:
            self.value, self.electricity = self.defaults
        else:
            pass
        self.firing = False
        return


    def params(self):
        return {'value': self.value, 'electricity': self.electricity}




a = np.random.randint(-10,10,(3,3)) *0.01
a = np.reshape(a, (3,3))
a = np.array([a-1,a-3,a-2.3,a+1.2,a])

neuron = Neuron(a.shape[0], (3,3))
neuron.accumulation(a)

print(neuron.params())
print(neuron.fire())
neuron.exhaust()