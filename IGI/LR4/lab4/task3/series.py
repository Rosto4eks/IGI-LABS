import math
from matplotlib import pyplot as plt
import statistics as st

class Series:
    part_init = 1000;

    def calc_acos_series(self, x: float, eps: float):
        '''
        calculates acos series function with eps accuracy
        return calculated value and iterations count
        '''
        sum = math.pi / 2;
        part = eps * self.part_init;
        n = 0;
        while (True):
            temp = math.factorial(2 * n) * math.pow(x, 2 * n + 1) / (math.pow(4, n) * math.pow(math.factorial(n),2) * (2 * n + 1))
            if (abs(part - temp) < eps):
                break
            part = temp
            sum -= part
            n = n + 1
        return sum, n


    def calc_acos(self, n:int, eps: float):
        '''
        calculates acos from x=-1 to 1 and prints table
        number of elements = n
        accuracy = eps
        '''
        if (n < 2):
            print("iteration count must be greater than 1")
            return
        if (eps < 0):   
            print("accuracy must be greater than 0")
            return
        step = 2 / (n - 1)
        if (step > 500):
            raise Exception("iteration count more than 500")
        data = [[],[],[],[],[]]
        x = -1
        data[0].append("x")
        data[1].append("n")
        data[2].append("F(x)")
        data[3].append("Math F(x)")
        data[4].append("eps")
        while (x <= 1):
            try:
                series, n = self.calc_acos_series(x, eps)
            except:
                series = "calculation overflow"
                n = "inf"
            fn = math.acos(x)
            data[0].append(x.__str__())
            data[1].append(n.__str__())
            data[2].append(series.__str__())
            data[3].append(fn.__str__())
            data[4].append(eps.__str__())
            x += step
        return data


class SeriesTask(Series):
    def __init__(self, n, acc):
        self.n = n
        self.acc = acc
        self.data = None


    def calculate(self):
        '''
        calculate series and plot all data
        '''
        self.data = super().calc_acos(self.n, self.acc)
        self.plot()    


    def plot(self):
        '''
        display plots and data
        '''
        data = self.data
        x = []
        y1 = []
        y2 = []
        for elem in data[0][1:]:
            x.append(float(elem))
        for elem in data[2][1:]:
            y1.append(float(elem))
        for elem in data[3][1:]:
            y2.append(float(elem))
        plt.plot(x, y1, label="math f(x)")
        plt.plot(x, y2, label="f(x) series")
        plt.annotate(f"average mean = {self.ar_mean()}\nmedian = {self.median()}\nvariance = {self.variance()}\nstd = {self.std()}", xy = {-0.95, 0.6})
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True)
        plt.title('y = arccos(x)')
        plt.savefig('plot.png')
        plt.show()


    def ar_mean(self):
        '''
        return mean of data
        '''
        x = []
        for elem in self.data[3][1:]:
            x.append(float(elem))
        return st.mean(x)
    

    def median(self):
        '''
        return median of data
        '''
        x = []
        for elem in self.data[3][1:]:
            x.append(float(elem))
        return st.median(x)
        
    
    def variance(self):
        '''
        return variance of data
        '''
        x = []
        for elem in self.data[3][1:]:
            x.append(float(elem))
        return st.variance(x)
    

    def std(self):
        '''
        return std of data
        '''
        x = []
        for elem in self.data[3][1:]:
            x.append(float(elem))
        return st.stdev(x)