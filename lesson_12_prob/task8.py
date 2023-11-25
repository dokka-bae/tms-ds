# Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8.
# Стрелок выстрелил 100 раз. Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.
import numpy as np
from scipy import stats


class Handler:
    def __init__(self, numbers: np.int64, predict_numbers: np.int64, probability: np.float64) -> None:
        self.numbers: np.int64 = numbers
        self.predict_numbers: np.int64 = predict_numbers
        self.probability: np.float64 = probability
        self.run()

    def run(self) -> None:
        print(stats.binom.pmf(self.predict_numbers,self.numbers,self.probability))

if __name__ == '__main__':
    Handler(numbers=100,predict_numbers=85,probability=0.8)
