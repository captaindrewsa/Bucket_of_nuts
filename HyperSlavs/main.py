import numpy as np
import Matrix


if __name__ == '__main__':
    a = Matrix.Matrix(10,9)
    t1 = a.matrix[0,0].Kernel_n
    t2 = a.matrix[0,0].Kernel_n

    # t3 = np.stack((t1,t2))
    # print(t3)
    # print(t3.shape)
    for elem in t1[0,:,:2]:
        print("Элемент:\n",elem)
    # # for elem in a.matrix[0,0].Kernel[0,:,:,:2]:
    # #     print(elem,"\n")