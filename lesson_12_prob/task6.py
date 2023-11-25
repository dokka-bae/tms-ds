# Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?
import numpy as np
from scipy import stats


class Handler:
    def __init__(self, numbers: np.int64, predict_numbers: np.int64) -> None:
        self.numbers: np.int64 = numbers
        self.predict_numbers: np.int64 = predict_numbers
        self.run()

    def run(self) -> None:
        print(stats.binom.pmf(self.predict_numbers, self.numbers, 0.5))


if __name__ == '__main__':
    Handler(numbers=144, predict_numbers=70)
