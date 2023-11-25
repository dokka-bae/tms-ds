# Рост взрослого населения города X имеет нормальное распределение.
# Причем, средний рост равен 174 см, а среднее квадратичное отклонение равно 8 см.
# Какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
# а). больше 182 см
# б). больше 190 см
# в). от 166 см до 190 см
# г). от 166 см до 182 см
# д). от 158 см до 190 см
# е). не выше 150 см или не ниже 190 см
# ё). не выше 150 см или не ниже 198 см
# ж). ниже 166 см.
import numpy as np
from scipy import stats


class Handler:
    def __init__(self, mean: np.float64, std: np.float64) -> None:
        self.mean: np.float64 = mean
        self.std: np.float64 = std
        self.run()

    def run(self) -> None:
        print(f"a) {1- stats.norm.cdf(x=182,loc=self.mean,scale=self.std)}")
        print(f"б) {1- stats.norm.cdf(x=190,loc=self.mean,scale=self.std)}")
        print(f"в) {stats.norm.cdf(x=190,loc=self.mean,scale=self.std) - stats.norm.cdf(x=166,loc=self.mean,scale=self.std)}")
        print(f"г) {stats.norm.cdf(x=182,loc=self.mean,scale=self.std) - stats.norm.cdf(x=166,loc=self.mean,scale=self.std)}")
        print(f"д) {stats.norm.cdf(x=190,loc=self.mean,scale=self.std) - stats.norm.cdf(x=158,loc=self.mean,scale=self.std)}")
        print(f"е) {stats.norm.cdf(x=150,loc=self.mean,scale=self.std) + 1 - stats.norm.cdf(x=190,loc=self.mean,scale=self.std)}")
        print(f"ё) {stats.norm.cdf(x=150,loc=self.mean,scale=self.std) + 1 - stats.norm.cdf(x=198,loc=self.mean,scale=self.std)}")
        print(f"ж) {stats.norm.cdf(x=166,loc=self.mean,scale=self.std)}")


if __name__ == '__main__':
    Handler(mean=174, std=8)
