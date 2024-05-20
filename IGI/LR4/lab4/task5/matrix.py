import numpy as np

class Matrix:
    def __init__(self, n: int, m: int):
        self._n = n
        self._m = m
        self._arr = np.random.randint(low=0, high=100, size=(n, m))


    def get(self):
        '''
        return matrix
        '''
        return self._arr
    

    def OddandEvenCount(self):
        '''
        return count of odd and even elements
        '''
        odd = 0
        even = 0
        for i in self._arr:
            for j in i:
                if j % 2 == 0:
                    even += 1
                else:
                    odd += 1
        return odd, even

    def Corr(self):
        '''
        return correlation coefficient of data
        '''
        odd = []
        even = []
        k = 0
        for i in self._arr:
            for j in i:
                if k % 2 == 0:
                    even.append(j)
                else:
                    odd.append(j)
                k += 1
        return np.corrcoef(even, odd)[0][1]