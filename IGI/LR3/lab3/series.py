import math

def calc_acos_series(x: float, eps: float):
    '''
    calculates acos series function with eps accuracy
    return calculated value and iterations count
    '''
    sum = math.pi / 2;
    part = eps * 1337;
    n = 0;
    while (True):
        temp = math.factorial(2 * n) * math.pow(x, 2 * n + 1) / (math.pow(4, n) * math.pow(math.factorial(n),2) * (2 * n + 1))
        if (abs(part - temp) < eps):
            break
        part = temp
        sum -= part
        n = n + 1
    return sum, n

def CalcDecorator(func):
    def fn(*args):
        data = func(*args)
        print_table(data)
    return fn

@CalcDecorator
def calc_acos(n:int, eps: float):
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
            series, n = calc_acos_series(x, eps)
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


def print_table(data: list[list]):
    '''
    prints table for calc_acos
    '''
    lengths = []
    for i in range(len(data)):
        lengths.append(max(len(s) for s in data[i]))
        if i == 0:
            print("┏━━" + "━" * lengths[i], end="━━┳━━")
        elif i != len(data) - 1:
            print("━" * (lengths[i] + 3), end="━━┳━━")
        else:
            print("━" * (lengths[i] + 3), end="━━┓")
    print("")
    for i in range(len(data[0])):
        for j in range(len(data)):
            if j == 0:
                print("┃  " + data[j][i] + " " * (lengths[j] - len(data[j][i])), end="  ┃  ",)
            else:
                print(data[j][i] + " " * (lengths[j] + 3 - len(data[j][i])), end="  ┃  ",)
        print("")
        for j in range(len(data)):
            if i != len(data[0]) - 1:
                if j == 0:
                    print("┣━━" + "━" * lengths[j], end="━━╋━━")
                elif j != len(data) - 1:
                    print("━" * (lengths[j] + 3), end="━━╋━━")
                else:
                    print("━" * (lengths[j] + 3), end="━━┫")
            else:
                if j == 0:
                    print("┗━━" + "━" * lengths[j], end="━━┻━━")
                elif j != len(data) - 1:
                    print("━" * (lengths[j] + 3), end="━━┻━━")
                else:
                    print("━" * (lengths[j] + 3), end="━━┛")
        print("")