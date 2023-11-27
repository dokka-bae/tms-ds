# Случайная непрерывная величина A имеет равномерное распределение на промежутке (200, 800].
# Найдите ее среднее значение и дисперсию.
import numpy as np
from scipy import stats


class Handler():
    def __init__(self, start: np.int64, end: np.int64) -> None:
        self.start: np.int64 = start
        self.end: np.int64 = end
        self.run()

    def mean(self) -> np.float64:
        return (self.startself.end)/2

    def variance(self) -> np.float64:
        return (self.end-self.start)**2/12

    def run(self) -> None:
        print(self.mean(), self.variance())


if __name__ == '__main__':
    Handler(start=200, end=800)
