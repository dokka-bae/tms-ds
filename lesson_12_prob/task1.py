# Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150. 
# Посчитать (желательно без использования статистических методов наподобие std, var, mean) среднее арифметическое, 
# среднее квадратичное отклонение, смещенную и несмещенную оценки дисперсий для данной выборки.
import numpy as np


class Handler:
    def __init__(self, data: np.ndarray(shape=(),dtype=np.int64)) -> None:
        self.data: np.ndarray(shape=(),dtype=np.int64) = data
        self.run()

    def mean(self) -> np.float64:
        return np.sum(self.data,dtype=np.int64)/self.data.shape[0]

    def RMSE(self) -> np.float64:
        return np.sqrt(np.sum((self.data-self.mean())**2,dtype=np.float64)/self.data.shape[0],dtype=np.float64) # корень из mse есть ср. кв. отклонение

    def sample_variance(self) -> np.float64:
        return np.sum((self.data - self.mean())**2,dtype=np.float64)/self.data.shape[0]

    def sample_unbiased_variance(self) -> np.float64:
        return np.sum((self.data - self.mean())**2,dtype=np.float64)/(self.data.shape[0]-1)

    def run(self) -> None:
        # значения из реализованных функций = значение из функций библиотеки
        print(f"{self.mean()} = {self.data.mean()}")
        print(f"{self.RMSE()} = {self.data.std()}")
        print(f"{self.sample_variance()} = {self.data.var(ddof=0)}")
        print(f"{self.sample_unbiased_variance()} = {self.data.var(ddof=1)}")


if __name__ == '__main__':
    data = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150],dtype=np.int64)
    Handler(data)