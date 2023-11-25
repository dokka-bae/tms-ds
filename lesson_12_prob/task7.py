# Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004.
# В жилом комплексе после ремонта в один день включили 5000 новых лампочек.
# Какова вероятность, что ни одна из них не перегорит в первый день?
# Какова вероятность, что перегорят ровно две?
import numpy as np
from scipy import stats


class Handler:
    def __init__(self, numbers: np.int64, predict_numbers: np.int64) -> None:
        self.numbers: np.int64 = numbers
        self.predict_numbers: np.int64 = predict_numbers
        self.run()

    def run(self) -> None:
        print("Ни одна лампа не перегорит:", stats.poisson.pmf(
            self.predict_numbers[0], self.numbers * 0.0004))
        print("Две лампы сгорят:", stats.poisson.pmf(
            self.predict_numbers[1], self.numbers * 0.0004))


if __name__ == '__main__':
    Handler(numbers=5000, predict_numbers=[0, 2])
